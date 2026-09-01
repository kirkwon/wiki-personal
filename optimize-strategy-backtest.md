---
type: concept
title: Optimize Strategy Backtest
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - trading
---

# optimize-strategy-backtest

>-

## Usage

# TradingView Strategy Backtest Optimizer

## Purpose

Drive the TradingView web chart end-to-end to iteratively optimize a Pine Script® strategy: open the Pine Editor, replace its contents with your strategy code, compile it onto the chart, read the Strategy Tester's backtest metrics, adjust the strategy's inputs, and repeat — searching for a parameter set that **minimizes Max Equity Drawdown** while **maximizing Net Return**. This is an agentic optimization loop, not a one-shot extraction: each iteration produces a (params → metrics) data point, and the agent does coordinate/grid search across the strategy's inputs to converge on the best risk-adjusted configuration.

**Read-only with respect to the user's account** (never Publish, never Save to the public library, never place a real Trade) — but it *does* require an authenticated TradingView session, because compiling any custom script onto the chart is gated behind sign-in.

## When to Use

- "Backtest this Pine strategy on AAPL/BTCUSD/ES and tune it for the best return-to-drawdown ratio."
- "Find MA-length + stop-loss settings that keep max drawdown under X% while staying net-profitable."
- Sweeping a strategy's `input.*` parameters and recording Net Profit / Max Equity Drawdown for each combination.
- Any flow that needs Strategy Tester metrics for a custom script. (Built-in indicator screening is a different, lighter task.)

## Workflow

`recommended_method: browser`. There is **no public API, URL deep-link, or MCP** for the Pine Editor or Strategy Tester — the chart is a heavyweight canvas/WebSocket app and the only surface. A bare (no-proxy, no-stealth) remote session loads the chart fine; no anti-bot was encountered. The one hard precondition is **authentication** (see Gotchas — every "Add to chart" path triggers a sign-in wall for a guest).

### 0. Precondition: be logged in

Reuse an authenticated browser context (persisted cookies / `browse cloud contexts`, or a session that has already completed TradingView sign-in). A guest session can open the chart and the Pine Editor and paste code, but **cannot compile a script onto the chart** — see Gotchas. Without a logged-in session this task cannot reach a single backtest metric.

### 1. Open the chart

```bash
sid=$(browse cloud sessions create --keep-alive | node -e "let s='';process.stdin.on('data',c=>s+=c).on('end',()=>process.stdout.write(JSON.parse(s).id))")
export BROWSE_SESSION="$sid"
browse open "https://www.tradingview.com/chart/" --remote
browse wait load --remote
# the canvas keeps streaming; give it a few seconds
sleep 5
```

Set the symbol/timeframe you want to backtest on *before* adding the strategy (top-left symbol search + the interval button, e.g. `button: 1 day`). The Strategy Tester backtests against whatever symbol+interval is loaded.

### 2. Open the Pine Editor

The editor is a right-rail toggle, **not** a bottom-footer tab on the default layout. `browse snapshot` and find `button: Pine` (the right-side icon rail) a

...(truncated)