---
date: 2026-07-19
type: concept
title: Gbrain Ops
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/gbrain-ops
description: 'Manage gbrain operations: sync, dream, health checks, and concept synthesis.'
---

# Gbrain Ops

> Manage gbrain operations: sync, dream, health checks, and concept synthesis.

## Overview

- **1. Advisor Scan (entry point)** — The advisor surfaces 3 categories of findings, highest-severity first:
- **2. Sync** — The sync is delta-aware — it only processes changed files. Your cron jobs (`sync-llm-wiki-to-gbrain.sh`, `gbrain-live-sync.sh`) run this automatically.
- **3. Dream Cycle** — Runs nightly via cron. Cross-links concepts, generates summaries, evolves the knowledge graph. No manual intervention needed.

## Further detail

### 6. Concept Synthesis (Heavy Work)

The `concept-synthesis` skillpack does 4 phases:

### 7. Retrieval Reflex

GBrain's Retrieval Reflex has two parts:

### 8. Temporal Retrieval & Recency Decay

gbrain already has a full temporal-retrieval substrate: `effective_date` (when a page is *about*), hyperbolic recency decay at search time (`coefficient × halflife / (halflife + days_old)` per slug-prefix), intent→recency auto-on, and trajectory injection in `gbrain think`. The decay map is tunable via a 4-level override chain: `DEFAULT → gbrain.yml recency: → GBRAIN_RECENCY_DECAY env → per-call`. Parse errors fail loud (do not "fix" this to skip-bad-entry).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/gbrain-ops/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
