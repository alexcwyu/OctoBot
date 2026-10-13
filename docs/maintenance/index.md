# OctoBot: portable verification records

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `5cc86ef09d81da82a1227d590ba4ec7d374c0fa2` · [Current architecture and feature guide](../ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


These records retain exact commands, outcomes, original-log hashes and available source snapshots. Failed, interrupted and earlier exploratory commands remain visible. A later focused pass proves only its own scope.

[Machine-readable records](verification.json) · [Validation](../validation.md) · [Engineering guide](../ayu-develop.md)

Original logs remain in the workspace maintenance evidence. Tracked source hashes exclude untracked additions and later edits, as stated in each captured snapshot.

| Check | Exit | Duration | Command |
| --- | ---: | ---: | --- |
| build | 0 | 1.0s | `uv build --python 3.15` |
| compile | 0 | 0.13s | `<workspace>/OctoBot-Backtesting/.venv/bin/python -m compileall -q src` |
| final-build-2 | 0 | 0.97s | `uv build --python 3.15.0` |
| final-build | 0 | 1.49s | `uv build --python 3.15.0` |
| final-compile-2 | 0 | 0.08s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.09s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.46s | `uv lock --upgrade` |
| final-lock | 0 | 0.25s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` |
| final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` |
| lock-3.15 | 0 | 1.42s | `uv lock --upgrade --python 3.15` |
| public-manager-sync | 0 | 0.56s | `uv sync --all-extras --python 3.15` |
| sync-3.15 | 0 | 2.28s | `uv sync --all-extras --python 3.15` |
| tests-2 | 0 | 6.59s | `.venv/bin/python -m pytest tests` |
| tests-3 | 0 | 2.51s | `.venv/bin/python -m pytest tests` |
| tests | 2 | 1.97s | `<workspace>/OctoBot-Backtesting/.venv/bin/python -m pytest tests` |
| build | 0 | 1.0s | `uv build --python 3.15` |
| compile | 0 | 0.18s | `<workspace>/OctoBot-Commons/.venv/bin/python -m compileall -q src` |
| counter-final-tests | 0 | 14.27s | `.venv/bin/python -m pytest tests` |
| final-build-2 | 0 | 1.04s | `uv build --python 3.15.0` |
| final-build | 0 | 1.52s | `uv build --python 3.15.0` |
| final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.4s | `uv lock --upgrade` |
| final-lock | 0 | 0.19s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.04s | `uv sync --all-extras --frozen --python 3.15.0` |
| final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` |
| lock-3.15 | 0 | 0.28s | `uv lock --upgrade --python 3.15` |
| sync-3.15 | 0 | 0.94s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 3.2s | `.venv/bin/python -m pytest tests` |
| tests-3 | 1 | 29.49s | `.venv/bin/python -m pytest tests` |
| tests-4 | 1 | 31.8s | `.venv/bin/python -m pytest tests` |
| tests-5 | 1 | 19.59s | `.venv/bin/python -m pytest tests` |
| tests-6 | 0 | 14.69s | `.venv/bin/python -m pytest tests` |
| tests | 2 | 3.4s | `<workspace>/OctoBot-Commons/.venv/bin/python -m pytest tests` |
| tls-diagnostic | 0 | 4.24s | `.venv/bin/python -m pytest tests/test_aiohttp_util.py tests/test_async_job.py::test_run_stop_run -s --log-cli-level INFO` |
| build | 0 | 1.04s | `uv build --python 3.14` |
| compile | 0 | 0.13s | `<workspace>/OctoBot-Evaluators/.venv/bin/python -m compileall -q src` |
| directory-resource-sync | 0 | 0.77s | `uv sync --all-extras --python 3.14.8` |
| final-build-2 | 0 | 0.89s | `uv build --python 3.14.8` |
| final-build | 0 | 1.25s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.07s | `.venv/bin/python -m compileall -q src` |
| final-existing-tests-2 | 0 | 1.39s | `.venv/bin/python -m pytest tests` |
| final-existing-tests | 2 | 1.13s | `.venv/bin/python -m pytest tests` |
| final-lock-2 | 0 | 0.41s | `uv lock --upgrade` |
| final-lock | 0 | 0.25s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.56s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.08s | `uv sync --all-extras --frozen --python 3.14.8` |
| local-manager-sync | 0 | 1.85s | `uv sync --all-extras --python 3.14` |
| lock-3.14 | 0 | 0.88s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 1.37s | `uv lock --upgrade --python 3.15` |
| public-manager-sync | 0 | 1.12s | `uv sync --all-extras --python 3.14` |
| compile | 0 | 0.05s | `.venv/bin/python -Werror -m compileall -q src` |
| sync | 0 | 1.36s | `uv sync --all-extras --frozen --python 3.15.0` |
| build | 0 | 0.94s | `uv build --python 3.15.0` |
| compile | 0 | 0.13s | `/tmp/octobot-evaluators-final315-control/bin/python -Werror -m compileall -q src` |
| lock | 0 | 0.13s | `uv lock` |
| sync | 0 | 0.78s | `uv sync --all-extras --frozen --python 3.15.0` |
| tests | 0 | 3.52s | `/tmp/octobot-evaluators-final315-control/bin/python -m pytest tests --tb=short` |
| sync-3.14 | 0 | 1.37s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 2 | 0.04s | `uv sync --all-extras --python 3.15` |
| tests-2 | 1 | 8.46s | `.venv/bin/python -m pytest tests` |
| tests-3 | 2 | 2.19s | `.venv/bin/python -m pytest tests` |
| tests-4 | 2 | 2.16s | `.venv/bin/python -m pytest tests` |
| tests-5 | 2 | 2.15s | `.venv/bin/python -m pytest tests` |
| tests-6 | 1 | 3.34s | `.venv/bin/python -m pytest tests` |
| tests | 2 | 2.39s | `<workspace>/OctoBot-Evaluators/.venv/bin/python -m pytest tests` |
| updated-manager-sync | 0 | 0.61s | `uv sync --all-extras --python 3.14` |
| build | 0 | 1.01s | `uv build --python 3.13` |
| compile | 0 | 0.08s | `<workspace>/OctoBot-Market-Making/.venv/bin/python -m compileall -q src` |
| current-sync-2 | 0 | 2.14s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 0.61s | `uv sync --all-extras --python 3.14` |
| final-build-2 | 0 | 1.06s | `uv build --python 3.14.8` |
| final-build | 0 | 2.03s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.09s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.09s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.5s | `uv lock --upgrade` |
| final-lock | 0 | 0.58s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.59s | `uv sync --all-extras --frozen --python 3.14.8` |
| lock-3.13 | 0 | 0.77s | `uv lock --upgrade --python 3.13` |
| lock-3.14 | 0 | 0.34s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 1.64s | `uv lock --upgrade --python 3.15` |
| compile | 0 | 0.06s | `.venv/bin/python -Werror -m compileall -q src` |
| sync | 0 | 3.02s | `uv sync --all-extras --frozen --python 3.15.0` |
| build | 0 | 1.06s | `uv build --python 3.15.0` |
| compile | 0 | 0.08s | `/tmp/octobot-market-making-final315-control/bin/python -Werror -m compileall -q src` |
| lock | 0 | 1.9s | `uv lock` |
| sync | 0 | 1.41s | `uv sync --all-extras --frozen --python 3.15.0` |
| tests | 0 | 9.62s | `/tmp/octobot-market-making-final315-control/bin/python -m pytest tests --tb=short` |
| sync-3.13 | 1 | 7.62s | `uv sync --all-extras --python 3.13` |
| sync-3.14 | 1 | 3.9s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 5.22s | `uv sync --all-extras --python 3.15` |
| tests-2 | 3 | 34.54s | `.venv/bin/python -m pytest tests` |
| tests-3 | 0 | 9.86s | `.venv/bin/python -m pytest tests` |
| tests | 1 | 0.04s | `<workspace>/OctoBot-Market-Making/.venv/bin/python -m pytest tests` |
| build | 0 | 0.95s | `uv build --python 3.13` |
| compile | 0 | 0.08s | `<workspace>/OctoBot-Script/.venv/bin/python -m compileall -q src` |
| current-sync-2 | 0 | 0.97s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 0.4s | `uv sync --all-extras --python 3.14` |
| final-build-2 | 0 | 3.13s | `uv build --python 3.14.8` |
| final-build-3 | 0 | 2.68s | `uv build --python 3.14.8` |
| final-build | 0 | 5.09s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.49s | `uv lock --upgrade` |
| final-lock | 0 | 0.48s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 2.17s | `uv sync --all-extras --frozen --python 3.14.8` |
| lock-3.13 | 0 | 0.85s | `uv lock --upgrade --python 3.13` |
| lock-3.14 | 0 | 0.72s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 0.61s | `uv lock --upgrade --python 3.15` |
| report-build | 0 | 11.97s | `npm run build` |
| report-install | 0 | 24.44s | `npm ci` |
| compile | 0 | 0.05s | `.venv/bin/python -Werror -m compileall -q src` |
| sync | 0 | 3.16s | `uv sync --all-extras --frozen --python 3.15.0` |
| build | 0 | 2.5s | `uv build --python 3.15.0` |
| compile | 0 | 0.08s | `/tmp/octobot-script-final315-control/bin/python -Werror -m compileall -q src` |
| lock | 0 | 1.9s | `uv lock` |
| sync | 0 | 1.42s | `uv sync --all-extras --frozen --python 3.15.0` |
| tests | 0 | 18.4s | `/tmp/octobot-script-final315-control/bin/python -m pytest tests --tb=short` |
| sync-3.13 | 1 | 2.17s | `uv sync --all-extras --python 3.13` |
| sync-3.14 | 1 | 4.65s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 6.04s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 35.64s | `.venv/bin/python -m pytest tests` |
| tests-3 | 2 | 20.53s | `.venv/bin/python -m pytest tests` |
| tests-4 | 0 | 38.37s | `.venv/bin/python -m pytest tests` |
| tests | 1 | 0.04s | `<workspace>/OctoBot-Script/.venv/bin/python -m pytest tests` |
| api-collection-check | 0 | 7.85s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--collect-only','--tb=short']))` |
| archive-install-2 | 0 | 5.88s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` |
| archive-install | 1 | 5.34s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` |
| archive-pack-2 | 0 | 4.93s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` |
| archive-pack | 1 | 0.05s | `../OctoBot/.venv/bin/python -m octobot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` |
| bounded-current-api-full-tests | -15 | 901.69s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=60','--tb=short']))` |
| build | 0 | 3.43s | `uv build --python 3.15` |
| compile | 0 | 1.25s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m compileall -q src` |
| converted-mode-focused-tests-2 | 0 | 20.71s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Mode/dca_trading_mode/tests','tentacles/Trading/Mode/index_trading_mode/tests','tentacles/Trading/Mode/grid_trading_mode/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short']))` |
| converted-mode-focused-tests | 1 | 31.69s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Mode/dca_trading_mode/tests','tentacles/Trading/Mode/index_trading_mode/tests','tentacles/Trading/Mode/grid_trading_mode/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short']))` |
| current-api-archive-install | 0 | 6.44s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-archive-pack | 0 | 7.23s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-10 | 0 | 4.63s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-11 | 0 | 22.94s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-2 | 0 | 5.17s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-3 | 0 | 4.94s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-4 | 0 | 5.37s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-5 | 0 | 3.69s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-6 | 0 | 3.4s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-7 | 0 | 5.07s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-8 | 0 | 4.82s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-9 | 0 | 5.43s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export | 0 | 5.97s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-full-tests-2 | -15 | 914.82s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=90','--tb=short']))` |
| current-api-full-tests | -15 | 784.99s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| current-api-install-10 | 0 | 18.07s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-2 | 0 | 3.7s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-3 | 0 | 4.05s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-4 | 0 | 3.56s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-5 | 0 | 3.74s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-6 | 0 | 5.23s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-7 | 0 | 3.56s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-8 | 0 | 4.8s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-9 | 0 | 4.17s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install | 0 | 5.21s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-exchange-lock | 0 | 1.81s | `uv lock --upgrade` |
| current-exchange-sync | 0 | 0.75s | `uv sync --frozen --all-extras --python 3.14.8` |
| current-host-exchange-focused-tests | 1 | 53.8s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Evaluator/Strategies','tentacles/Meta/Keywords/scripting_library/tests/orders/order_types/test_multiple_orders_creation.py','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short','-p','bots_test_observer']))` |
| current-observed-existing-tests-2 | 1 | 297.96s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=120']))` |
| current-observed-existing-tests | -15 | 172.82s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=120']))` |
| current-sync | 0 | 5.27s | `uv sync --all-extras --python 3.14` |
| current-web-focused-tests-2 | 1 | 53.03s | `.venv/bin/python -m pytest tentacles/Services/Interfaces/web_interface/tests tentacles/Trading/Mode/trading_view_signals_trading_mode/tests tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py tentacles/Meta/Keywords/scripting_library/tests --tb=short` |
| current-web-focused-tests-3 | 1 | 52.89s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-4 | 1 | 38.84s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-5 | 1 | 37.67s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-6 | 1 | 68.37s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-7 | 1 | 47.12s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=60']))` |
| current-web-focused-tests | 1 | 5.21s | `.venv/bin/python -m pytest tentacles/Services/Interfaces/web_interface/tests --tb=short` |
| final-build-2 | 0 | 3.75s | `uv build --python 3.14.8` |
| final-build | 0 | 8.86s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.28s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 1.35s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.28s | `uv lock --upgrade` |
| final-lock | 0 | 0.31s | `uv lock --upgrade` |
| final-selected-python315-compile | 0 | Nones | `.venv/bin/python -Werror -m compileall -q src conftest.py` |
| final-selected-python315-sync | 0 | Nones | `uv sync --all-extras --frozen --python 3.15.0` |
| final-sync-2 | 0 | 0.49s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.18s | `uv sync --all-extras --frozen --python 3.14.8` |
| host-archive-install | 0 | 11.06s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| host-archive-pack | 0 | 9.33s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| host-complete-deps-lock | 0 | 2.98s | `uv lock --upgrade` |
| host-complete-deps-sync | 0 | 1.42s | `uv sync --all-extras --dev` |
| host-interface-lock | 0 | 2.19s | `uv lock --upgrade` |
| host-interface-sync | 0 | 1.74s | `uv sync --all-extras --frozen --python 3.14` |
| host-port-tests-2 | 1 | 100.85s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| host-port-tests | 1 | 2.99s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');import tests.test_utils.config;os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| installed-archive-tests | 1 | 18.28s | `<workspace>/OctoBot/.venv/bin/python -c import os,sys,pytest; os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors']))` |
| lock-3.15 | 0 | 0.24s | `uv lock --upgrade --python 3.15` |
| final-selected-python315-build | 0 | Nones | `uv build --python 3.15.0` |
| python315-complete-original-suite | 1 | 693.67s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tentacles --tb=short` |
| scripting-existing-tests | 1 | 6.24s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Meta/Keywords/scripting_library/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short','-p','bots_test_observer']))` |
| sync-3.15 | 0 | 0.61s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 30.72s | `.venv/bin/python -m pytest src/octobot_tentacles` |
| tests-3 | 2 | 20.43s | `.venv/bin/python -m pytest src/octobot_tentacles` |
| tests-helper-context | 1 | 6.93s | `.venv/bin/python -m pytest src/octobot_tentacles --continue-on-collection-errors` |
| tests | 2 | 4.01s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m pytest src/octobot_tentacles` |
| websocket-lifecycle-diagnostic-tests-2 | 1 | 86.86s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short']))` |
| websocket-lifecycle-diagnostic-tests-3 | 0 | 81.81s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short']))` |
| websocket-lifecycle-diagnostic-tests | 1 | 84.11s | `.venv/bin/python -c import os,sys,pytest,faulthandler;faulthandler.dump_traceback_later(45,repeat=True);sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-vv','-s']))` |
| websocket-lifecycle-existing-tests | -15 | 387.18s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=90','--tb=short']))` |
| allocation-diagnosis-tests | 1 | 2.69s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` |
| backend-compat-sync | 0 | 0.78s | `uv sync --all-extras --python 3.14.8` |
| backend-compat-tests | 1 | 58.41s | `.venv/bin/python -m pytest tests` |
| build | 0 | 2.28s | `uv build --python 3.14` |
| ccxt-current-tests | 1 | 60.83s | `.venv/bin/python -m pytest tests` |
| compile | 0 | 1.03s | `<workspace>/OctoBot-Trading/.venv/bin/python -m compileall -q src` |
| connection-diagnosis-tests | 1 | 1.97s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` |
| counter-focused-tests-2 | 1 | 2.54s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| counter-focused-tests-3 | 1 | 6.07s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| counter-focused-tests | 1 | 49.62s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| current-sync-2 | 1 | 0.05s | `uv sync --all-extras --python 3.14` |
| current-sync-3 | 1 | 0.09s | `uv sync --all-extras --python 3.14` |
| current-sync-4 | 1 | 0.08s | `uv sync --all-extras --python 3.14` |
| current-sync-5 | 0 | 0.88s | `uv sync --all-extras --python 3.14` |
| current-sync-6 | 0 | 0.78s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 32.8s | `uv sync --all-extras --python 3.14` |
| deadlock-diagnostic | 1 | 18.05s | `.venv/bin/python -m pytest tests/modes/test_abstract_mode_consumer.py::test_create_order_if_possible_ensure_no_deadlock_when_canceling_orders` |
| directory-resource-sync | 0 | 1.15s | `uv sync --all-extras --python 3.14.8` |
| final-build-2 | 0 | 1.55s | `uv build --python 3.14.8` |
| final-build-current | 0 | 1.41s | `uv build --python 3.14.8` |
| final-build | 0 | 2.99s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.12s | `.venv/bin/python -m compileall -q src` |
| final-compile-current | 0 | 0.18s | `.venv/bin/python -m compileall -q src vendor` |
| final-compile | 0 | 0.19s | `.venv/bin/python -m compileall -q src` |
| final-current-tests | 1 | 297.63s | `.venv/bin/python -m pytest tests` |
| final-existing-tests-2 | 0 | 150.7s | `.venv/bin/python -m pytest tests` |
| final-existing-tests | 1 | 66.7s | `.venv/bin/python -m pytest tests` |
| final-lock-2 | 0 | 0.23s | `uv lock --upgrade` |
| final-lock | 0 | 0.24s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.13s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.14.8` |
| fixture-owned-tests-2 | 1 | 292.57s | `.venv/bin/python -m pytest tests` |
| fixture-owned-tests | 4 | 0.61s | `.venv/bin/python -m pytest tests` |
| full-current-tests | 1 | 68.65s | `.venv/bin/python -m pytest tests` |
| lazy-positional-tests | 1 | 15.56s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| lock-3.14 | 0 | 0.46s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 6.15s | `uv lock --upgrade --python 3.15` |
| manager-owned-tests | 0 | 151.0s | `.venv/bin/python -m pytest tests` |
| public-manager-sync | 0 | 1.6s | `uv sync --all-extras --python 3.14` |
| scheduled-session-tests | 0 | 16.38s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| stopped-paused-tests | 1 | 15.08s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| sync-3.14 | 0 | 0.3s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 63.71s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 8.94s | `.venv/bin/python -m pytest tests` |
| tests-3 | 1 | 113.46s | `.venv/bin/python -m pytest tests` |
| tests-4 | 1 | 137.25s | `.venv/bin/python -m pytest tests` |
| tests-5 | 2 | 23.83s | `.venv/bin/python -m pytest tests` |
| tests-6 | 2 | 20.81s | `.venv/bin/python -m pytest tests` |
| tests-7 | 2 | 11.76s | `.venv/bin/python -m pytest tests` |
| tests | 2 | 18.96s | `<workspace>/OctoBot-Trading/.venv/bin/python -m pytest tests` |
| transport-abort-tests | 1 | 14.89s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| transport-diagnosis-tests | 1 | 117.64s | `.venv/bin/python -X tracemalloc=10 -m pytest tests/exchanges/traders/test_trader.py` |
| transport-lazy-tests | 1 | 66.04s | `.venv/bin/python -m pytest tests` |
| transport-owned-tests | 1 | 16.23s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| updated-manager-sync | 0 | 1.32s | `uv sync --all-extras --python 3.14` |
| build | 0 | 14.05s | `uv build --python 3.13` |
| client-current-tests-2 | 1 | 8.06s | `npm --prefix packages/client/octobot_client_ts test` |
| client-current-tests-3 | 0 | 4.61s | `npm --prefix packages/client/octobot_client_ts test` |
| client-current-tests | 1 | 3.67s | `npm --prefix packages/client/octobot_client_ts test` |
| client-latest-build | 0 | 0.5s | `npm --prefix packages/client/octobot_client_ts run build` |
| client-latest-tests | 1 | 8.8s | `npm --prefix packages/client/octobot_client_ts test` |
| client-npm-install-2 | 0 | 2.51s | `npm --prefix packages/client/octobot_client_ts install` |
| client-npm-install | 1 | 0.92s | `npm --prefix packages/client/octobot_client_ts install` |
| client-serial-tests | 1 | 29.5s | `npm --prefix packages/client/octobot_client_ts test -- --maxWorkers=1` |
| committed-extended-linter | 0 | 36.44s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| compile | 0 | 12.28s | `<workspace>/OctoBot/.venv/bin/python -m compileall -q src packages` |
| complete-sync | 0 | 4.42s | `uv sync --all-extras --python 3.14` |
| current-full-sync | 0 | 1.21s | `uv sync --all-extras --python 3.14.8` |
| current-host-strategy-baseline-tests | 1 | 27.27s | `.venv/bin/python -m pytest tentacles/Evaluator/Strategies/dip_analyser_strategy_evaluator/tests/test_dip_analyser_strategy_evaluator.py tentacles/Evaluator/Strategies/mixed_strategies_evaluator/tests/test_technical_analysis_strategy_evaluator.py --tb=short` |
| current-sync-2 | 0 | 0.13s | `uv sync --all-extras --python 3.14` |
| current-sync-3 | 0 | 1.15s | `uv sync --all-extras --python 3.14` |
| current-sync-4 | 0 | 1.58s | `uv sync --all-extras --python 3.14` |
| current-sync-5 | 0 | 1.04s | `uv sync --all-extras --python 3.14` |
| current-sync-6 | 0 | 3.22s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 2.55s | `uv sync --all-extras --python 3.14` |
| exchange-core-tests | 0 | 117.85s | `.venv/bin/python -m pytest tests` |
| exchange-final-build | 0 | 155.44s | `uv build --python 3.14` |
| exchange-final-compile | 0 | 1.9s | `.venv/bin/python -m compileall -q src packages` |
| extended-linter-2 | 1 | 0.45s | `.venv/bin/python -m tools.extended_linter --base origin/master` |
| extended-linter | 1 | 0.5s | `.venv/bin/python -m tools.extended_linter --base origin/master` |
| final-build-3 | 0 | 59.56s | `uv build --python 3.14.8` |
| final-build-current | 0 | 58.57s | `uv build --python 3.14.8` |
| final-build | 0 | 111.64s | `uv build --python 3.14.8` |
| final-compile-3 | 0 | 0.08s | `.venv/bin/python -m compileall -q src` |
| final-compile-current | 0 | 3.81s | `.venv/bin/python -m compileall -q src packages` |
| final-compile | 0 | 0.22s | `.venv/bin/python -m compileall -q src` |
| final-core-tests | 0 | 107.72s | `.venv/bin/python -m pytest tests` |
| final-extended-linter-2 | 1 | 20.25s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| final-extended-linter-3 | 0 | 38.84s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| final-extended-linter | 1 | 0.3s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| final-lock-2 | 0 | 0.39s | `uv lock --upgrade` |
| final-lock | 0 | 0.36s | `uv lock --upgrade` |
| final-selected-python315-compile | 0 | Nones | `.venv/bin/python -Werror -m compileall -q src packages` |
| final-selected-python315-sync | 0 | Nones | `uv sync --all-extras --frozen --python 3.15.0` |
| final-sync-2 | 0 | 0.08s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.84s | `uv sync --all-extras --frozen --python 3.14.8` |
| fixture-final-tests-2 | 0 | 68.36s | `.venv/bin/python -m pytest tests` |
| fixture-final-tests | 2 | 12.05s | `.venv/bin/python -m pytest tests` |
| frontend-build | 0 | 9.4s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-compatible-generator-2 | 0 | 1.03s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run generate-client` |
| frontend-compatible-generator-install | 0 | 3.57s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` |
| frontend-compatible-tests | 0 | 6.85s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |
| frontend-current-generator | 0 | 0.98s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run generate-client` |
| frontend-generated-build-2 | 0 | 2.85s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-generated-build | 1 | 0.93s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-generated-tests | 1 | 3.38s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |
| frontend-generator-api-install-2 | 0 | 1.61s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` |
| frontend-generator-api-install | 1 | 0.97s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` |
| frontend-latest-build | 1 | 0.77s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-latest-install | 0 | 11.47s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` |
| frontend-latest-tests | 0 | 4.56s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` |
| frontend-table9-build-2 | 0 | 3.23s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-table9-build | 1 | 1.26s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| frontend-table9-tests | 0 | 6.26s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |
| frontend-tests | 0 | 7.22s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` |
| frontend-ts7-build | 1 | 1.05s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` |
| latest-exchange-lock-2 | 0 | 13.07s | `uv lock --upgrade` |
| latest-exchange-lock | 0 | 1.58s | `uv lock --upgrade` |
| latest-exchange-sync-2 | 0 | 10.46s | `uv sync --all-extras --frozen --python 3.14` |
| latest-exchange-sync | -15 | 222.31s | `uv sync --all-extras --frozen --python 3.14` |
| latest-sync | 0 | 1.67s | `uv sync --all-extras --python 3.14` |
| lock-3.13 | 0 | 0.4s | `uv lock --upgrade --python 3.13` |
| lock-3.14 | 0 | 0.83s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 0.6s | `uv lock --upgrade --python 3.15` |
| maintenance-final-build | 0 | 21.06s | `uv build --python 3.14.8` |
| maintenance-final-compile | 0 | 1.83s | `uv run --frozen --all-extras python -m compileall -q src packages` |
| manager-import-existing-tests-2 | 0 | 10.45s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` |
| manager-import-existing-tests | 1 | 6.32s | `.venv/bin/python -m pytest packages/tentacles_manager/tests --tb=short` |
| manager-import-extended-linter | 0 | 29.62s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| manager-import-strict-compile | 0 | 0.14s | `uv run --frozen --all-extras python -W error -m compileall -q packages/tentacles_manager/octobot_tentacles_manager/api/inspector.py` |
| package-agents-exchange-tests | 0 | 13.14s | `.venv/bin/python -c import os,pytest;os.chdir('packages/agents');raise SystemExit(pytest.main(['tests']))` |
| package-agents-tests-current | 0 | 3.27s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-agents-tests | 2 | 11.14s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-async_channel-exchange-tests | 0 | 1.84s | `.venv/bin/python -c import os,pytest;os.chdir('packages/async_channel');raise SystemExit(pytest.main(['tests']))` |
| package-async_channel-tests-current | 0 | 0.6s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-async_channel-tests | 0 | 2.77s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-backtesting-exchange-tests | 0 | 13.47s | `.venv/bin/python -c import os,pytest;os.chdir('packages/backtesting');raise SystemExit(pytest.main(['tests']))` |
| package-backtesting-tests-current | 0 | 2.81s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-backtesting-tests | 1 | 11.49s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-commons-exchange-tests | 0 | 57.99s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` |
| package-commons-final-2 | 0 | 19.21s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` |
| package-commons-final | 1 | 33.51s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` |
| package-commons-tests-current | 1 | 20.07s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-commons-tests | 2 | 17.7s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-copy-current | 1 | 5.37s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` |
| package-copy-exchange-tests | 0 | 15.31s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` |
| package-copy-final-tests | 0 | 10.1s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` |
| package-copy-final | 0 | 3.61s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` |
| package-copy-tests-current | 1 | 3.89s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-copy-tests | 1 | 13.85s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-evaluators-exchange-tests | 0 | 15.93s | `.venv/bin/python -c import os,pytest;os.chdir('packages/evaluators');raise SystemExit(pytest.main(['tests']))` |
| package-evaluators-tests-current | 0 | 3.6s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-evaluators-tests | 0 | 13.29s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-flow-current-tests-2 | 1 | 76.83s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-current-tests | 1 | 68.59s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-exchange-tests | 0 | 148.08s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-final-2 | 1 | 8.59s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-final-3 | 1 | 19.95s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-final-4 | 1 | 72.46s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-final-tests | 1 | 102.95s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-final | 1 | 10.03s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` |
| package-flow-tests-current | 2 | 5.86s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-flow-tests | 2 | 20.68s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-manager-final-2 | 0 | 11.7s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` |
| package-manager-final | 1 | 12.52s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` |
| package-node-final-tests | 0 | 422.58s | `.venv/bin/python -c import os,pytest;os.chdir('packages/node');raise SystemExit(pytest.main(['tests']))` |
| package-node-tests-current | 1 | 652.61s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-node-tests | 1 | 660.54s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-services-exchange-tests | 0 | 10.91s | `.venv/bin/python -c import os,pytest;os.chdir('packages/services');raise SystemExit(pytest.main(['tests']))` |
| package-services-tests-current | 0 | 4.57s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-services-tests | 1 | 10.92s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-source-final-build | 0 | 13.96s | `uv build --python 3.14` |
| package-sync-current-tests | 1 | 20.63s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` |
| package-sync-exchange-tests | 0 | 24.78s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` |
| package-sync-final-tests | 0 | 10.98s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` |
| package-sync-tests-current | 1 | 14.09s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-sync-tests | 2 | 17.41s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-tentacles_manager-exchange-tests | 0 | 39.89s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` |
| package-tentacles_manager-tests-current | 1 | 3.38s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-tentacles_manager-tests | 1 | 14.49s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-trading-current-tests | 1 | 426.78s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-current | 1 | 92.44s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-exchange-tests-2 | 0 | 214.41s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-exchange-tests | 1 | 203.57s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-final-tests-2 | 0 | 197.25s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-final-tests | 1 | 248.11s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-owned-tests | 1 | 407.77s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` |
| package-trading-tests-current | 1 | 82.47s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| package-trading-tests | 1 | 156.02s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| protocol-codegen-tests-2 | 1 | 0.86s | `npm --prefix packages/protocol run test:postprocess:codegen` |
| protocol-codegen-tests-3 | 0 | 0.65s | `npm --prefix packages/protocol run test:postprocess:codegen` |
| protocol-codegen-tests | 1 | 1.43s | `npm --prefix packages/protocol run test:postprocess:codegen` |
| protocol-existing-tests | 0 | 2.83s | `.venv/bin/python -c import os,pytest;os.chdir('packages/protocol');raise SystemExit(pytest.main(['test']))` |
| protocol-latest-install | 0 | 3.57s | `npm --prefix packages/protocol install` |
| protocol-node-tests | 0 | 1.24s | `npm --prefix packages/protocol run test:postprocess` |
| python315-complete-host-root | 0 | 33.9s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| final-selected-python315-build | 0 | Nones | `uv build --python 3.15.0` |
| python315-package-tentacles_manager | 0 | 7.55s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-agents | 0 | 2.2s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-async_channel | 0 | 0.52s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-backtesting | 0 | 2.41s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-commons | 0 | 19.23s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-copy | 0 | 2.67s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-evaluators | 0 | 2.98s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-flow | 0 | 77.84s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-node | 0 | 355.56s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-services | 0 | 4.07s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-sync | 0 | 10.5s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| python315-package-trading | 0 | 185.96s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tests --tb=short` |
| OctoBot-python315-protocol-tests.log | 0 | 1.58s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest test --tb=short` |
| root-final-tests | 1 | 44.93s | `.venv/bin/python -m pytest tests` |
| root-tests-2 | 4 | 19.27s | `.venv/bin/python -m pytest tests` |
| root-tests-4 | 2 | 24.25s | `.venv/bin/python -m pytest tests` |
| root-tests-5 | 2 | 14.99s | `.venv/bin/python -m pytest tests` |
| root-tests-6 | 1 | 110.13s | `.venv/bin/python -m pytest tests` |
| root-tests-7 | 1 | 73.08s | `.venv/bin/python -m pytest tests` |
| root-tests | 4 | 13.89s | `.venv/bin/python -m pytest tests` |
| sync-3.13 | 1 | 2.03s | `uv sync --all-extras --python 3.13` |
| sync-3.14 | 1 | 2.23s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 3.84s | `uv sync --all-extras --python 3.15` |
| tentacles-install | 0 | 17.0s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles --install --location output/any_platform.zip --all` |
| tentacles-pack-2 | 255 | 10.79s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` |
| tentacles-pack-3 | 0 | 55.05s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` |
| tentacles-pack | 255 | 7.55s | `.venv/bin/python src/start.py tentacles -d packages/tentacles -p any_platform.zip` |
| tests-current-api | 1 | 43.62s | `.venv/bin/python -m pytest tests` |
| tests-markers | 1 | 44.71s | `.venv/bin/python -m pytest tests` |
| tests | 1 | 0.04s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` |
| websocket-final-build | 0 | 14.56s | `uv build` |
| websocket-final-compile | 0 | 0.14s | `uv run --no-sync python -W error -m compileall -q packages/trading/octobot_trading/exchanges packages/trading/octobot_trading/util/test_tools/websocket_test_tools.py` |
| websocket-final-extended-linter | 0 | 28.3s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` |
| websocket-helper-diagnostic-existing-tests | 0 | 51.08s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests/exchanges/test_abstract_websocket_exchange.py','tests/exchanges/implementations/test_default_websocket_exchange.py','tests/exchanges/types/test_websocket_exchange.py','tests/exchanges/connectors/ccxt','--tb=short']))` |
| websocket-lifecycle-build-2 | 0 | 14.73s | `uv build` |
| websocket-lifecycle-build | 0 | 14.34s | `uv build` |
| websocket-lifecycle-compile | 0 | 0.13s | `uv run --no-sync python -W error -m compileall -q packages/trading/octobot_trading/exchanges` |
| websocket-lifecycle-focused-tests-2 | 1 | 26.69s | `uv run --no-sync pytest packages/trading/tests/exchanges/test_abstract_websocket_exchange.py packages/trading/tests/exchanges/implementations/test_default_websocket_exchange.py packages/trading/tests/exchanges/types/test_websocket_exchange.py packages/trading/tests/exchanges/connectors/ccxt --tb=short` |
| websocket-lifecycle-focused-tests | 0 | 4.75s | `uv run --no-sync pytest packages/trading/tests/exchanges/test_abstract_websocket_exchange.py packages/trading/tests/exchanges/implementations/test_default_websocket_exchange.py packages/trading/tests/exchanges/types/test_websocket_exchange.py --tb=short` |
| websocket-lifecycle-package-tests-2 | 0 | 24.23s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests/exchanges/test_abstract_websocket_exchange.py','tests/exchanges/implementations/test_default_websocket_exchange.py','tests/exchanges/types/test_websocket_exchange.py','tests/exchanges/connectors/ccxt','--tb=short']))` |
| websocket-lifecycle-package-tests | 0 | 26.83s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests/exchanges/test_abstract_websocket_exchange.py','tests/exchanges/implementations/test_default_websocket_exchange.py','tests/exchanges/types/test_websocket_exchange.py','tests/exchanges/connectors/ccxt','--tb=short']))` |
