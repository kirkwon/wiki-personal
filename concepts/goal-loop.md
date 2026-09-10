---
date: 2026-07-19
type: concept
title: Goal Loop
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/goal-loop
description: Goal-based cron loop — runs until a condition is met, then auto-pauses.
---

# Goal Loop

> Goal-based cron loop — runs until a condition is met, then auto-pauses.

## Overview

- **The 4-Condition Test — before you build** — > Miss one condition and the loop costs more than it returns. —@0xCodez
- **When to use a goal loop (vs plain cron)** — Use a goal loop when a task: - Happens **repeatedly** (every N minutes/hours) - Has a **measurable end condition** (file count, API response, test passes) - Should **stop itself** once the condition is met (no manual cleanup)
- **How it works** — Two files at `~/.hermes/scripts/`:

## Further detail

### Check commands (examples)

| Goal | Check command | |------|--------------| | File count reaches N | `test $(ls ~/processed/*.md 2>/dev/null \| wc -l) -ge 100` | | API returns done | `curl -sf http://api/status \| grep -q '"done": true'` | | Database has results | `sqlite3 db.sqlite "SELECT COUNT(*) FROM results" \| grep -q "^5"` | | Stale pages cleared | `python3 -c "from wiki_api import WikiVault; v=WikiVault(); print(sum(1 for _ in v.pages_by_tag('stale')))" \| grep -q "^0"` | | File exists | `test -f /tmp/completion-marker.txt` |

### Pitfalls

- **The check command runs AFTER the task** — if the task itself could cause the goal, this is correct. If the goal is external, the check runs on every tick regardless of task success. - **`--job-id` must match the actual cron job** — create it first, then hardcode. Don't pass a placeholder. - **Paused jobs stay paused** — they don't resume automatically. The user explicitly resumes with `cronjob action='resume' job_id='...'` or the Hermes UI. - **`set -e` in goal-loop.sh** — if the task script has `set -e` internally, that's fine. The wrapper captures the task exit code and proceeds to the c

### Verification

After setting up a goal loop:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/goal-loop/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
