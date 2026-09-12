------

# Mean Variance Analyzer

> Apply portfolio theory (expected value, variance, efficient frontier) to compare options with uncertain outcomes. Includes documented limitations under stochastic volatility and PCA/RMT overparameterization.

## Overview

- **Purpose** — Apply portfolio theory principles to life decisions, treating different options as assets with expected returns and variances. Helps quantify trade-offs between expected outcomes and uncertainty/risk.
- **When to Apply** — - Comparing multiple options with uncertain outcomes - Life decisions involving trade-offs between reward and risk (career, investments, relationships) - Resource allocation across different activities or goals - When you need to move beyond simple pros/cons lists to quantitative comparison - Before making significant time/energy/money commitments
- **Core Principles** — - **Expected Value**: Probability-weighted average outcome - **Variance/Risk**: Measure of outcome uncertainty or volatility - **Diversification**: Spreading resources across uncorrelated options - **Efficient Frontier**: Optimal combinations offering max return for given risk - **Risk-Return Tradeoff**: Higher expected returns require accepting higher variance

## Further detail

### Output Structure

1. **Option Analysis**: Each option's expected value, variance, key assumptions 2. **Correlation Matrix**: How options move together (diversification benefits) 3. **Efficient Frontier**: Optimal portfolios for different risk tolerances 4. **Recommendations**: Optimal allocations based on risk preference 5. **Sensitivity Analysis**: How conclusions change with assumption variations

### Verification

- [ ] All probabilities sum to 100% for each option - [ ] Outcomes are measurable and comparable across options - [ ] Variance calculations are non-negative - [ ] Correlation matrix is symmetric with 1.0 on diagonal - [ ] Portfolio weights sum to 100% - [ ] Recommendations align with stated risk tolerance - [ ] Key assumptions explicitly stated and questioned

### Example Application

**Decision**: How to allocate 10 hours/week for skill development over 6 months

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/mean-variance-analyzer/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[portfolio-analyzer]]
