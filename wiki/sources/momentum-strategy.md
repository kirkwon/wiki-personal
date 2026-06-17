---
type: source
title: Momentum Strategy
description: "This source documents the momentum investment strategy — one of the most robust market anomalies, persisting across asset classes, geographies, and time periods for 90+ years."
created: 2026-04-24
updated: 2026-05-09
tags:
- investing
- factor-investing
- momentum
- quant
- trend
- systematic
- technical
- algorithmic
sources:
- momentum-strategy.md
---
--
# Momentum Strategy

This source documents the momentum investment strategy — one of the most robust market anomalies, persisting across asset classes, geographies, and time periods for 90+ years. The core insight is that assets which have performed well in the past tend to continue performing well in the near future. It covers the 12-1 momentum metric, cross-sectional and time-series momentum, dual momentum for asset allocation, trend following using moving averages, and momentum crashes with mitigation strategies.

## Overview

Momentum is defined as the tendency for assets that have performed well in the past to continue performing well in the near future. The core metric is 12-1 momentum: (Price today / Price 12 months ago) − (Price today / Price 1 month ago). Look-back period is 3–12 months (most common: 12 months), skipping the recent month to avoid reversals, with holding periods of 1–12 months (typically 3–6 months).

The effect persists across asset classes, geographies, and 90+ years of data (Jegadeesh and Titman 1993). Explanations include underreaction to new information, behavioral biases like herding and trend extrapolation, risk compensation (momentum stocks are riskier), and liquidity effects.

## Key Findings

- **Momentum Effect**: Stocks that have gone up recently continue to go up. Most common look-back period is 12 months, skipping the most recent month to avoid reversals.
- **Backtesting (1927–2023)**: Pure momentum returned 16.8% annualized vs. 10.2% for S&P 500, with volatility of 25.1%. Momentum + Value achieved the best risk-adjusted returns (Sharpe 0.77) with max drawdown of -58%.
- **Momentum Crashes**: Sharp reversals occur in bear markets (2008–2009, 2020 COVID) where momentum stocks underperform dramatically.
- **Dual Momentum**: Applying momentum to asset allocation (stocks vs. Treasuries) provides simpler, lower-cost exposure.
- **Implementation**: Can be implemented via stock picking, momentum ETFs (MTUM, QMOM, UMOM, DMOM), or factor portfolios combining momentum with value, quality, and low volatility.

## Momentum Metrics

**Price Momentum (12-1)**: Calculate 12-month return excluding the most recent month, rank all stocks, buy the top decile or top 20%, hold 3–6 months, rebalance monthly.

**Cross-Sectional Momentum**: Compare stocks to each other within the same universe — buy the best performers, avoid the worst.

**Time-Series Momentum**: Compare an asset to its own past performance — e.g., if the S&P 500 is up 15% over 12 months, buy it. Different from cross-sectional in that it evaluates a single asset against its own history.

## Momentum Strategies

**Simple Momentum (12-1)**: Look back 12 months (exclude last month), buy top 20% of stocks by return, hold 3 months, rebalance monthly. Simple and well-researched but with high turnover and sudden crash risk.

**Momentum + Quality**: Filter for high-quality stocks (ROE > 15%, low debt), then pick top 20% by momentum. Reduces crashes and avoids value traps.

**Momentum + Value**: Filter for cheap stocks (low P/E, P/B), then buy those with positive momentum. Avoids "value traps" (falling knives) but may miss turnaround stories.

**Dual Momentum**: Compare S&P 500 vs. Treasuries over past 12 months. If S&P 500 > Treasuries, buy S&P 500; otherwise buy Treasuries. Simpler with lower transaction costs.

**Trend Following (Long-Term Momentum)**: Use 200-day moving average for S&P 500. If price > 200-day MA, buy stocks; if price < 200-day MA, buy bonds/cash. Avoids major bear markets but suffers from whipsaws.

## Backtesting Results

Historical performance (US Stocks, 1927–2023):

| Strategy | Return | Sharpe | Max Drawdown |
|---|---|---|---|
| Market (S&P 500) | 10.2% | 0.55 | -86% (Great Depression) |
| Value | 13.5% | 0.61 | -81% (1929–1932) |
| Momentum | 16.8% | 0.67 | -72% (2008–2009) |
| Momentum + Value | 15.2% | 0.77 | -58% (2008) |

## Momentum Crashes

Sudden sharp reversals where momentum stocks underperform dramatically. Historical examples: 2008 (momentum -30% vs market -40%), 2009 (momentum -50% while market recovered), 2020 COVID (momentum -40% vs market -34%). Crashes occur at bear market starts, sharp reversals, high valuations, and low volatility periods.

Mitigation strategies include diversifying across timeframes, combining with value, using stop losses, volatility targeting, and dual momentum approaches.

## Implementation

Stock picking uses monthly rebalancing with the 12-1 momentum metric on all US stocks (market cap > $500M). ETF alternatives include MTUM (US Large Cap, 0.15%), QMOM (US Mid Cap, 0.45%), UMOM (International, 0.30%), DMOM (Developed Markets, 0.35%). A factor portfolio allocation: 30% Value, 30% Momentum, 20% Quality, 20% Low Volatility, rebalanced quarterly.

## Risk Management

- Volatility targeting (reduce position size when volatility spikes)
- Stop losses (trailing stop at 15% below highest price)
- Diversify across timeframes (3-month, 6-month, 12-month)
- Combine with value to reduce crash risk

## Related Concepts

- [[factor-investing]]
- [[trend-following]]
- [[mean-reversion-strategy]]
- [[technical-analysis-basics]]
- [[statistical-arbitrage]]
- [[risk-assessment-framework]]

## Further Reading

- "Expected Returns" by Antti Ilmanen
- "Your Complete Guide to Factor-Based Investing" by Larry Swedroe
- "Trend Following" by Michael Covel