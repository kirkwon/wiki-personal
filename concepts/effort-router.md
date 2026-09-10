---
date: 2026-07-19
type: concept
title: Effort Router
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- decision
sources:
- hermes://skill/effort-router
description: Rule-based + learned reasoning effort classifier. Maps task descriptions
  to low/medium/high/max reasoning_effort. Tier 1 is deterministic (~100µs); Tier
  3 uses Thompson sampling bandit that learns from outcomes.
---

# Effort Router

> Rule-based + learned reasoning effort classifier. Maps task descriptions to low/medium/high/max reasoning_effort. Tier 1 is deterministic (~100µs); Tier 3 uses Thompson sampling bandit that learns from outcomes.

## Overview

- **Tier 1: Rule-Based (Always Available)** — Deterministic keyword-based classifier. Outputs `low` / `medium` / `high` / `max`. Pure regex/string matching, sub-millisecond, no dependencies.
- **Tier 3: Learned Router (After Data Accumulation)** — Thompson sampling bandit that learns the cheapest effort level per task cluster. See `references/integration-guide.md` for full architecture.
- **Override Hierarchy** — 1. Explicit user instruction → highest 2. Cron model pin → skip router 3. This router → default 4. Config default: medium

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/decision/effort-router/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
