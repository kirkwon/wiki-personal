---
date: 2026-04-24
title: Options Fundamentals
description: "Options are contracts that give the buyer the right, but not the obligation, to buy (call) or sell (put) an underlying asset at a predetermined price within a specified time period."
created: 2026-04-24
updated: 2026-05-09
type: concept
tags:
- investing
- options
- trading
- derivatives
- personal-finance
- options-trading
sources:
- raw/ingested/Personal Finance/Options Trading Guide.md
- Options Trading Guide.md
related:
- theta-time-decay
- leaps-long-term-equity-anticipation-securities
- straddle-strategies
- butterfly-spreads
- covered-calls
- credit-spreads
- ITM-vs-OTM-options
- LEAPS-options
---
--

# Options Fundamentals

Options are contracts that give the buyer the right, but not the obligation, to buy (call) or sell (put) an underlying asset at a predetermined price within a specified time period.

## Overview

This page is part of the [[options-trading-guide]]. See also:
- [[investing]]
- [[trading]]
- [[risk-management]]

## Key Components

- **Underlying Asset**: Stock, index, ETF, commodity, or other security
- **Strike Price**: Price at which option can be exercised
- **Expiration Date**: Last day the option can be exercised
- **Premium**: Price paid for the option contract
- **Contract Size**: Typically 100 shares per standard option contract

## Option Types

- **Call Option**: Right to buy underlying asset
- **Put Option**: Right to sell underlying asset
- **LEAPS**: Long-term Equity AnticiPation Securities (up to 3 years)
- **Weekly Options**: Options with weekly expiration cycles
- **Quarterly Options**: Options with quarterly expiration cycles

## Option Pricing

**Option Premium Components**:
- **Intrinsic Value**: Real value if exercised immediately
  - Calls: Stock Price - Strike Price (if positive)
  - Puts: Strike Price - Stock Price (if positive)
- **Extrinsic Value (Time Value)**: Premium beyond intrinsic value
  - Time value premium
  - Volatility premium
  - Interest rate premium

**Option Value Factors**:
- Stock Price: Primary determinant of intrinsic value
- Strike Price: Relationship to stock price determines option type
- Time to Expiration: Longer time = higher premium
- Implied Volatility: Higher volatility = higher premium
- Interest Rates: Higher rates = higher call premiums
- Dividends: Higher dividends = lower call premiums

## Moneyness

- **In-the-Money (ITM)**: Option has intrinsic value; higher premium, lower theta, higher probability of profit
- **At-the-Money (ATM)**: Strike price near current stock price; highest theta, balanced risk/reward
- **Out-of-the-Money (OTM)**: No intrinsic value; lower premium, higher theta sensitivity, higher leverage

Understanding these fundamentals is essential before implementing any options strategy. Understanding fundamentals connects to all other options concepts including [[theta-time-decay]], [[ITM-vs-OTM-options]], and [[LEAPS-options]].^[raw/articles/Options Trading Guide.md]
