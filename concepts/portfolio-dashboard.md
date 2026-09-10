---
date: 2026-07-19
type: concept
title: Portfolio Dashboard
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- finance
sources:
- hermes://skill/portfolio-dashboard
description: Portfolio dashboard with Flask, OpenBB (primary) / yfinance (fallback)
  via price_provider.py abstraction, Chart.js. Live data overlays, allocation, concentration,
  tax, performance, and risk attribution analytics (VaR/CVaR, factor exposure, drawdowns,
  correlation matrix, Sharpe ratio). IPS targets are placeholder defaults — see pitfalls.
---

# Portfolio Dashboard

> Portfolio dashboard with Flask, OpenBB (primary) / yfinance (fallback) via price_provider.py abstraction, Chart.js. Live data overlays, allocation, concentration, tax, performance, and risk attribution analytics (VaR/CVaR, factor exposure, drawdowns, correlation matrix, Sharpe ratio). IPS targets are placeholder defaults — see pitfalls.

## Overview

- **GraphWork Methodology Integration** — When enhancing this dashboard, consider using GraphWork methodology: - Scaffold project with `graph_scaffold.py` for proper structure - Define clear nodes in GRAPH.md for each feature (analysis, theming, D3.js integration, tooltips, LikeC4 diagrams) - Set up enforced protocols in AGENTS.md (decision logging, activity logging, checklists) - Establish research pipeline (02.Research/incoming → refined) for gathering enhancement ideas - Define measurable exit criteria and ground truth verification (e.g., dashboard renders correctly at localhost:5001) - Implement loops for continuous improvement (w
- **When This Skill Activates** — Use this skill when the user: - Wants to build or enhance a portfolio dashboard - Needs real-time portfolio analytics with live price data - Requires risk attribution analysis (VaR, CVaR, factor exposure) - Asks for concentration metrics, tax-loss harvesting candidates, or performance visualization - Wants to integrate GBrain/wiki knowledge with portfolio data - Needs automated cron jobs for notebook/snapshot updates
- **Architecture** — **Tech Stack:** - **Backend:** Flask (Python) with OpenBB (primary) / yfinance (fallback) for live prices - **Price Data:** Provider abstraction layer (`scripts/price_provider.py`) — all consuming code imports from here, never calls yfinance/OpenBB directly. See `references/price-provider-abstraction.md` for the full pattern. - **Frontend:** HTML5 + Chart.js for visualization - **Data Source:** YAML statement snapshots from `~/portfolio/statements/` - **Database:** None (stateless API, file-based statements)

## Further detail

### API Endpoints

| Endpoint | Method | Returns | |----------|--------|---------| | `/` | GET | Dashboard HTML | | `/api/prices` | GET | Live prices for all tickers (with cache) | | `/api/allocation` | GET | Asset class, sector, account allocation | | `/api/concentration` | GET | Top holdings, HHI, sector risks | | `/api/tax` | GET | Unrealized P&L, TLH candidates | | `/api/tax/chart` | GET | P&L distribution data for bar chart (sorted by unrealized gain/loss) | | `/api/performance` | GET | Timeline, account series, totals | | `/api/performance/breakdown` | GET | Portfolio value over time broken down by asset c

### Regime Detection Integration

The dashboard's built-in "Market Regime Analysis" (Risk Tab) uses simple 20-day rolling volatility. For production regime gating, use the **Markov Regime Detection** module instead:

### Risk Thresholds (Configuration)

Modify in `risk_analysis.py` or `app.py`:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/portfolio-dashboard/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
