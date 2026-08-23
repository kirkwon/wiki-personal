---
date: 2026-06-15
type: concept
title: Causal AI Pipeline
created: 2026-06-15
updated: 2026-06-15
tags: [finance, ai, inference, portfolio, methodology]
sources: [hermes-sessions]
confidence: high
---

# Causal AI Pipeline

Applied causal inference framework for portfolio risk management and factor analysis. Built from Pearl's Ladder of Causation, operationalized through DoWhy and EconML.

## Core Framework: DoWhy 4-Step

1. **Model** — encode causal assumptions as a directed acyclic graph (DAG)
2. **Identify** — determine if the causal effect is identifiable from observational data
3. **Estimate** — compute the causal effect using the identified estimand
4. **Refute** — validate with robustness checks (placebo, random common cause, data subset)

## EconML CATE

Conditional Average Treatment Effect estimation for regime-dependent portfolio effects. Uses double-ML and forest-based methods to estimate how treatment effects vary with covariates (market regimes, volatility states).

```python
# Pattern used in ~/portfolio/run_causal_real.py
from econml.dml import LinearDML
est = LinearDML(model_y=GradientBoostingRegressor(),
                model_t=GradientBoostingRegressor())
est.fit(Y, T, X=X, W=W)
treatment_effects = est.effect_inference(X_test)
```

## Application: SPY/TLT Analysis

Real data pipeline (replaces simulated data from early prototypes):

| Script | Purpose |
|--------|---------|
| `run_causal_real.py` | Yahoo Finance CSV download (no yfinance dependency) |
| `run_B_econml_cate.py` | EconML CATE on SPY/TLT data |
| `run_D_causal_discovery.py` | Causal structure discovery |

The `yf_download()` function uses the Yahoo Finance CSV API directly — avoids the broken `yfinance` package on Python 3.8 (multitasking compatibility issue).

## Decision Context

Decided 2026-06-03 to focus on **applied risk management + portfolio construction** over theory. Motivation: 5-10% allocation with sideways/peaking market conditions — causal methods help distinguish signal from regime-driven noise.

Learning path: Pearl Primer → DoWhy/EconML → finance-specific applications.

## Technical Details

- **Data:** SPY (market) + TLT (treasury) — causal pairs for regime detection
- **Self-Harness applied:** [[self-harness-paradigm]] methodology applied to `fetch_yf.py` and `pull_macro_data.py` — added CLI, logging, retry, deterministic fallback, modular functions
- **Blockers:** yfinance broken on Python 3.8, pip version parser crash, terminal tool intermittent blocking, delegate_task 600s timeout
- **Verification:** SHA256 hashes recorded for all scripts

## Connections

- [[loop-engineering]] — critic separation for backtest validation
- [[self-harness-paradigm]] — improvement methodology applied to financial scripts
- [[hermes-agent]] — the agent running the causal pipeline
