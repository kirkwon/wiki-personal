---
type: concept
title: Markov Regime Detection
ingested_via: put_page
ingested_at: '2026-07-22T00:44:29.709Z'
source_kind: put_page
created: 2026-07-22
---
# Markov Regime Detection

Detect Bull/Bear/Sideways regimes for ANY asset using observable Markov chains and optional Hidden Markov Models.

## Origin
- Framework: Roan (@RohOnChain)
- Source: https://x.com/ritonchain/status/2079554174623322367
- Adapted for Hermes: 2026-07-22

## What It Does
1. **Regime labeling** — Bull/Bear/Sideways from rolling returns (20-day window, ±5% threshold)
2. **Transition matrix** — 3×3 MLE Markov chain (P[regime_t+1 | regime_t])
3. **N-step forecast** — Chapman-Kolmogorov (P^n)
4. **Stationary distribution** — Long-run regime mix (left eigenvector)
5. **Walk-forward backtest** — No lookahead, O(n) incremental, Sharpe + maxDD
6. **Optional HMM** — Baum-Welch + Viterbi via hmmlearn (graceful degrade)

## Key Properties
- Asset-agnostic (stocks, ETFs, crypto, commodities, FX)
- Zero API keys (yfinance only)
- Signal is convex: `bull_prob - bear_prob` in [-1, 1]
- Stationary distribution reveals structural risk profile

## Verification (2026-07-22)
- SPY 10Y: Sharpe=0.272, MaxDD=-33.9%, HMM Bear=-0.168%/day
- Sector scan (12 assets): BTC Bull(+0.86), XLE Bull(+0.86), XLK Bear(-0.80)

## Location
- Module: ~/clawd/101.MarkovRegimeDetection/03.Scripts/markov_regime.py
- Scanner: ~/clawd/101.MarkovRegimeDetection/03.Scripts/sector_scanner.py
- Verify: ~/clawd/101.MarkovRegimeDetection/03.Scripts/verify_regime.py
- Skill: ~/.hermes/skills/finance/markov-regime-detection/SKILL.md

## Integrations
- portfolio-dashboard: signal as risk gate, position sizing by 1-bear_baseline
- finance-recommendation-verification: walk-forward Sharpe/maxDD as evidence
- mean-variance-analyzer: regime-aware covariance estimation
- options-market-analysis: block vol selling in Bear regime
