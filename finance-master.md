---
type: concept
title: Finance Master
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - uncategorized
---

# finance-master

"Meta-skill for financial analysis, portfolio management, options, and market modeling — pick the right analytical tool for any financial question."

## Usage

# finance-master

Meta-skill for financial analysis — portfolio monitoring, options, quantitative modeling, and market research.

Unlike knowledge-master (which is a pipeline), finance is a **toolkit** — each skill is a different analytical lens. Pick the right one for the question.

## Delegation Contract — Phase Discipline

Finance-master is a **toolkit** (not a pipeline), so the phase mapping is per-skill, not per-workflow-stage:

| Phase | Contract | Skills |
|---|---|---|
| **P1: Explore** | None — wide aperture | `catalyst-calendar` (events → candidates[]) |
| **P2: Sieve** | Light — ranking criteria | `mean-variance-analyzer`, `optionality-valuer`, `options-market-analysis` (candidates → ranked options) |
| **P3: Execute** | Strict — I/O schema | `portfolio-dashboard`, `portfolio-analyzer`, `causal-modeling`, `game-theoretic-finance-analysis` (data → verified output) |

**P3 contracts:**
- `portfolio-dashboard`: `{holdings[]}` → `{var_95, sharpe, allocation, pnl}`
- `causal-modeling`: `{data, treatment, outcome}` → `{ate, ci, regime_cate}`
- `game-theoretic-finance-analysis`: `{market_event, agent_types[]}` → `{dominant_strategies, distributions}`

## Decision Mechanisms

### A. What kind of financial question? (with Phase)

| User says | Phase | Contract | Dispatch to | I/O Shape |
|---|---|---|---|---|
| "How's my portfolio doing?" | P3 | Strict | `portfolio-dashboard` | `{holdings[]}` → `{var, sharpe, allocation}` |
| "Analyze my positions" | P3 | Strict | `portfolio-analyzer` | `{positions[]}` → `{eval_report}` |
| "What's the options chain look like?" | P2 | Light | `options-market-analysis` | `{symbol}` → `{pcr, skew, iv}` |
| "What's the efficient frontier?" | P2 | Light | `mean-variance-analyzer` | `{options[], probabilities[]}` → `{frontier, allocations}` |
| "What's the causal effect of X on Y?" | P3 | Strict | `causal-modeling` | `{data, treatment, outcome}` → `{ate, ci}` |
| "Simulate market dynamics" | P3 | Strict | `game-theoretic-finance-analysis` | `{event, agents[]}` → `{strategies, distributions}` |
| "What's this optionality worth?" | P2 | Light | `optionality-valuer` | `{choice, scenarios[]}` → `{option_value, recommendation}` |
| "Upcoming catalysts?" | P1 | None | `catalyst-calendar` | `{portfolio}` → `{events[]}` — deliberately loose |

### B. Decision Tree for Analysis Depth

```
"How's my portfolio?"
    ├── Quick check: portfolio-dashboard (live data, P&L, risk)
    └── Deep analysis: portfolio-analyzer (evaluation report)

"What's the market saying about X?"
    ├── Quant lens: mean-variance + optionality (is it worth it?)
    ├── Options lens: options-market-analysis (what's priced in?)
    ├── Causal lens: causal-modeling (what drives what?)
    └── Game lens: game-theoretic (how do agents interact?)

"Make a decision on X"
    ├── Know probabilities: mean-variance-analyzer
    ├── Know optionality: optionality-valuer
    ├── Know market structure: options-market-analysis
    └── Know second-order effects: game

...(truncated)