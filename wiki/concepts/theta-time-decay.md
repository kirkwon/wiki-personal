---
type: concept
title: Theta (Time Decay)
created: 2026-04-24
updated: 2026-05-09
tags:
- personal-finance
- investing
- options
- options-trading
- risk-management
sources:
- Options Trading Guide.md
related:
- options-fundamentals
- leaps-long-term-equity-anticipation-securities
- straddle-strategies
- butterfly-spreads
- options-position-sizing
- LEAPS-options
- ITM-vs-OTM-options
---
--
# Theta (Time Decay)

Theta measures the rate of decline in option value due to time passing, holding all other factors constant. It is the most critical risk factor for option sellers, a primary consideration for all options strategies, and the central concept governing strategy selection and management in options trading.

## Key Characteristics

- **Negative for Long Options**: Long positions lose value as time passes
- **Positive for Short Options**: Short positions gain value as time passes
- **Accelerating Decay**: Decay speeds up dramatically in the last 30 days
- **Zero at Expiration**: Options are worthless at expiration if they have no intrinsic value

## Theta Patterns

**Time Decay Acceleration**:
- Linear decay in the first 60% of an option's life
- Rapid accelerating decay in the last 40% of life
- Exponential decay in the last 30 days
- Maximum theta impact in expiration week

**Theta by Option Type**:
- ATM options have the highest theta (maximum time value)
- ITM options have lower theta (some intrinsic value provides buffer)
- OTM options have lower absolute theta but are more sensitive relative to premium; far OTM options have low theta but high relative decay sensitivity
- LEAPS have minimal theta (abundant time value)

**Typical Values**:
- Monthly options: 0.05–0.15 per day
- Weekly options: 0.10–0.30 per day
- LEAPS: 0.01–0.05 per day

## Interaction with Other Greeks

- **Gamma-Theta Relationship**: High gamma often correlates with high theta
- **Volatility Impact**: Higher implied volatility increases theta impact
- **Moneyness Effect**: ATM options are most sensitive to theta

## Theta Management Strategies

**For Long Options**:
- Use LEAPS to minimize theta impact
- Choose ITM options for intrinsic value buffer
- Enter when implied volatility is low
- Keep position sizes small relative to capital (1-5% of portfolio)
- Match option duration to expected move timing
- Allow 3-6 months for thesis to play out

**For Short Options**:
- Earn from time decay as a primary income source
- Use defined-risk strategies (covered calls, credit spreads, iron condors)
- Maintain sufficient margin buffer
- Monitor for early assignment risk
- Higher capital required for margin; naked shorts carry unlimited risk

## Theta-Aware Position Sizing

- **Long options**: 1-5% of portfolio per position due to theta risk
- **Short options**: 5-15% of portfolio per short position
- **LEAPS positions**: 10% of portfolio for long-term growth
- **Straddle positions**: 5% for volatility plays
- **Covered calls**: 15% for income generation
- **Iron condors**: 5% for range-bound markets
- **Cash reserves**: 65% for flexibility and risk management

Understanding theta is essential for all options strategies, from LEAPS for long-term growth to straddles for volatility capture to butterflies for range-bound markets. Theta connects to all major options strategies and is central to understanding [[LEAPS-options]], [[straddle-strategies]], and [[butterfly-spreads]].^[raw/articles/Options Trading Guide.md]