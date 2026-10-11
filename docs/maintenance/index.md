# OctoBot: portable verification records

Full raw logs are retained in the workspace maintenance evidence, not distributed here. Hashes identify those original logs. A successful build or selected test subset does not imply a full test-suite pass. Commands containing <workspace> describe the original execution environment.

[Machine-readable records](verification.json) · [Repository validation summary](../validation.md)

## Executed commands

| Check | Exit | Duration | Command | Outcomes |
| --- | ---: | ---: | --- | --- |
| Backtesting-build | 0 | 1.0s | `uv build --python 3.15` | Successfully built dist/octobot_backtesting-1.10.0.tar.gz<br>Successfully built dist/octobot_backtesting-1.10.0-py3-none-any.whl |
| Backtesting-compile | 0 | 0.13s | `<workspace>/OctoBot-Backtesting/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Backtesting-final-build | 0 | 1.49s | `uv build --python 3.15.0` | Successfully built dist/octobot_backtesting-1.10.0.tar.gz<br>Successfully built dist/octobot_backtesting-1.10.0-py3-none-any.whl |
| Backtesting-final-build-2 | 0 | 0.97s | `uv build --python 3.15.0` | Successfully built dist/octobot_backtesting-1.10.0.tar.gz<br>Successfully built dist/octobot_backtesting-1.10.0-py3-none-any.whl |
| Backtesting-final-compile | 0 | 0.09s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Backtesting-final-compile-2 | 0 | 0.08s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Backtesting-final-lock | 0 | 0.25s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Backtesting-final-lock-2 | 0 | 0.46s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Backtesting-final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` | See exit status; no test-count assertion. |
| Backtesting-final-sync-2 | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` | See exit status; no test-count assertion. |
| Backtesting-lock-3.15 | 0 | 1.42s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Backtesting-public-manager-sync | 0 | 0.56s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Backtesting-sync-3.15 | 0 | 2.28s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Backtesting-tests | 2 | 1.97s | `<workspace>/OctoBot-Backtesting/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Backtesting-tests-2 | 0 | 6.59s | `.venv/bin/python -m pytest tests` | 19 passed in 4.88s |
| Backtesting-tests-3 | 0 | 2.51s | `.venv/bin/python -m pytest tests` | 19 passed in 1.25s |
| Commons-build | 0 | 1.0s | `uv build --python 3.15` | Successfully built dist/octobot_commons-1.10.6.tar.gz<br>Successfully built dist/octobot_commons-1.10.6-py3-none-any.whl |
| Commons-compile | 0 | 0.18s | `<workspace>/OctoBot-Commons/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Commons-counter-final-tests | 0 | 14.27s | `.venv/bin/python -m pytest tests` | 322 passed in 13.66s |
| Commons-final-build | 0 | 1.52s | `uv build --python 3.15.0` | Successfully built dist/octobot_commons-1.10.6.tar.gz<br>Successfully built dist/octobot_commons-1.10.6-py3-none-any.whl |
| Commons-final-build-2 | 0 | 1.04s | `uv build --python 3.15.0` | Successfully built dist/octobot_commons-1.10.6.tar.gz<br>Successfully built dist/octobot_commons-1.10.6-py3-none-any.whl |
| Commons-final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Commons-final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Commons-final-lock | 0 | 0.19s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Commons-final-lock-2 | 0 | 0.4s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Commons-final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.15.0` | See exit status; no test-count assertion. |
| Commons-final-sync-2 | 0 | 0.04s | `uv sync --all-extras --frozen --python 3.15.0` | See exit status; no test-count assertion. |
| Commons-lock-3.15 | 0 | 0.28s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Commons-sync-3.15 | 0 | 0.94s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Commons-tests | 2 | 3.4s | `<workspace>/OctoBot-Commons/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Commons-tests-2 | 2 | 3.2s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Commons-tests-3 | 1 | 29.49s | `.venv/bin/python -m pytest tests` | 2 failed, 320 passed in 28.64s |
| Commons-tests-4 | 1 | 31.8s | `.venv/bin/python -m pytest tests` | 1 failed, 321 passed in 31.03s |
| Commons-tests-5 | 1 | 19.59s | `.venv/bin/python -m pytest tests` | 1 failed, 321 passed in 19.09s |
| Commons-tests-6 | 0 | 14.69s | `.venv/bin/python -m pytest tests` | 322 passed in 14.22s |
| Commons-tls-diagnostic | 0 | 4.24s | `.venv/bin/python -m pytest tests/test_aiohttp_util.py tests/test_async_job.py::test_run_stop_run -s --log-cli-level INFO` | ============================== 5 passed in 3.82s =============================== |
| Evaluators-build | 0 | 1.04s | `uv build --python 3.14` | Successfully built dist/octobot_evaluators-1.10.1.tar.gz<br>Successfully built dist/octobot_evaluators-1.10.1-py3-none-any.whl |
| Evaluators-compile | 0 | 0.13s | `<workspace>/OctoBot-Evaluators/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Evaluators-directory-resource-sync | 0 | 0.77s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| Evaluators-final-build | 0 | 1.25s | `uv build --python 3.14.8` | Successfully built dist/octobot_evaluators-1.10.1.tar.gz<br>Successfully built dist/octobot_evaluators-1.10.1-py3-none-any.whl |
| Evaluators-final-build-2 | 0 | 0.89s | `uv build --python 3.14.8` | Successfully built dist/octobot_evaluators-1.10.1.tar.gz<br>Successfully built dist/octobot_evaluators-1.10.1-py3-none-any.whl |
| Evaluators-final-compile | 0 | 0.07s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Evaluators-final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Evaluators-final-existing-tests | 2 | 1.13s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Evaluators-final-existing-tests-2 | 0 | 1.39s | `.venv/bin/python -m pytest tests` | 57 passed in 0.98s |
| Evaluators-final-lock | 0 | 0.25s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Evaluators-final-lock-2 | 0 | 0.41s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Evaluators-final-sync | 0 | 0.08s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Evaluators-final-sync-2 | 0 | 0.56s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Evaluators-local-manager-sync | 0 | 1.85s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Evaluators-lock-3.14 | 0 | 0.88s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| Evaluators-lock-3.15 | 0 | 1.37s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Evaluators-public-manager-sync | 0 | 1.12s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Evaluators-sync-3.14 | 0 | 1.37s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Evaluators-sync-3.15 | 2 | 0.04s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Evaluators-tests | 2 | 2.39s | `<workspace>/OctoBot-Evaluators/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Evaluators-tests-2 | 1 | 8.46s | `.venv/bin/python -m pytest tests` | 52 passed, 5 errors in 6.78s |
| Evaluators-tests-3 | 2 | 2.19s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Evaluators-tests-4 | 2 | 2.16s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Evaluators-tests-5 | 2 | 2.15s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Evaluators-tests-6 | 1 | 3.34s | `.venv/bin/python -m pytest tests` | 52 passed, 5 errors in 2.50s |
| Evaluators-updated-manager-sync | 0 | 0.61s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Market-Making-build | 0 | 1.01s | `uv build --python 3.13` | Successfully built dist/octobot_market_making-2.1.1.tar.gz<br>Successfully built dist/octobot_market_making-2.1.1-py3-none-any.whl |
| Market-Making-compile | 0 | 0.08s | `<workspace>/OctoBot-Market-Making/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Market-Making-current-sync | 0 | 0.61s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Market-Making-current-sync-2 | 0 | 2.14s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Market-Making-final-build | 0 | 2.03s | `uv build --python 3.14.8` | Successfully built dist/octobot_market_making-2.1.1.tar.gz<br>Successfully built dist/octobot_market_making-2.1.1-py3-none-any.whl |
| Market-Making-final-build-2 | 0 | 1.06s | `uv build --python 3.14.8` | Successfully built dist/octobot_market_making-2.1.1.tar.gz<br>Successfully built dist/octobot_market_making-2.1.1-py3-none-any.whl |
| Market-Making-final-compile | 0 | 0.09s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Market-Making-final-compile-2 | 0 | 0.09s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Market-Making-final-lock | 0 | 0.58s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Market-Making-final-lock-2 | 0 | 0.5s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Market-Making-final-sync | 0 | 0.59s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Market-Making-final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Market-Making-lock-3.13 | 0 | 0.77s | `uv lock --upgrade --python 3.13` | See exit status; no test-count assertion. |
| Market-Making-lock-3.14 | 0 | 0.34s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| Market-Making-lock-3.15 | 0 | 1.64s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Market-Making-sync-3.13 | 1 | 7.62s | `uv sync --all-extras --python 3.13` | See exit status; no test-count assertion. |
| Market-Making-sync-3.14 | 1 | 3.9s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Market-Making-sync-3.15 | 1 | 5.22s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Market-Making-tests | 1 | 0.04s | `<workspace>/OctoBot-Market-Making/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Market-Making-tests-2 | 3 | 34.54s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Market-Making-tests-3 | 0 | 9.86s | `.venv/bin/python -m pytest tests` | 1 passed in 6.63s |
| Script-build | 0 | 0.95s | `uv build --python 3.13` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| Script-compile | 0 | 0.08s | `<workspace>/OctoBot-Script/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Script-current-sync | 0 | 0.4s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Script-current-sync-2 | 0 | 0.97s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Script-final-build | 0 | 5.09s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| Script-final-build-2 | 0 | 3.13s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| Script-final-build-3 | 0 | 2.68s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| Script-final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Script-final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Script-final-lock | 0 | 0.48s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Script-final-lock-2 | 0 | 0.49s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Script-final-sync | 0 | 2.17s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Script-final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Script-lock-3.13 | 0 | 0.85s | `uv lock --upgrade --python 3.13` | See exit status; no test-count assertion. |
| Script-lock-3.14 | 0 | 0.72s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| Script-lock-3.15 | 0 | 0.61s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Script-report-build | 0 | 11.97s | `npm run build` | See exit status; no test-count assertion. |
| Script-report-install | 0 | 24.44s | `npm ci` | See exit status; no test-count assertion. |
| Script-sync-3.13 | 1 | 2.17s | `uv sync --all-extras --python 3.13` | See exit status; no test-count assertion. |
| Script-sync-3.14 | 1 | 4.65s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Script-sync-3.15 | 1 | 6.04s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Script-tests | 1 | 0.04s | `<workspace>/OctoBot-Script/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Script-tests-2 | 2 | 35.64s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Script-tests-3 | 2 | 20.53s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Script-tests-4 | 0 | 38.37s | `.venv/bin/python -m pytest tests` | ============================= 14 passed in 34.04s ============================== |
| Tentacles-archive-install | 1 | 5.34s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| Tentacles-archive-install-2 | 0 | 5.88s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| Tentacles-archive-pack | 1 | 0.05s | `../OctoBot/.venv/bin/python -m octobot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` | See exit status; no test-count assertion. |
| Tentacles-archive-pack-2 | 0 | 4.93s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` | See exit status; no test-count assertion. |
| Tentacles-build | 0 | 3.43s | `uv build --python 3.15` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| Tentacles-compile | 0 | 1.25s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Tentacles-current-api-archive-install | 0 | 6.44s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| Tentacles-current-api-archive-pack | 0 | 7.23s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` | See exit status; no test-count assertion. |
| Tentacles-current-sync | 0 | 5.27s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Tentacles-final-build | 0 | 8.86s | `uv build --python 3.14.8` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| Tentacles-final-build-2 | 0 | 3.75s | `uv build --python 3.14.8` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| Tentacles-final-compile | 0 | 1.35s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Tentacles-final-compile-2 | 0 | 0.28s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Tentacles-final-lock | 0 | 0.31s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Tentacles-final-lock-2 | 0 | 0.28s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Tentacles-final-sync | 0 | 0.18s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Tentacles-final-sync-2 | 0 | 0.49s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Tentacles-host-archive-install | 0 | 11.06s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| Tentacles-host-archive-pack | 0 | 9.33s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` | See exit status; no test-count assertion. |
| Tentacles-host-complete-deps-lock | 0 | 2.98s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Tentacles-host-complete-deps-sync | 0 | 1.42s | `uv sync --all-extras --dev` | See exit status; no test-count assertion. |
| Tentacles-host-interface-lock | 0 | 2.19s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Tentacles-host-interface-sync | 0 | 1.74s | `uv sync --all-extras --frozen --python 3.14` | See exit status; no test-count assertion. |
| Tentacles-host-port-tests | 1 | 2.99s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');import tests.test_utils.config;os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` | See exit status; no test-count assertion. |
| Tentacles-host-port-tests-2 | 1 | 100.85s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` | 43 failed, 386 passed, 13 errors in 97.39s (0:01:37) |
| Tentacles-installed-archive-tests | 1 | 18.28s | `<workspace>/OctoBot/.venv/bin/python -c import os,sys,pytest; os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors']))` | 25 failed, 95 passed, 43 errors in 16.46s |
| Tentacles-lock-3.15 | 0 | 0.24s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Tentacles-sync-3.15 | 0 | 0.61s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Tentacles-tests | 2 | 4.01s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| Tentacles-tests-2 | 2 | 30.72s | `.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| Tentacles-tests-3 | 2 | 20.43s | `.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| Tentacles-tests-helper-context | 1 | 6.93s | `.venv/bin/python -m pytest src/octobot_tentacles --continue-on-collection-errors` | 8 failed, 42 passed, 51 errors in 5.48s |
| Trading-allocation-diagnosis-tests | 1 | 2.69s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 failed, 1 passed in 1.28s |
| Trading-backend-compat-sync | 0 | 0.78s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| Trading-backend-compat-tests | 1 | 58.41s | `.venv/bin/python -m pytest tests` | 8 failed, 897 passed in 57.54s |
| Trading-build | 0 | 2.28s | `uv build --python 3.14` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| Trading-ccxt-current-tests | 1 | 60.83s | `.venv/bin/python -m pytest tests` | 8 failed, 888 passed, 10 errors in 59.93s |
| Trading-compile | 0 | 1.03s | `<workspace>/OctoBot-Trading/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Trading-connection-diagnosis-tests | 1 | 1.97s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 failed, 1 passed in 1.04s |
| Trading-counter-focused-tests | 1 | 49.62s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | See exit status; no test-count assertion. |
| Trading-counter-focused-tests-2 | 1 | 2.54s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | See exit status; no test-count assertion. |
| Trading-counter-focused-tests-3 | 1 | 6.07s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | 1 failed, 16 passed in 5.23s |
| Trading-current-sync | 0 | 32.8s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-current-sync-2 | 1 | 0.05s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-current-sync-3 | 1 | 0.09s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-current-sync-4 | 1 | 0.08s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-current-sync-5 | 0 | 0.88s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-current-sync-6 | 0 | 0.78s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-deadlock-diagnostic | 1 | 18.05s | `.venv/bin/python -m pytest tests/modes/test_abstract_mode_consumer.py::test_create_order_if_possible_ensure_no_deadlock_when_canceling_orders` | See exit status; no test-count assertion. |
| Trading-directory-resource-sync | 0 | 1.15s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| Trading-final-build | 0 | 2.99s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| Trading-final-build-2 | 0 | 1.55s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| Trading-final-build-current | 0 | 1.41s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| Trading-final-compile | 0 | 0.19s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Trading-final-compile-2 | 0 | 0.12s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| Trading-final-compile-current | 0 | 0.18s | `.venv/bin/python -m compileall -q src vendor` | See exit status; no test-count assertion. |
| Trading-final-current-tests | 1 | 297.63s | `.venv/bin/python -m pytest tests` | 2 failed, 903 passed in 296.07s (0:04:56) |
| Trading-final-existing-tests | 1 | 66.7s | `.venv/bin/python -m pytest tests` | 1 failed, 902 passed, 3 errors in 65.54s (0:01:05) |
| Trading-final-existing-tests-2 | 0 | 150.7s | `.venv/bin/python -m pytest tests` | 905 passed in 148.88s (0:02:28) |
| Trading-final-lock | 0 | 0.24s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Trading-final-lock-2 | 0 | 0.23s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| Trading-final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Trading-final-sync-2 | 0 | 0.13s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| Trading-fixture-owned-tests | 4 | 0.61s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-fixture-owned-tests-2 | 1 | 292.57s | `.venv/bin/python -m pytest tests` | 3 failed, 902 passed in 291.25s (0:04:51) |
| Trading-full-current-tests | 1 | 68.65s | `.venv/bin/python -m pytest tests` | 2 failed, 900 passed, 3 errors in 66.94s (0:01:06) |
| Trading-lazy-positional-tests | 1 | 15.56s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 14.00s |
| Trading-lock-3.14 | 0 | 0.46s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| Trading-lock-3.15 | 0 | 6.15s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| Trading-manager-owned-tests | 0 | 151.0s | `.venv/bin/python -m pytest tests` | 905 passed in 149.65s (0:02:29) |
| Trading-public-manager-sync | 0 | 1.6s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-scheduled-session-tests | 0 | 16.38s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 35 passed in 14.46s |
| Trading-stopped-paused-tests | 1 | 15.08s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 13.86s |
| Trading-sync-3.14 | 0 | 0.3s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| Trading-sync-3.15 | 1 | 63.71s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| Trading-tests | 2 | 18.96s | `<workspace>/OctoBot-Trading/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-tests-2 | 2 | 8.94s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-tests-3 | 1 | 113.46s | `.venv/bin/python -m pytest tests` | 16 failed, 888 passed, 1 error in 111.06s (0:01:51) |
| Trading-tests-4 | 1 | 137.25s | `.venv/bin/python -m pytest tests` | 8 failed, 897 passed in 134.71s (0:02:14) |
| Trading-tests-5 | 2 | 23.83s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-tests-6 | 2 | 20.81s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-tests-7 | 2 | 11.76s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| Trading-transport-abort-tests | 1 | 14.89s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 3 failed, 32 passed in 13.74s |
| Trading-transport-diagnosis-tests | 1 | 117.64s | `.venv/bin/python -X tracemalloc=10 -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 102.02s (0:01:42) |
| Trading-transport-lazy-tests | 1 | 66.04s | `.venv/bin/python -m pytest tests` | 6 failed, 896 passed, 5 errors in 64.97s (0:01:04) |
| Trading-transport-owned-tests | 1 | 16.23s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 3 failed, 32 passed in 14.67s |
| Trading-updated-manager-sync | 0 | 1.32s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| build | 0 | 14.05s | `uv build --python 3.13` | Successfully built dist/octobot-2.0.14.tar.gz<br>Successfully built dist/octobot-2.0.14-py3-none-any.whl |
| client-current-tests | 1 | 3.67s | `npm --prefix packages/client/octobot_client_ts test` |  Test Files  1 failed \| 49 passed (50)<br>      Tests  1 failed \| 768 passed (769) |
| client-current-tests-2 | 1 | 8.06s | `npm --prefix packages/client/octobot_client_ts test` |  Test Files  1 failed \| 49 passed (50)<br>      Tests  1 failed \| 768 passed (769) |
| client-current-tests-3 | 0 | 4.61s | `npm --prefix packages/client/octobot_client_ts test` |  Test Files  50 passed (50)<br>      Tests  769 passed (769) |
| client-latest-build | 0 | 0.5s | `npm --prefix packages/client/octobot_client_ts run build` | See exit status; no test-count assertion. |
| client-latest-tests | 1 | 8.8s | `npm --prefix packages/client/octobot_client_ts test` |  Test Files  1 failed \| 49 passed (50)<br>      Tests  1 failed \| 768 passed (769) |
| client-npm-install | 1 | 0.92s | `npm --prefix packages/client/octobot_client_ts install` | See exit status; no test-count assertion. |
| client-npm-install-2 | 0 | 2.51s | `npm --prefix packages/client/octobot_client_ts install` | See exit status; no test-count assertion. |
| client-serial-tests | 1 | 29.5s | `npm --prefix packages/client/octobot_client_ts test -- --maxWorkers=1` |  Test Files  1 failed \| 49 passed (50)<br>      Tests  1 failed \| 768 passed (769) |
| committed-extended-linter | 0 | 36.44s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| compile | 0 | 12.28s | `<workspace>/OctoBot/.venv/bin/python -m compileall -q src packages` | See exit status; no test-count assertion. |
| complete-sync | 0 | 4.42s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-full-sync | 0 | 1.21s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| current-sync | 0 | 2.55s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-2 | 0 | 0.13s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-3 | 0 | 1.15s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-4 | 0 | 1.58s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-5 | 0 | 1.04s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-6 | 0 | 3.22s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| exchange-core-tests | 0 | 117.85s | `.venv/bin/python -m pytest tests` | 511 passed in 102.84s (0:01:42) |
| exchange-final-build | 0 | 155.44s | `uv build --python 3.14` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| exchange-final-compile | 0 | 1.9s | `.venv/bin/python -m compileall -q src packages` | See exit status; no test-count assertion. |
| extended-linter | 1 | 0.5s | `.venv/bin/python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| extended-linter-2 | 1 | 0.45s | `.venv/bin/python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| final-build | 0 | 111.64s | `uv build --python 3.14.8` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| final-build-3 | 0 | 59.56s | `uv build --python 3.14.8` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| final-build-current | 0 | 58.57s | `uv build --python 3.14.8` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| final-compile | 0 | 0.22s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-3 | 0 | 0.08s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-current | 0 | 3.81s | `.venv/bin/python -m compileall -q src packages` | See exit status; no test-count assertion. |
| final-core-tests | 0 | 107.72s | `.venv/bin/python -m pytest tests` | 511 passed in 92.75s (0:01:32) |
| final-extended-linter | 1 | 0.3s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| final-extended-linter-2 | 1 | 20.25s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| final-extended-linter-3 | 0 | 38.84s | `uv run --frozen --all-extras python -m tools.extended_linter --base origin/master` | See exit status; no test-count assertion. |
| final-lock | 0 | 0.36s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-lock-2 | 0 | 0.39s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-sync | 0 | 0.84s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| final-sync-2 | 0 | 0.08s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| fixture-final-tests | 2 | 12.05s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| fixture-final-tests-2 | 0 | 68.36s | `.venv/bin/python -m pytest tests` | 511 passed in 60.17s (0:01:00) |
| frontend-build | 0 | 9.4s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-compatible-generator-2 | 0 | 1.03s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run generate-client` | See exit status; no test-count assertion. |
| frontend-compatible-generator-install | 0 | 3.57s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` | See exit status; no test-count assertion. |
| frontend-compatible-tests | 0 | 6.85s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |  Test Files  79 passed (79)<br>      Tests  897 passed (897) |
| frontend-current-generator | 0 | 0.98s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run generate-client` | See exit status; no test-count assertion. |
| frontend-generated-build | 1 | 0.93s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-generated-build-2 | 0 | 2.85s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-generated-tests | 1 | 3.38s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |  Test Files  15 failed \| 64 passed (79)<br>      Tests  775 passed (775) |
| frontend-generator-api-install | 1 | 0.97s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` | See exit status; no test-count assertion. |
| frontend-generator-api-install-2 | 0 | 1.61s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` | See exit status; no test-count assertion. |
| frontend-latest-build | 1 | 0.77s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-latest-install | 0 | 11.47s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface install` | See exit status; no test-count assertion. |
| frontend-latest-tests | 0 | 4.56s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` |  Test Files  79 passed (79)<br>      Tests  897 passed (897) |
| frontend-table9-build | 1 | 1.26s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-table9-build-2 | 0 | 3.23s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| frontend-table9-tests | 0 | 6.26s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test -- --run` |  Test Files  79 passed (79)<br>      Tests  897 passed (897) |
| frontend-tests | 0 | 7.22s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface test` |  Test Files  79 passed (79)<br>      Tests  897 passed (897) |
| frontend-ts7-build | 1 | 1.05s | `npm --prefix packages/tentacles/Services/Interfaces/node_web_interface run build` | See exit status; no test-count assertion. |
| latest-exchange-lock | 0 | 1.58s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| latest-exchange-lock-2 | 0 | 13.07s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| latest-exchange-sync | -15 | 222.31s | `uv sync --all-extras --frozen --python 3.14` | See exit status; no test-count assertion. |
| latest-exchange-sync-2 | 0 | 10.46s | `uv sync --all-extras --frozen --python 3.14` | See exit status; no test-count assertion. |
| latest-sync | 0 | 1.67s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| lock-3.13 | 0 | 0.4s | `uv lock --upgrade --python 3.13` | See exit status; no test-count assertion. |
| lock-3.14 | 0 | 0.83s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-3.15 | 0 | 0.6s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| maintenance-final-build | 0 | 21.06s | `uv build --python 3.14.8` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| maintenance-final-compile | 0 | 1.83s | `uv run --frozen --all-extras python -m compileall -q src packages` | See exit status; no test-count assertion. |
| package-agents-exchange-tests | 0 | 13.14s | `.venv/bin/python -c import os,pytest;os.chdir('packages/agents');raise SystemExit(pytest.main(['tests']))` | 14 passed in 8.27s |
| package-agents-tests | 2 | 11.14s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| package-agents-tests-current | 0 | 3.27s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 14 passed in 2.31s |
| package-async_channel-exchange-tests | 0 | 1.84s | `.venv/bin/python -c import os,pytest;os.chdir('packages/async_channel');raise SystemExit(pytest.main(['tests']))` | 55 passed in 0.72s |
| package-async_channel-tests | 0 | 2.77s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 55 passed in 1.55s |
| package-async_channel-tests-current | 0 | 0.6s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 55 passed in 0.29s |
| package-backtesting-exchange-tests | 0 | 13.47s | `.venv/bin/python -c import os,pytest;os.chdir('packages/backtesting');raise SystemExit(pytest.main(['tests']))` | 78 passed in 10.46s |
| package-backtesting-tests | 1 | 11.49s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 28 failed, 50 passed in 8.60s |
| package-backtesting-tests-current | 0 | 2.81s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 78 passed in 2.11s |
| package-commons-exchange-tests | 0 | 57.99s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` | 875 passed, 5 skipped in 55.16s |
| package-commons-final | 1 | 33.51s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` | 1 failed, 874 passed, 5 skipped in 30.97s |
| package-commons-final-2 | 0 | 19.21s | `.venv/bin/python -c import os,pytest;os.chdir('packages/commons');raise SystemExit(pytest.main(['tests']))` | 875 passed, 5 skipped in 17.83s |
| package-commons-tests | 2 | 17.7s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| package-commons-tests-current | 1 | 20.07s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 1 failed, 874 passed, 5 skipped in 18.96s |
| package-copy-current | 1 | 5.37s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` | 129 passed, 7 errors in 4.16s |
| package-copy-exchange-tests | 0 | 15.31s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` | 136 passed in 9.72s |
| package-copy-final | 0 | 3.61s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` | 136 passed in 2.73s |
| package-copy-final-tests | 0 | 10.1s | `.venv/bin/python -c import os,pytest;os.chdir('packages/copy');raise SystemExit(pytest.main(['tests']))` | 136 passed in 6.67s |
| package-copy-tests | 1 | 13.85s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 129 passed, 7 errors in 10.22s |
| package-copy-tests-current | 1 | 3.89s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 129 passed, 7 errors in 2.95s |
| package-evaluators-exchange-tests | 0 | 15.93s | `.venv/bin/python -c import os,pytest;os.chdir('packages/evaluators');raise SystemExit(pytest.main(['tests']))` | 86 passed in 6.53s |
| package-evaluators-tests | 0 | 13.29s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 86 passed in 5.48s |
| package-evaluators-tests-current | 0 | 3.6s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 86 passed in 1.63s |
| package-flow-current-tests | 1 | 68.59s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 12 failed, 476 passed, 7 skipped in 60.56s (0:01:00) |
| package-flow-current-tests-2 | 1 | 76.83s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 8 failed, 480 passed, 7 skipped in 65.09s (0:01:05) |
| package-flow-exchange-tests | 0 | 148.08s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 488 passed, 7 skipped in 120.04s (0:02:00) |
| package-flow-final | 1 | 10.03s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | See exit status; no test-count assertion. |
| package-flow-final-2 | 1 | 8.59s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | See exit status; no test-count assertion. |
| package-flow-final-3 | 1 | 19.95s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 68 failed, 420 passed, 7 skipped in 10.19s |
| package-flow-final-4 | 1 | 72.46s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 22 failed, 466 passed, 7 skipped in 65.35s (0:01:05) |
| package-flow-final-tests | 1 | 102.95s | `.venv/bin/python -c import os,pytest;os.chdir('packages/flow');raise SystemExit(pytest.main(['tests']))` | 3 failed, 485 passed, 7 skipped in 85.27s (0:01:25) |
| package-flow-tests | 2 | 20.68s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| package-flow-tests-current | 2 | 5.86s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| package-manager-final | 1 | 12.52s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` | ================== 1 failed, 32 passed, 3 warnings in 10.39s =================== |
| package-manager-final-2 | 0 | 11.7s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` | ======================= 166 passed, 3 warnings in 10.77s ======================= |
| package-node-final-tests | 0 | 422.58s | `.venv/bin/python -c import os,pytest;os.chdir('packages/node');raise SystemExit(pytest.main(['tests']))` | 995 passed, 3 skipped in 405.68s (0:06:45) |
| package-node-tests | 1 | 660.54s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 38 failed, 957 passed, 3 skipped in 650.83s (0:10:50) |
| package-node-tests-current | 1 | 652.61s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 25 failed, 970 passed, 3 skipped in 647.52s (0:10:47) |
| package-services-exchange-tests | 0 | 10.91s | `.venv/bin/python -c import os,pytest;os.chdir('packages/services');raise SystemExit(pytest.main(['tests']))` | 19 passed in 4.03s |
| package-services-tests | 1 | 10.92s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 3 failed, 16 passed in 0.92s |
| package-services-tests-current | 0 | 4.57s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 19 passed in 1.46s |
| package-source-final-build | 0 | 13.96s | `uv build --python 3.14` | Successfully built dist/octobot-3.0.0b3.tar.gz<br>Successfully built dist/octobot-3.0.0b3-py3-none-any.whl |
| package-sync-current-tests | 1 | 20.63s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` | ============ 1 failed, 319 passed, 1 skipped, 5 warnings in 13.33s ============= |
| package-sync-exchange-tests | 0 | 24.78s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` | ================= 320 passed, 1 skipped, 5 warnings in 16.46s ================== |
| package-sync-final-tests | 0 | 10.98s | `.venv/bin/python -c import os,pytest;os.chdir('packages/sync');raise SystemExit(pytest.main(['tests']))` | ================== 320 passed, 1 skipped, 5 warnings in 7.07s ================== |
| package-sync-tests | 2 | 17.41s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| package-sync-tests-current | 1 | 14.09s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | ============ 10 failed, 310 passed, 1 skipped, 5 warnings in 10.51s ============ |
| package-tentacles_manager-exchange-tests | 0 | 39.89s | `.venv/bin/python -c import os,pytest;os.chdir('packages/tentacles_manager');raise SystemExit(pytest.main(['tests']))` | ============================= 166 passed in 36.52s ============================= |
| package-tentacles_manager-tests | 1 | 14.49s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | ================== 1 failed, 11 passed, 3 warnings in 11.59s =================== |
| package-tentacles_manager-tests-current | 1 | 3.38s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | =================== 1 failed, 11 passed, 3 warnings in 2.56s =================== |
| package-trading-current | 1 | 92.44s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 4 failed, 1313 passed, 1 error in 88.72s (0:01:28) |
| package-trading-current-tests | 1 | 426.78s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 4 failed, 1314 passed in 423.68s (0:07:03) |
| package-trading-exchange-tests | 1 | 203.57s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 1 failed, 1317 passed in 198.49s (0:03:18) |
| package-trading-exchange-tests-2 | 0 | 214.41s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 1318 passed in 207.86s (0:03:27) |
| package-trading-final-tests | 1 | 248.11s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 1 failed, 1317 passed in 236.60s (0:03:56) |
| package-trading-final-tests-2 | 0 | 197.25s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 1318 passed in 188.78s (0:03:08) |
| package-trading-owned-tests | 1 | 407.77s | `.venv/bin/python -c import os,pytest;os.chdir('packages/trading');raise SystemExit(pytest.main(['tests']))` | 75 failed, 856 passed, 387 errors in 404.79s (0:06:44) |
| package-trading-tests | 1 | 156.02s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 66 failed, 1251 passed, 1 error in 147.70s (0:02:27) |
| package-trading-tests-current | 1 | 82.47s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | 9 failed, 1309 passed in 80.50s (0:01:20) |
| protocol-codegen-tests | 1 | 1.43s | `npm --prefix packages/protocol run test:postprocess:codegen` | See exit status; no test-count assertion. |
| protocol-codegen-tests-2 | 1 | 0.86s | `npm --prefix packages/protocol run test:postprocess:codegen` | See exit status; no test-count assertion. |
| protocol-codegen-tests-3 | 0 | 0.65s | `npm --prefix packages/protocol run test:postprocess:codegen` | See exit status; no test-count assertion. |
| protocol-existing-tests | 0 | 2.83s | `.venv/bin/python -c import os,pytest;os.chdir('packages/protocol');raise SystemExit(pytest.main(['test']))` | ============================= 179 passed in 2.00s ============================== |
| protocol-latest-install | 0 | 3.57s | `npm --prefix packages/protocol install` | See exit status; no test-count assertion. |
| protocol-node-tests | 0 | 1.24s | `npm --prefix packages/protocol run test:postprocess` | See exit status; no test-count assertion. |
| root-final-tests | 1 | 44.93s | `.venv/bin/python -m pytest tests` | 510 passed, 1 error in 40.98s |
| root-tests | 4 | 13.89s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| root-tests-2 | 4 | 19.27s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| root-tests-4 | 2 | 24.25s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| root-tests-5 | 2 | 14.99s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| root-tests-6 | 1 | 110.13s | `.venv/bin/python -m pytest tests` | 56 failed, 454 passed, 1 error in 98.47s (0:01:38) |
| root-tests-7 | 1 | 73.08s | `.venv/bin/python -m pytest tests` | 56 failed, 454 passed, 1 error in 60.72s (0:01:00) |
| sync-3.13 | 1 | 2.03s | `uv sync --all-extras --python 3.13` | See exit status; no test-count assertion. |
| sync-3.14 | 1 | 2.23s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| sync-3.15 | 1 | 3.84s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| tentacles-install | 0 | 17.0s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles --install --location output/any_platform.zip --all` | See exit status; no test-count assertion. |
| tentacles-pack | 255 | 7.55s | `.venv/bin/python src/start.py tentacles -d packages/tentacles -p any_platform.zip` | See exit status; no test-count assertion. |
| tentacles-pack-2 | 255 | 10.79s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` | See exit status; no test-count assertion. |
| tentacles-pack-3 | 0 | 55.05s | `env ALLOW_UNSIGNED_TENTACLES=true .venv/bin/OctoBot tentacles -d packages/tentacles -p any_platform.zip` | See exit status; no test-count assertion. |
| tests | 1 | 0.04s | `<workspace>/OctoBot/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-current-api | 1 | 43.62s | `.venv/bin/python -m pytest tests` | 3 failed, 508 passed, 1 error in 39.24s |
| tests-markers | 1 | 44.71s | `.venv/bin/python -m pytest tests` | 9 failed, 502 passed in 39.53s |
