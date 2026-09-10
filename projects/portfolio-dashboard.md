---
type: project
title: Portfolio Dashboard
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P2
ingested_via: put_page
ingested_at: '2026-09-10T13:00:28.981Z'
source_kind: put_page
---

# Portfolio Dashboard

## Summary
Live portfolio dashboard (port 5001) with allocation, concentration, tax-loss harvesting, and performance views.

## Why
Centralize portfolio visibility across Schwab, Fidelity, Etrade, MS, JPM. Enable data-driven rebalancing and tax-loss harvesting decisions.

## Progress

- [x] Dashboard running (port 5001, launchd managed)
- [x] CLI `portfolio` (6 commands, pip install -e)
- [x] 30+ missing tickers backfilled, cost_basis=0 suppressed
- [x] Broker statements organized in `~/portfolio/statements/`
- [x] Reports: `portfolio-report.html`, `benchmark-report.html`
- [ ] Causal hedge agent integration (causal-hedge project)
- [ ] Live data pipeline (currently manual refresh)

## Next Steps
1. Wire Alpha Vantage MCP for live pricing (replace yfinance dependency)
2. Integrate causal hedge signals into dashboard
3. Add SPCX position tracking with NDX-100 inclusion countdown

## Blockers / Needs Input
- yfinance broken on Python 3.8 — using CSV workaround (legacy scripts)
- Causal validation deferred pending EconML/DoWhy integration

## Key Files / Resources
- `~/portfolio/` — main project dir
- `~/clawd/portfolio_scripts/` — older scripts (duplicate, to consolidate)
- `~/portfolio/statements/` — broker statements (Schwab, Fidelity, Etrade, MS, JPM)

## Automation / Cron
- `60685b518206` — Weekly Hedge Signal (Mon 9am)
- `531be4d2c050` — SPCX Daily Monitor (Mon-Fri 6:30am)

## Notes
- Stock price hierarchy: Alpha Vantage MCP > EDGAR MCP > local firecrawl. Do NOT use web search.
