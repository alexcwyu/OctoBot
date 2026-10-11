---
title: Maintenance validation
description: Exact local validation evidence and compatibility decisions.
---

# OctoBot maintenance validation

Recorded 2026-10-12T02:37:19.381314+08:00. Branch `feature/ayu_develop`; upstream default `upstream/master` is merged: **true**. Branch/tag synchronization records are retained in the workspace maintenance evidence. Feature branch publication is coordinated separately.

Runtime: **CPython 3.14.8**, uv **0.13.0**, build backend `hatchling.build`. Tulipy 0.4.11b13 has no Python 3.15 distribution; managed Python 3.14.8 is the complete binary-compatible environment.

Existing suite: **511 passed in 102.84s (0:01:42)** (exit `0`). All selected existing Python suites pass: 511 core tests, 4,550 package tests and 179 protocol tests (5,240 total), with 16 existing skips. The embedded frontend passes 897 existing Vitest tests and builds with TypeScript 7.0.2, Vite 8.3.4 and TanStack Table 9.2.8. The TypeScript client passes 769 existing tests; protocol JavaScript tooling passes 22 existing cases. The official exchange fork supplies the current CoinRabbit connector. Node/Flow fixture stores use the real AbstractObjectStore interface and fixtures close owned managers and HTTP sessions.

No test cases were added. Existing assertions and strict warning behavior remain active; repaired fixtures own their loops, sessions, files and configuration paths. Existing upstream platform skips and configured deselections are reported exactly.

## Final build commands

| Check | Exact command | Exit | Seconds |
| --- | --- | ---: | ---: |
| lock | `uv lock --upgrade` | 0 | 13.07 |
| sync | `uv sync --all-extras --frozen --python 3.14` | 0 | 10.46 |
| build | `uv build --python 3.14.8` | 0 | 21.06 |
| compile | `uv run --frozen --all-extras python -m compileall -q src packages` | 0 | 1.83 |

## Existing test and compatibility evidence

| Check | Exact command | Exit | Result |
| --- | --- | ---: | --- |
| lock-3.15 | `uv lock --upgrade --python 3.15` | 0 | Check completed; see exact exit code. |
| sync-3.15 | `uv sync --all-extras --python 3.15` | 1 | Check completed; see exact exit code. |
| tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | Check completed; see exact exit code. |
| latest-sync | `uv sync --all-extras --python 3.14` | 0 | Check completed; see exact exit code. |
| root-tests | `.venv/bin/python -m pytest tests` | 4 | Check completed; see exact exit code. |
| root-tests-2 | `.venv/bin/python -m pytest tests` | 4 | Check completed; see exact exit code. |
| tentacles-pack | `.venv/bin/python src/start.py tentacles -d packages/tentacles -p any_platform.zip` | 255 | Check completed; see exact exit code. |
| tentacles-pack-2 | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` | 255 | Check completed; see exact exit code. |
| tentacles-pack-3 | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` | 0 | Check completed; see exact exit code. |
| tentacles-install | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles --install --location output/any_platform.zip --all` | 0 | Check completed; see exact exit code. |
| root-tests-4 | `.venv/bin/python -m pytest tests` | 2 | 1 error in 8.41s |
| extended-linter | `.venv/bin/python -m tools.extended_linter --base origin/master` | 1 | Check completed; see exact exit code. |
| extended-linter-2 | `.venv/bin/python -m tools.extended_linter --base origin/master` | 1 | Check completed; see exact exit code. |
| root-tests-5 | `.venv/bin/python -m pytest tests` | 2 | 1 error in 4.40s |
| root-tests-6 | `.venv/bin/python -m pytest tests` | 1 | 56 failed, 454 passed, 1 error in 98.47s (0:01:38) |
| root-tests-7 | `.venv/bin/python -m pytest tests` | 1 | 56 failed, 454 passed, 1 error in 60.72s (0:01:00) |
| package-backtesting-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 28 failed, 50 passed in 8.60s |
| package-commons-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 2 | 6 errors in 13.06s |
| package-agents-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 2 | 2 errors in 6.86s |
| package-evaluators-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 86 passed in 5.48s |
| package-tentacles_manager-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | ================== 1 failed, 11 passed, 3 warnings in 11.59s =================== |
| package-copy-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 129 passed, 7 errors in 10.22s |
| package-node-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 38 failed, 957 passed, 3 skipped in 650.83s (0:10:50) |
| package-sync-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 2 | ========================= 5 warnings, 1 error in 5.37s ========================= |
| package-async_channel-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 55 passed in 1.55s |
| package-trading-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 66 failed, 1251 passed, 1 error in 147.70s (0:02:27) |
| package-services-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 3 failed, 16 passed in 0.92s |
| package-flow-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 2 | 3 errors in 9.82s |
| tests-markers | `.venv/bin/python -m pytest tests` | 1 | 9 failed, 502 passed in 39.53s |
| tests-current-api | `.venv/bin/python -m pytest tests` | 1 | 3 failed, 508 passed, 1 error in 39.24s |
| root-final-tests | `.venv/bin/python -m pytest tests` | 1 | 510 passed, 1 error in 40.98s |
| fixture-final-tests | `.venv/bin/python -m pytest tests` | 2 | 1 error in 3.25s |
| fixture-final-tests-2 | `.venv/bin/python -m pytest tests` | 0 | 511 passed in 60.17s (0:01:00) |
| package-backtesting-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 78 passed in 2.11s |
| package-commons-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 1 failed, 874 passed, 5 skipped in 18.96s |
| package-agents-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 14 passed in 2.31s |
| package-evaluators-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 86 passed in 1.63s |
| package-tentacles_manager-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | =================== 1 failed, 11 passed, 3 warnings in 2.56s =================== |
| package-copy-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 129 passed, 7 errors in 2.95s |
| package-node-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 25 failed, 970 passed, 3 skipped in 647.52s (0:10:47) |
| package-sync-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | ============ 10 failed, 310 passed, 1 skipped, 5 warnings in 10.51s ============ |
| package-async_channel-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 55 passed in 0.29s |
| package-trading-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 1 | 9 failed, 1309 passed in 80.50s (0:01:20) |
| package-services-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 0 | 19 passed in 1.46s |
| package-flow-tests-current | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -m pytest tests` | 2 | 3 errors in 2.46s |
| package-copy-current | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/copy'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 129 passed, 7 errors in 4.16s |
| package-trading-current | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 4 failed, 1313 passed, 1 error in 88.72s (0:01:28) |
| package-copy-final | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/copy'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 136 passed in 2.73s |
| package-flow-final | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | Check completed; see exact exit code. |
| package-manager-final | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/tentacles_manager'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | ================== 1 failed, 32 passed, 3 warnings in 10.39s =================== |
| final-core-tests | `.venv/bin/python -m pytest tests` | 0 | 511 passed in 92.75s (0:01:32) |
| package-commons-final | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/commons'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 1 failed, 874 passed, 5 skipped in 30.97s |
| package-flow-final-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | Check completed; see exact exit code. |
| package-flow-final-3 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 68 failed, 420 passed, 7 skipped in 10.19s |
| package-manager-final-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/tentacles_manager'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | ======================= 166 passed, 3 warnings in 10.77s ======================= |
| package-flow-final-4 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 22 failed, 466 passed, 7 skipped in 65.35s (0:01:05) |
| package-commons-final-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/commons'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 875 passed, 5 skipped in 17.83s |
| package-trading-owned-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 75 failed, 856 passed, 387 errors in 404.79s (0:06:44) |
| package-flow-current-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 12 failed, 476 passed, 7 skipped in 60.56s (0:01:00) |
| package-sync-current-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/sync'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | ============ 1 failed, 319 passed, 1 skipped, 5 warnings in 13.33s ============= |
| package-trading-current-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 4 failed, 1314 passed in 423.68s (0:07:03) |
| package-flow-current-tests-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 8 failed, 480 passed, 7 skipped in 65.09s (0:01:05) |
| package-sync-final-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/sync'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | ================== 320 passed, 1 skipped, 5 warnings in 7.07s ================== |
| package-trading-final-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 1 failed, 1317 passed in 236.60s (0:03:56) |
| package-copy-final-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/copy'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 136 passed in 6.67s |
| package-flow-final-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 3 failed, 485 passed, 7 skipped in 85.27s (0:01:25) |
| latest-exchange-lock | `uv lock --upgrade` | 0 | Check completed; see exact exit code. |
| package-trading-final-tests-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 1318 passed in 188.78s (0:03:08) |
| latest-exchange-sync | `uv sync --all-extras --frozen --python 3.14` | -15 | Check completed; see exact exit code. |
| latest-exchange-lock-2 | `uv lock --upgrade` | 0 | Check completed; see exact exit code. |
| latest-exchange-sync-2 | `uv sync --all-extras --frozen --python 3.14` | 0 | Check completed; see exact exit code. |
| package-agents-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/agents'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 14 passed in 8.27s |
| package-backtesting-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/backtesting'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 78 passed in 10.46s |
| package-evaluators-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/evaluators'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 86 passed in 6.53s |
| package-copy-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/copy'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 136 passed in 9.72s |
| package-tentacles_manager-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/tentacles_manager'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | ============================= 166 passed in 36.52s ============================= |
| package-async_channel-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/async_channel'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 55 passed in 0.72s |
| package-commons-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/commons'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 875 passed, 5 skipped in 55.16s |
| package-services-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/services'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 19 passed in 4.03s |
| package-sync-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/sync'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | ================= 320 passed, 1 skipped, 5 warnings in 16.46s ================== |
| package-flow-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/flow'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 488 passed, 7 skipped in 120.04s (0:02:00) |
| exchange-core-tests | `.venv/bin/python -m pytest tests` | 0 | 511 passed in 102.84s (0:01:42) |
| package-source-final-build | `uv build --python 3.14` | 0 | Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| frontend-tests | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` | 0 | Tests  897 passed (897) |
| package-trading-exchange-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 1 | 1 failed, 1317 passed in 198.49s (0:03:18) |
| package-node-final-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/node'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 995 passed, 3 skipped in 405.68s (0:06:45) |
| package-trading-exchange-tests-2 | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/trading'"'"');raise SystemExit(pytest.main(['"'"'tests'"'"']))'` | 0 | 1318 passed in 207.86s (0:03:27) |
| protocol-node-tests | `npm --prefix packages/protocol run test:postprocess` | 0 | ℹ tests 14; ℹ pass 14; ℹ fail 0; ℹ skipped 0 |
| protocol-existing-tests | `.venv/bin/python -c 'import os,pytest;os.chdir('"'"'packages/protocol'"'"');raise SystemExit(pytest.main(['"'"'test'"'"']))'` | 0 | ============================= 179 passed in 2.00s ============================== |
| protocol-codegen-tests | `npm --prefix packages/protocol run test:postprocess:codegen` | 1 | ℹ tests 8; ℹ pass 5; ℹ fail 3; ℹ skipped 0 |
| protocol-codegen-tests-2 | `npm --prefix packages/protocol run test:postprocess:codegen` | 1 | ℹ tests 8; ℹ pass 7; ℹ fail 1; ℹ skipped 0 |
| protocol-codegen-tests-3 | `npm --prefix packages/protocol run test:postprocess:codegen` | 0 | ℹ tests 8; ℹ pass 8; ℹ fail 0; ℹ skipped 0 |
| client-npm-install | `npm --prefix packages/client/octobot_client_ts install` | 1 | Check completed; see exact exit code. |
| client-npm-install-2 | `npm --prefix packages/client/octobot_client_ts install` | 0 | Check completed; see exact exit code. |
| protocol-latest-install | `npm --prefix packages/protocol install` | 0 | Check completed; see exact exit code. |
| frontend-latest-install | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` | 0 | Check completed; see exact exit code. |
| client-latest-build | `npm --prefix packages/client/octobot_client_ts run build` | 0 | Check completed; see exact exit code. |
| frontend-latest-build | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | 1 | Check completed; see exact exit code. |
| frontend-latest-tests | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` | 0 | Tests  897 passed (897) |
| client-latest-tests | `npm --prefix packages/client/octobot_client_ts test` | 1 | Tests  1 failed \| 768 passed (769) |
| client-serial-tests | `npm --prefix packages/client/octobot_client_ts test -- --maxWorkers=1` | 1 | Tests  1 failed \| 768 passed (769) |
| client-current-tests | `npm --prefix packages/client/octobot_client_ts test` | 1 | Tests  1 failed \| 768 passed (769) |
| frontend-table9-tests | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` | 0 | Tests  897 passed (897) |
| client-current-tests-2 | `npm --prefix packages/client/octobot_client_ts test` | 1 | Tests  1 failed \| 768 passed (769) |
| client-current-tests-3 | `npm --prefix packages/client/octobot_client_ts test` | 0 | Tests  769 passed (769) |

Raw logs remain in the workspace maintenance evidence directory. The [portable verification record](maintenance/verification.json) retains exact command arrays, exits, timing, runtime inventory and log filenames. Earlier failed attempts remain recorded and are not treated as successful final validation.

## Installed dependency versions

This is the selected environment after locked synchronization; isolated wheel build dependencies are resolved by the build backend and recorded in build output.

| Distribution | Version |
| --- | --- |
| aioboto3 | 15.5.0 |
| aiobotocore | 2.25.1 |
| aiodns | 4.0.4 |
| aiofiles | 25.1.0 |
| aiohappyeyeballs | 2.7.1 |
| aiohttp | 3.14.5 |
| aiohttp-fast-zlib | 0.3.0 |
| aioitertools | 0.13.0 |
| aiosignal | 1.4.0 |
| aiosqlite | 0.22.1 |
| annotated-doc | 0.0.5 |
| annotated-types | 0.8.0 |
| anyio | 4.15.1 |
| argon2-cffi | 25.1.0 |
| argon2-cffi-bindings | 26.1.0 |
| asgiref | 3.12.1 |
| asyncpraw | 8.0.3 |
| asyncprawcore | 4.0.0 |
| attrs | 26.1.0 |
| bcrypt | 5.0.0 |
| bitarray | 3.12.0 |
| blinker | 1.9.0 |
| boto3 | 1.40.61 |
| botocore | 1.40.61 |
| cachetools | 7.2.1 |
| certifi | 2026.6.17 |
| cffi | 2.0.0 |
| charset-normalizer | 3.4.7 |
| ckzg | 2.1.8 |
| click | 8.5.0 |
| clickhouse-connect | 1.10.0 |
| coingecko-openapi-client | 1.4.0 |
| colorlog | 6.12.0 |
| coverage | 7.16.2 |
| cryptography | 50.0.2 |
| Cython | 3.3.0 |
| cytoolz | 1.2.0 |
| dbos | 3.2.0 |
| defusedxml | 0.7.1 |
| deprecation | 2.1.0 |
| eth-account | 0.14.0 |
| eth-hash | 0.8.0 |
| eth-keyfile | 0.10.0 |
| eth-keys | 0.8.0 |
| eth-rlp | 3.0.0 |
| eth-typing | 6.0.0 |
| eth-utils | 6.0.0 |
| eth_abi | 6.0.0 |
| execnet | 2.1.2 |
| fastapi | 0.143.0 |
| Flask | 3.1.3 |
| flask-cors | 6.0.5 |
| Flask-Login | 0.6.3 |
| Flask-WTF | 1.3.0 |
| frozenlist | 1.8.0 |
| gmqtt | 0.8.0 |
| greenlet | 3.5.6 |
| h11 | 0.16.0 |
| h2 | 4.4.1 |
| hexbytes | 2.0.0 |
| hpack | 4.2.0 |
| httpcore | 1.0.9 |
| httpcore2 | 2.13.1 |
| httpx | 0.28.1 |
| httpx-sse | 0.4.3 |
| httpx2 | 2.13.1 |
| hyperframe | 6.1.0 |
| idna | 3.18 |
| iniconfig | 2.3.1 |
| itsdangerous | 2.2.0 |
| Jinja2 | 3.1.6 |
| jiter | 0.17.0 |
| jmespath | 1.1.0 |
| jsonschema | 4.26.0 |
| jsonschema-specifications | 2025.9.1 |
| lz4 | 4.4.5 |
| MarkupSafe | 3.0.4 |
| mcp | 1.30.0 |
| mnemonic | 0.21 |
| mock | 5.2.0 |
| multidict | 7.1.0 |
| numpy | 2.4.2 |
| octobot | 3.0.0b3 |
| octobot-ccxt | 4.5.68 |
| OctoBot-Tulipy | 0.4.11b13 |
| openai | 3.29.0 |
| opentelemetry-api | 1.45.1 |
| orjson | 3.11.9 |
| packaging | 26.3 |
| parsimonious | 0.10.0 |
| passlib | 1.7.4 |
| PGPy | 0.6.0 |
| pluggy | 1.6.0 |
| postgrest | 2.32.0 |
| propcache | 0.5.2 |
| protobuf | 7.36.2 |
| psutil | 7.2.2 |
| psycopg | 3.3.6 |
| psycopg-binary | 3.3.6 |
| py-ecc | 8.0.0 |
| pyasn1 | 0.6.4 |
| pycares | 5.1.0 |
| pycparser | 3.0 |
| pycryptodome | 3.24.0 |
| pydantic | 2.14.0 |
| pydantic-settings | 2.15.0 |
| pydantic_core | 2.50.0 |
| Pygments | 2.21.0 |
| PyJWT | 2.15.1 |
| pyngrok | 8.1.2 |
| pytest | 9.1.1 |
| pytest-asyncio | 1.4.0 |
| pytest-cov | 7.1.0 |
| pytest-timeout | 2.4.0 |
| pytest-xdist | 3.8.0 |
| python-dateutil | 2.9.0.post0 |
| python-dotenv | 1.2.4 |
| python-multipart | 0.0.32 |
| python-telegram-bot | 22.8 |
| pyunormalize | 18.0.0 |
| PyYAML | 6.0.3 |
| realtime | 2.32.0 |
| referencing | 0.37.0 |
| regex | 2026.9.29 |
| requests | 2.34.2 |
| rlp | 5.0.0 |
| rpds-py | 2026.9.1 |
| ruff | 0.17.0 |
| s3transfer | 0.14.0 |
| sentry-sdk | 2.71.0 |
| setuptools | 84.0.0 |
| simplifiedpytrends | 1.1.2 |
| six | 1.17.0 |
| sniffio | 1.3.1 |
| sortedcontainers | 2.4.0 |
| SQLAlchemy | 2.1.4 |
| sse-starlette | 3.5.0 |
| standard-imghdr | 3.13.0 |
| starfish-identities | 3.0.0a72 |
| starfish-keyring | 3.0.0a72 |
| starfish-protocol | 3.0.0a72 |
| starfish-replica | 3.0.0a72 |
| starfish-sdk | 3.0.0a72 |
| starfish-server | 3.0.0a72 |
| starfish-sharing | 3.0.0a72 |
| starfish-spaces | 3.0.0a72 |
| starlette | 1.7.0 |
| storage3 | 2.32.0 |
| StrEnum | 0.4.15 |
| supabase | 2.32.0 |
| supabase-auth | 2.32.0 |
| supabase-functions | 2.32.0 |
| tinydb | 4.9.0 |
| toolz | 1.2.0 |
| truststore | 0.10.4 |
| typing-inspection | 0.4.4 |
| typing_extensions | 4.16.0 |
| update_checker | 1.0.0 |
| urllib3 | 2.7.0 |
| uvicorn | 0.54.0 |
| uvloop | 0.22.1 |
| vaderSentiment | 3.3.2 |
| web3 | 8.0.0 |
| websockets | 15.0.1 |
| Werkzeug | 3.1.9 |
| wrapt | 1.17.3 |
| WTForms | 3.2.2 |
| yarl | 1.25.1 |
| zlib-ng | 1.0.0 |

See [architecture](ayu-develop.md) for source-linked component/sequence/workflow diagrams and [development](development.md) for reproducible uv commands.
