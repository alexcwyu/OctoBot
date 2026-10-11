"""
Pytest configuration for OctoBot tests.
Sets up correct paths for test module imports.
"""
import asyncio
import os
import sys
import pytest

# Get the OctoBot root from this conftest.py location
OCTOBOT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_ROOT = os.path.dirname(os.path.abspath(__file__))
TEST_UTILS_ROOT = os.path.join(TESTS_ROOT, "test_utils")
PACKAGES_TENTACLES_ROOT = os.path.join(OCTOBOT_ROOT, "packages", "tentacles")

# Add OctoBot root to sys.path so 'import tentacles' works
if OCTOBOT_ROOT not in sys.path:
    sys.path.insert(0, OCTOBOT_ROOT)

# Add tests root to sys.path so 'from tests.test_utils import ...' works
if TESTS_ROOT not in sys.path:
    sys.path.insert(0, TESTS_ROOT)

# Add test_utils root to sys.path so 'from config import ...' works
if TEST_UTILS_ROOT not in sys.path:
    sys.path.insert(0, TEST_UTILS_ROOT)

from test_utils.journal_test_support import disabled_node_journal_environment


def pytest_configure(config):
    """Change working directory to OctoBot root before any tests run."""
    os.chdir(OCTOBOT_ROOT)

    # Use the manager-installed namespace. The source archive is not importable
    # until its generated package initializers have been installed.
    import octobot_tentacles_manager.constants as tm_constants
    tm_constants.TENTACLES_PATH = os.path.join(OCTOBOT_ROOT, "tentacles")


@pytest.fixture(autouse=True)
def disable_node_journal():
    with disabled_node_journal_environment():
        yield


@pytest.fixture(autouse=True)
def close_test_event_loops(monkeypatch):
    """Close loops allocated by test startup paths before fixture mocks are removed."""
    loops = []
    original_new_loop = asyncio.events.new_event_loop

    def new_owned_loop():
        loop = original_new_loop()
        loops.append(loop)
        return loop

    monkeypatch.setattr(asyncio, "new_event_loop", new_owned_loop)
    monkeypatch.setattr(asyncio.events, "new_event_loop", new_owned_loop)
    yield
    for loop in reversed(loops):
        if not loop.is_closed() and not loop.is_running():
            tasks = asyncio.all_tasks(loop)
            for task in tasks:
                task.cancel()
            if tasks:
                loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()
