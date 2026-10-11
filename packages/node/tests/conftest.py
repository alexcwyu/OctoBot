import contextlib
import mock
import os
import pytest
import sys

_OCTOBOT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_TESTS_ROOT = os.path.join(_OCTOBOT_ROOT, "tests")
if _OCTOBOT_ROOT not in sys.path:
    sys.path.insert(0, _OCTOBOT_ROOT)
if _TESTS_ROOT not in sys.path:
    sys.path.insert(0, _TESTS_ROOT)

from test_utils.journal_test_support import disabled_node_journal_environment

_TESTS_RUN_OCTOBOT_PROCESS_WAITING_TIME_SECONDS = 2
_TESTS_RUN_OCTOBOT_PROCESS_PING_TIMEOUT_SECONDS = 30.0

os.environ.setdefault(
    "RUN_OCTOBOT_PROCESS_WAITING_TIME_SECONDS",
    str(_TESTS_RUN_OCTOBOT_PROCESS_WAITING_TIME_SECONDS),
)
os.environ.setdefault(
    "RUN_OCTOBOT_PROCESS_PING_TIMEOUT_SECONDS",
    str(_TESTS_RUN_OCTOBOT_PROCESS_PING_TIMEOUT_SECONDS),
)

import octobot.community.local_authenticator as local_community_auth


@contextlib.contextmanager
def mocked_local_user_configuration():
    with mock.patch.object(
        local_community_auth,
        "get_user_configuration",
        local_community_auth.get_stateless_configuration,
    ):
        yield


@pytest.fixture(autouse=True)
def disable_node_journal():
    with disabled_node_journal_environment():
        yield


@pytest.fixture(autouse=True)
def _mock_local_user_configuration():
    with mocked_local_user_configuration():
        yield


@pytest.fixture(autouse=True)
def _fast_run_octobot_process_recall(monkeypatch):
    import octobot_node.constants as node_constants

    monkeypatch.setattr(
        node_constants,
        "RUN_OCTOBOT_PROCESS_WAITING_TIME_SECONDS",
        _TESTS_RUN_OCTOBOT_PROCESS_WAITING_TIME_SECONDS,
    )
    monkeypatch.setattr(
        node_constants,
        "RUN_OCTOBOT_PROCESS_PING_TIMEOUT_SECONDS",
        _TESTS_RUN_OCTOBOT_PROCESS_PING_TIMEOUT_SECONDS,
    )


@pytest.fixture(autouse=True)
def _disable_auto_open_in_web_browser():
    import tentacles.Meta.DSL_operators.octobot_process_operators.octobot_process_ops as octobot_process_ops
    with mock.patch.object(octobot_process_ops, "AUTO_OPEN_IN_WEB_BROWSER", False):
        yield


@pytest.fixture(autouse=True)
def use_installed_host_directory(monkeypatch):
    """Functional automation loads metadata from the host archive directory."""
    monkeypatch.chdir(_OCTOBOT_ROOT)


"""Release HTTP sessions allocated by mocked exchange test setups."""
import asyncio

import aiohttp
import pytest_asyncio

from octobot_trading.exchanges.exchange_manager import ExchangeManager
from octobot_trading.exchanges.types.rest_exchange import RestExchange


@pytest_asyncio.fixture(autouse=True)
async def close_test_http_sessions(monkeypatch):
    sessions = []
    managers = []
    manager_init = ExchangeManager.__init__
    manager_stop = ExchangeManager.stop

    def tracked_manager_init(self, *args, **kwargs):
        manager_init(self, *args, **kwargs)
        managers.append(self)

    monkeypatch.setattr(ExchangeManager, "__init__", tracked_manager_init)
    original_init = aiohttp.ClientSession.__init__

    def tracked_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        sessions.append(self)

    monkeypatch.setattr(aiohttp.ClientSession, "__init__", tracked_init)
    yield
    for manager in managers:
        if isinstance(manager.exchange, RestExchange):
            await manager_stop(manager)
    await asyncio.sleep(0)
    for session in sessions:
        await session.close()
    # TLS transports finish asynchronously after ClientSession.close().
    if sessions:
        await asyncio.sleep(0.25)
