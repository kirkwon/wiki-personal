---
tags: [causal, ai, finance, portfolio, hedge, risk, results]
created: 2026-06-15
date: 2026-06-15
type: analysis
description: "Causal Pipeline Results — Real Data (SPY/TLT 2007–2024)"
---

# Causal Pipeline Results — Real Data (SPY/TLT 2007–2024)

Three scripts running on real Yahoo Finance data (CSV API, no yfinance dependency).

## Common Data

- **Period:** 2007-01-03 → 2024-12-30 (4,529 rows)
- **Assets:** SPY (equities), TLT (bonds)
- **Context:** 5-10% bond allocation, sideways/peaking markets
- **Causal approach:** DoWhy backdoor adjustment + EconML CATE + causal discovery

## Pipeline A: Causal Inference (DoWhy) — `run_causal_real.py`

Estimates the causal effect of holding bonds (when equities beat bonds) on forward 20-day bond CVaR.

| Method | ATE | 95% CI |
|--------|-----|--------|
| Naive (confounded) | -0.0084 | — |
| OLS backdoor | -0.0054 | [-0.0075, -0.0033] |
| PSM (trimmed) | -0.0084 | n=4509 |
| IPW | +0.0009 | — |
| Bootstrap | -0.006 | [-0.007, -0.004] |

**Key finding:** Bonds reduce CVaR by ~0.5-0.6pp when selected after equity outperformance. The naive estimate overstates the reduction (selection bias: you hold bonds in risky conditions).

**CATE by regime:**

| Market Regime | Vol Regime | CATE | n |
|:---:|:---:|:---:|:---:|
| Low | Low | -0.005 | 1,590 |
| Low | High | -0.007 | 181 |
| Mid | Low | -0.003 | 476 |
| Mid | High | -0.005 | 488 |
| High | Low | -0.004 | 478 |
| High | High | -0.006 | 1,296 |

CATE stable across regimes (≈ -0.003 to -0.007) — hedge effect is consistent regardless of market regime.

## Pipeline B: EconML CATE (Heterogeneity) — `run_B_econml_cate.py`

CausalForestDML to detect heterogeneous treatment effects by vol regime.

| Metric | Value |
|--------|-------|
| OLS ATE | -0.00578 [-0.00794, -0.00362] |
| CausalForestDML ATE | -0.00008 (SE: 0.00001) |
| CATE high-vol | -0.00019 |
| CATE low-vol | +0.00001 |
| Diff (high − low) | -0.00020 |

**Key finding:** Virtually no heterogeneity by vol regime. The bond hedge effect is uniform — no evidence for regime-dependent allocation adjustment. A flat 5% allocation is defensible.

## Pipeline D: Causal Discovery — `run_D_causal_discovery.py`

Random Forest feature importance + dynamic allocation rule extraction to find what causes regime transitions.

| Predictor | Importance |
|-----------|:---------:|
| realized_vol_lag1 | 0.169 |
| drawdown_lag1 | 0.134 |
| vol_of_vol_lag1 | 0.128 |
| volume_z_lag1 | 0.113 |
| vol_change_lag1 | 0.111 |
| tlt_mom_lag1 | 0.108 |
| corr_proxy_lag1 | 0.107 |
| ret_spread_lag1 | 0.105 |

**Dynamic allocation rules discovered:**

1. **INCREASE HEDGE** — When vol_change + vol_of_vol both > 75th percentile → increase bonds 5% → 10%
2. **HOLD OVERWEIGHT** — When ret_spread < 0 AND vol_regime == 1 → stay overweight bonds
3. **REDUCE HEDGE** — When vol_change < 25th percentile AND vol_regime == 0 → reduce hedge to 2-3%

**Key finding:** Regime transitions are rare (3.8% of days, mean duration 26.6 days). The top predictor is realized_vol_lag1 — volatility spikes precede regime shifts. When vol rises fast AND vol_of_vol is also elevated, doubling the bond allocation is warranted.

## Files

- Script: `~/clawd/run_causal_real.py`
- Script B: `~/clawd/run_B_econml_cate.py`
- Script D: `~/clawd/run_D_causal_discovery.py`
- Data: `~/clawd/price_data.csv`, `~/clawd/volume_data.csv`
- Results: `~/clawd/result_real.txt`, `~/clawd/result_B.txt`, `~/clawd/result_D.txt`

## Next Steps

- **Gap 5 (Backtest):** Compare causal estimates against actual portfolio returns
- **Gap 2 (EconML CATE):** CATE heterogeneity already done — no meaningful effect modification
- **Gap 6 (Regime transition):** D pipeline covers this — actionable rules extracted
