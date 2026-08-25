---
title: Clawd Workspace Infrastructure
status: active
priority: P3
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Clawd Workspace Infrastructure

## Summary
Core Hermes workspace (`~/clawd/`): AGENTS.md, SOUL.md, MEMORY.md, heartbeat, memory files, and supporting tooling.

## Why
The workspace is the agent's home — maintaining it ensures continuity across sessions, clean state management, and durable memory.

## Progress

- [x] AGENTS.md established with workspace conventions
- [x] SOUL.md (Bayesian Rogue identity) stable
- [x] MEMORY.md with curated long-term memory (last curated Jun 12)
- [x] HEARTBEAT.md with checklist
- [x] SENSITIVE-DATA-POLICY.md established
- [x] Memory Tier System v1.0 active (demotion cron, promotion tracker)
- [x] 49 cron jobs running (4 paused, 1 erroring)
- [x] Project dashboard infrastructure (this project)
- [ ] MEMORY.md needs re-curation (stale — Jun 12)
- [ ] Master backlog (25 items) needs reconciliation with project dashboard
- [ ] B_D_blockers.md needs review
- [ ] LLM_S1_S2_Failure_Analysis (4 versions) — consolidate or archive

## Next Steps
1. Re-curate MEMORY.md (move project details to project files, keep only identity + preferences)
2. Reconcile master-backlog items into project files
3. Clean up stale files (4 failure analysis versions, empty verify script)
4. Review paused cron jobs (4 paused — resume or remove?)

## Blockers / Needs Input
- Which paused crons to resume? (kanban-gemini-dispatch/collect, GBrain health check old version, morning briefing old version)

## Key Files / Resources
- `~/clawd/AGENTS.md` — workspace conventions
- `~/clawd/MEMORY.md` — curated memory
- `~/clawd/HEARTBEAT.md` — heartbeat checklist
- `~/clawd/master-backlog-from-history.md` — recovered backlog (25 items)
- `~/clawd/B_D_blockers.md` — blockers file
- `~/clawd/skills-dashboard-spec.md` — skills dashboard spec

## Automation / Cron
- `0bc2dcd68bb7` — Weekly Conversation Review (Sun 9pm)
- `4896a2d1320d` — Cron Monthly Audit (1st of month 8am)
- `8bd88c70187d` — Cron Failure Watchdog (every 30m)
- `e5ab906956e9` — Memory Tier Demotion (Sun 9am) ⚠️ ERROR
- `44caca47bd0a` — Weekly Review (Sun 6pm)
- `b7a7fecc44d3` — Comprehension Debt Weekly (Mon 9am)
- `456a93125a05` — Stale Page Watchdog (Mon 10am)

## Notes
- 2 cron jobs erroring: Financial Strategy Notebook + Memory Tier Demotion — both need investigation
- Kanban/Symphony infrastructure exists but dispatch is paused (see Loop Engineering project)
