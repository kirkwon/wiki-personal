---
created: 2026-08-23
updated: 2026-08-23
---
# Decision: Vol- and Volume-Aware Kelly Sizing

## Context
Viral GARCH thread (Aug 2026) prompted the question: how should volatility and volume impact Kelly sizing? Review of corpus showed the principle was decided (distribution over direction, via /kelly-sizer + Bayesian Rogue workflow) but no recorded application of vol-regime modeling to sizing. Stubs exist (risk-parity, volatility-surface, position-risk-profile — all empty).

## The Decision
Volatility enters the formula; volume enters the confidence.

1. Volatility -> direct, quadratic. Kelly: f* = mu/sigma^2. Double forecast vol -> quarter the size. Use forward-looking sigma^2 (GARCH(1,1) or volume-enhanced variants) over backward realized vol. Vol-regime shift = mechanical resize, before the distribution confirms.

2. Volume -> three indirect channels:
   * Estimation quality: volume-vol models (GARCH-V, HAR-RV) forecast sigma^2 better than price-only; high-volume moves carry more vol information
   * Edge erosion: mu must be net of price impact (Amihud); thin volume shrinks capturable edge, Kelly-on-net-mu auto-sizes down
   * Regime staleness: abnormal volume = earliest tell that (mu, sigma^2) inputs are stale

3. Operating rule:
   * Full fractional Kelly only when inputs stable
   * Volume anomaly (vs trailing median) -> drop to half-Kelly until regime re-prices
   * Vol spike -> resize immediately per formula; no discretion

## Supersedes / Relates
* Relates: [[kelly-criterion-bet-sizing]] (stub — promote or delete)
* Relates: [[risk-parity]] (stub), [[volatility-surface]] (stub), [[position-risk-profile]] (stub)
* Source stimulus: GARCH thread @Hrundel75, Aug 22 2026

## Open Items
* [ ] Choose vol estimator (GARCH(1,1) vs 20d realized vs HAR-RV)
* [ ] Define volume anomaly threshold (median multiple over lookback)
* [ ] Triage the three stubs: promote or delete