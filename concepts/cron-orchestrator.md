---
type: concept
title: Cron Orchestrator
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Cron Orchestrator
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- cron
- scheduling
- orchestration
- optimization
- automation
- token-savings
- devops
sources:
- hermes://skill/cron-orchestrator
description: 'Monthly cron job orchestrator — audits, tunes, and migrates scheduled
  jobs. Three modes: Audit (read-only report), Tune (adjust schedules within bounds),
  Migrate (convert agent→deterministic). Designed for the Bayesian Rogue''s maintenance-over-willpower
  philosophy.'
---

# Cron Orchestrator

> Monthly cron job orchestrator — audits, tunes, and migrates scheduled jobs. Three modes: Audit (read-only report), Tune (adjust schedules within bounds), Migrate (convert agent→deterministic). Designed for the Bayesian Rogue's maintenance-over-willpower philosophy.

## Overview

- **Design Philosophy** — > "Maintenance over willpower. A system that tunes itself is a system that scales."
- **Job Classification Taxonomy** — | Type | `no_agent` | Burns Tokens | Typical Schedule | Example | |------|-----------|-------------|-----------------|---------| | **Deterministic** | `true` | No | Every 5m–24h | Sync, export, health check | | **Agent-Light** | `false` | Low (1-2 tool calls) | Daily–Weekly | Update check, simple report | | **Agent-Heavy** | `false` | High (reasoning) | Weekly–Monthly | Conversation review, synthesis | | **Hybrid** | `false` | Medium | Daily | Dream cycle (script + agent interpretation) |
- **Token Cost Model** — | Job Type | Est. Tokens/Run | Runs/Day | Daily Cost | |----------|----------------|----------|------------| | Deterministic (no_agent) | 0 | Any | 0 | | Agent-Light | 2K–5K | 1–8 | 2K–40K | | Agent-Heavy | 10K–30K | 0.1–1 | 1K–30K | | Hybrid | 5K–15K | 1 | 5K–15K |

## Further detail

### Schedule Bounds Reference

| Job | Min Interval | Max Interval | Rationale | |-----|-------------|-------------|-----------| | Health check | 5 min | 15 min | Fast failure detection | | Delta sync | 30 min | 6 hours | Balance freshness vs cost | | Export/backup | 1 hour | 24 hours | Data loss window | | Report generation | 6 hours | 24 hours | Human consumption rate | | Deep synthesis | 1 day | 7 days | Research doesn't change hourly | | Vault maintenance | 1 day | 14 days | Low urgency |

### Dependency Graph

Some jobs must run in order:

### Orchestrator Cron Jobs

| Job | Schedule | Mode | Script | |-----|----------|------|--------| | `cron-monthly-audit` | 1st of month, 8am | Audit | `cron-audit.sh` (no_agent=true) | | `cron-quarterly-tune` | 1st of quarter, 9am | Tune | `cron-tune.sh` |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/cron-orchestrator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
