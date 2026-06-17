---
type: concept
title: Momentum Strategy
description: "Momentum is the tendency for assets that have performed well in the past to continue performing well in the near future."
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
related:
- factor-investing
- trend-following
- mean-reversion-strategy
- technical-analysis-basics
- statistical-arbitrage
- risk-assessment-framework
- decision-making-frameworks
---
--
# Momentum Strategy

Momentum is the tendency for assets that have performed well in the past to continue performing well in the near future. It is one of the most robust market anomalies, persisting across asset classes, geographies, and time periods for 90+ years.

## The Momentum Effect

### Definition

**Momentum** = "Stocks that have gone up recently will continue to go up."

- Look-back period: 3-12 months (most common: 12 months)
- Skip recent month (to avoid reversals)
- Holding period: 1-12 months, with 3-6 months being typical

### Evidence

- **Academic research**: Jegadeesh and Titman (1993) — first to document
- **Persistence**: Has worked for 90+ years
- **Global**: Works in US, Europe, Asia, emerging markets
- **Cross-asset**: Works in stocks, bonds, commodities, currencies

## Core Mechanism

The strategy is built on a simple observation: stocks that have gone up recently will continue to go up. The most common implementation uses a 12-month look-back period while skipping the most recent month to avoid short-term reversals. Holdings typically run 1-12 months, with 3-6 months being typical.

The 12-1 momentum metric is calculated as:

```
Momentum = (Price today / Price 12 months ago) - (Price today / Price 1 month ago)
```

## Momentum Metrics

### Price Momentum (12-1)

**Implementation**:
1. Calculate 12-month return (excluding most recent month)
2. Rank all stocks by this metric
3. Buy top decile (or top 20%)
4. Hold for 3-6 months
5. Rebalance monthly

### Cross-Sectional Momentum

Compare stocks to each other within the same universe. Buy the best performers, avoid the worst.

### Time-Series Momentum

Compare an asset to its own past performance. If the S&P 500 is up 15% over 12 months, buy it. Different from cross-sectional in that it evaluates a single asset against its own history.

## Why It Works

Several explanations have been proposed for why momentum persists:

| Explanation | Theory |
|-------------|--------|
| **Underreaction** | Prices react slowly to new information |
| **Behavioral bias** | Herding and extrapolation of past trends |
| **Risk compensation** | Momentum stocks carry higher risk |
| **Liquidity** | Less liquid stocks show stronger momentum effects |

## Historical Performance

Backtesting on US stocks from 1927-2023 shows momentum significantly outperforms the market:

| Strategy | Annual Return | Volatility | Sharpe Ratio |
|----------|---------------|------------|--------------|
| Market (S&P 500) | 10.2% | 18.5% | 0.55 |
| Value | 13.5% | 22.3% | 0.61 |
| Momentum | 16.8% | 25.1% | 0.67 |
| Momentum + Value | 15.2% | 19.8% | 0.77 |

Momentum has the highest raw returns but also the highest volatility. The combination of momentum + value delivers the best risk-adjusted returns with a Sharpe ratio of 0.77.

### Drawdowns

| Strategy | Max Drawdown | Worst Period |
|----------|--------------|--------------|
| Market | -86% (Great Depression) | 1929-1932 |
| Momentum | -72% (2008-2009) | 2008-2009 |
| Value | -81% (1929-1932) | 1929-1932 |
| Momentum + Value | -58% (2008) | 2007-2009 |

All strategies beat the market over the long term.

## Strategy Variants

### Simple Momentum (12-1)

Buy the top 20% of stocks by 12-1 momentum, hold for 3 months, rebalance monthly. Simple and well-researched but with high turnover and sudden crash risk.

### Momentum + Quality

Filter for high-quality stocks (ROE > 15%, low debt) then pick top momentum stocks within that subset. This reduces crashes and avoids value traps.

### Momentum + Value

Filter for cheap stocks (low P/E, P/B) then buy those with positive momentum. This avoids falling knives while capturing value turnarounds, but may miss turnaround stories.

### Dual Momentum

Apply momentum to asset allocation: compare S&P 500 vs. Treasuries over the past 12 months and allocate accordingly. If S&P 500 > Treasuries, buy S&P 500; otherwise buy Treasuries. Simpler and lower transaction costs.

### Trend Following (Long-Term Momentum)

Use longer look-back periods (e.g., 200-day moving average) for asset allocation between stocks and bonds/cash. If price > 200-day MA, buy stocks; if price < 200-day MA, buy bonds/cash. Avoids major bear markets but suffers from whipsaws.

## Momentum Crashes

Momentum crashes are sudden, sharp reversals where momentum stocks underperform dramatically. Historical examples include 2008 (-30% vs market -40%), 2009 (-50% while market recovered), and 2020 COVID (-40% vs market -34%).

Crashes occur at bear market starts when high-beta momentum stocks fall faster, during sharp reversals when trend followers sell simultaneously, when momentum stocks are overpriced, and during periods of low volatility and complacency.

### Mitigation Strategies

1. Diversify across timeframes (3-month, 6-month, 12-month momentum)
2. Combine with value (reduces volatility)
3. Use stop losses (exit when momentum turns negative)
4. Volatility targeting (reduce position size when vol spikes)
5. Dual momentum (add safe assets when stocks are weak)

## Implementation

### Stock Picking

Monthly rebalancing: calculate 12-1 momentum across all US stocks (market cap > $500M), buy top 20 percentile, equal-weight the portfolio.

### ETF Approach

Momentum ETFs include MTUM (US Large Cap, 0.15% expense ratio), QMOM (US Mid Cap, 0.45%), UMOM (International, 0.30%), and DMOM (Developed Markets, 0.35%).

### Factor Portfolio

Combine momentum with other factors: 30% Value, 30% Momentum, 20% Quality, 20% Low Volatility, rebalanced quarterly.

## Risk Management

### Position Sizing

Volatility-based sizing: Position Size = (Target Risk / Stock Volatility) × (1 / Number of Stocks). Example: target portfolio risk 15%, average stock volatility 30%, 50 stocks → 1% position size each.

### Stop Losses

Trailing stop loss: Stop Loss = Highest Price × (1 - Stop Percentage), typically 15%. Example: stock bought at $100, highest price $120, stop 15% → stop loss at $102.

### Volatility Targeting

Reduce position when vol spikes: New Position = Old Position × (Target Volatility / Current Volatility). Example: current vol 25%, target 15% → reduce position size by 40%.

## Common Mistakes

- Using only price momentum without quality filters
- Rebalancing too frequently
- Ignoring transaction costs in backtests
- No risk management (stop losses, volatility targeting)
- Overfitting to recent data
- Not accounting for tax implications of frequent rebalancing

## Related Concepts

- [[12-1-momentum]] — The primary momentum metric
- [[momentum-crashes]] — Key risk to manage
- [[dual-momentum]] — Asset allocation variant
- [[factor-investing]] — Momentum as a factor
- [[trend-following]] — Longer-term momentum approach
- [[mean-reversion-strategy]] — Opposite approach
- [[technical-analysis-basics]] — Identifying trends as prerequisite
- [[risk-assessment-framework]] — Risk management and position sizing
- [[statistical-arbitrage]] — Related quantitative approaches
- [[decision-making-frameworks]] — Decision processes for systematic strategies
