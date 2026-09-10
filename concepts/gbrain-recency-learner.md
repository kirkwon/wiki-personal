---
date: 2026-07-19
type: concept
title: Gbrain Recency Learner
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gbrain
- retrieval
- recency
- temporal
- learning-loop
- bayesian
- decay
- uncategorized
sources:
- hermes://skill/gbrain-recency-learner
description: 'Self-tuning recency-decay halflives for gbrain retrieval. Nightly loop:
  contradiction probe → supersession rate per prefix → Wilson-CI-gated halflife update
  → human-reviewed env var (GBRAIN_RECENCY_DECAY).'
---

# Gbrain Recency Learner

> Self-tuning recency-decay halflives for gbrain retrieval. Nightly loop: contradiction probe → supersession rate per prefix → Wilson-CI-gated halflife update → human-reviewed env var (GBRAIN_RECENCY_DECAY).

## Overview

- **The problem** — gbrain discounts older knowledge via a per-prefix hyperbolic decay map (`coefficient × halflife / (halflife + days_old)`). The map is static defaults + manual YAML/env overrides. Nothing adjusts it from evidence. Result: halflives are guesses, and "we weren't vigilant about timestamping" means the guesses are uncorrectable for fallback-dated pages.
- **The signal** — `gbrain eval suspected-contradictions` classifies retrieval pairs into six verdicts. One of them — `temporal_supersession` — means "a newer claim overtook an older claim that retrieval surfaced alongside it." That is exactly "we discounted too little for this prefix." The finding carries the slug, so it's per-prefix attributable.
- **Why this design works (grounded in gbrain source)** — - **Zero code changes to gbrain.** The decay map is resolved fresh per search call via `resolveRecencyDecayMap()`. That function reads `process.env.GBRAIN_RECENCY_DECAY` on every invocation (`postgres-engine.ts:5498`, `pglite-engine.ts:5343`, both call it with no args — env + defaults only). The learned map is delivered as this env var.

## Further detail

### Parameters (tunable via script constants)

| Parameter | Default | Meaning | |---|---|---| | `HIGH_THRESHOLD` | 0.15 | Wilson CI lower bound above which we shrink halflife | | `LOW_THRESHOLD` | 0.03 | Wilson CI upper bound below which we grow halflife | | `SHRINK_FACTOR` | 0.8 | Multiply halflife when supersession is too high | | `GROW_FACTOR` | 1.1 | Multiply halflife when supersession is too low | | `MIN_JUDGED_PAIRS` | 30 | Below this, Wilson CI too wide to act (skip) | | `MAX_MOVE_PCT` | 0.25 | Clamp any single halflife change to ±25% | | `BUDGET_USD` | 1.0 | Per-run LLM cost cap (probe judge model) | | `TOP_K` | 5 | Retrieval dept

### Verification (the "verifiable" requirement)

Two gates before a learned map is committed:

### Pitfalls

- **Empty table on first run.** `eval_contradictions_runs` starts empty. The first probe run populates it. The script handles this — it runs the probe even with no history, then aggregates from whatever it finds.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gbrain-recency-learner/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
