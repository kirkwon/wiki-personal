---
type: note
title: Cron Environment Systemic Fixes
source: hermes-memory
recency: '2026-08-03T00:00:00.000Z'
frequency: high
offloaded: '2026-08-03T00:00:00.000Z'
importance: critical
truthfulness: verified
last_verified: '2026-08-03T00:00:00.000Z'
ingested_via: put_page
ingested_at: '2026-08-03T22:28:10.870Z'
source_kind: put_page
created: 2026-08-03
---
# Cron Environment Systemic Fixes

## FIX-008: gbrain not on cron PATH
- gbrain binary at ~/gbrain/bin/gbrain, NOT in ~/.local/bin
- Fix: symlink ~/.local/bin/gbrain → ~/gbrain/bin/gbrain
- Scope: 76 scripts, 20 active cron jobs

## FIX-009: PYTHONPATH poisoning across NLM/MCP scripts
- Hermes venv (Py3.11) PYTHONPATH leaks into nlm (Py3.12) subprocess
- pydantic_core ABI mismatch: ModuleNotFoundError
- Fix: `unset PYTHONPATH` in wrapper scripts
- 8 scripts patched: update-*-notebook.sh (5), weekly_macro_brief_p7.sh, notebooklm_to_gbrain.sh
- MCP SDK 2.0.0 removed decorators — pin mcp<2

## FIX-010: uv shebang missing --with deps
- Finance/cron scripts need: `uv run --with pandas --with yfinance --with numpy python`
- /usr/bin/python3 (3.9) ELIMINATED — all cron scripts use uv

## FIX-012: NLM→GBrain export compound fix
- Query timeout 300s, gbrain put timeout 60s
- no_agent=True on cron job bdc0a7bb8025
- All 4 notebooks: aiml-analysis, financial-strategy, loop-eng, wealth-synthesis

## Additional
- Wrappers need: `export PATH="$HOME/.local/bin:$PATH"`
- Fix-router: queue dedup + rotation (max 30)
- knowledge-eval threshold 900→2500
- Tracker: ~/clawd/decisions/cron-fix-tracker.md
- Sweep: job 1fe93561f006
