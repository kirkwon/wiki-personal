---
source_path: Users/kirkwon/obsidian_vaults/personal/Personal Finance/Concepts/Options
  Trading.md
ingested: 2026-04-24
sha256: e43c6bd95f46dced5d3c5688c846ced0da7b5bbc1e7a8d347446bf1941420791
date: 2026-05-14
title: Options Trading
type: note
created: '2026-05-14'
updated: '2026-05-14'
---


---
type: concept
category:
- Personal Clients
created: 2026-04-20
modified: 2026-04-20
tags:
- personal-finance
- options
- derivatives
- risk
- leverage
- trading
related: []
status: complete
---


# Options Trading


## Quick Reference

### Field**: [[personal-clients]]
### Type**: Derivatives Strategy
### Purpose**: Leverage, hedging, income generation
### Key Concepts**: Calls, Puts, Greeks, Spreads
### Related Concepts**: [[risk-management]], [[retirement-planning]]



## Summary
Options are derivative contracts giving the right (but not obligation) to buy or sell an asset at a predetermined price (strike) by a specific date (expiration). Used for speculation (leverage), hedging (protection), and income generation (selling premium). Complex instruments with significant risk, especially for sellers.

## Option Basics

### Call Option
**Definition:** Right to BUY asset at strike price

**Profitable when:** Asset price > strike price + premium paid

**Use cases:**
- Bullish speculation
- Leveraged upside
- Income generation (covered calls)

**Example:**
- Stock at $100
- Buy $105 call for $2 premium
- At expiration:
  - If stock = $110 → Profit = $110 - $105 - $2 = $3/contract
  - If stock = $100 → Loss = $2 premium paid

### Put Option
**Definition:** Right to SELL asset at strike price

**Profitable when:** Asset price < strike price - premium paid

**Use cases:**
- Bearish speculation
- Portfolio insurance (protective puts)
- Income generation (cash-secured puts)

**Example:**
- Stock at $100
- Buy $95 put for $2 premium
- At expiration:
  - If stock = $80 → Profit = $95 - $80 - $2 = $13/contract
  - If stock = $100 → Loss = $2 premium paid

### Option Terminology

| Term | Definition | Example |
|-------|-------------|----------|
| **Strike Price** | Price at which you can buy/sell | $105, $95 |
| **Expiration** | Date option expires | Monthly, weekly |
| **Premium** | Price of option | $2/share = $200/contract |
| **In the Money (ITM)** | Option has intrinsic value | $105 call on $110 stock |
| **Out of the Money (OTM)** | No intrinsic value | $95 put on $100 stock |
| **Intrinsic Value** | ITM amount | $5 ($110 stock - $105 strike) |
| **Time Value** | Premium - intrinsic value | Extrinsic value |

**Note:** 1 option contract = 100 shares

## The Greeks

### Delta (Δ)
**Definition:** How much option price moves for $1 change in stock

**Range:** 0 to 1 for calls, -1 to 0 for puts

**Interpretation:**
- Delta = 0.5: Option moves $0.50 for every $1 stock move
- Delta = 0.8: Option moves almost 1:1 with stock
- Near expiration: Delta approaches 1 or 0

**Use:** Hedge ratio (number of shares to hedge)

### Gamma (Γ)
**Definition:** How much delta changes for $1 change in stock

**Interpretation:**
- High gamma: Delta changes rapidly (near expiration, near strike)
- Low gamma: Delta stable

**Risk:** Position delta changes unexpectedly

### Theta (Θ)
**Definition:** Daily time decay (options lose value as time passes)

**Typical values:**
- Far from expiration: -$0.01/day
- Near expiration: -$0.10/day
- At expiration: All time value goes to zero

**Lesson:** Time is premium seller's friend, buyer's enemy

### Vega (ν)
**Definition:** How much option price changes for 1% change in volatility

**Interpretation:**
- High vega: Option very sensitive to volatility changes
- Low vega: Option less sensitive

**Use:** Trade volatility, not just direction

### Rho (ρ)
**Definition:** How much option price changes for 1% change in interest rates

**Importance:** Generally low, more important for LEAPS (long-term options)

## Option Strategies

### 1. Covered Call
**Setup:** Own stock + sell call option

**Example:**
- Own 100 shares at $100
- Sell $105 call for $2 premium

**Profit scenarios:**
- Stock = $110: Sell at $105 + $2 premium = $107 (vs. $110 at $100)
- Stock = $100: Keep stock + $2 premium = $2 income
- Stock = $90: Keep stock + $2 premium = -$8 (stock loss) + $2 = -$6

**Use case:** Generate income on stocks you own
**Risk:** Missed upside if stock > strike

### 2. Protective Put (Married Put)
**Setup:** Own stock + buy put option

**Example:**
- Own 100 shares at $100
- Buy $95 put for $2 premium

**Profit scenarios:**
- Stock = $110: Keep stock, put expires worthless = -$2 premium
- Stock = $100: Keep stock, put expires worthless = -$2 premium
- Stock = $80: Put pays $15 ($95 strike - $80), net profit = $15 - $2 = $13

**Use case:** Insurance against market crash
**Cost:** Premium paid (like insurance premium)

### 3. Long Straddle
**Setup:** Buy call + buy put at same strike and expiration

**Example:**
- Buy $100 call for $3
- Buy $100 put for $3
- Total cost: $6

**Profit scenarios:**
- Stock = $110: Call = $10, Put = $0, Net = $10 - $6 = $4
- Stock = $90: Call = $0, Put = $10, Net = $10 - $6 = $4
- Stock = $100: Both worthless, Loss = $6

**Use case:** Expect big move (don't know direction)
**Break-even:** $106 or $94 (strike + cost)

### 4. Vertical Spread
**Setup:** Buy option + sell option at different strike

**Types:**
- **Bull Call Spread:** Buy lower strike call, sell higher strike call
- **Bear Put Spread:** Buy higher strike put, sell lower strike put

**Example (Bull Call Spread):**
- Buy $100 call for $5
- Sell $110 call for $2
- Net debit: $3

**Profit scenarios:**
- Stock = $115: Both ITM, Profit = $10 (long) - $5 (short) - $3 = $2
- Stock = $105: Long = $5, Short = $0, Net = $5 - $3 = $2
- Stock = $95: Both worthless, Loss = $3
---

**Use case:** Limited risk, leveraged directional bet

### 5. Iron Condor
**Setup:** Bull put spread + bear call spread

**Example:**
- Buy $90 put, Sell $95 put (credit $1)
- Buy $110 call, Sell $105 call (credit $1)
- Total credit: $2

**Profit scenarios:**
- Stock stays between $95 and $105: Keep full $2 credit
- Stock > $110: Loss = max loss from call spread
- Stock < $90: Loss = max loss from put spread

**Use case:** Income generation when expecting low volatility
**Risk:** Max loss known, limited upside

## Risk Management for Options

### 1. Position Sizing
**Rule:** Don't risk >2-5% of portfolio per trade

**Example:**
- Portfolio: $100k
- Max risk: $2-5k
- If option cost: $2 ($200/contract)
- Max contracts: 10-25 contracts

### 2. Greeks Limits
**Guidelines:**
- **Theta:** Understand daily time decay cost
- **Gamma:** Manage delta risk (especially near expiration)
- **Delta:** Know your effective share exposure

### 3. Stop Losses
**Hard stops:** Sell if option loses 50%
**Time stops:** Exit if not working by certain date
**Profit targets:** Take 50-100% gains early (don't get greedy)

### 4. Avoid High-Risk Strategies
**Naked calls:** Selling calls without owning stock (unlimited risk)
**Naked puts:** Selling puts without cash (substantial margin requirement)
**Binary options:** All-or-nothing, casino-like odds

## Trading Considerations

### Volatility
- **Implied Volatility (IV):** Market's expectation of future volatility
- **Historical Volatility (HV):** Actual volatility over past period
- **Mean Reversion:** High IV tends to fall, low IV tends to rise

**Trading ideas:**
- Buy options when IV is low (cheap)
- Sell options when IV is high (expensive)
- IV rank: Where current IV sits vs. historical range

### Time Decay
**Theta is enemy of buyers:**
- Options lose value daily
- Weekly options: Fast decay
- Monthly options: Moderate decay
- LEAPS (>1 year): Slow decay

**Rule:** If buying options, get direction right quickly

### Liquidity
- **Open Interest (OI):** Number of outstanding contracts
- **Volume:** Daily contracts traded

**Guidelines:**
- Trade options with high volume and OI
- Tight bid-ask spreads (<10% of mid-price)
- Avoid illiquid options (hard to exit)

### Assignment Risk
**Sellers of in-the-money options:**
- May be assigned to buy/sell shares
- Usually happens near expiration
- Plan for possibility of assignment

## Tax Treatment

### Short-Term vs. Long-Term
- **<1 year holding:** Ordinary income tax rate
- **>1 year holding:** Long-term capital gains rate

### Section 1256
- **Non-equity options (indexes, futures):** 60% of gains taxed at long-term rate, 40% at short-term
- More favorable than ordinary rates
- Requires mark-to-market annually

### Wash Sale Rule
- **30-day window:** Can't claim loss on same security
- Applies to options on same underlying
- Plan trades accordingly

## Common Mistakes

### ❌ Buying Out-of-the-Money Options
- Low probability of becoming profitable
- Options expire worthless frequently
- Better: Buy ITM or ATM

### ❌ Ignoring Time Decay
- Options lose value daily
- Don't hold too long without movement
- Understand theta cost

### ❌ Selling Naked Options
- Unlimited risk (calls) or substantial risk (puts)
- Margin requirements
- Need substantial capital

### ❌ Overleveraging
- Too many contracts for portfolio size
- One bad trade wipes out account
- Respect position sizing

### ❌ Not Understanding Greeks
- Don't know delta, gamma, theta exposure
- Portfolio behaves unexpectedly
- Understand your risk profile

## Best Practices

1. **Start small** - 1-2 contracts maximum
2. **Understand the math** - Profit/loss scenarios before entering
3. **Respect time decay** - Options have expiration
4. **Manage Greeks** - Know your delta, gamma, theta
5. **Use stops** - Exit losers quickly
6. **Avoid naked selling** - Unlimited risk scenarios
7. **Trade liquid options** - Easy entry/exit
8. **Consider volatility** - Buy low, sell high IV
9. **Plan for assignment** - If selling options
10. **Paper trade first** - Practice before real money

## When to Use Options

### **Appropriate for:**
- Experienced investors
- Understanding of derivatives
- Clear risk tolerance
- Time to monitor positions
- Adequate capital

### **Inappropriate for:**
- Beginning investors
- Retirement accounts (unless approved)
- Investors who can't monitor
- Limited capital (<$25k)
- Risk-averse individuals

## Alternatives

### **ETFs with Options Exposure:**
- **Covered call ETFs:** Automatic income generation
- **Protective put ETFs:** Built-in downside protection
- **Put-write ETFs:** Systematic option selling

### **Leveraged ETFs (no options knowledge needed):**
- **2x/3x ETFs:** Simplified leverage
- **Warning:** Decay from daily rebalancing
- **Use:** Short-term trading only

### **Direct Ownership:**
- **Stocks:** No time decay, no expiration
- **Index funds:** Diversified, low cost
- **Long-term holding:** Compounding works for you

## See Also
[[risk-management]] | [[retirement-planning]] | [[alternative-investments]] | [[derivatives]]

---
*Created: 2026-04-20*
