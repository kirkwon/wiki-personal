---
date: 2026-07-19
type: concept
title: Dojo To Production Pipeline
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-to-production-pipeline
description: 'End-to-end: eval, triage, tune, validate, document.'
---

# Dojo To Production Pipeline

> End-to-end: eval, triage, tune, validate, document.

## Overview

- **When to Use** — - Dojo eval shows high correction counts, retry loops, or skill gaps. - Multiple tool failures appear but share an underlying root cause. - You need to tune false positives out of the detection logic. - You want structured documentation (diagrams + postmortem) after a fix.
- **Prerequisites** — - Dojo eval scripts at `~/.hermes/scripts/dojo-eval.py` and `~/.hermes/scripts/dojo-analyze.py`. - Circuit breakers at `~/.hermes/dojo-eval/circuit-breakers.json`. - Thresholds at `~/.hermes/dojo-eval/thresholds.json`. - `dojo-eval` and `cron-job-triage-repair` skills loaded for reference.
- **How to Run** — 1. Run eval: `terminal` → `python3 ~/.hermes/scripts/dojo-eval.py --days 7` 2. Read analysis: `read_file ~/.hermes/dojo-eval/latest_analysis.json` 3. Triage: classify each finding as real vs false positive. 4. Tune: `patch` the eval/analyze scripts to suppress false positives. 5. Validate: re-run eval, compare metrics. 6. Document: write postmortem with before/after tables and diagrams.

## Further detail

### Cross-Subsystem Root Cause Method

The same triage approach applies to any subsystem, not just dojo. The pattern from this session:

### Pitfalls

- **Do NOT encode environment-dependent failures as permanent constraints**. "browser tools don't work" or "vision_analyze is broken" are snapshots, not rules. The fix belongs in setup/troubleshooting, not in skills or memory. A negative claim hardens into a self-imposed refusal that persists months after the fix. - **One detector patch can eliminate dozens of findings** — don't create compensatory skills or error handlers for each finding when the detector itself is over-matching. Fix the detector. - **Thresholds drift as detection improves** — tightening patterns lowers counts, which may re-

### Verification

After the full pipeline, these must all be true:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-to-production-pipeline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
