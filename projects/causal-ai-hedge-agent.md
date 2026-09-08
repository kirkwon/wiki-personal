---
type: project
title: Causal AI & Hedge Agent
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P2
ingested_via: put_page
ingested_at: '2026-09-08T13:00:20.556Z'
source_kind: put_page
---

# Causal AI & Hedge Agent

## Summary
Applied causal inference (Pearl/DoWhy/EconML) for risk management and portfolio construction, building toward an autonomous causal hedge signal generator.

## Why
Traditional correlation-based risk fails in regime changes. Causal models provide counterfactual reasoning for hedging and portfolio construction in a 5-10% allocation, sideways/peaking market.

## Progress

- [x] Causal discovery script written and runs clean (`run_D_causal_discovery.py`, uses CSV API)
- [x] EconML CATE script written and runs clean (`run_B_econml_cate.py`, uses CSV)
- [x] Causal hedge agent plan created (`~/clawd/plans/2026-06-13-causal-hedge-agent.md`)
- [x] Finance MCP architecture mapped (`~/clawd/finance_mcp_project_mapping.md`)
- [x] FRED unblock plan created
- [x] Weekly hedge signal running (cron `60685b518206`)
- [x] Self-harness causal discovery plan (`~/clawd/plans/self-harness-causal-discovery.md`)
- [ ] Macro pipeline consolidation (plan exists: `2026-06-20-p2-macro-pipeline-consolidation.md`)
- [ ] Portfolio live data pipeline (plan exists: `2026-06-20-p3-portfolio-live-data.md`)
- [ ] SPCX live weights integration (plan exists: `2026-06-20-p4-spcx-live-weights.md`)
- [ ] Causal validation via NotebookLM (plan exists: `2026-06-20-p6-p7-causal-validation-notebooklm.md`)

## Next Steps
1. Consolidate macro pipeline (P2 plan ready)
2. Wire live data pipeline (P3 plan ready)
3. Integrate causal signals into Portfolio Dashboard
4. Validate causal models via NotebookLM cross-reference

## Blockers / Needs Input
- Python 3.8 (Anaconda) too old for MCP 3.10+ — symlink workaround exists but fragile
- yfinance broken on 3.8 — using CSV workaround; should migrate to Alpha Vantage MCP

## Key Files / Resources
- `~/clawd/plans/` — 6 detailed plans (causal hedge, FRED unblock, macro consolidation, live data, SPCX weights, validation)
- `~/clawd/run_D_causal_discovery.py` — causal discovery (working)
- `~/clawd/run_B_econml_cate.py` — EconML CATE (working)
- `~/clawd/hedge_signal.py` — weekly hedge signal
- `~/clawd/plans/self-harness-causal-discovery.md` — self-harness plan

## Automation / Cron
- `60685b518206` — Weekly Hedge Signal (Mon 9am)
- `7d77047f6b88` — Weekly Macro Brief → NotebookLM (Mon 7am)
- `547b7683a43e` — P7 Weekly Macro Brief (Mon 9am)
- `c3303354e3ec` — Update Financial Strategy Notebook (Mon 7am) ⚠️ ERROR

## Notes
- 5 detailed implementation plans from Jun 20 ready to execute when unblocked
- Pairs with Loop Engineering (autonomous quant loops) and Portfolio Dashboard
- Financial Strategy Notebook cron has error status — needs investigation
