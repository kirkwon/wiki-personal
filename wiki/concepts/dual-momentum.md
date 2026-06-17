---
type: concept
title: Dual Momentum
description: "Dual momentum is a strategy variant that applies momentum to asset allocation rather than individual stock selection."
created: 2026-04-24
updated: 2026-05-09
tags:
- investing
- momentum
- asset-allocation
- quant
sources:
- momentum-strategy.md
related:
- momentum-strategy
- trend-following
- factor-investing
---
--

# Dual Momentum

Dual momentum is a strategy variant that applies momentum to asset allocation rather than individual stock selection. It compares broad asset classes—typically equities versus treasuries—and allocates toward the winner.

## Strategy Rules

1. Compare S&P 500 vs. Treasuries over the past 12 months
2. If S&P 500 > Treasuries: Buy S&P 500
3. If Treasuries > S&P 500: Buy Treasuries
4. Rebalance monthly

## Advantages

- Simpler implementation with lower transaction costs
- Better risk-adjusted returns than pure momentum
- Built-in crash protection by shifting to safe assets when stocks are weak

## Limitations

- Misses sector rotation opportunities
- Less granular than stock-level momentum
- Monthly rebalancing can generate unnecessary turnover

## Distinction from Trend-Following

Dual momentum is distinct from [[trend-following]], which uses longer look‑back periods (e.g., a 200‑day moving average) for asset allocation decisions.

## Related

- [[momentum-strategy]] – Core momentum framework
- [[trend-following]] – Similar approach using moving averages
- [[factor-investing]] – Broader factor framework