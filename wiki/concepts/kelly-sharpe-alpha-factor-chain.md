---
type: concept
title: "Kelly-Sharpe-Alpha Factor Chain"
tags: [finance, quantitative, risk-adjusted-returns, kelly-criterion, sharpe-ratio, alpha, portfolio-theory]
source: "clawd/24.Risk-Adjusted-Returns/kelly_sharpe_alpha.md"
generated: 2026-07-04
created: 2026-07-04
provenance: brain/ (retired 2026-09-13)
---
# Kelly-Sharpe-Alpha Factor Chain

> **The unifying identity:** Kelly fraction, Sharpe ratio, and Jensen's alpha are not three separate metrics — they are the same information (return per unit risk) viewed through three lenses. The Kelly fraction equals Sharpe divided by volatility.

## The Core Identity

$$f^* \approx \frac{\mu}{\sigma^2} = \frac{\text{Sharpe}}{\sigma_{\text{annual}}} = \frac{\alpha + \beta(R_m - r_f)}{\sigma_p^2}$$

| Concept | Formula | What it measures |
|---------|---------|-----------------|
| **Jensen's Alpha (α)** | $\alpha = R_p - [r_f + \beta(R_m - r_f)]$ | Edge *above* what beta explains |
| **Sharpe Ratio (S)** | $S = \frac{R_p - r_f}{\sigma_p}$ | Edge *per unit* of total risk |
| **Kelly Fraction (f\*)** | $f^* = \frac{\mu}{\sigma^2} = \frac{S}{\sigma}$ | Optimal capital to deploy |

**The chain reads:** Alpha is the raw edge → Sharpe normalizes it by risk → Kelly tells you how much to bet on it.

## Computed Results (Real Portfolio, 2026-07-04)

Data: 751 daily returns (2023-07 → 2026-07), 125 positions ($2.27M AUM). Benchmark: SPY. Risk-free: 4.3%.

| Metric | Value | Interpretation |
|--------|------:|:---------------|
| Annualized Return | 25.35% | Gross portfolio return |
| Annualized Volatility | 15.35% | Total risk |
| Sharpe Ratio | 1.197 | Excellent (>1.0), but see DSR |
| Sortino Ratio | 2.189 | 1.83× Sharpe — strong downside protection |
| Sortino/Sharpe Spread | 0.992 | Asymmetry signal — skill in cutting losses |
| Beta vs SPY | −0.034 | Essentially uncorrelated to market |
| Jensen's Alpha (annual) | 20.71% | Return above CAPM prediction |
| Information Ratio | 0.122 | Low — alpha is noisy |
| Tracking Error | 22.03% | High — diverges from SPY |
| Kelly (discrete, win/loss) | 0.132 | Bet 13% of bankroll per trial |
| Kelly (continuous, μ/σ²) | 7.79 | Leverage signal (unconstrained) |
| Kelly = Sharpe/σ | 7.80 | Matches continuous — confirms identity |
| Deflated Sharpe (trials=9) | 0.000 | ⚠ Sharpe not significant after multiple-testing correction |

## The Two Kelly Numbers — Why They Diverge

The discrete Kelly (0.13) and continuous Kelly (7.79) differ by **59×**. This is the single most important diagnostic:

- **Discrete Kelly** uses actual win/loss counts (57% win rate, symmetric payoff → modest size)
- **Continuous Kelly** assumes normal i.i.d. returns and computes μ/σ² — explodes when variance is low but ignores survival constraints

**Bayesian Rogue reading:** The 7.79 is a leverage *signal* (edge is real in-sample); the 0.13 is the *honest* bet size respecting the actual return distribution. Always apply fractional Kelly (¼ to ½) to the *discrete* number.

## The DSR Red Flag

The Deflated Sharpe Ratio = 0.000 (Bailey & López de Prado, 2014) means: if 9 independent strategies were tested, the probability that this Sharpe (1.197) represents a true positive edge — rather than survivorship bias — is effectively zero.

**Honest conclusion:** The portfolio performed well, but we cannot reject "lucky survivor" at conventional confidence with one sample and 9 trials. The Sortino/Sharpe spread and near-zero beta are more convincing skill signals than the Sharpe itself.

## Decision Framework — When Each Metric Decides

| Decision | Metric | Why |
|----------|--------|-----|
| "Is there skill?" | Jensen's Alpha + Sortino/Sharpe spread | Alpha detects edge; spread detects downside skill |
| "Is this better than that?" | Sharpe (with DSR) | Risk-normalized comparison; DSR guards data-mining |
| "How much do I bet?" | Kelly (discrete, then fractional) | Growth-optimal sizing with survival constraint |
| "Is the Sharpe real or lucky?" | Deflated Sharpe Ratio | Multiple-testing correction |
| "Am I just holding leveraged beta?" | Beta + Information Ratio | β≈0 + IR>0 = alpha; β>1 + IR≈0 = hidden leverage |

## Connection to the Bayesian Rogue Framework

The chain maps onto the Rogue funnel:

```
Alpha (edge detected)
    ├── Phase 1: Explore — Is the edge real? (DSR, multiple-testing check)
    ├── Phase 2: Sieve — How much edge per unit risk? (Sharpe)
    └── Phase 3: Execute — How much to deploy? (Kelly, fractional)
```

**Kelly Sizer skill** operationalizes Phase 3. **Mean-variance-analyzer** serves Phase 2. This document is the bridge that makes them agree on definitions.

## Black Swan Caveats

Kelly maximizes log-wealth growth assuming correct probability estimates and i.i.d. returns. Two failure modes:

1. **Parameter uncertainty:** If Sharpe is estimated with error (DSR=0 suggests it is), full Kelly is reckless. Fractional Kelly mandatory.
2. **Non-stationarity:** Kelly assumes stable distribution. Regime shifts break this. Always keep a survival floor.

## Key Formulas

```
Sharpe    = sqrt(252) * mean(excess) / std(excess)
Sortino   = sqrt(252) * mean(excess) / sqrt(mean(downside^2))
Kelly_c   = mean(excess) / var(excess)
Kelly_d   = (win_rate * payoff_ratio - loss_rate) / payoff_ratio
Kelly     = Sharpe / annualized_volatility        [identity]
Jensen_α  = portfolio_return - [r_f + β * (market_return - r_f)]
DSR       = multiple-testing-corrected p-value of observed Sharpe
```

## Reproduction

Scripts: `risk_metrics.py`, `coverage_example.py`, `alpha_extraction_analysis.ipynb` (in `clawd/24.Risk-Adjusted-Returns/` and `clawd/kelly_coverage_demo/`).

```bash
cd ~/clawd/24.Risk-Adjusted-Returns
python3 risk_metrics.py -i returns.csv --rf 0.043 --mar 0.0 --periods 252 --dsr --trials 9
cd ~/clawd/kelly_coverage_demo
python3 coverage_example.py -i ../24.Risk-Adjusted-Returns/returns.csv --rf 0.043 --periods 252
```

## Visual Artifacts

- `graphics/factor_chain_diagram.png` — Alpha→Sharpe→Kelly chain with master identity
- `graphics/kelly_sharpe_surface.png` — Kelly=Sharpe/σ curves + return distribution
- `graphics/alpha_decomposition.png` — Metrics dashboard + return decomposition

## References

- Kelly, J. L. (1956). "A New Interpretation of Information Rate."
- Sharpe, W. F. (1966). "Mutual Fund Performance." *Journal of Business*.
- Jensen, M. C. (1968). "The Performance of Mutual Funds in the Period 1945–1964."
- Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." *Journal of Derivatives*.
- Thorp, E. O. (2011). "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market."
- MacLean, Thorp & Ziemba (2011). *The Kelly Capital Growth Investment Criterion*.

## Connections

- Related to: [[kelly-criterion]], [[kelly-criterion-bet-sizing]], [[sharpe-ratio]], [[beta-investing]], [[strategic-decision-framework]]
- Operationalized by: kelly-sizer skill, mean-variance-analyzer skill
- Source implementation: `clawd/24.Risk-Adjusted-Returns/`, `clawd/kelly_coverage_demo/`, `clawd/01.Signals-Macro/alpha_extraction_analysis.ipynb`
