---
date: 2026-07-19
type: concept
title: Knowledge Health
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- evals
- memory
- health
- monitoring
- automation
- research
sources:
- hermes://skill/knowledge-health
description: Monitor and maintain the 3-type memory system health (procedural/semantic/episodic).
  Use this skill when setting up, running, or extending the knowledge-eval.py pipeline,
  interpreting eval reports, tuning thresholds, or adding new health metrics to the
  knowledge metabolism loop. Covers the "evals" layer of the Memory + loops + harness
  + evals = self-improving agent formula.
---

# Knowledge Health

> Monitor and maintain the 3-type memory system health (procedural/semantic/episodic). Use this skill when setting up, running, or extending the knowledge-eval.py pipeline, interpreting eval reports, tuning thresholds, or adding new health metrics to the knowledge metabolism loop. Covers the "evals" layer of the Memory + loops + harness + evals = self-improving agent formula.

## Overview

- **Architecture** — The eval system is a single entry point that collects all metrics, compares against thresholds, stores a time series, and alerts on degradation:
- **When This Skill Activates** — Use this skill when: - The user asks to "check knowledge health", "run the eval", "see how healthy the system is" - Setting up or modifying the daily eval cron (job `knowledge-eval-daily` at 8am) - Tuning thresholds in `~/.hermes/knowledge-eval/thresholds.json` - Adding new metrics to `knowledge-eval.py` - The cron watchdog reports a threshold breach - Interpreting the time series in `~/.hermes/knowledge-eval/history.json` - Designing the eval layer for a new loop (external news, code intelligence, etc.)
- **The 3D Cube Pattern** — The eval fits into the broader **Knowledge Metabolism** framework (see `reference/3d-cube-pattern.md`):

## Further detail

### Key Files

| File | Purpose | |---|---| | `~/.hermes/scripts/knowledge-eval.py` | Main eval script — run daily by cron | | `~/.hermes/knowledge-eval/thresholds.json` | Configurable alert thresholds | | `~/.hermes/knowledge-eval/history.json` | Time series of all metrics (up to 365 entries) | | `~/.hermes/scripts/comprehension-debt-report.py` | Procedural memory eval (cross-ref gaps) | | `~/.hermes/scripts/stale-page-watchdog.sh` | Semantic memory eval (stale pages) | | `~/.hermes/scripts/gbrain-health-check.sh` | Semantic memory eval (brain score, orphans) | | `~/.hermes/scripts/memory-demotion.py` | Sem

### Cron

- **Job:** `knowledge-eval-daily` (id `38e94c97bf84`) - **Schedule:** `0 8 * * *` (daily at 8am) - **Type:** `no_agent` — runs `knowledge-eval.py` and outputs to origin - **Exit codes:** 0 = all nominal, 1 = threshold breach (triggers cron watchdog alert)

### Remediation Loop

The eval doesn't just detect — it **acts**. After collecting metrics, the cron wrapper runs `knowledge-gap-remediation.py`, which:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/knowledge-health/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
