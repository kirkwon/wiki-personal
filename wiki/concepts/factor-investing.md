---
date: 2026-04-24
type: concept
title: Factor Investing
description: "Factor investing is a systematic approach to selecting stocks based on attributes (factors) that have historically provided excess returns."
created: 2026-04-24
updated: 2026-04-24
tags:
- finance
- investing
- factors
- quantitative
- systematic
sources:
- factor-investing.md
related:
- momentum-strategy
- value-investing
- small-cap-premium
- modern-portfolio-theory
- risk-management
---
--
# Factor Investing

Factor investing is a systematic approach to selecting stocks based on attributes (factors) that have historically provided excess returns. Instead of picking individual companies based on qualitative judgment, you construct portfolios based on measurable factors like value, momentum, quality, and size.

## The Five Primary Factors

Factor investing rests on five core factors, each with specific metrics and implementation rules:

- **[[value-factor]]** – Cheap relative to fundamentals (P/E, P/B, P/S, EV/EBITDA, FCF yield)
- **[[momentum-factor]]** – Past 3-12 month performance predicts future returns (excluding most recent month)
- **[[size-factor]]** – Small caps outperform large caps over time (small cap premium)
- **[[quality-factor]]** – Profitable, stable, low-debt companies outperform
- **[[low-volatility-factor]]** – Low beta/standard deviation provides better risk-adjusted returns

## Portfolio Construction

Investors can build **single-factor portfolios** (e.g., buy the cheapest 20% of stocks for value) or **multi-factor portfolios** that combine multiple factors to diversify away factor-specific risk. Multi-factor approaches are more complex and factors may offset each other.

Three optimization approaches:
- **Equal-Weighted Factors** – Simple and easy to implement
- **Mean-Variance Optimization** – Maximize return for given risk, requires historical data
- **Risk Parity** – Equal risk contribution from each factor, better diversification

Rebalancing frequency varies by factor: monthly for momentum, quarterly for value/quality, annually for size/low volatility.

## Backtesting

Backtesting must guard against several pitfalls: data snooping, survivorship bias, look-ahead bias, overfitting, and transaction costs. Walk-forward testing is recommended. Key metrics include CAGR >10%, Sharpe Ratio >1.0, Max Drawdown <30%, Sortino Ratio >1.5, and Alpha >3%.

## Regime-Dependent Performance

Factor performance varies by market regime:
- Bull markets: Momentum, Quality
- Bear markets: Value, Low Volatility
- Recoveries: Small Cap, Momentum
- High inflation: Value, Small Cap

## Smart Beta ETFs

Low-cost implementation via Smart Beta ETFs like VTV (Value, 0.04%), MTUM (Momentum, 0.15%), VFH (Low Volatility, 0.13%), VBR (Size+Value, 0.07%), and QUAL (Quality, 0.15%).

## Risks and Limitations

Factors can underperform for extended periods (3-10 years). Momentum crashes and value traps are known risks. Factor crowding when many investors pile into the same factor can cause underperformance. See [[factor-crowding-rotation]] for more.

## Related Concepts

- [[momentum-strategy]] – Deep dive on momentum factor
- [[mean-reversion-strategy]] – Opposite of momentum
- [[statistical-arbitrage]] – More advanced factor-based strategies
- [[quant-strategy]] – Systematic, data-driven investment approaches