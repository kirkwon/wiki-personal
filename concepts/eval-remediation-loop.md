---
date: 2026-07-19
type: concept
title: Eval Remediation Loop
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Cron
- Remediation
- Self-Healing
- Evals
- Loops
- devops
sources:
- hermes://skill/eval-remediation-loop
description: Close the loop on monitoring crons with auto-remediation.
---

# Eval Remediation Loop

> Close the loop on monitoring crons with auto-remediation.

## Overview

- **When to Use** — - A cron measures a metric and alerts on breach but never fixes the root cause - Docs say "Auto-enqueue remediation" or "self-healing" but nothing is wired - A gap metric exists (count) but there's no path from detection to action - You want to close the Detect→Act loop on an existing eval without adding infrastructure
- **Prerequisites** — - An existing eval/monitoring script that exits with a breach code (e.g., exit 1 = threshold exceeded) - The Hermes task queue at `~/.hermes/queue/__main__.py` with `enqueue`/`list` subcommands - A **gap source that lists individual items by name** — not just a count. If the source only emits a number, enhance it first (you can't remediate what you can't name)
- **How to Run** — Invoke through the `terminal` tool. The workflow is four phases — Orient, Build, Wire, Validate — executed via the `plan` skill then `subagent-driven-development`.

## Further detail

### Pitfalls

- **Count-only gap source**: `cross-ref --hermes` outputs `547` (a count), `cross-ref --wiki` outputs named items. Only the named direction can be auto-remediated. Check before planning. - **Phantom gap (measurement artifact)**: Before building remediation, verify the metric measures what you think. The stale-pages metric (`STALE_DAYS=90` in `wiki_api.py`) flags pages with *no frontmatter date* as stale — on a batch-imported vault, 90%+ of "stale" pages are missing metadata, not decaying content. The real fix is a one-time metadata backfill, not a remediation loop. Always check the gap source'

### Verification

Expected: eval metrics (exit 1 breach swallowed) → "🔧 Running gap remediation..." → N items enqueued → `exit 0`. Then confirm the queue shows tasks tagged with your gap tag, and the state file tracks exactly those N names.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/eval-remediation-loop/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
