---
date: 2026-07-19
type: concept
title: Gbrain Minions
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gbrain
- minions
- jobs
- background
- durable
- research
sources:
- hermes://skill/gbrain-minions
description: Durable job queue for GBrain — replaces fragile sub-agent spawning for
  deterministic work. Survives gateway restarts, streams progress, supports pause/resume.
  v0.11+.
---

# Gbrain Minions

> Durable job queue for GBrain — replaces fragile sub-agent spawning for deterministic work. Survives gateway restarts, streams progress, supports pause/resume. v0.11+.

## Overview

- **When This Skill Activates** — Use this skill when the user: - Mentions "minions", "background jobs", "durable queue" - Needs to run deterministic work on a schedule (sync, embed, exports) - Wants to avoid fragile sub-agent spawning for background tasks - Asks about `gbrain jobs` commands - Mentions gateway crashes or spawn failures
- **Routing Rule** — > **Deterministic** (same input → same steps → same output) → **Minions** > **Judgment** (input requires assessment or decision) → **Subagents**
- **Production Numbers (Garry Tan's Deployment)** — | Metric | Minions | `sessions_spawn` (Subagents) | |---------|----------|-----------------------------| | Wall time (30-day social pull) | **753ms** | **>10,000ms** (gateway timeout) | | Token cost | **$0.00** | ~$0.03 per run | | Success rate | **100%** | **0%** (couldn't even spawn) | | Memory/job | ~2 MB | ~80 MB | | Scale (19 crons, 36mo data) | 15 min total, $0 | ~9 min best case, ~$1.08, ~40% failure |

## Further detail

### Stalled Job Detection

Minions detects stalled jobs (no heartbeat for >5min) and marks them as `failed`.

### Minions vs Hermes Cron

| Feature | Minions | Hermes Cron | |---------|----------|-------------| | Survives restart | ✅ | ✅ | | Progress streaming | ✅ | ❌ | | Pause/resume | ✅ | ❌ | | Durable across workers | ✅ | ❌ | | Hermes session context | ❌ | ✅ | | Token cost for deterministic work | $0 | $0+ (if using LLM) |

### Pitfalls

- **`sessions_spawn` for deterministic work is categorically wrong** — 753ms vs 10,000ms, $0 vs tokens, 100% vs 0% success - **Minions requires Postgres backend for full durability** — PGLite has limited job queue features - **Supervisor vs raw worker** — Always prefer `gbrain jobs supervisor` (auto-restart, PID lock, audit). Raw `gbrain jobs work` has no crash recovery - **Stalled jobs** — Check `gbrain jobs stats` for stalled jobs. Minions auto-detects (>5min no heartbeat) but manual cleanup may be needed - **Fan-out aggregation** — Children must write to `child_done` inbox. Aggregator must

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/gbrain-minions/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
