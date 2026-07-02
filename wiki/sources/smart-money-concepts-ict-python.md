---
type: source
title: "Smart Money Concepts — ICT Trading Indicators in Python"
author: "Josh Yattridge (joshyattridge)"
repo_url: "https://github.com/joshyattridge/smart-money-concepts"
pkg: "smartmoneyconcepts"
stars: 1809
language: Python
updated: 2026-06-29
tags:
  - trading
  - ict
  - order-blocks
  - fvg
  - liquidity
  - market-structure
  - price-action
  - pattern-detection
related:
  - mean-variance-myopia-under-stochastic-volatility
  - pca-random-matrix-theory-equity-markets
  - factors
---

# Smart Money Concepts — ICT Trading Indicators in Python

A Python package implementing Inner Circle Trader (ICT) concepts as deterministic OHLC pattern detectors. 1.8k ⭐, published on PyPI.

## Indicators

### Fair Value Gap (FVG)
3-candle pattern: when the previous high is lower than the next low (bullish) or the previous low is higher than the next high (bearish). Tracks when the gap gets mitigated (filled). Has an option to join consecutive FVGs into one zone.

**Vectorized implementation** — pure numpy `np.where()` on shifted columns. ~10 lines of core logic.

### Swing Highs/Lows
Rolling window pivot detection: a candle is a swing high if its high is the max of `swing_length` candles before and after. Includes an iterative cleanup loop that resolves competing swings (if two highs are adjacent, keep the higher one).

### Break of Structure (BOS) / Change of Character (CHoCH)
Pattern-matches sequences of alternating swings against ideal market structure:
- Bullish BOS: `[-1, 1, -1, 1]` with ascending levels → trend continuation
- Bullish CHoCH: `[-1, 1, -1, 1]` where the last swing exceeds the first → trend reversal

The distinction between BOS and CHoCH is that BOS maintains the trend direction while CHoCH signals a reversal. Both track a "broken index" when price reaches the level.

### Order Blocks (OB)
**Most sophisticated indicator** — a full lifecycle state machine:
1. When price breaks a swing high/low, mark the preceding candle(s) as the order block zone
2. Track active OBs in two lists (bullish/bearish)
3. Each tick, check if price has returned to the OB → mark as "breaker" (activated)
4. If price continues past the OB's far side → invalidate the OB and remove from state
5. Volume confirmation via 3-candle sum and a strength ratio (min/max of recent volume blocks)

### Liquidity
Simple clustering algorithm: scan swing highs/lows within a `range_percent` band. If 2+ swing points cluster within X% of each other, it's a liquidity pool. Tracks the "swept" index when price reaches the cluster.

### Sessions & Kill Zones
Hard-coded time windows for major forex sessions: Sydney (21:00-06:00), Tokyo (00:00-09:00), London (07:00-16:00), New York (13:00-22:00), plus "kill zones" for Asian open, London open, NY open, and London close.

### Retracements
Percentage pullback from the last swing high/low. Tracks both current and deepest retracement within the current swing segment.

## Architecture Notes

- **Clean pattern**: Each indicator is a `@classmethod` on the `smc` class. Consistent I/O: OHLC DataFrame in → multi-column Series out.
- **Validated input**: Custom `@inputvalidator` decorator normalizes column names and checks required columns exist.
- **Pure numpy**: Core logic is vectorized `np.where`, `np.roll`, `np.searchsorted`. The OB code is the only one with Python loops (for the state machine tracking).
- **Pandas-native**: Returns DataFrames with named columns that can be merged back or used with `.loc` for backtesting.

## Limitations

- **No statistical validation** — zero. Deterministic patterns with no backtested P&L, Sharpe, or win rate.
- **ICT is retail lore** — invented by Michael Huddleston (Inner Circle Trader), a controversial figure. No quant desk uses BOS/CHoCH as factors.
- **Single timeframe** — all indicators operate on one timeframe with no multi-timeframe confirmation or regime conditioning.
- **No risk management** — pure signal generation. No position sizing, stop loss logic, or portfolio integration.

## Ideas Worth Extracting

1. **OB lifecycle as a general zone state machine** — the active→breaker→invalidated pattern is a clean abstraction for any support/resistance system. Could be generalized to work with statistical zones (e.g., PCA eigenportfolio bands) instead of exact price levels.

2. **FVG on factor-hedged residuals** — Fair Value Gaps in the idiosyncratic return component (after stripping the 5-15 eigenportfolios) would be more tradeable than gaps in raw price, because the market-wide tide is already removed. This is a direct bridge between this repo and [[sources/pca-random-matrix-theory-equity-markets|the PCA/RMT framework]].

3. **Volume confirmation as a signal filter** — the OB code's volume ratio (comparing breakout candle volume to the preceding 2 candles) is simple but effective. Could be added as a filter to any entry signal.

4. **Session-aware analysis** — the kill zone concept overlays time-based regime context that could complement our vol regime modeling in [[mean-variance-myopia-under-stochastic-volatility|causal-portfolio-research]].

## Cross-References

- [[pca-random-matrix-theory-equity-markets]] — FVG on residuals vs raw price is the key synthesis point
- [[mean-variance-myopia-under-stochastic-volatility]] — OB lifecycle as a regime detection state machine
- [[factors]] — price-action factors vs statistical factors; complementary lenses on market structure
