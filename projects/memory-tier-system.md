---
type: project
title: Memory Tier System (4-Tier HOT/WARM/COOL/COLD)
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P1
ingested_via: put_page
ingested_at: '2026-09-10T13:00:28.127Z'
source_kind: put_page
---

# Memory Tier System

## Summary
4-tier memory hierarchy for Hermes agent: HOT (session state), WARM (MEMORY.md), COOL (session search), COLD (GBrain/wikis). Implements importance-scored eviction, cron-driven demotion, event-driven promotion.

## Progress

### Phase A: Foundation (COMPLETE)
- [x] Memory budget bumped: WARM 2200→3500, User 1375→2000
- [x] `memory-demotion.py` written (weekly scan, stale→COLD)
- [x] `promotion-tracker.py` written (observation counter, promote after 3+ hits)
- [x] `tier-tracker.json` infrastructure created
- [x] Spec v1.0 written (230 lines, 11 sections)

### Phase B: Core Scripts (COMPLETE)
- [x] Demotion cron script functional
- [x] Promotion tracker infrastructure built
- [x] Hermes scheduler wiring
- [x] End-to-end test with dummy stale entry

### Phase C: Intelligence (IN PROGRESS)
- [x] c1: Conflict detection on memory writes (script started)
- [ ] c2: Importance-scored eviction when tiers overflow
- [ ] c3: Session-start promotion checks

### Phase D: Monitoring (NOT STARTED)
- [ ] d1: Weekly health report (tier sizes, promotion/demotion counts)

## Next Steps
1. Complete Phase C (eviction logic + session-start checks)
2. Build Phase D (weekly health report)
3. Test `memory-health.py` consolidated script

## Key Files
- `~/wiki-personal/hermes-memory-tier-system-spec.md` — spec v1.0 (230 lines)
- `~/.hermes/scripts/memory-demotion.py` — weekly demotion scanner
- `~/.hermes/scripts/promotion-tracker.py` — promotion tracker
- `~/.hermes/memory/tier-tracker.json` — tier tracking state
- `~/.hermes/scripts/memory-health.py` — Phase C+D consolidated (incomplete)

## Automation / Cron
- `e5ab906956e9` — Memory Tier Demotion (Sun 9am) ⚠️ ERRORING — needs investigation

## Blockers
- Memory Tier Demotion cron `e5ab906956e9` is erroring — needs debugging
- Phase C partially built (`memory-health.py` started but not complete)

## Notes
- Tier precedence: COLD wins facts, HOT wins operational state
- Demotion: weekly cron scan, stale entries → COLD/GBrain
- Promotion: event-driven, after 3+ session observations
- Write strategy: tiered by severity (critical=write-through, routine=write-back)
