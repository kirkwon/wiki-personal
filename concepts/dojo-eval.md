---
date: 2026-07-19
type: concept
title: Dojo Eval
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/dojo-eval
description: 'Session performance evaluation: monitor agent session logs, analyze
  failures, apply auto-fixes, and update circuit breakers. Implements the full monitor
  → analyze → auto‑fix → circuit‑breaker pipeline.'
---

# Dojo Eval

> Session performance evaluation: monitor agent session logs, analyze failures, apply auto-fixes, and update circuit breakers. Implements the full monitor → analyze → auto‑fix → circuit‑breaker pipeline.

## Overview

- **Output** — The eval produces:
- **Thresholds** — Configured in `~/.hermes/dojo-eval/thresholds.json`:
- **The Dojo Pipeline (Auto‑Heal)** — **Note:** The auto-fix phase (step 6) routes all recommendations through `fix-router.py`, an effort-based classifier. Easy fixes (`add_prerequisite`, `reset_circuit`) are auto-executed with SHA256 verification. Medium fixes (`increase_timeout`) are recommended with config file paths but not auto-applied. Complex fixes (`add_retry_handling`, `investigate`) gather prior-art resources from disk + learned patterns + circuit state, then generate scaffolded plans in `~/clawd/.hermes/plans/` with a Prior Art section. See `references/auto-heal-idempotency-fix.md` for why fake comment-only patches were

## Further detail

### Related

- `/dojo-fix` — Applies the fix recommendations (legacy, still available) - `read-the-damn-docs` — Retry Discipline rules (prevents loops) - `knowledge-metabolism` — run‑health includes dojo‑eval - `references/outer-loop-self-healing.md` — Details on the self‑healing mechanism for the outer‑loop eval script - `references/auto-heal-process.md` — Overview of the monitor → analyze → auto‑fix → circuit‑breaker pipeline - `references/classification-execution-gap.md` — Three-layer fix for the analyzer→router leak - `scripts/dojo-weekly-rca.py` — Weekly RCA review script (runs via `weekly-dojo-rca` c

### Triage Methodology — Most Reports Are 1-3 Root Causes, Not N Bugs

When a dojo report arrives with many flagged items, most are **cascading symptoms of 1-3 shared root causes**, not independent bugs. Do not action items one-by-one — group by the underlying error and fix the root.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/dojo-eval/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
