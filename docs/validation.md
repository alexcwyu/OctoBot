# OctoBot: validation results

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `5cc86ef09d81da82a1227d590ba4ec7d374c0fa2` · [Current architecture and feature guide](ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


The current monorepo builds with managed Python **3.15.0**, uv **0.13.0** and current compatible locked dependencies. Complete native source builds, source-distribution-to-wheel builds and strict compilation pass. Source commit: `a77468479eda47d959afa87cef5ea1b216184921`. The older Python 3.14 fallback was superseded by the licensed Tulipy source build and pycares’ supported system c-ares configuration.

## Existing suites

5,240 supplied Python cases passed: 511 core, 4,550 package and 179 protocol cases. Sixteen pre-existing skips remain. The embedded frontend passed 897 Vitest cases, the TypeScript client passed 769, and protocol JavaScript tooling passed 22. Current frontend/client builds, Python wheel/source build and owned-source compilation passed. No new cases, skips or filters were added.

## Repairs and provenance

Current APIs replace removed aiohttp subclassing, database/context fixture contracts and TanStack Table interfaces. Test-owned exchange managers and HTTP sessions are stopped and closed; strict resource warning policy is preserved. The pairing-code distribution fixture still samples 4,000 genuinely random codes and generates real code-bound signatures; it reuses one real device identity and fixed valid KEM certificate only for this distribution check, restores them in a finally block, and retains the original statistical assertions and timeout. Separate identity and cryptography cases continue to generate real keys.

The current official OctoBot CCXT Git source is locked immutably because the latest published distribution lacks the required CoinRabbit connector. See [development](development.md) for the actual package and JavaScript workflows. The committed HEAD-based extended linter passed, including real tentacle packaging/install, OpenAPI generation and frontend build hooks. TypeScript 7.0.2 provides the native compiler via an npm alias; TypeScript 6.0.3 provides the generator AST API. HeyAPI 0.86.12 is the newest compatible line retaining the existing Axios/CancelablePromise client contract. Newer incompatible generator probes remain documented.

## Portable evidence

[Exact executed commands and outcomes](maintenance/index.html) · [Machine-readable verification](maintenance/verification.json) · [Offline engineering guide](ayu-develop.html). Failed exploratory runs are retained; later success applies only to the scope of the corresponding command.


## Final Python 3.15 scope

The complete original Python scope passed across its actual package working directories: **5,240 passed and 16 pre-existing skips**. This combines the 511 root cases, 4,550 package cases and 179 Python protocol cases; it is not a claim that a single root invocation collects every package. The separate frontend, TypeScript client and JavaScript protocol checks above retain their own exact recorded commands.

The selected main environment was synchronized frozen on Python 3.15 after an isolated complete-suite control, then strictly compiled. Native financial cases in the adjacent Tentacles repository also passed in the selected main environment with unchanged expected returns.

[Latest Tulipy provenance](../vendor/octobot-tulipy/PROVENANCE.md) records the original source, license, upstream revision, complete source manifest and strict floating-point compiler settings. These prevent ARM fused multiply/add differences from changing exact RSI decisions. No indicator formulas, fixture market data or financial golden values were changed.

The [Supabase client](../src/octobot/community/supabase_backend/supabase_client.py) closes HTTP clients retired by actual authentication callbacks. The [WebSocket feed owner](../packages/trading/octobot_trading/exchanges/connectors/ccxt/ccxt_websocket_connector.py) stops and awaits its real feed tasks before closing their shared client. See [development](development.md) for native prerequisites and [portable evidence](maintenance/index.md) for complete commands, prior failures and log hashes.
