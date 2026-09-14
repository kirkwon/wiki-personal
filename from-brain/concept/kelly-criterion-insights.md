---
type: concept
title: Kelly Criterion Insights - Risk Management and Edge Estimation
source: Twitter thread @RuujSs status 2082475631590469785
ingested_via: put_page
ingested_at: '2026-07-30T06:28:56.101Z'
source_kind: put_page
tags:
  - expected-value
  - kelly-criterion
  - position-sizing
  - risk-management
  - trading
created: 2026-07-30
---
# Kelly Criterion Insights

Key insights from Twitter thread by @RuujSs on the Kelly Criterion:

## Core Principle
The Kelly Criterion is simple: "if you know your edge, this is exactly how much to risk."
It provides the optimal fraction of capital to bet based on your edge.

## The Real Challenge
The difficulty isn't in the Kelly formula itself - it's in accurately estimating your edge (expected return).
Research shows that getting your expected return wrong can cost you 10x to 50x more than getting your risk estimates wrong, depending on aggression level.

## Key Takeaways
- Kelly sizing is about allocating capital to alpha (edge)
- The critical skill is estimating your true edge/expected return accurately
- Errors in expected value estimation are far more costly than errors in volatility/risk estimation
- Kelly grows your bankroll optimally when your edge estimates are correct

## Connection to Trading/Investing
- In trading contexts: Kelly size = optimal position size for a given strategy
- Requires accurate estimation of: win rate, average win, average loss (to compute edge)
- Misestimating edge leads to severe over/under-betting consequences

## Related Concepts
- Edge = Expected value of a bet/trade
- Kelly fraction = (edge / variance) approximately for small edges
- Fractional Kelly (betting less than full Kelly) reduces variance at cost of slower growth
