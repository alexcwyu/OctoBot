# OctoBot Development Guide

## Development Setup

### Prerequisites

- Python 3.13+
- `uv` (recommended) or `pip`
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Drakkar-Software/OctoBot.git
cd OctoBot

# Install with uv (recommended)
uv sync --active --all-groups

# Or install with pip
pip install -e ".[full]"

# Install default tentacles
python start.py tentacles --install --all
```

### Running OctoBot

```bash
# Standard start (creates config on first run)
python start.py

# Start in simulation mode
python start.py --simulate

# Start with backtesting
python start.py --backtesting --backtesting-files path/to/data.json

# Start without web interface
python start.py --no_web

# Start without telegram
python start.py --no-telegram

# Start strategy optimizer
python start.py -o TechnicalAnalysisStrategyEvaluator

# Show version
python start.py --version

# Encrypt exchange API keys
python start.py --encrypter

# Start in node mode (distributed)
python start.py node --master --port 8000

# Start sync server
python start.py sync --host 0.0.0.0 --port 3000
```

### Configuration

Configuration is stored in the `user/` directory:

```
user/
  config.json              # Main bot configuration
  profiles/
    default/
      profile.json         # Profile settings
      tentacles_config.json   # Tentacle activation
      specific_config/     # Per-tentacle configuration
    custom_profile/
      ...
```

Key configuration areas:
- **Exchanges**: API keys, enabled/disabled, exchange type (spot/futures)
- **Trader**: Real trader or simulator toggle, risk level (0-1)
- **Crypto Currencies**: Trading pairs and associated exchanges
- **Trading**: Reference market, risk settings

## Project Structure

```
OctoBot/
  src/octobot/
    __init__.py                  # VERSION, PROJECT_NAME, AUTHOR
    octobot.py                   # Main OctoBot class
    cli.py                       # CLI argument parsing and startup
    commands.py                  # Bot control commands (start, stop, restart)
    constants.py                 # All constants, URLs, env vars
    enums.py                     # Enumerations (distributions, optimizer modes)
    errors.py                    # Custom exception classes
    configuration_manager.py     # Config state management
    initializer.py               # Bot initialization sequence
    task_manager.py              # Async loop and thread management
    octobot_channel_consumer.py  # Global channel event routing
    octobot_api.py               # Public API for external access
    octobot_backtesting_factory.py # Backtesting entry point
    octobot_node.py              # Node distribution mode
    logger.py                    # Logging setup
    limits.py                    # Config limit enforcement
    disclaimer.py                # Terms of service text
    databases_util.py            # Database helper utilities
    
    api/                         # Public API modules
      __init__.py
      backtesting.py             # Backtesting API
      strategy_optimizer.py      # Optimizer API
      updater.py                 # Update API
    
    automation/                  # Automation framework
      automation.py              # Automation engine
      bases/
        automation_step.py       # Base class for all steps
        abstract_trigger_event.py   # Trigger event base
        abstract_condition.py    # Condition base
        abstract_action.py       # Action base
        abstract_channel_based_trigger_event.py  # Channel trigger
        execution_details.py     # Execution context
    
    backtesting/                 # Backtesting engine
      octobot_backtesting.py     # Core backtesting orchestrator
      independent_backtesting.py # Standalone backtesting
      abstract_backtesting_test.py  # Test base class
      minimal_data_importer.py   # Minimal data import
    
    channels/                    # Channel definitions
      octobot_channel.py         # OctoBotChannel, Producer, Consumer
    
    community/                   # Community integration
      authentication.py          # Supabase auth with JWT
      community_manager.py       # Metrics and bot registration
      community_analysis.py      # Community data analysis
      community_bot.py           # Community bot operations
      identifiers_provider.py    # Environment-aware identifiers
      tentacles_packages.py      # Community tentacle packages
      graphql_requests.py        # GraphQL query definitions
      errors.py                  # Community-specific errors
      feeds/                     # MQTT/WebSocket feeds
      supabase_backend/          # Supabase database operations
      wallet_backend/            # Wallet operations
      history_backend/           # Clickhouse/Iceberg backends
      models/                    # Data models
    
    config/                      # Default configuration files
      default_config.json
      config_schema.json
      profile_schema.json
      logging_config.ini
    
    producers/                   # OctoBotChannel producers
      exchange_producer.py       # Exchange lifecycle
      evaluator_producer.py      # Evaluator matrix setup
      interface_producer.py      # Interface/notifier creation
      service_feed_producer.py   # Service feed management
    
    storage/                     # Data storage
      trading_metadata.py        # Run metadata storage
      db_databases_pruning.py    # Database size management
    
    strategy_optimizer/          # Strategy optimization
      strategy_optimizer.py      # Brute-force optimizer
      strategy_design_optimizer.py     # Genetic algorithm optimizer
      strategy_design_optimizer_factory.py  # Optimizer creation
      strategy_test_suite.py     # Test suite runner
      test_suite_result.py       # Result formatting
      scored_run_result.py       # Scoring system
      fitness_parameter.py       # Fitness parameters
      optimizer_filter.py        # Result filters
      optimizer_constraint.py    # Optimization constraints
      optimizer_settings.py      # Optimizer configuration
    
    updater/                     # Bot update mechanisms
  
  tests/                         # Test suite
  additional_tests/              # Extended tests
  docker/                        # Docker configuration
  Dockerfile                     # Production Docker image
  docker-compose.yml             # Docker Compose setup
  pyproject.toml                 # Build configuration
```

## Tentacle Development Guide

Tentacles are the primary extension mechanism. All evaluators, trading modes, services, and interfaces are tentacles.

### Tentacle Directory Structure

Installed tentacles live in the `tentacles/` directory:

```
tentacles/
  Evaluator/
    TA/                    # Technical Analysis evaluators
      MyRSIEvaluator/
        __init__.py
        my_rsi_evaluator.py
    Strategies/            # Strategy evaluators
    Social/                # Social evaluators
    RealTime/              # Real-time evaluators
  Trading/
    Mode/                  # Trading modes
  Services/
    Interfaces/            # Web, Telegram interfaces
    Notifiers/             # Notification services
    Services_bases/        # Base service implementations
  Automation/
    trigger_events/        # Automation triggers
    conditions/            # Automation conditions
    actions/               # Automation actions
```

### Creating a Custom TA Evaluator

```python
# tentacles/Evaluator/TA/my_evaluator/my_evaluator.py

import octobot_evaluators.evaluators as evaluators
import octobot_commons.enums as enums


class MyCustomEvaluator(evaluators.TAEvaluator):
    """
    Custom Technical Analysis Evaluator
    
    Evaluates price action using a custom indicator.
    Output: value in [-1, +1] range written to the evaluator matrix.
    """

    def init_user_inputs(self, inputs: dict) -> None:
        """Define configurable parameters for this evaluator."""
        self.period = self.UI.user_input(
            "period", enums.UserInputTypes.INT,
            14, inputs,
            min_val=2, max_val=200,
            title="Indicator period"
        )
        self.threshold = self.UI.user_input(
            "threshold", enums.UserInputTypes.FLOAT,
            0.5, inputs,
            min_val=0.0, max_val=1.0,
            title="Signal threshold"
        )

    async def ohlcv_callback(
        self,
        exchange: str,
        exchange_id: str,
        cryptocurrency: str,
        symbol: str,
        time_frame: str,
        candle: dict,
        init_call: bool = False,
    ):
        """Called when new OHLCV data is available."""
        # Skip initialization calls
        if init_call:
            return

        # Get historical candle data
        candles = self.get_symbol_candles(exchange, exchange_id, symbol, time_frame)
        close_prices = candles.get_symbol_close_candles()

        if len(close_prices) < self.period:
            # Not enough data yet
            self.eval_note = 0
        else:
            # Calculate your custom indicator
            indicator_value = self._calculate_indicator(close_prices)
            
            # Map to [-1, +1] range
            if indicator_value > self.threshold:
                self.eval_note = min(1.0, indicator_value)  # Buy signal
            elif indicator_value < -self.threshold:
                self.eval_note = max(-1.0, indicator_value)  # Sell signal
            else:
                self.eval_note = 0  # Neutral

        # Write evaluation to the matrix
        await self.evaluation_completed(
            cryptocurrency, symbol, time_frame,
            eval_time=candle.get(enums.PriceIndexes.IND_PRICE_TIME.value, None)
        )

    def _calculate_indicator(self, close_prices):
        """Custom indicator calculation."""
        # Your indicator logic here
        recent = close_prices[-self.period:]
        sma = sum(recent) / len(recent)
        current = close_prices[-1]
        return (current - sma) / sma  # Normalized deviation

    @classmethod
    def get_is_symbol_wildcard(cls) -> bool:
        """Return True if this evaluator applies to all symbols."""
        return False
```

### Key Evaluator Methods

| Method | Purpose |
|--------|---------|
| `init_user_inputs(inputs)` | Define configurable parameters |
| `ohlcv_callback(...)` | Called on new candle data (TA evaluators) |
| `evaluation_completed(...)` | Write evaluation to matrix and notify |
| `get_symbol_candles(...)` | Access historical candle data |
| `get_is_symbol_wildcard()` | Whether evaluator runs on all symbols |
| `get_is_time_frame_wildcard()` | Whether evaluator runs on all time frames |

### Evaluator Output Convention

- Write to `self.eval_note` (float in [-1, +1])
- Call `await self.evaluation_completed(...)` to push to matrix
- The strategy evaluator reads these values and combines them

## Evaluator Development

### Strategy Evaluator

Strategy evaluators combine signals from multiple evaluators:

```python
import octobot_evaluators.evaluators as evaluators
import octobot_commons.enums as enums


class MyStrategyEvaluator(evaluators.StrategyEvaluator):
    """Combines TA and Social evaluator signals."""

    def init_user_inputs(self, inputs: dict) -> None:
        self.ta_weight = self.UI.user_input(
            "ta_weight", enums.UserInputTypes.FLOAT,
            0.7, inputs, min_val=0, max_val=1,
            title="Weight for TA evaluators"
        )

    async def matrix_callback(
        self,
        matrix_id,
        evaluator_name,
        evaluator_type,
        eval_note,
        eval_note_type,
        exchange_name,
        cryptocurrency,
        symbol,
        time_frame,
    ):
        """Called when any evaluator updates the matrix."""
        # Read all evaluator values from the matrix
        ta_values = self.get_evaluator_values(
            matrix_id, exchange_name, symbol, time_frame,
            evaluator_type="TA"
        )
        social_values = self.get_evaluator_values(
            matrix_id, exchange_name, symbol, time_frame,
            evaluator_type="SOCIAL"
        )

        # Combine with weights
        ta_avg = sum(ta_values) / len(ta_values) if ta_values else 0
        social_avg = sum(social_values) / len(social_values) if social_values else 0

        self.eval_note = (
            self.ta_weight * ta_avg +
            (1 - self.ta_weight) * social_avg
        )

        await self.evaluation_completed(
            cryptocurrency, symbol, time_frame
        )

    @classmethod
    def get_required_time_frames(cls, config, tentacles_setup_config):
        """Return required time frames for this strategy."""
        return [enums.TimeFrames.ONE_HOUR, enums.TimeFrames.FOUR_HOURS]
```

## Trading Mode Development

Trading modes translate strategy signals into orders:

```python
import octobot_trading.modes as trading_modes


class MyTradingMode(trading_modes.AbstractTradingMode):
    """Custom trading mode that creates orders based on strategy signals."""

    def init_user_inputs(self, inputs: dict) -> None:
        self.buy_threshold = self.UI.user_input(
            "buy_threshold", enums.UserInputTypes.FLOAT,
            0.5, inputs, min_val=0, max_val=1,
            title="Minimum signal strength to buy"
        )
        self.position_size_pct = self.UI.user_input(
            "position_size", enums.UserInputTypes.FLOAT,
            10.0, inputs, min_val=1, max_val=100,
            title="Position size (% of portfolio)"
        )

    async def on_matrix_callback(self, matrix_id, **kwargs):
        """Called when strategy evaluation updates."""
        # Read the strategy signal
        signal = self.get_signal(matrix_id, **kwargs)
        
        if abs(signal) < self.buy_threshold:
            return  # Signal too weak
        
        if signal > 0:
            # Buy signal
            await self.create_buy_order(signal, **kwargs)
        else:
            # Sell signal
            await self.create_sell_order(signal, **kwargs)
```

## Automation Development

### Custom Trigger Event

```python
import octobot.automation.bases.abstract_trigger_event as abstract_trigger_event


class MyTriggerEvent(abstract_trigger_event.AbstractTriggerEvent):
    """Triggers automation based on custom condition."""

    async def _get_next_event(self):
        """Wait for and return the next event description."""
        # Wait for your condition (e.g., poll every 60 seconds)
        await asyncio.sleep(60)
        if self._check_my_condition():
            return "My condition was met"
        return None  # No event, will loop again
```

### Custom Action

```python
import octobot.automation.bases.abstract_action as abstract_action


class MyAction(abstract_action.AbstractAction):
    """Custom automation action."""

    async def process(self, execution_details):
        """Execute the action."""
        # Access bot API via execution_details
        # Perform your custom action
        pass
```

## Testing Patterns

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_octobot.py

# Run with coverage
pytest --cov=octobot tests/

# Run backtesting tests
pytest tests/backtesting/
```

### Writing Tests

```python
import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch

import octobot.octobot as octobot_module


class TestMyEvaluator:
    """Tests for custom evaluator."""

    @pytest.fixture
    def evaluator(self):
        """Create evaluator instance for testing."""
        evaluator = MyCustomEvaluator()
        evaluator.period = 14
        evaluator.threshold = 0.5
        return evaluator

    def test_indicator_calculation(self, evaluator):
        """Test indicator produces expected values."""
        prices = [100, 101, 102, 103, 104, 105, 106, 107,
                  108, 109, 110, 111, 112, 113, 114]
        result = evaluator._calculate_indicator(prices)
        assert -1.0 <= result <= 1.0

    @pytest.mark.asyncio
    async def test_ohlcv_callback(self, evaluator):
        """Test evaluation on candle data."""
        # Mock the required dependencies
        evaluator.get_symbol_candles = MagicMock()
        evaluator.evaluation_completed = AsyncMock()
        
        await evaluator.ohlcv_callback(
            exchange="binance",
            exchange_id="test-id",
            cryptocurrency="Bitcoin",
            symbol="BTC/USDT",
            time_frame="1h",
            candle={},
            init_call=False,
        )
        
        evaluator.evaluation_completed.assert_called_once()
```

### Backtesting Tests

```python
import pytest
from octobot.backtesting.abstract_backtesting_test import AbstractBacktestingTest


class TestMyStrategy(AbstractBacktestingTest):
    """Backtesting tests for custom strategy."""

    @pytest.mark.asyncio
    async def test_strategy_profitability(self):
        """Ensure strategy is profitable on test data."""
        result = await self.run_backtesting(
            data_files=["tests/data/btc_usdt_1h.json"],
            symbols={"binance": ["BTC/USDT"]},
        )
        assert result.profitability > 0
```

### Development Tips

1. **Always test with backtesting first** before running with real money
2. **Use simulation mode** (`--simulate`) for live testing without real trades
3. **Check tentacle activation** -- ensure your tentacle is enabled in the profile's tentacle config
4. **Watch the logs** -- OctoBot logs extensively; check `logs/OctoBot.log`
5. **Use user inputs** -- Make parameters configurable rather than hardcoded
6. **Respect the [-1, +1] range** -- Evaluator outputs must be normalized
7. **Handle init_call** -- Skip processing during initialization callbacks
8. **Test edge cases** -- Insufficient data, exchange errors, empty order books

## Configuration Reference

OctoBot's main configuration lives in `user/config.json`. The schema is defined in `src/octobot/config/config_schema.json`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `exchanges` | `object` | `{}` | Exchange configurations (keyed by exchange name). Each entry contains API keys, enabled status, and exchange type. |
| `exchanges.<name>.api-key` | `string` | `""` | Exchange API key (encrypt with `--encrypter`) |
| `exchanges.<name>.api-secret` | `string` | `""` | Exchange API secret (encrypt with `--encrypter`) |
| `exchanges.<name>.api-password` | `string` | `""` | Exchange API passphrase (for exchanges that require it) |
| `exchanges.<name>.enabled` | `boolean` | `true` | Whether this exchange is active |
| `exchanges.<name>.exchange-type` | `string` | `"spot"` | Exchange type: `"spot"`, `"margin"`, `"future"` |
| `backtesting.files` | `array[string]` | `[]` | Paths to backtesting data files |
| `services` | `object` | `{}` | Service-specific configuration (web, telegram, etc.) |
| `services.web.auto-open-in-web-browser` | `boolean` | `true` | Auto-open web UI on startup |
| `notification.global-info` | `boolean` | `true` | Enable global info notifications |
| `notification.price-alerts` | `boolean` | `true` | Enable price alert notifications |
| `notification.trades` | `boolean` | `true` | Enable trade notifications |
| `notification.trading-script-alerts` | `boolean` | `true` | Enable trading script alert notifications |
| `notification.other` | `boolean` | `true` | Enable other notifications |
| `notification.notification-type` | `array[string]` | `["web"]` | Notification channels: `"web"`, `"telegram"`, `"email"` |
| `profile` | `string` | `"default"` | Active profile name (maps to `user/profiles/<name>/`) |
| `accepted_terms` | `boolean` | `false` | Whether the user has accepted the disclaimer |
| `distribution` | `string` | `"default"` | Bot distribution mode: `"default"`, `"market_making"`, `"prediction_market"`, `"node"`, `"sync"` |
| `DEBUG` | `boolean` | `false` | Enable debug mode |
| `DEV-MODE` | `boolean` | `false` | Enable developer mode |
| `SAVE_EVALUATIONS` | `boolean` | `false` | Save evaluator outputs to database |
| `metrics.enabled` | `boolean` | `false` | Enable anonymous usage metrics |
| `metrics.metrics-bot-id` | `string` | `""` | Bot ID for metrics reporting |
| `community-token` | `string` | `""` | OctoBot Cloud community authentication token |
| `watched_symbols` | `array[string]` | `[]` | Symbols to watch without trading |

Profile configuration (`user/profiles/<name>/profile.json`) controls tentacle activation and per-tentacle settings via `tentacles_config.json` and `specific_config/` files.

## Troubleshooting

### 1. `ImportError: No module named 'octobot_trading'` (or other `octobot_*` package)

OctoBot depends on several companion packages. Install with the full extra:
```bash
pip install -e ".[full]"
```

### 2. Tentacles not found or `No tentacle to install`

Tentacles must be installed separately after the main package:
```bash
python start.py tentacles --install --all
```
If tentacles become corrupted, delete the `tentacles/` directory and reinstall.

### 3. Exchange connection fails with authentication errors

- Ensure API keys are encrypted: `python start.py --encrypter`
- Verify the exchange name in `config.json` matches exactly (case-sensitive, e.g., `"binance"` not `"Binance"`)
- Check that API key permissions include trading (read-only keys will fail order placement)
- Some exchanges require an API passphrase in addition to key/secret

### 4. Backtesting data not found

Backtesting requires pre-collected data files. Collect data through the web interface (Data Collector tab) or specify paths explicitly:
```bash
python start.py --backtesting --backtesting-files user/data/binance_BTC_USDT_1h.data
```

### 5. Web interface not loading (port 5001)

- Check if the port is already in use: `lsof -i :5001`
- Try starting without the web: `python start.py --no_web` to verify the bot itself works
- Check `logs/OctoBot.log` for startup errors

### 6. `asyncio` event loop errors

OctoBot is heavily async. If you see `RuntimeError: This event loop is already running`:
- Do not call `asyncio.run()` inside tentacle code -- use `await` directly
- Use `api.run_in_main_asyncio_loop(coroutine)` from synchronous contexts

### 7. Evaluator always returns 0 / no trades generated

- Check that your evaluator tentacle is **activated** in the profile's `tentacles_config.json`
- Verify `self.eval_note` is set and `await self.evaluation_completed(...)` is called
- Ensure the strategy evaluator's required time frames match what the exchange provides
- Check that the signal exceeds the trading mode's threshold

### 8. Memory issues during long backtesting runs

OctoBot includes a memory leak detector. Enable backtesting timeout to prevent runaway tests:
```bash
python start.py --backtesting --enable-backtesting-timeout --backtesting-files data.json
```

### 9. Docker container exits immediately

Check logs with `docker logs <container>`. Common causes:
- Missing `user/config.json` -- mount the config volume correctly
- Missing tentacles -- run tentacle install inside the container first
- Port conflicts -- ensure `-p 5001:5001` is mapped

### 10. Profile import/export fails

Profiles must match the schema defined in `src/octobot/config/profile_schema.json`. Ensure the profile directory contains both `profile.json` and `tentacles_config.json`.

## Security Considerations

### API Key Management

- **Always encrypt API keys** -- Use the built-in encrypter before storing keys in `config.json`:
  ```bash
  python start.py --encrypter
  ```
  This encrypts keys so they are not stored as plaintext in the configuration file.
- **Restrict API key permissions** -- On your exchange, create API keys with only the permissions OctoBot needs (typically: read account, place/cancel orders). Disable withdrawal permissions.
- **Never share `config.json`** -- It contains encrypted exchange credentials. Add `user/` to `.gitignore`.

### Credential Storage

- Exchange credentials in `config.json` are encrypted by the encrypter, but the encryption key is local to the machine. Moving `config.json` to another machine requires re-encryption.
- Community authentication tokens (`community-token`, `supabase.auth.token`) are stored in `config.json`. Treat this file as sensitive.
- The `.env` file (if used) can contain `COMMUNITY_BACKEND_KEY` and other tokens -- restrict file permissions:
  ```bash
  chmod 600 .env user/config.json
  ```

### Network Security

- **Web interface** -- By default, the web UI binds to `0.0.0.0:5001` with no authentication. In production:
  - Place behind a reverse proxy (nginx/caddy) with TLS and basic auth
  - Or bind to localhost only and use SSH tunneling
- **Telegram bot** -- The Telegram interface exposes bot control commands. Ensure only trusted users have the bot token.
- **Community/Cloud connections** -- OctoBot connects to `octobot.cloud` for profiles, signals, and updates. Connections use HTTPS/TLS (Supabase backend). Disable with `DISABLE_COMMUNITY_EXTENSIONS_CHECK=true`.
- **MQTT feeds** -- Community signal feeds use MQTT (iot.fr-par.scw.cloud). Traffic is encrypted but the feed URL is configurable via `COMMUNITY_FEED_URL` environment variable.
- **Docker** -- Use the official Docker image and avoid running as root. Map only necessary ports (`5001` for web).

### Data Privacy

- Anonymous usage metrics can be sent to OctoBot Cloud if `metrics.enabled` is `true`. Disable this in `config.json` if you prefer not to share usage data.
- Backtesting results and trade history are stored locally in the `user/` directory.
- Webhook URLs (TradingView integration) should be treated as secrets -- anyone with the URL can send signals to your bot.

---
## See Also
- [README](README.md) — Project overview and quick start
- [Architecture](architecture.md) — System design and components
- [Workflow](workflow.md) — Event flows and processing pipelines
- [State Management](state-management.md) — State lifecycle and data models
