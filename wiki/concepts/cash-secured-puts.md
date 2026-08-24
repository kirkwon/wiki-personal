---
created: 2026-08-23
updated: 2026-08-23
---

--
# Cash-Secured Puts

A cash-secured put strategy involves selling put options while setting aside cash to purchase the underlying stock if assigned. This strategy combines income generation with potential stock acquisition at lower prices. Cash-secured puts are a conservative strategy for generating income and acquiring stocks at desired prices.^[raw/articles/Options Trading Guide.md]

## How It Works

- **Setup**: Hold cash equal to the strike price × 100 shares
- **Sell put**: Collect premium while waiting for stock to decline to your target price
- **If stock stays above strike**: You keep the premium as income
- **If stock falls below strike**: Stock is assigned and you acquire it at the strike price minus premium received

## Example

- Sell $50 put for $2 premium
- Cash reserved: $5,000 (100 shares × $50)
- Income: $200 per contract if stock stays above $50
- If assigned: acquire stock at $50 (effectively bought at $48 net after premium)

## Applications

- **Income Generation**: Regular premium income from time decay. Works well when expecting flat or rising markets. Earn premium while waiting for entry points.
- **Dollar-Cost Averaging**: Buy stocks at lower prices through put assignment. Particularly useful for retirement accounts and education funding.
- **Retirement Accounts**: Conservative income generation in IRA/401(k) accounts. Cash-secured puts are allowed but no naked options. Suitable for defined-risk strategies in retirement accounts.
- **LEAPS Puts**: Long-term portfolio protection

## Risk Management

- Assignment risk if stock falls below strike
- Opportunity cost if stock rises significantly or if holding cash
- Premium collected provides cushion against downside
- Position sizing: 5-15% of portfolio for short option strategies
- Need to maintain sufficient cash reserves

Cash-secured puts complement [[covered-calls]] as a conservative income strategy and integrate with [[options-position-sizing]].

See also: [[options-fundamentals]]

See also: [[options-for-retirement-planning]]

See also: [[credit-spreads]]

See also: [[theta-time-decay]]
