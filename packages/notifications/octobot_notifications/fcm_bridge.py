#  Drakkar-Software OctoBot-Notifications
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import asyncio
import json
import logging
import os

import nats
import firebase_admin
import firebase_admin.messaging as fcm_messaging
from firebase_admin import credentials
from aiohttp import web


logger = logging.getLogger(__name__)

NATS_SUBJECT = "notifications.>"
QUEUE_GROUP = "fcm-bridge"
SUBJECT_PREFIX = "notifications."


async def run_fcm_bridge(
    nats_url: str | None = None,
    fcm_credentials_path: str | None = None,
    healthz_port: int = 9090,
):
    nats_url = nats_url or os.environ.get("NATS_URL", "nats://localhost:4222")
    fcm_credentials_path = fcm_credentials_path or os.environ.get(
        "FCM_SERVICE_ACCOUNT_PATH", "/run/secrets/fcm-sa.json"
    )

    # Initialize Firebase Admin SDK
    cred = credentials.Certificate(fcm_credentials_path)
    firebase_admin.initialize_app(cred)
    logger.info("Firebase Admin SDK initialized")

    # Connect to NATS
    nc = await nats.connect(nats_url)
    logger.info("Connected to NATS at %s", nats_url.split("@")[-1])

    subscription_active = False

    async def _handle_message(msg):
        subject = msg.subject
        if not subject.startswith(SUBJECT_PREFIX):
            logger.warning("Unexpected subject: %s", subject)
            return
        fcm_topic = subject[len(SUBJECT_PREFIX):]
        try:
            payload = json.loads(msg.data.decode())
        except (json.JSONDecodeError, UnicodeDecodeError):
            logger.error("Invalid message payload on %s", subject)
            return
        title = payload.get("title", "")
        body = payload.get("body", "")
        data = payload.get("data")
        message = fcm_messaging.Message(
            topic=fcm_topic,
            notification=fcm_messaging.Notification(title=title, body=body),
            data={k: str(v) for k, v in data.items()} if data else None,
        )
        try:
            message_id = fcm_messaging.send(message)
            logger.info("Sent FCM message %s to topic %s", message_id, fcm_topic)
        except Exception:
            logger.exception("Failed to send FCM message to topic %s", fcm_topic)

    # Subscribe with queue group for exactly-once delivery across bridge instances
    sub = await nc.subscribe(NATS_SUBJECT, queue=QUEUE_GROUP, cb=_handle_message)
    subscription_active = True
    logger.info(
        "Subscribed to %s with queue group %s", NATS_SUBJECT, QUEUE_GROUP
    )

    # Health check server
    async def _healthz(request):
        if subscription_active and nc.is_connected:
            return web.json_response({"ok": True})
        return web.json_response({"ok": False}, status=503)

    app = web.Application()
    app.router.add_get("/healthz", _healthz)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", healthz_port)
    await site.start()
    logger.info("Health check server listening on :%d", healthz_port)

    # Run until interrupted
    try:
        while True:
            await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass
    finally:
        subscription_active = False
        await sub.unsubscribe()
        await nc.drain()
        await runner.cleanup()
        logger.info("FCM bridge shut down")
