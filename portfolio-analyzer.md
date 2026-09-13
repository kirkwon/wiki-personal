---
type: concept
title: Portfolio Analyzer
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - finance
---

# portfolio-analyzer

>-

## Usage

# Portfolio Analyzer — Investment Portfolio Analysis

Analyze portfolio health using the dashboard at `~/portfolio/` (v1.2.0).

## Architecture (as of 2026-07-18)

```
~/portfolio/
├── dashboard/app.py        # Flask app, 10 API endpoints, port 5001
├── scripts/
│   ├── portfolio.py        # Holdings parser + TICKER_META
│   ├── price_provider.py   # Price data abstraction (OpenBB primary, yfinance fallback)
│   ├── generate_report.py  # Offline HTML report generator
│   └── extract_schwab.py   # Statement PDF/CSV extractor
├── statements/             # Parsed Schwab/Fidelity/JPM YAML statements
└── .venv/                  # Python 3.12, OpenBB 4.7.2
```

**Data source:** `price_provider.py` is the single import point for all price/benchmark data. Never call yfinance or OpenBB directly in app code — always go through the provider.

## Quick Start

```bash
cd ~/portfolio
.venv/bin/python scripts/portfolio.py
```

## Dashboard (port 5001)

```bash
# Check if running
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001

# Verify all 10 endpoints
for ep in prices allocation concentration tax performance rebalance catalyst risk compare; do
  curl -s -o /dev/null -w "$ep: %{http_code}\n" "http://127.0.0.1:5001/api/$ep"
done
curl -s -o /dev/null -w "benchmark: %{http_code}\n" "http://127.0.0.1:5001/api/benchmark/SPY"

# Open in browser
open http://127.0.0.1:5001
```

### Restart after code changes

```bash
lsof -ti:5001 | xargs kill -9 2>/dev/null; sleep 2
cd ~/portfolio && .venv/bin/python dashboard/app.py &
sleep 8 && curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001
```

## Key Metrics

| Metric | What It Tells You |
|--------|-------------------|
| HHI (Herfindahl) | Concentration risk — <100 diversified, >1000 concentrated |
| TLH candidates | Tax-loss harvesting opportunities with estimated savings |
| Drift by asset class | Current allocation vs target |
| VaR/CVaR | Daily value-at-risk metrics |
| Factor exposures | SPY/TLT/HYG/EEM/IWM betas |
| Sharpe ratio | Risk-adjusted return |

## ⚠ IPS Drift Targets Are Placeholder Defaults

The `/api/rebalance` endpoint reports drift against hardcoded IPS targets (35% US Equity / 30% FI / 15% Intl / 10% Cash / 5% RE / 5% Commodities). These are **generic placeholders**, not the user's actual Investment Policy Statement.

**Do not present drift alerts as actionable** without first confirming whether the targets reflect the user's thesis. The user's actual investment thesis (post-2022 regime: bonds too correlated to equities, prefers sector rotation + commodities as hedges) means the bond-heavy target is noise, not signal.

**Investment thesis:** `clawd/01.Signals-Macro/INVESTMENT-THESIS.md` / gbrain: `kirk-won-investment-thesis`

## Thesis-Driven Rebalancing (Correlation-First Workflow)

When the user asks for a **rebalance** (not a generic dashboard check), use this workflow. It validates the thesis with live correlation data before generating target weights and a trade plan. This is t

...(truncated)