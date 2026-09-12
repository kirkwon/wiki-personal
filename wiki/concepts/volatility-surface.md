---
tags: [concept, stub]
created: 2026-06-16
date: 2026-06-16
type: concept
---

# volatility-surface

A volatility surface is a graphical representation that maps implied volatilities across different strike prices and time to expiration for options contracts on an underlying asset. It plots the relationship between these three variables (time, strike, and volatility) to provide a comprehensive view of market expectations regarding future price fluctuations. Unlike simple single-point estimates, the surface captures how volatility changes based on both moneyness (the ratio of strike to current price) and time decay, which is crucial for accurate option pricing models like Black-Scholes.

## Relevance to my decisions

The surface is the market's forward vol forecast — the σ² input that vol-aware Kelly ([[vol-volume-aware-kelly-2026-08-23]]) wants, implied rather than estimated. Regime shifts often show in the surface (term-structure inversion) before realized vol confirms.

See: [[index]] | [[vol-volume-aware-kelly-2026-08-23]]
---