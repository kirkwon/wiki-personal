title: Mega-IPO & SPCX Tracking
status: active
priority: P2
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Mega-IPO & SPCX Tracking

## Summary
Tracking SpaceX (SPCX) IPO mechanics, Nasdaq-100 inclusion catalyst (Jul 7), and Anthropic/OpenAI IPO pipelines with automated monitoring.

## Why
SPCX is the largest IPO in history ($85.7B raised, $2.1T market cap) with a confirmed Nasdaq-100 inclusion creating forced passive buying. Understanding the mechanics enables informed positioning.

## Progress

- [x] Alpha Vantage MCP verified for SPCX pricing ($153.23 Jun 26 close)
- [x] 30-day daily data pulled: spike-and-fade confirmed ($161 → $226 → $153)
- [x] Research confirmed: Nasdaq-100 inclusion Jul 7, 2026 (fastest in history)
- [x] Social sentiment research completed (Reddit, X, HN scan)
- [x] IPO Catalyst Tracker cron updated with correct SpaceX context
- [x] SPCX Daily Monitor cron running (Mon-Fri 6:30am)
- [x] Quadruple witching alerts scheduled (Sep, Dec, Mar, Jun)
- [x] Deep-dive scenario analysis (`~/brain/spacex-spcx-deep-dive-scenarios.md`)
- [x] Anthropic margin cascade model (`~/brain/anthropic-gross-margin-cascade-model.md`)
- [ ] Monitor Jul 1-2 forced buying window
- [ ] Track post-Jul 7 lock-up expiry impact

## Next Steps
1. **Jul 7:** Monitor NDX-100 inclusion — first passive flow estimates
2. **Post-Jul 7:** Track lock-up expiry timeline and insider selling pressure
3. Track Anthropic S-1 filing (target Oct 2026 listing)

## Blockers / Needs Input
- Markets closed (weekend) — next data Mon Jun 29

## Key Files / Resources
- `~/brain/spacex-spcx-deep-dive-scenarios.md` — SOTP + 4 scenarios
- `~/brain/anthropic-gross-margin-cascade-model.md` — margin cascade
- `~/brain/mega-ipo-index-impact-2026.md` — passive flow mechanics
- `~/clawd/research/spcx_scenario_dashboard.html` — interactive dashboard
- Price data: Alpha Vantage MCP > EDGAR MCP > local firecrawl

## Automation / Cron
- `41cdd29b040b` — Mega-IPO Catalyst Tracker (every 6h)
- `531be4d2c050` — SPCX Daily Monitor (Mon-Fri 6:30am)
- `b52b3bc774e8` — Quadruple Witching Sep 2026
- `f21ce00491bb` — Quadruple Witching Dec 2026
- `364f97e6d830` — Quadruple Witching Mar 2027
- `df0ec59f8367` — Quadruple Witching Jun 2027
- `987d15a345c0` — Market Close Summary (Mon-Fri 1:05pm)

## Notes
- SPCX = SpaceX, NOT the Defiance SPAC ETF (that's SPAK)
- S&P 500 declined to change rules (needs 4 profitable quarters) — NDX-100 only
- MSCI added SpaceX to Global Standard indexes effective Jun 29
- Leveraged ETFs: SPCF/SPCL (2x long), SPCH (2x long), SSPC (2x short)
