------


# Kelly Criterion (Bet Sizing)

**Also known as:** Kelly Bet, Optimal Bet Size, Growth-Optimal Betting

A formula for determining the optimal size of a series of bets to maximize long-term growth. Developed by John L. Kelly Jr. at Bell Labs in 1956.

## Core Idea

Given a known edge (probability of winning) and odds (payout ratio), the Kelly Criterion tells you exactly how much to bet to maximize your long-term growth rate. Bet too little and you grow slower. Bet too much and you risk ruin.

## The Formula

```
f* = (bp - q) / b

Where:
f* = fraction of bankroll to bet
b  = net odds received (e.g., b=1 means even money)
p  = probability of winning
q  = probability of losing (1-p)
```

For even-money bets: `f* = 2p - 1`

## Practical Application

- **Full Kelly** — maximizes growth but ~33% drawdown risk (aggressive)
- **Half Kelly** — 75% of maximum growth but only ~12% drawdown (conservative)
- **Quarter Kelly** — near-zero drawdown risk, still solid growth

## Connection to Strategic Framework

Kelly Criterion informs **Step 4 (Resource Positioning)** in the Strategic Filter. When deciding how much time/effort/tokens to commit, Kelly gives the mathematical framework for sizing your bet. Use Half Kelly for most strategic decisions — good growth with bounded downside.

## Key Insight

If the Kelly formula says "don't bet" (f* ≤ 0), you have no edge — skip the decision entirely. This is the mathematical basis for the SKIP outcome in the filter.

## Related
- Margin of Safety — buffer against estimation errors
- Leverage and Risk — what happens when you over-bet
- Peril of Leverage — the downside of over-concentration
- Base Rate Neglect — misestimating probabilities

Sources: [[Super Thinking - Gabriel Weinberg]]

See also: [[margin-of-safety-financial]]

See also: [[tail-event-thinking]]

See also: [[leverage-and-randomness]]

See also: [[peril-of-leverage]]

See also: [[base-rate-neglect]]

[[kelly-sizer]]
