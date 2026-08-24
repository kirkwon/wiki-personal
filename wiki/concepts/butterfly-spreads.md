---
created: 2026-08-23
updated: 2026-08-23
---

--
# Butterfly Spreads

A butterfly spread combines multiple options at different strike prices to create a position with limited risk and limited reward. Best suited for range-bound or neutral market conditions.

## Common Butterfly Types

- **Long Call Butterfly**: Buy 1 low call, sell 2 middle calls, buy 1 high call
- **Long Put Butterfly**: Buy 1 low put, sell 2 middle puts, buy 1 high put
- **Iron Butterfly**: Combination of straddle and strangle
- **Condor**: Butterfly with wider wing separation

## Characteristics

- **Limited Risk**: Maximum loss is the net debit paid
- **Limited Reward**: Maximum profit is limited and occurs at middle strike
- **Neutral Bias**: Best for range-bound markets
- **Theta Advantage**: Can benefit from time decay

## Theta Dynamics

**Long Butterfly**:
- Mixed theta exposure: long options lose value, short options gain value
- Net effect typically benefits from time decay
- Short options decay faster than long options
- Profit enhancement increases as expiration approaches

**Short Butterfly**:
- Negative theta: net time decay works against position
- Requires active management
- Sensitive to volatility changes

## Applications

### Range-Bound Markets
- Use in sideways trading markets
- Middle strike at current price
- Defined price range for maximum profit
- Defined risk

### Earnings Plays
- Sell ATM straddle, buy OTM wings
- Expecting muted volatility after earnings
- Benefits from time decay if stock stays near strike

### High Volatility Plays
- Buy butterfly after volatility spike
- Expecting volatility to normalize
- Enter after volatility expansion, exit before expiration

## Example

Stock XYZ at $50, long call butterfly: Buy $45 call, sell 2 $50 calls, buy $55 call. Net debit $3.00, max profit $2.00 at $50 strike. Maximum loss $3.00 if stock moves beyond wings.^[raw/articles/Options Trading Guide.md]

Butterfly spreads share theta management considerations with [[theta-time-decay]] and connect to other defined-risk strategies like [[credit-spreads]] and [[iron-condors]].

See also: [[options-fundamentals]]

See also: [[straddle-strategies]]
