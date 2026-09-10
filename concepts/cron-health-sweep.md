---
date: 2026-07-19
type: concept
title: Cron Health Sweep
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/cron-health-sweep
description: Audit all cron jobs, classify failures, and batch-fix shared root causes.
---

# Cron Health Sweep

> Audit all cron jobs, classify failures, and batch-fix shared root causes.

## Overview

- **When to Use** — - Multiple cron jobs erroring simultaneously (likely shared root cause). - After any system-level change (Python version, PATH, `.env`, Hermes upgrade). - Dojo eval shows widespread tool failures across sessions. - Weekly/monthly cron hygiene check ("are all my jobs healthy?"). - A job references a deleted skill or moved script (`last_run_at: null`).
- **Prerequisites** — - `cronjob` tool for listing and managing jobs. - `terminal` tool for running scripts and probes. - `read_file` for inspecting scripts, `.env`, circuit breakers. - `search_files` for finding scripts and error patterns.
- **How to Run** — 1. `cronjob` action=`list` — snapshot all jobs and their `last_status`. 2. Group erroring jobs by failure pattern (shared root cause vs independent). 3. Test the shared-suspect hypothesis (`.env` quoting, PATH, missing deps). 4. Apply fixes, verify each job, clean up duplicates and stale circuits.

## Further detail

### Pitfalls

- **Dojo eval false positives**: The analyzer generates generic "add error handling" recommendations. Cross-reference against actual error logs before acting. Most are noise. - **`hermes cron edit`, not `hermes cron update`** — the CLI subcommand is `edit` (`list/create/add/edit/pause/resume/run/remove/status/runs/history/incidents/notepad/doctor/tick`). `update` errors out. - **Agent jobs pinned to slow providers die as `TimeoutError: idle Ns (limit 600s) — waiting for non-streaming API response`** — the model, not the script, is the bottleneck. Fix: `hermes cron edit <id> --model <faster-mod

### Verification

All erroring jobs should now show `last_status: ok`:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/cron-health-sweep/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
