---
date: 2026-08-02
type: concept
title: Finance Recommendation Verification
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- finance
- verification
- portfolio
- backtesting
sources:
- hermes://skill/finance-recommendation-verification
description: 'Iron rule: backtest any portfolio allocation/trade recommendation against
  the current portfolio before presenting it as advice. Thesis-aligned ≠ return-positive.'
---

# Finance Recommendation Verification

> Iron rule: backtest any portfolio allocation/trade recommendation against the current portfolio before presenting it as advice. Thesis-aligned ≠ return-positive.

## Overview

- **The Iron Rule** — **Never present target/rebalanced/optimized portfolio weights as advice without first backtesting the proposed allocation against the *current* portfolio's actual historical performance.** Thesis-aligned ≠ return-positive.
- **Why This Skill Exists** — Session 2026-07-20: A portfolio rebalance recommendation was derived *correctly* from a confirmed bond-equity correlation breakdown (90-day rolling corr = 0.61, thesis validated). But the proposed target weights would have cost **$412K** over 3 years vs. the existing concentrated winners — selling FDGRX/FCNTX/AAPL/ORCL (the alpha engine) to buy lower-returning commodities/gold. The diagnosis was right; the prescription was wrong. The user called it "terrible advice." They were right.
- **The Required Sequence** — 1. **Diagnose** (correlation analysis, thesis validation, etc.) — fine. 2. **Generate candidate target weights** — fine. 3. **⛔ GATE 1: Regime Check** — Before backtesting, check the current Markov regime for each asset in the recommendation. - Run: `python3 ~/clawd/101.MarkovRegimeDetection/03.Scripts/regime_risk_gate.py --years 5` - Scale target weights by `(1 - stationary_bear)` — this is the **regime-adjusted position size**. - If any asset has `stationary_bear > 0.15` (RED gate): flag it explicitly. The recommendation must acknowledge elevated bear risk. - If portfolio-level `stationary_b

## Further detail

### What Counts as a "Recommendation"

This gate applies to *any* allocation recommendation: - Efficient frontier output - Risk-parity / factor allocation - Thesis-driven rebalance - Options-overlay cost analysis (if you can't backtest it, you must state "untested" explicitly — never "recommended")

### Decision Reversal (When the Backtest Kills the Recommendation)

When the backtest shows the recommendation underperforms, the correct action is to **reverse**, not defend:

### Optimizer Artifacts to Flag

When running Markowitz optimization (efficient frontier):

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance-recommendation-verification/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
