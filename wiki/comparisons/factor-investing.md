---
created: 2026-04-24
sources:
- factor-investing.md
tags:
- quant
- factor
- investing
title: Factor Investing
description: "Factor investing is a systematic approach to selecting stocks based on attributes (factors) that have historically provided excess returns."
type: comparison
updated: 2026-05-09
related:
- momentum-strategy
- value-factor
- quality-factor
- low-volatility-factor
- smart-beta-etfs
---
--

# Factor Investing

## Infobox

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Prerequisites** | [[modern-portfolio-theory]], [[risk-management]] |
| **Related Concepts** | [[momentum-strategy]], [[value-investing]], [[small-cap-premium]], [[smart-beta-etfs]], [[factor-crowding-rotation]] |
| **Holding Period** | 1-12 months (varies by factor) |
| **Risk Profile** | Moderate to High |

## Overview

Factor investing is a systematic approach to selecting stocks based on attributes (factors) that have historically provided excess returns. Instead of picking individual companies, you construct portfolios based on factors like value, momentum, quality, and size.

## The Factors

### Value Factor

**Premise**: Value stocks (cheap relative to fundamentals) outperform growth stocks over time.

**Metrics**:
- **P/E Ratio**: Price to earnings (lower = cheaper)
- **P/B Ratio**: Price to book value
- **P/S Ratio**: Price to sales
- **EV/EBITDA**: Enterprise value to EBITDA
- **Free Cash Flow Yield**: FCF / Market cap

**Implementation**:
1. Screen for top decile by value metrics
2. Equal-weight or market-cap weighted
3. Rebalance annually

**Risks**:
- Value traps (cheap for good reason)
- Can underperform for extended periods (3-10 years)

### Momentum Factor

**Premise**: Stocks that have performed well in the past 3-12 months continue to outperform.

**Metrics**:
- **12-month return** (excluding most recent month to avoid reversal)
- **3-month momentum**
- **6-month momentum**

**Implementation**:
1. Screen for top decile by past returns
2. Exclude most recent month (to avoid reversals)
3. Rebalance monthly or quarterly

**Risks**:
- Sudden reversals (momentum crashes)
- High turnover = higher transaction costs

### Size Factor

**Premise**: Small cap stocks outperform large cap stocks over time (small cap premium).

**Metrics**:
- **Market capitalization**: Price × Shares outstanding
- Small cap: <$2B (varies by definition)
- Micro cap: <$300M

**Implementation**:
1. Invest in small cap index or small cap ETF
2. Equal-weight small caps
3. Be aware of liquidity constraints

**Risks**:
- Higher volatility
- Less liquidity (harder to enter/exit)
- Less analyst coverage = more information asymmetry

### Quality Factor

**Premise**: High-quality companies (profitable, stable, low debt) outperform.

**Metrics**:
- **Return on Equity (ROE)**
- **Return on Assets (ROA)**
- **Profit margins (gross, operating, net)**
- **Debt-to-equity ratio** (lower = better)
- **Earnings stability** (low variance)

**Implementation**:
1. Screen for companies with ROE > 15%
2. Debt-to-equity < 50%
3. Positive cash flow for 5+ years
4. Rebalance annually

**Risks**:
- Quality stocks can be expensive (low value)
- May underperform in speculative markets

### Low Volatility Factor

**Premise**: Low volatility stocks provide better risk-adjusted returns.

**Metrics**:
- **Standard deviation** of daily/weekly/monthly returns
- **Beta** to market (lower = less volatile)
- **Maximum drawdown**

**Implementation**:
1. Screen for lowest volatility decile
2. Equal-weight or market-cap weighted
3. Rebalance quarterly

**Risks**:
- Can underperform during strong bull markets
- May concentrate in defensive sectors (utilities, consumer staples)

## Factor Strategies

### Single-Factor Portfolios

Invest based on a single factor:

```
Value Strategy → Buy cheapest 20% of stocks
Momentum Strategy → Buy top 20% performers
```

**Pros**: Simple, clear exposure
**Cons**: High factor-specific risk

### Multi-Factor Portfolios

Combine multiple factors to diversify:

```
Screen for: Value AND Momentum AND Quality
Or: Buy equal portions of Value, Momentum, Quality, Size
```

**Pros**: Diversified factor exposure, smoother returns
**Cons**: More complex, factors may offset each other

### Smart Beta ETFs

ETFs that implement factor strategies:

| ETF | Factor | Expense Ratio |
|-----|--------|---------------|
| VTV | Value (large cap) | 0.04% |
| MTUM | Momentum | 0.15% |
| VFH | Low volatility | 0.13% |
| VBR | Size + Value | 0.07% |
| QUAL | Quality | 0.15% |

## Backtesting

### Key Metrics

| Metric | What It Measures | Good Value |
|--------|------------------|------------|
| **CAGR** | Compound annual growth rate | >10% (beat market) |
| **Sharpe Ratio** | Risk-adjusted return | >1.0 |
| **Max Drawdown** | Largest peak-to-trough decline | <30% |
| **Sortino Ratio** | Downside risk-adjusted return | >1.5 |
| **Alpha** | Excess return vs. market | >3% annually |
| **Beta** | Sensitivity to market | 1.0 = matches market |

### Backtesting Process

1. **Define the strategy** (factors, screens, rebalance frequency)
2. **Gather historical data** (price, fundamentals)
3. **Simulate trades** (account for transaction costs, slippage)
4. **Analyze results** (CAGR, Sharpe, drawdown)
5. **Out-of-sample test** (validate on unseen data)

### Common Pitfalls

| Pitfall | Why It's Bad | Solution |
|---------|--------------|----------|
| Data snooping | Using all data to optimize | Use walk-forward testing |
| Survivorship bias | Ignoring delisted companies | Include delisted stocks |
| Transaction costs | Real trading is expensive | Include 0.1-0.2% per trade |
| Look-ahead bias | Using future data | Only use data available at time |
| Overfitting | Strategy too specific | Keep rules simple |

## Portfolio Construction

### Factor Exposure Targeting

Determine how much exposure you want to each factor:

```
Target Weights:
  Value: 30%
  Momentum: 25%
  Quality: 25%
  Size: 20%
```

### Optimization Approaches

**Equal-Weighted Factors**
- Simple, understandable
- Easy to implement
- May not be optimal

**Mean-Variance Optimization**
- Maximize return for given risk
- Requires historical data
- Can be unstable

**Risk Parity**
- Equal risk contribution from each factor
- Better risk diversification
- More complex to implement

### Rebalancing

**Frequency**:
- **Monthly**: Momentum factors
- **Quarterly**: Value, quality factors
- **Annually**: Size, low volatility factors

**Triggers**:
- Time-based (monthly, quarterly, annually)
- Threshold-based (when factor drifts >10% from target)

## Implementation

### Direct Stock Picking

1. **Screen** for stocks meeting factor criteria
2. **Buy** top 20-50 stocks
3. **Rebalance** on schedule

**Pros**: Full control, low costs
**Cons**: Time-intensive, requires monitoring

### Smart Beta ETFs

1. **Select** ETFs for desired factors
2. **Buy** and hold
3. **Rebalance** quarterly

**Pros**: Simple, low effort, diversified
**Cons**: Management fees, less control

### Factor-Based Mutual Funds

1. **Choose** factor-based funds (e.g., AQR, Vanguard)
2. **Invest** according to allocation

**Pros**: Professional management, low minimums
**Cons**: Higher fees, less transparency

## Risk Management

### Factor Crowding

When everyone piles into the same factor, it can underperform.

**Signs**:
- High valuations for factor stocks
- Media hype around factor
- Factor performance divergence from fundamentals

### Factor Rotation

Different factors outperform in different market regimes:

| Market Regime | Outperforming Factors |
|---------------|----------------------|
| Bull market (growth) | Momentum, Quality |
| Bear market | Value, Low Volatility |
| Recovery | Small Cap, Momentum |
| High inflation | Value, Small Cap |

### Diversification

- **Don't over-concentrate** in one factor
- **Maintain broad market exposure** (core + factors)
- **Monitor factor correlations** (avoid highly correlated factors)

## Common Mistakes

| Mistake | How to Fix |
|---------|------------|
| Chasing last year's best factor | Look at long-term performance, not recent |
| Ignoring transaction costs | Factor outperforms net of costs |
| Overfitting backtests | Use walk-forward testing |
| Rebalancing too frequently | Balance turnover vs. responsiveness |
| Not accounting for taxes | Tax-loss harvest, use tax-efficient vehicles |

## Related Concepts

- [[momentum-strategy]] - Deep dive on momentum factor
- [[mean-reversion-strategy]] - Opposite of momentum
- [[statistical-arbitrage]] - More advanced factor-based strategies
- [[risk-management]] - Managing factor-specific risks
- [[modern-portfolio-theory]] - Mathematical foundation
- [[smart-beta-etfs]] - ETFs implementing factor strategies
- [[factor-crowding-rotation]] - Managing crowding and regime changes

## Further Reading

- "Your Complete Guide to Factor-Based Investing" by Larry Swedroe
- "Factor-Based Investing" by Andrew Ang
- "Smart Beta ETFs" by ETF.com

## Data Sources

- **Factor Research**: AQR, Dimensional Fund Advisors, MSCI
- **Screening Tools**: Portfolio123, Stock Rover, Finviz
- **Backtesting**: QuantConnect, Quantopian, Python libraries (pandas, backtrader)
