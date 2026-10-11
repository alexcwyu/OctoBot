# in conftest.py to load the .env file before any test is run or any import is done

import dotenv
import os
import sys

dotenv.load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

import mock
import pytest

_OCTOBOT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_TESTS_ROOT = os.path.join(_OCTOBOT_ROOT, "tests")
if _OCTOBOT_ROOT not in sys.path:
    sys.path.insert(0, _OCTOBOT_ROOT)
if _TESTS_ROOT not in sys.path:
    sys.path.insert(0, _TESTS_ROOT)

from test_utils.journal_test_support import disabled_node_journal_environment


@pytest.fixture(autouse=True)
def disable_node_journal():
    with disabled_node_journal_environment():
        yield


@pytest.fixture(autouse=True)
def _disable_auto_open_in_web_browser():
    import tentacles.Meta.DSL_operators.octobot_process_operators.octobot_process_ops as octobot_process_ops
    with mock.patch.object(octobot_process_ops, "AUTO_OPEN_IN_WEB_BROWSER", False):
        yield


pytest_plugins = (
    "tests.functionnal_tests.octobot_process_actions.octobot_process_functional_shared",
)


@pytest.fixture(autouse=True)
def use_installed_host_directory(monkeypatch):
    """Flow functional tests execute the host's installed tentacle archive."""
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
