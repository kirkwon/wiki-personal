---
date: 2026-08-02
type: concept
title: Dojo Eval Tuning
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-eval-tuning
description: Patch dojo-eval.py + fix-router.py to cut false positives, prevent queue
  accumulation, and calibrate monitoring thresholds.
---

# Dojo Eval Tuning

> Patch dojo-eval.py + fix-router.py to cut false positives, prevent queue accumulation, and calibrate monitoring thresholds.

## Overview

- **When to Use** — - The dojo report shows 50+ user corrections but most are system messages - Retry loop count is 200+ but 95% come from one free-tier model - Tool failures show 🔴 but all are model usage errors (wrong params) - `skills_list` shows as a failing tool (persisted-output false positive) - After a tuning session, you need to verify the patches hold
- **The Tuning Targets** — Each false-positive class maps to a specific patch location in `dojo-eval.py`. Work through them top-to-bottom — earlier fixes reduce noise that obscures later diagnosis.
- **The Outer-Loop Plan Regeneration Trap** — **Symptom:** The outer-loop self-healing crons (`outer_loop_dojo_eval.py`, `outer_loop_knowledge_eval.py`, running every 15 min) generate 90+ plan files over 10 days. Same plan types regenerated daily. Zero plans applied.

## Further detail

### Fix-Router Queue Deduplication (fix-router.py)

**Problem**: `queue_complex()` in `fix-router.py` had zero deduplication. Every daily cron run re-queued the same 10 recommendations → 70 entries after 5 days (all `status: pending`), plus 29 duplicate plan files in `~/clawd/.hermes/plans/`. The queue grew monotonically and was never drained because no downstream process consumes it.

### Knowledge-Eval Structural Threshold Calibration

**Problem**: `knowledge-eval.py` had `stale_pages_max: 100` (default) / `900` (thresholds.json override), but actual stale pages = 2464 (88% of 2796 wiki pages). The threshold was **structurally impossible** — it could never pass. `STALE_DAYS = 90` in `wiki_api.py` means most wiki pages are "stale" by design (knowledge archive, not a news feed).

### Verification

- ✅ No threshold breaches - All tool failures 🟡 with `(model error)` or `(stale ref)` tags - Corrections single digits (< 15)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-eval-tuning/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
