---
date: 2026-05-09
type: source
title: 'Source: factor-investing.md'
created: 2026-05-09
updated: 2026-05-09
sources:
- factor-investing.md
tags:
- quant
- factor
- investing
- systematic
- momentum
- value
related: []
---
-

# Factor Investing

Systematic portfolio construction that selects stocks based on measurable attributes—**factors**—which have historically generated excess returns. The approach relies on five primary factors: **Value, Momentum, Size, Quality, and Low Volatility**. Implementation is rules‑based, with clear screening criteria, rebalancing schedules, and performance metrics.

**Prerequisites**: [[modern-portfolio-theory]], [[risk-management]]  
**Related Concepts**: [[momentum-strategy]], [[value-investing]], [[small-cap-premium]]  
**Holding Period**: 1‑12 months (varies by factor)  
**Risk Profile**: Moderate to High  

---

## The Five Factors

### Value Factor
- **Definition**: Cheap relative to fundamentals.  
- **Metrics**: P/E, P/B, P/S, EV/EBITDA, Free Cash Flow Yield.  
- **Screening**: Top decile; equal‑weight or market‑cap weighted.  
- **Rebalancing**: Annually.  
- **Risks**: Value traps, extended underperformance (3‑10 years).

### Momentum Factor
- **Definition**: Past 3‑12 month performance predicts future returns.  
- **Implementation**: Use 12‑month return **excluding** the most recent month to avoid short‑term reversals.  
- **Rebalancing**: Monthly or quarterly.  
- **Risks**: Sudden reversals (momentum crashes), high turnover.

### Size Factor (Small Cap Premium)
- **Definition**: Small caps outperform large caps over time.  
- **Screening**: Market‑cap based.  
- **Risks**: Higher volatility, lower liquidity, less analyst coverage.

### Quality Factor
- **Definition**: Profitability, stable earnings, low debt outperform.  
- **Metrics**: ROE, ROA, profit margins, debt‑to‑equity, earnings stability.  
- **Screening**: ROE > 15 %, debt‑to‑equity < 50 %, positive cash flow for ≥5 years.  
- **Risks**: Can be expensive; may lag in speculative markets.

### Low Volatility Factor
- **Definition**: Low beta/standard deviation delivers better risk‑adjusted returns.  
- **Screening**: Lowest volatility decile.  
- **Rebalancing**: Quarterly.  
- **Risks**: Underperforms in strong bull markets; may concentrate in defensive sectors.

---

## Backtesting & Performance Metrics

Key benchmarks for a well‑constructed factor portfolio:

| Metric | Target |
|--------|--------|
| CAGR | > 10 % |
| Sharpe Ratio | > 1.0 |
| Max Drawdown | < 30 % |
| Sortino Ratio | > 1.5 |
| Alpha | > 3 % |
| Beta | ≈ 1.0 |

**Pitfalls to avoid**  
- Data snooping  
- Survivorship bias  
- Look‑ahead bias  
- Overfitting  

*Walk‑forward testing* is recommended to guard against these issues.

---

## Factor Crowding & Rotation

Factor performance is regime‑dependent:

- **Bull markets**: Momentum & Quality tend to lead.  
- **Bear markets**: Value & Low Volatility tend to lead.  
- **Recoveries**: Small Cap & Momentum tend to lead.  
- **High inflation**: Value & Small Cap tend to lead.  

**Crowding** occurs when many investors pile into the same factor, potentially eroding the premium and causing underperformance.

---

## Smart Beta ETFs

| ETF | Factor | Expense Ratio |
|-----|--------|---------------|
| VTV | Value (large cap) | 0.04 % |
| MTUM | Momentum | 0.15 % |
| VFH | Low volatility | 0.13 % |
| VBR | Size + Value | 0.07 % |
| QUAL | Quality | 0.15 % |

---

## Data Sources, Tools & Further Reading

- **Factor Research**: AQR, Dimensional Fund Advisors, MSCI.  
- **Screening Tools**: Portfolio123, Stock Rover, Finviz.  
- **Backtesting Platforms**: QuantConnect, Quantopian, Python libraries (pandas, backtrader).  
- **Authors**: Larry Swedroe, Andrew Ang.  

**Further Reading**  
- *Your Complete Guide to Factor‑Based Investing* – Larry Swedroe  
- *Factor‑Based Investing* – Andrew Ang  
- *Smart Beta ETFs* – ETF.com  

---

## Related Wiki Pages

- [[momentum-strategy]]  
- [[value-investing]]  
- [[small-cap-premium]]  
- [[risk-management]]  
- [[modern-portfolio-theory]]  
- [[quant-strategy]]  
- [[risk-assessment-framework]]  
- [[decision-making-frameworks]]  
- [[systematic-decision-making]]  

---

## Summary of Findings & Caveats

- **Core claim**: Historical factor premiums (value, momentum, size, quality, low volatility) provide excess returns when systematically implemented.  
- **Evidence**: Backtested metrics (CAGR > 10 %, Sharpe > 1.0, alpha > 3 %) are descriptive benchmarks; actual empirical results are limited by survivorship bias, overfitting, and data snooping.  
- **Strength**: The framework is methodologically sound and useful for constructing factor portfolios, but lacks rigorous empirical grounding within this document.  
- **Key caveat**: Factor crowding can eliminate premiums; value factors may underperform for 3‑10 years, and momentum can experience sudden crashes.  

The approach does **not** contradict existing wiki content and integrates naturally with [[momentum-strategy]], [[value-investing]], [[small-cap-premium]], and broader risk‑management and portfolio‑theory concepts.