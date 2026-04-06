# OctoBot State Management

## Bot Lifecycle

The OctoBot bot goes through a well-defined lifecycle from startup through running to shutdown.

```mermaid
stateDiagram-v2
    [*] --> ConfigLoading: CLI start

    ConfigLoading --> ProfileLoading: Config loaded
    ConfigLoading --> Error: Invalid config

    ProfileLoading --> CommunityAuth: Profile loaded
    ProfileLoading --> Error: No valid profile

    CommunityAuth --> TentacleLoading: Auth complete (or skipped)
    CommunityAuth --> TentacleLoading: Auth failed (continue)

    TentacleLoading --> TentacleInstall: No tentacles found
    TentacleInstall --> TentacleLoading: Install complete
    TentacleLoading --> Initializing: Tentacles loaded

    Initializing --> CreatingProducers: Storage & channels initialized
    CreatingProducers --> StartingProducers: All producers created

    StartingProducers --> Running: All producers started
    note right of Running
        Bot is fully operational
        - Exchanges connected
        - Evaluators running
        - Interfaces active
        - Automations started
    end note

    Running --> Stopping: Stop signal (SIGINT/API)
    Running --> Restarting: Profile update / API restart
    Running --> Error: Unrecoverable error

    Restarting --> ConfigLoading: After delay

    Stopping --> Stopped: All subsystems stopped
    Stopped --> [*]

    Error --> Stopped: Force exit
```

### Initialization Sequence States

The `OctoBot.initialize()` method progresses through these internal states:

| State | Code Location | What Happens |
|-------|---------------|-------------|
| Clock Sync | `_ensure_clock()` | Synchronize system clock (if real trading enabled) |
| Community Auth Init | `community_auth.init_account()` | Initialize community account session |
| Tentacles Config | `initializer.create()` | Load `tentacles_setup_config`, init bot storage, create OctoBotChannel |
| Log Config | `_log_config()` | Log exchanges, trader type, symbols, trading mode |
| Tools Tasks | `_start_tools_tasks()` | Init aiohttp session, start community handler |
| Create Producers | `create_producers()` | Instantiate Exchange, Evaluator, Interface, ServiceFeed producers |
| Start Producers | `start_producers()` | Run evaluators, exchanges, service feeds, interfaces in order |
| System Watchers | `_ensure_watchers()` | Start RAM/resource monitoring if enabled |
| Post Initialize | `_post_initialize()` | Set `initialized=True`, start automations, store metadata |

### The `initialized` Flag

The `OctoBot.initialized` attribute is the primary readiness indicator:

- **`False`** during startup -- APIs should not serve data yet
- **`True`** after `_post_initialize()` completes -- bot is fully operational
- Checked by `OctoBotAPI.is_initialized()` which web interfaces use to gate requests

## Evaluator State Management

Evaluators maintain state through the **Evaluator Matrix**, a centralized data structure managed by `OctoBot-Evaluators`.

```mermaid
stateDiagram-v2
    [*] --> Uninitialized: Evaluator class loaded

    Uninitialized --> Initializing: create_evaluator()
    Initializing --> Active: start()

    state Active {
        [*] --> WaitingForData
        WaitingForData --> Processing: New candle/data received
        Processing --> Updated: Evaluation computed
        Updated --> WaitingForData: Ready for next data

        Updated --> MatrixUpdate: Write to matrix
        MatrixUpdate --> WaitingForData
    }

    Active --> Stopped: stop_evaluator()
    Stopped --> [*]
```

### Matrix Evaluation Values

Each evaluator writes a normalized value to the matrix:

| Value Range | Meaning |
|-------------|---------|
| `-1.0` | Strong sell signal |
| `-0.5` | Moderate sell signal |
| `0.0` | Neutral / no signal |
| `+0.5` | Moderate buy signal |
| `+1.0` | Strong buy signal |

The matrix is indexed by:
- **Exchange name**
- **Symbol** (trading pair)
- **Time frame** (for TA evaluators)
- **Evaluator name**

Strategy evaluators read all relevant matrix entries and produce a combined signal.

### Strategy Evaluator State

```mermaid
stateDiagram-v2
    [*] --> Idle: Strategy initialized

    Idle --> Evaluating: Matrix callback triggered
    Evaluating --> ReadingMatrix: Read all evaluator values

    ReadingMatrix --> Combining: All values collected
    Combining --> SignalReady: Weighted combination computed

    SignalReady --> Idle: Signal written to matrix
    note right of SignalReady
        Signal triggers trading mode
        callback via matrix channel
    end note
```

## Trading Mode States

Trading modes interpret strategy signals and manage order creation.

```mermaid
stateDiagram-v2
    [*] --> Initialized: Trading mode activated

    Initialized --> WaitingForSignal: Registered on matrix channel

    state WaitingForSignal {
        [*] --> Listening
        Listening --> SignalReceived: on_matrix_callback()
    }

    SignalReceived --> AnalyzingSignal: Read strategy evaluation

    state AnalyzingSignal {
        [*] --> CheckStrength
        CheckStrength --> StrongBuy: signal > buy_threshold
        CheckStrength --> StrongSell: signal < sell_threshold
        CheckStrength --> Neutral: within thresholds
    }

    StrongBuy --> CreatingBuyOrder: Calculate amount & price
    StrongSell --> CreatingSellOrder: Calculate amount & price
    Neutral --> WaitingForSignal: No action

    CreatingBuyOrder --> WaitingForSignal: Order submitted
    CreatingSellOrder --> WaitingForSignal: Order submitted

    WaitingForSignal --> Stopped: stop_trading_mode()
    Stopped --> Paused: pause_trader()
    Paused --> [*]
```

### Trading Mode Pause/Stop

The `ExchangeProducer` can stop all trading modes and pause traders through:

```
OctoBotAPI.stop_all_trading_modes_and_pause_traders(stop_reason, execution_details)
  --> ExchangeProducer.stop_all_trading_modes_and_pause_traders()
    --> send(STOP_EXCHANGE_TRADING_MODES_AND_PAUSE_TRADER) via OctoBotChannel
      --> Trading consumer handles the stop/pause action per exchange
```

This is used by the automation system (e.g., stop on drawdown) and community bot error handling.

## Exchange Connection States

```mermaid
stateDiagram-v2
    [*] --> Creating: ExchangeProducer.create_exchange()

    Creating --> Connecting: ExchangeManager initialized
    Connecting --> LoadingMarkets: Exchange connector ready
    LoadingMarkets --> LoadingSymbols: Markets loaded
    LoadingSymbols --> InitializingData: Symbols configured

    state InitializingData {
        [*] --> FetchingCandles
        FetchingCandles --> FetchingBalance
        FetchingBalance --> FetchingContracts
        FetchingContracts --> FetchingPrice
        FetchingPrice --> DataReady
    }

    DataReady --> Connected: All required topics initialized
    note right of Connected
        Required topics:
        - CANDLES
        - CONTRACTS
        - PRICE
        - BALANCE
    end note

    Connected --> Running: Start data feeds (WS/REST)

    Running --> Reconnecting: Connection lost
    Reconnecting --> Running: Reconnected
    Reconnecting --> Error: Max retries exceeded

    Running --> Stopping: stop_exchange()
    Stopping --> Stopped: Exchange resources released
    Stopped --> [*]

    Error --> Stopped: Force stop
```

### Exchange Creation Tracking

The `ExchangeProducer` tracks exchange creation progress:

```
to_create_exchanges_count: int  -- total exchanges to create
exchange_manager_ids: list[str] -- IDs of created exchanges
created_all_exchanges: asyncio.Event  -- set when all exchanges are created
```

When `len(exchange_manager_ids) == to_create_exchanges_count`, the `created_all_exchanges` event fires. This gates:
- Run metadata storage
- Automation initialization
- Community bot status reporting

## Order State Tracking

Orders go through states managed by `OctoBot-Trading`:

```mermaid
stateDiagram-v2
    [*] --> PendingCreation: Trading mode creates order

    PendingCreation --> Open: Order submitted to exchange
    PendingCreation --> Failed: Submission error

    Open --> PartiallyFilled: Partial execution
    PartiallyFilled --> Filled: Fully executed
    PartiallyFilled --> Canceling: Cancel requested

    Open --> Filled: Fully executed
    Open --> Canceling: Cancel requested
    Open --> Expired: TTL exceeded (if set)

    Canceling --> Canceled: Cancel confirmed
    Canceling --> Failed: Cancel failed

    Filled --> [*]
    Canceled --> [*]
    Failed --> [*]
    Expired --> [*]

    note right of Open
        Simulated orders fill
        immediately at market price
        in backtesting mode
    end note
```

## Configuration State Management

OctoBot maintains three versions of configuration simultaneously:

```mermaid
stateDiagram-v2
    [*] --> StartupConfig: Config loaded from disk

    state ConfigurationManager {
        StartupConfig: Startup Config\n(immutable reference)
        EditedConfig: Edited Config\n(modified by user/API)
        CurrentConfig: Current Config\n(active in OctoBot)
    }

    StartupConfig --> EditedConfig: Deep copy at startup
    StartupConfig --> CurrentConfig: Deep copy at startup

    EditedConfig --> SavedToDisk: User saves changes
    EditedConfig --> CurrentConfig: Bot restart applies changes

    note right of StartupConfig
        Read-only snapshot of
        config at bot start time
    end note

    note right of EditedConfig
        Modified through web UI
        or API calls. Not active
        until restart.
    end note
```

The `ConfigurationManager` tracks both `CONFIG_KEY` (global config) and `TENTACLES_SETUP_CONFIG_KEY` (tentacle activation) using `ConfigurationElement` instances that hold:
- `config` -- the original element
- `startup_config` -- deep copy at creation time
- `edited_config` -- deep copy that receives user modifications

## Backtesting State

```mermaid
stateDiagram-v2
    [*] --> Created: OctoBotBacktesting instantiated

    Created --> InitializingMatrix: initialize_and_run()
    InitializingMatrix --> InitializingBacktesting: Matrix created
    InitializingBacktesting --> InitializingEvaluators: Backtesting engine ready
    InitializingEvaluators --> ConfiguringTimeWindow: Evaluators initialized
    ConfiguringTimeWindow --> InitializingExchanges: Time window set
    InitializingExchanges --> CreatingEvaluators: Simulated exchanges created
    CreatingEvaluators --> Running: All evaluators started

    Running --> Completing: All historical data replayed
    Completing --> StoringMetadata: Store run results
    StoringMetadata --> Stopping: Metadata saved

    Stopping --> MemoryCheck: stop(memory_check=True)
    Stopping --> Stopped: stop(memory_check=False)
    MemoryCheck --> Stopped: No leaks detected
    MemoryCheck --> LeakWarning: References remain

    Stopped --> [*]

    Running --> Error: Exception during replay
    Error --> Stopping: Cleanup resources
```

## Automation State

```mermaid
stateDiagram-v2
    [*] --> Disabled: ENABLE_AUTOMATIONS=False

    [*] --> Loading: ENABLE_AUTOMATIONS=True
    Loading --> ConfigLoaded: Read automation config
    ConfigLoaded --> CreatingDetails: Parse trigger/condition/action

    state CreatingDetails {
        [*] --> ParseTrigger
        ParseTrigger --> ParseConditions
        ParseConditions --> ParseActions
        ParseActions --> DetailCreated
    }

    DetailCreated --> Running: asyncio.create_task()

    state Running {
        [*] --> WaitingForTrigger
        WaitingForTrigger --> TriggerFired: Event detected
        TriggerFired --> CheckingConditions: Evaluate conditions
        CheckingConditions --> ExecutingActions: All conditions met
        CheckingConditions --> WaitingForTrigger: Condition failed
        ExecutingActions --> WaitingForTrigger: Actions complete
    }

    Running --> Stopped: stop() / cancel tasks
    Running --> Restarting: restart()
    Restarting --> Loading: Stop then reload config

    Stopped --> [*]
    Disabled --> [*]
```

> **Note:** Order states (`PendingCreation`, `Open`, `PartiallyFilled`, `Filled`, `Canceling`, `Canceled`, `Failed`, `Expired`) are defined in the companion [`OctoBot-Trading`](https://github.com/Drakkar-Software/OctoBot-Trading) package, not in the core OctoBot repository. The order state machine above reflects the states managed by that package's order management system.

---
## See Also
- [README](README.md) — Project overview and quick start
- [Architecture](architecture.md) — System design and components
- [Workflow](workflow.md) — Event flows and processing pipelines
- [Development](development.md) — Development guide and best practices
