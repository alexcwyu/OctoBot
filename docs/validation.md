# OctoBot: validation results

The current monorepo builds with managed Python 3.14.8, uv 0.13.0 and current compatible locked dependencies. Python 3.15 was attempted; the actual OctoBot-Tulipy native distribution requires the selected fallback.

## Existing suites

5,240 supplied Python cases passed: 511 core, 4,550 package and 179 protocol cases. Sixteen pre-existing skips remain. The embedded frontend passed 897 Vitest cases, the TypeScript client passed 769, and protocol JavaScript tooling passed 22. Current frontend/client builds, Python wheel/source build and owned-source compilation passed. No new cases, skips or filters were added.

## Repairs and provenance

Current APIs replace removed aiohttp subclassing, database/context fixture contracts and TanStack Table interfaces. Test-owned exchange managers and HTTP sessions are stopped and closed; strict resource warning policy is preserved. The pairing-code distribution fixture still samples 4,000 genuinely random codes and generates real code-bound signatures; it reuses one real device identity and fixed valid KEM certificate only for this distribution check, restores them in a finally block, and retains the original statistical assertions and timeout. Separate identity and cryptography cases continue to generate real keys.

The current official OctoBot CCXT Git source is locked immutably because the latest published distribution lacks the required CoinRabbit connector. See [development](development.md) for the actual package and JavaScript workflows. The committed HEAD-based extended linter passed, including real tentacle packaging/install, OpenAPI generation and frontend build hooks. TypeScript 7.0.2 provides the native compiler via an npm alias; TypeScript 6.0.3 provides the generator AST API. HeyAPI 0.86.12 is the newest compatible line retaining the existing Axios/CancelablePromise client contract. Newer incompatible generator probes remain documented.

## Portable evidence

[Exact executed commands and outcomes](maintenance/index.html) · [Machine-readable verification](maintenance/verification.json) · [Offline engineering guide](ayu-develop.html). Failed exploratory runs are retained; later success applies only to the scope of the corresponding command.
