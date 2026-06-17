---
type: concept
title: Momentum Factor
description: "The momentum factor is based on the premise that stocks which have performed well in the past 3-12 months tend to continue outperforming."
created: 2026-04-24
updated: 2026-04-24
tags:
- quant
- factor
- investing
- momentum
sources:
- factor-investing.md
related:
- factor-investing
- momentum-strategy
- smart-beta-etfs
---
--
# Momentum Factor

The momentum factor is based on the premise that stocks which have performed well in the past 3-12 months tend to continue outperforming. This is closely related to but distinct from the broader [[momentum-strategy]] page.

## Metrics

- **12-month return** (excluding most recent month to avoid reversals)
- **3-month momentum**
- **6-month momentum**

## Implementation

1. Screen for top decile by past returns
2. Exclude most recent month (to avoid reversals)
3. Rebalance monthly or quarterly

## Risks

- Sudden reversals (momentum crashes)
- High turnover leads to higher transaction costs

## Connection to Factor Investing

Momentum is one of five primary factors in [[factor-investing]]. MTUM ETF implements this factor at 0.15% expense ratio. Momentum tends to outperform in bull markets and during recoveries.

## Related Concepts

- [[factor-investing]]
- [[momentum-strategy]]
- [[smart-beta-etfs]]
- [[factor-crowding-rotation]]