---
date: 2026-06-30
type: concept
title: "Mean-Variance Myopia Under Stochastic Volatility"
description: "The static mean-variance efficient frontier is the myopic special case of the full intertemporal portfolio problem. When volatility is stochastic, the optimal strategy includes a positive intertemporal hedging demand that static M-V ignores."
created: 2026-06-30
updated: 2026-06-30
tags:
  - portfolio-theory
  - stochastic-volatility
  - intertemporal-hedging
  - limitation
sources:
  - optimal-investment-stochastic-volatility-chiarella-hsiao
  - pca-random-matrix-theory-equity-markets
related:
  - factors
  - factor-investing
  - mean-variance-analyzer
  - asymmetry-hunter
  - causal-portfolio-research
---

# Mean-Variance Myopia Under Stochastic Volatility

## The Core Problem

Static [[mean-variance-analyzer|mean-variance optimization]] treats the portfolio problem as a one-period decision. This assumes the investment opportunity set is constant — that expected returns, volatilities, and correlations don't change over the investment horizon.

Under [[factors|stochastic volatility]], this assumption is false. Volatility is time-varying, persistent, and partially predictable. An investor who ignores this is making the **myopic** choice — optimizing each period as if it were the last, with no hedge against shifts in the opportunity set itself.

## What the Chiarella & Hsiao Paper Shows

The [[sources/optimal-investment-stochastic-volatility-chiarella-hsiao|Chiarella & Hsiao (2010)]] paper compares three stochastic volatility models (Stein/Stein, Heston, extended Heston+CEV) and finds that **all three produce a positive intertemporal hedging demand** beyond the static M-V portfolio:

$$\text{Optimal Demand} = \underbrace{\text{Myopic M-V}}_{\text{static efficient frontier}} + \underbrace{\text{Intertemporal Hedge}}_{\text{hedge against shifts in opportunity set}}$$

| Model | Vol Process | Hedging Demand |
|-------|-------------|----------------|
| Stein/Stein | Gaussian OU | Positive |
| Heston | CIR square-root | Positive |
| Extended Heston + CEV | CEV (V^γ) | Positive (sensitive to γ) |

The intertemporal hedging term reflects Merton's (1973) ICAPM insight: investors care not just about current wealth, but about the **distribution of future investment opportunities**. If volatility is high today, it changes the risk-return trade-off tomorrow.

## Practical Implications

### For Our Quant Skills

1. **[[mean-variance-analyzer]]** — The current implementation computes a static efficient frontier. This is appropriate for short-horizon decisions (< 1 month) but **underestimates optimal hedging demand** for longer horizons under SV. Add a caveat: the efficient frontier is the myopic baseline; true optimal portfolios include intertemporal hedging.

2. **[[causal-portfolio-research]]** — Stochastic volatility is a key confounder in bond-hedging causal models. The EKF from Chiarella & Hsiao provides a principled way to estimate latent vol states rather than using ad-hoc proxies (realized vol tertiles, etc.).

3. **[[asymmetry-hunter]]** — The intertemporal hedging demand is itself an asymmetric payoff: you pay a cost now (reduced myopic return) for protection against adverse regime shifts. This fits the asymmetry framework directly.

4. **[[options-market-analysis]]** — The Heston model is the standard for options pricing under SV. The paper's EKF estimation approach means you can infer latent vol states from equity returns alone, not just options data.

### The M-History Problem

The paper also highlights a fundamental data limitation: to estimate a 500×500 covariance matrix you need ~500 daily observations, but those 500 observations span different volatility regimes. The covariance matrix you get is **an average across regimes**, not a snapshot of the current regime. This is the same problem that [[sources/pca-random-matrix-theory-equity-markets|PCA + RMT]] addresses — most of those 125,250 covariance entries are noise anyway.

**Synthesis:** PCA reduces the dimensionality (500 stocks → 5-15 eigenportfolios), and the Merton/Chiarella result shows that even those reduced factors are time-varying and require intertemporal hedging. The two results are complementary, not competing.

## When Static M-V Is Still Useful

- **Short horizons** (< 1 month) — vol is approximately constant
- **IIID returns** — if returns truly are i.i.d., Merton's myopic demand is optimal
- **Benchmarking** — the static frontier is the baseline; the hedging demand is the markup
- **Small allocations** — for small portfolio weights, the hedging term is second-order

## [[gbrain]] Connections to Add

```yaml
links:
  - [[mean-variance-analyzer]] → add intertemporal hedging caveat
  - [[causal-portfolio-research]] → EKF for latent vol estimation
  - [[asymmetry-hunter]] → hedging demand as asymmetric payoff
  - [[options-market-analysis]] → Heston model + EKF
  - [[factors]] → stochastic vol as an unobserved factor
  - [[factor-investing]] → ICAPM factors vs statistical factors
  - [[sources/optimal-investment-stochastic-volatility-chiarella-hsiao]] → the paper
  - [[sources/pca-random-matrix-theory-equity-markets]] → complementary PCA+RMT view
  - [[sources/smart-money-concepts-ict-python]] → ICT order block lifecycle as a zone state machine for regime transitions
```

## Open Questions

1. How do we incorporate intertemporal hedging demand into our existing mean-variance-analyzer without making it impractically complex? A simple approximation: add a regime-sensitive adjustment to the covariance matrix based on the current vol state.
2. Can we estimate the EKF-based latent volatility from our existing data feeds (Yahoo Finance CSV API, FRED), or do we need options data? The paper shows equity returns alone are sufficient.
3. For our bond-hedging causal model (causal-portfolio-research), how much does the intertemporal hedge change the optimal allocation vs the static bond allocation of 5-8%?
