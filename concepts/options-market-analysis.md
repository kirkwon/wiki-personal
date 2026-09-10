---
date: 2026-07-19
type: concept
title: Options Market Analysis
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Finance
- Options
- Derivatives
- IV
- PutCall
- EventDriven
- finance
sources:
- hermes://skill/options-market-analysis
description: 'Analyze options chains for event-driven and directional trading: P/C
  ratio term structures, ATM IV extraction, IV skew, cross-asset divergence, and volume/OI
  decomposition. Uses OpenBB MCP derivatives tools.'
---

# Options Market Analysis

> Analyze options chains for event-driven and directional trading: P/C ratio term structures, ATM IV extraction, IV skew, cross-asset divergence, and volume/OI decomposition. Uses OpenBB MCP derivatives tools.

## Overview

- **When to Use** — - **Index rebalances** (SPCX → NDX, Tesla → S&P 500): What are passive funds forced to buy/sell? - **Earnings events**: Is the market pricing a big move? Which direction? - **IPO analysis**: What does the options market say about post-lock-up trajectory? - **Cross-asset risk**: Is the risk index-specific (QQQ) or market-wide (SPY)? - **Any event-driven trade**: Does options positioning confirm or contradict the fundamental thesis?
- **Data Retrieval: OpenBB MCP** — Options chains are fetched via the OpenBB MCP server's `derivatives_options_chains` tool.
- **Reusable Scripts & Templates** — - `scripts/fetch_options.py` — handles the full MCP handshake, fetches chains for multiple symbols, and outputs P/C ratios, IV stats, and top contracts. Modify the symbol list and run. - `templates/scenario-dashboard.html` — dark-themed interactive HTML dashboard template. Price input slider → live model recalculation → auto-updating stats, tables, and Chart.js charts. Copy, replace the model constants and chart data, open in browser. Used for SPCX NDX rebalance visualization (Jun 2026).

## Further detail

### Pitfalls

- **OpenBB MCP uses SSE transport** — not simple JSON-RPC. Must extract `mcp-session-id` from response **headers** (not body), send `notifications/initialized`, then parse SSE `data:` lines. See the reference file. - **yfinance options data can be stale on weekends/holidays** — always check `last_trade_time` timestamps. - **Yahoo Finance rate-limits aggressively** — if direct yfinance calls fail, use the OpenBB MCP server instead (it has its own rate limiting). - **IV values from yfinance can be >100%** for highly volatile names (SPCX at 320% IV for deep OTM). Always filter to ATM strikes. - *

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/options-market-analysis/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
