
--
# ITM vs OTM Options

Understanding the trade-offs between in-the-money (ITM) and out-of-the-money (OTM) options is fundamental to strategy selection. The choice affects cost, leverage, theta sensitivity, probability of profit, and risk profile.

## In-the-Money (ITM) Options

**Definition**: Options with intrinsic value. Calls are ITM when stock price > strike price; puts are ITM when stock price < strike price.

**Characteristics**:
- Higher premium due to intrinsic value
- Lower theta (less sensitive to time decay)
- Higher probability of being profitable
- Less leverage per dollar of exposure

**Advantages**:
- Time decay resistance from intrinsic value buffer
- Higher success rate
- More predictable option pricing behavior
- Lower gamma risk

**Disadvantages**:
- Higher cost requiring more capital
- Lower percentage returns
- Less leverage
- Less responsive to volatility changes

## Out-of-the-Money (OTM) Options

**Definition**: Options with no intrinsic value. Calls are OTM when stock price < strike price; puts are OTM when stock price > strike price.

**Characteristics**:
- Lower premium (cheaper)
- Higher theta (very sensitive to time decay)
- Lower probability of being profitable
- Higher leverage per dollar of exposure

**Advantages**:
- Lower cost
- Higher percentage returns if successful
- More exposure for less capital
- Higher gamma (more responsive to price movements)

**Disadvantages**:
- High theta risk and time decay sensitivity
- Need larger price moves to profit
- More likely to expire worthless
- More sensitive to implied volatility changes

## Decision Framework

**Risk Tolerance**:
- Conservative: ITM options (70-90% moneyness)
- Moderate: Near ATM options (85-105% moneyness)
- Aggressive: OTM options (110-150% moneyness)

**Time Horizon**:
- Short-term (1-4 weeks): ITM or ATM options
- Medium-term (1-6 months): ATM or slightly OTM
- Long-term (6+ months): OTM LEAPS options

**Capital Consideration**:
- Large capital: ITM for stability
- Moderate capital: ATM for balance
- Limited capital: OTM for leverage

This framework connects to [[theta-time-decay]] and [[options-position-sizing]].

See also: [[LEAPS-options]]

See also: [[covered-calls]]
