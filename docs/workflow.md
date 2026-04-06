# OctoBot Workflows

## Trading Signal Flow

The primary data flow in OctoBot goes from market data through evaluators and strategies to order execution.

```mermaid
sequenceDiagram
    participant Exchange as Exchange (ccxt)
    participant ExMgr as ExchangeManager
    participant DataChan as Trading Channels<br/>(OHLCV, Ticker, OrderBook)
    participant TAEval as TA Evaluator<br/>(RSI, MACD, etc.)
    participant RTEval as RealTime Evaluator
    participant SocEval as Social Evaluator
    participant Matrix as Evaluator Matrix
    participant Strategy as Strategy Evaluator
    participant TMode as Trading Mode
    participant Trader as Trader
    participant Notifier as Notifier

    Exchange->>ExMgr: Market data (REST/WebSocket)
    ExMgr->>DataChan: Publish OHLCV, ticker, order book

    par Evaluator Processing
        DataChan->>TAEval: Candle update
        TAEval->>Matrix: Update TA evaluation [-1, +1]

        DataChan->>RTEval: Real-time data
        RTEval->>Matrix: Update RT evaluation [-1, +1]

        SocEval->>Matrix: Update social evaluation [-1, +1]
    end

    Matrix->>Strategy: All evaluations updated
    Strategy->>Strategy: Combine evaluations
    Strategy->>Matrix: Final strategy signal

    Matrix->>TMode: Strategy signal received
    TMode->>TMode: Decide order type & size
    TMode->>Trader: Create order(s)
    Trader->>Exchange: Submit order
    Exchange-->>Trader: Order confirmation
    Trader->>Notifier: Order notification
    Notifier->>Notifier: Send to Telegram/Web/Email
```

## Key Workflows

### 1. Bot Initialization and Startup

```mermaid
sequenceDiagram
    participant CLI as CLI (cli.py)
    participant Config as Configuration
    participant Community as CommunityAuth
    participant Tentacles as TentaclesManager
    participant OB as OctoBot
    participant Init as Initializer
    participant TM as TaskManager
    participant GC as GlobalConsumer
    participant EP as ExchangeProducer
    participant EvP as EvaluatorProducer
    participant IP as InterfaceProducer
    participant SFP as ServiceFeedProducer

    CLI->>Config: Load config.json
    CLI->>Config: Load/create profile
    CLI->>Community: Authenticate (if cloud/saved session)
    CLI->>Tentacles: Load or install tentacles
    CLI->>Config: Apply forced configs (env vars, community)
    CLI->>Config: Health check (encryption, trader state)
    CLI->>OB: Create OctoBot instance

    OB->>Init: create(init_bot_storage=True)
    Init->>Tentacles: Load tentacles_setup_config
    Init->>Init: Initialize bot storage (databases)
    Init->>GC: initialize() - create OctoBotChannel

    GC->>GC: Register trading consumer
    GC->>GC: Register evaluator consumer
    GC->>GC: Register service consumer

    OB->>TM: start_tools_tasks()
    TM->>TM: Init aiohttp session
    TM->>TM: Start community handler task

    OB->>EvP: run() - Initialize evaluators
    EvP->>EvP: Create evaluator matrix
    EvP->>EvP: Create evaluator channels

    OB->>EP: run() - Create exchanges
    EP->>EP: For each enabled exchange: send CREATION event
    Note over GC: Trading consumer handles EXCHANGE creation

    OB->>SFP: run() - Create service feeds
    OB->>IP: run() - Create interfaces & notifiers
    IP->>IP: Start web interface
    IP->>IP: Start telegram interface

    OB->>OB: _post_initialize()
    OB->>OB: Start automation engine
    OB->>OB: Store run metadata
```

### 2. Evaluator to Trading Mode to Order

This is the core trading loop that runs continuously:

```mermaid
sequenceDiagram
    participant OHLCV as OHLCV Channel
    participant TA as TA Evaluator
    participant Matrix as Matrix
    participant Strategy as Strategy
    participant TMode as Trading Mode
    participant Creator as Order Creator
    participant Trader as Trader/Simulator

    OHLCV->>TA: New candle data
    TA->>TA: Calculate indicator (e.g., RSI)
    TA->>Matrix: set_eval(symbol, timeframe, value)
    Note over Matrix: Value in range [-1, +1]

    Matrix->>Strategy: Trigger strategy re-evaluation
    Strategy->>Matrix: Read all evaluator values
    Strategy->>Strategy: Weighted combination
    Strategy->>Matrix: set_eval(symbol, strategy_value)

    Matrix->>TMode: on_matrix_callback()
    TMode->>TMode: Interpret signal strength
    alt Strong Buy Signal (> threshold)
        TMode->>Creator: create_buy_order()
        Creator->>Trader: submit_order(BUY, amount, price)
    else Strong Sell Signal (< -threshold)
        TMode->>Creator: create_sell_order()
        Creator->>Trader: submit_order(SELL, amount, price)
    else Neutral
        Note over TMode: No action
    end
```

### 3. Market Data Collection

```mermaid
sequenceDiagram
    participant Config as Config
    participant EP as ExchangeProducer
    participant ExMgr as ExchangeManager
    participant REST as REST Updater
    participant WS as WebSocket Feed
    participant Chan as Data Channels

    EP->>ExMgr: Create exchange (name, config)
    ExMgr->>ExMgr: Initialize exchange connector (ccxt)
    ExMgr->>ExMgr: Load markets, symbols, timeframes

    alt WebSocket Available
        ExMgr->>WS: Start WebSocket connection
        WS->>Chan: Stream OHLCV, ticker, order book, trades
    else REST Only
        ExMgr->>REST: Start REST polling
        loop Periodic Fetch
            REST->>REST: Fetch OHLCV candles
            REST->>REST: Fetch ticker
            REST->>REST: Fetch order book
            REST->>Chan: Publish updates
        end
    end

    Chan->>Chan: Notify evaluator subscribers
```

### 4. Tentacle Loading and Initialization

```mermaid
sequenceDiagram
    participant CLI as CLI
    participant TM as TentaclesManager
    participant FS as File System
    participant Config as TentaclesSetupConfig
    participant Init as Initializer

    CLI->>FS: Check tentacles/ directory exists
    alt No tentacles directory
        CLI->>TM: install_all_tentacles()
        TM->>TM: Download tentacle package (zip)
        TM->>FS: Extract to tentacles/
        TM->>Config: Create default activation config
    else Tentacles exist
        CLI->>TM: Check version compatibility
        alt Version mismatch
            TM->>TM: Update tentacles
        end
    end

    CLI->>Config: Load profiles
    CLI->>Init: create()
    Init->>TM: get_tentacles_setup_config(path)
    TM->>Config: Read activation config
    TM->>Config: Read per-tentacle configs

    Note over Config: Tentacles now available<br/>for evaluator/trading mode creation
```

### 5. Backtesting Execution

```mermaid
sequenceDiagram
    participant User as User (CLI/Web)
    participant Factory as BacktestingFactory
    participant BT as OctoBotBacktesting
    participant Import as Data Importers
    participant Matrix as Evaluator Matrix
    participant Exchange as Simulated Exchange
    participant Eval as Evaluators
    participant TMode as Trading Mode
    participant Storage as Run Storage

    User->>Factory: Start backtesting(data_files, config)
    Factory->>BT: initialize_and_run()

    BT->>Matrix: Create evaluator matrix
    BT->>Import: Initialize backtesting importers
    Import->>Import: Load historical data files
    BT->>BT: Configure time window (start, end)

    BT->>Exchange: Create simulated exchange(s)
    BT->>Eval: Create and start evaluators
    BT->>BT: Create service feeds (if social data)

    BT->>Import: Start backtesting replay
    loop For each historical candle
        Import->>Exchange: Feed candle data
        Exchange->>Eval: Trigger evaluator updates
        Eval->>Matrix: Update evaluations
        Matrix->>TMode: Strategy signal
        TMode->>Exchange: Create simulated orders
        Exchange->>Exchange: Fill orders at simulated price
    end

    BT->>Storage: Store run metadata
    BT->>Storage: Store trade history
    BT->>BT: Memory leak checkup
    BT->>User: Return results (profitability, trades)
```

### 6. Strategy Evaluation Cycle

```mermaid
sequenceDiagram
    participant Data as Market Data
    participant TA1 as RSI Evaluator
    participant TA2 as MACD Evaluator
    participant TA3 as Bollinger Evaluator
    participant Social as Social Evaluator
    participant Matrix as Evaluator Matrix
    participant Strategy as Strategy Evaluator

    Data->>TA1: Price update
    Data->>TA2: Price update
    Data->>TA3: Price update

    TA1->>Matrix: RSI = 0.7 (overbought signal)
    TA2->>Matrix: MACD = 0.3 (bullish)
    TA3->>Matrix: BB = -0.2 (near lower band)
    Social->>Matrix: Sentiment = 0.5 (positive)

    Matrix->>Strategy: All evaluators updated for symbol+timeframe
    Strategy->>Strategy: Apply weights and combination logic
    Note over Strategy: weighted_avg = (0.7*w1 + 0.3*w2 - 0.2*w3 + 0.5*w4)
    Strategy->>Matrix: Final signal = 0.45 (moderate buy)
```

### 7. Web Interface Events

```mermaid
sequenceDiagram
    participant Browser as Browser
    participant WebIF as Web Interface
    participant API as OctoBotAPI
    participant OB as OctoBot
    participant Config as Configuration

    Browser->>WebIF: GET /dashboard
    WebIF->>API: get_exchange_manager_ids()
    WebIF->>API: get_trading_mode()
    WebIF-->>Browser: Dashboard data (portfolio, trades, signals)

    Browser->>WebIF: POST /config/update (change trading pair)
    WebIF->>API: get_edited_config()
    WebIF->>Config: Update edited config
    WebIF-->>Browser: Config saved, restart required

    Browser->>WebIF: POST /backtesting/start
    WebIF->>API: create_independent_backtesting()
    WebIF->>API: initialize_and_run_independent_backtesting()
    Note over WebIF: Backtesting runs asynchronously
    Browser->>WebIF: GET /backtesting/status
    WebIF-->>Browser: Progress, results

    Browser->>WebIF: POST /commands/restart
    WebIF->>API: restart_bot()
    API->>OB: task_manager.stop_tasks()
    Note over OB: Graceful shutdown and restart
```

## Event/Channel System

OctoBot uses a hierarchical channel system for inter-component communication:

```mermaid
graph TB
    subgraph OctoBotChannel["OctoBot Channel (High-Level)"]
        direction TB
        OC[OctoBotChannel]
        OC --> |"CREATION / NOTIFICATION"| TC[Trading Consumer]
        OC --> |"CREATION"| EC[Evaluator Consumer]
        OC --> |"CREATION / UPDATE"| SC[Service Consumer]
        OC --> |"*"| LC[Logger Consumer]
    end

    subgraph TradingChannels["Trading Channels (Per-Exchange)"]
        direction TB
        OHLCV[OHLCV Channel]
        Ticker[Ticker Channel]
        OBook[OrderBook Channel]
        Trades[Trades Channel]
        Orders[Orders Channel]
        Balance[Balance Channel]
        Positions[Positions Channel]
    end

    subgraph EvalChannels["Evaluator Channels"]
        direction TB
        EvalChan[Evaluator Channel<br/>per matrix_id]
        MatrixChan[Matrix Channel]
    end

    TC --> TradingChannels
    EC --> EvalChannels
```

### Channel Message Structure

Messages on the `OctoBotChannel` follow this format:

| Field | Type | Description |
|-------|------|-------------|
| `bot_id` | `str` | UUID identifying the bot instance |
| `subject` | `str` | `CREATION`, `UPDATE`, or `NOTIFICATION` |
| `action` | `str` | Specific action (e.g., `EXCHANGE`, `EVALUATOR`, `INTERFACE`) |
| `data` | `dict` | Action-specific payload |

### Consumer Routing

The `OctoBotChannelGlobalConsumer` dispatches messages based on action:

| Action | Handler | Effect |
|--------|---------|--------|
| `EXCHANGE` (notification) | `ExchangeProducer.register_created_exchange_id()` | Register new exchange, create evaluators for it |
| `EVALUATOR` (notification) | `ServiceFeedProducer.start_feeds()` | Start service feeds after evaluators register requirements |
| `INTERFACE` (notification) | `InterfaceProducer.register_interface()` | Register web/telegram interface |
| `NOTIFICATION` (notification) | `InterfaceProducer.register_notifier()` | Register notification handler |
| `SERVICE_FEED` (notification) | `ServiceFeedProducer.register_service_feed()` | Register service data feed |
| `EXCHANGE` (creation) | Trading consumer | Create ExchangeManager via OctoBot-Trading |
| `EVALUATOR` (creation) | Evaluator consumer | Create evaluator instances via OctoBot-Evaluators |
| `INTERFACE` (creation) | Service consumer | Create interface via OctoBot-Services |
| `STOP_EXCHANGE_TRADING_MODES` (update) | Trading consumer | Stop trading and pause trader on exchange |

### Automation Workflow

```mermaid
sequenceDiagram
    participant Auto as Automation Engine
    participant Trigger as Trigger Event
    participant Cond as Condition
    participant Action as Action
    participant Bot as OctoBotAPI

    Auto->>Auto: Load automation config
    Auto->>Auto: Create AutomationDetails<br/>(trigger, conditions, actions)

    loop Automation Task
        Auto->>Trigger: next_execution() [async generator]
        Trigger-->>Auto: ExecutionDetails (event occurred)
        
        loop Check Conditions
            Auto->>Cond: call_process(execution_details)
            alt Condition not met
                Note over Auto: Skip this event
            end
        end

        Note over Auto: All conditions met
        loop Execute Actions
            Auto->>Action: call_process(execution_details)
            Action->>Bot: Perform action (notify, stop, etc.)
        end
    end
```

---
## See Also
- [README](README.md) — Project overview and quick start
- [Architecture](architecture.md) — System design and components
- [State Management](state-management.md) — State lifecycle and data models
- [Development](development.md) — Development guide and best practices
