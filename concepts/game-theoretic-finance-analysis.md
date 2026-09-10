---
date: 2026-07-19
type: concept
title: Game Theoretic Finance Analysis
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- finance
sources:
- hermes://skill/game-theoretic-finance-analysis
description: 'Agent-based market simulation for game-theoretic finance analysis. Hybrid
  model: rule-based agents for market microstructure (index funds, momentum, value,
  hedgers, market makers, retail, lock-up holders) + LLM-powered strategic agents
  for key decision-makers. Monte Carlo over hundreds of runs produces probability
  distributions of outcomes, dominant strategies, and tradeable signals. Inspired
  by MiroFish multi-agent simulation, adapted for financial markets per CWM pattern
  (Lehrach et al., 2025).'
---

# Game Theoretic Finance Analysis

> Agent-based market simulation for game-theoretic finance analysis. Hybrid model: rule-based agents for market microstructure (index funds, momentum, value, hedgers, market makers, retail, lock-up holders) + LLM-powered strategic agents for key decision-makers. Monte Carlo over hundreds of runs produces probability distributions of outcomes, dominant strategies, and tradeable signals. Inspired by MiroFish multi-agent simulation, adapted for financial markets per CWM pattern (Lehrach et al., 2025).

## Overview

- **When to Use** — - Index inclusion / rebalancing events (forced buying/selling dynamics) - Lock-up expiry analysis (insider selling pressure) - IPO trading strategies (squeeze mechanics) - Competitive dynamics modeling (multiple funds, strategic actors) - Any market situation where "who are the players and what are their incentives?" matters more than DCF
- **When NOT to Use** — - Single-stock fundamental valuation → use `dcf-model` or `comps-analysis` - Simple price prediction → use `earnings-analysis` - No strategic interaction (single player vs market) → use `options-market-analysis`
- **Agent Types** — | Agent Type | Capital Source | Decision Logic | LLM? | |-----------|---------------|----------------|------| | **Index Fund** | Index AUM | Mechanical: match target weight | No | | **Momentum** | ~5% of mcap | Trend-following with threshold | No | | **Value** | ~15% of mcap | Buy below fair value, sell above | No | | **Hedger** | ~3% of mcap | Delta-hedge, periodic rebalance | No | | **Market Maker** | ~1% of mcap | Provide liquidity, capture spread | No | | **Retail** | ~2% of mcap | Sentiment-driven noise | No | | **Lock-up Holder** | Restricted shares | Sell gradually post-unlock | No | |

## Further detail

### Game-Theoretic Interpretation

The simulation discovers the **emergent Nash equilibrium** of the market game:

### Calibration

The model should be calibrated against historical analogs:

### Limitations

1. **No options market** — the simulation models spot price only, not options Greeks 2. **Simplified order matching** — no limit order book depth modeling 3. **No cross-asset effects** — doesn't model spillover to other stocks (mega-cap trims) 4. **Strategic agents are heuristic** — not full LLM reasoning (upgrade path exists) 5. **No intraday dynamics** — each timestep is a full trading period 6. **Calibration needed** — parameters are estimated, not fitted to historical data 7. **Common-knowledge front-running** (v2 fix) — agents now anticipate other agents' anticipation, but the model still

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/game-theoretic-finance-analysis/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
