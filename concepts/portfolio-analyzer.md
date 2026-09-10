---
date: 2026-07-19
type: concept
title: Portfolio Analyzer
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/portfolio-analyzer
description: Analyze investment portfolios — concentration, allocation, tax efficiency,
  risk metrics, rebalancing needs. Runs the portfolio dashboard scripts and interprets
  results. Covers HHI concentration scores, TLH candidates, drift analysis, Sharpe
  ratios, and factor exposures. Trigger on phrases like "portfolio analysis", "portfolio
  health", "concentration", "allocation", "tax loss harvesting", "rebalance", "portfolio
  risk".
---

# Portfolio Analyzer

> Analyze investment portfolios — concentration, allocation, tax efficiency, risk metrics, rebalancing needs. Runs the portfolio dashboard scripts and interprets results. Covers HHI concentration scores, TLH candidates, drift analysis, Sharpe ratios, and factor exposures. Trigger on phrases like "portfolio analysis", "portfolio health", "concentration", "allocation", "tax loss harvesting", "rebalance", "portfolio risk".

## Overview

- **Architecture (as of 2026-07-18)** — **Data source:** `price_provider.py` is the single import point for all price/benchmark data. Never call yfinance or OpenBB directly in app code — always go through the provider.
- **Key Metrics** — | Metric | What It Tells You | |--------|-------------------| | HHI (Herfindahl) | Concentration risk — <100 diversified, >1000 concentrated | | TLH candidates | Tax-loss harvesting opportunities with estimated savings | | Drift by asset class | Current allocation vs target | | VaR/CVaR | Daily value-at-risk metrics | | Factor exposures | SPY/TLT/HYG/EEM/IWM betas | | Sharpe ratio | Risk-adjusted return |
- **⚠ IPS Drift Targets Are Placeholder Defaults** — The `/api/rebalance` endpoint reports drift against hardcoded IPS targets (35% US Equity / 30% FI / 15% Intl / 10% Cash / 5% RE / 5% Commodities). These are **generic placeholders**, not the user's actual Investment Policy Statement.

## Further detail

### Thesis-Driven Rebalancing (Correlation-First Workflow)

When the user asks for a **rebalance** (not a generic dashboard check), use this workflow. It validates the thesis with live correlation data before generating target weights and a trade plan. This is the opposite of the placeholder-IPS drift endpoint — the targets are *derived* from the current correlation regime, not assumed.

### portfolio.py API Quick Reference

The analyzer's `portfolio.py` has a specific data shape. These are the fields and functions that matter:

### yfinance Data Quirks (when used outside price_provider)

`price_provider.py` is the canonical import point. But for correlation/rebalance analysis that downloads proxy ETF series directly, these quirks bite:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/portfolio-analyzer/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
