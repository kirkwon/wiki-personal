---
type: concept
title: Backtesting Pitfalls in Factor Investing
created: 2026-04-24
updated: 2026-04-24
tags:
- quant
- factor
- investing
- backtesting
- risk-management
sources:
- factor-investing.md
related:
- factor-investing
- risk-management
- modern-portfolio-theory
---
--
# Backtesting Pitfalls in Factor Investing

Backtesting factor strategies requires careful attention to common errors that can produce misleading results.

## Common Pitfalls

| Pitfall | Why It's Bad | Solution |
|---------|-------------|----------|
| Data snooping | Using all data to optimize parameters | Use walk-forward testing |
| Survivorship bias | Ignoring delisted companies | Include delisted stocks |
| Transaction costs | Real trading is expensive | Include 0.1-0.2% per trade |
| Look-ahead bias | Using future data | Only use data available at time |
| Overfitting | Strategy too specific to historical data | Keep rules simple |

## Key Metrics

- **CAGR** – Compound annual growth rate (>10% to beat market)
- **Sharpe Ratio** – Risk-adjusted return (>1.0)
- **Max Drawdown** – Largest peak-to-trough decline (<30%)
- **Sortino Ratio** – Downside risk-adjusted return (>1.5)
- **Alpha** – Excess return vs. market (>3% annually)
- **Beta** – Sensitivity to market (~1.0)

## Best Practices

1. Define the strategy (factors, screens, rebalance frequency)
2. Gather historical data (price, fundamentals)
3. Simulate trades (account for transaction costs, slippage)
4. Analyze results (CAGR, Sharpe, drawdown)
5. Out-of-sample test (validate on unseen data)

## Related Concepts

- [[factor-investing]]
- [[risk-management]]
- [[modern-portfolio-theory]]