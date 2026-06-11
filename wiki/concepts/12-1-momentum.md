---
type: concept
title: 12-1 Momentum
created: 2026-04-24
updated: 2026-04-24
tags:
- investing
- momentum
- metrics
sources:
- momentum-strategy.md
related:
- momentum-strategy
- factor-investing
- cross-sectional-momentum
- time-series-momentum
---
-
# 12-1 Momentum

12-1 momentum is the primary metric used to measure price momentum. It calculates the 12-month return minus the 1-month return, skipping the most recent month to avoid short-term reversals.

## Formula

```
Momentum = (Price today / Price 12 months ago) - (Price today / Price 1 month ago)
```

## Implementation Steps

1. Calculate 12-month return (excluding the most recent month)
2. Rank all stocks by this metric
3. Buy the top decile (or top 20%)
4. Hold for 3-6 months
5. Rebalance monthly

## Why Skip the Most Recent Month

The most recent month is excluded because it often contains reversal signals. Including it would capture short-term mean reversion rather than the persistent momentum effect.

## Related Metrics

- **Cross-Sectional Momentum**: Compares stocks to each other within the same universe
- **Time-Series Momentum**: Compares an asset to its own past performance
- [[dual-momentum]]: Applies momentum logic to asset classes rather than individual stocks
---