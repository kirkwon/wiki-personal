---
date: 2026-07-19
type: concept
title: Bash Set E Arithmetic Trap
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/bash-set-e-arithmetic-trap
description: 'Diagnostic pattern for the deadly bash combination of `set -e` (or `set
  -euo pipefail`) with `((VAR++))` arithmetic increment. When the increment result
  is 0 (i.e., the FIRST increment from 0→1 returns exit code 1), `set -e` kills the
  script. This is the #1 cause of silent cron script failures.'
---

# Bash Set E Arithmetic Trap

> Diagnostic pattern for the deadly bash combination of `set -e` (or `set -euo pipefail`) with `((VAR++))` arithmetic increment. When the increment result is 0 (i.e., the FIRST increment from 0→1 returns exit code 1), `set -e` kills the script. This is the #1 cause of silent cron script failures.

## Overview

- **Root Cause** — Bash's `((expr))` arithmetic evaluation returns exit code 1 when the expression evaluates to **0**, and exit code 0 when it evaluates to **non-zero**. This is the opposite of what most programmers expect.
- **When `set -e` IS appropriate** — - Pure data processing scripts where every command MUST succeed - Scripts with no loops or counters - Build scripts where you want fail-fast behavior
- **When `set -e` is NOT appropriate** — - Scripts calling external APIs (nlm, gbrain, curl) — these fail non-fatally - Scripts with counters/accumulators - Cron jobs that need to complete even if one step fails - Scripts with `((var++))` or `((var += n))`

## Further detail

### Remediation Checklist

1. Find scripts with both `set -euo pipefail` and `((VAR++))` 2. Change `set -euo pipefail` → `set -uo pipefail` (drop the `-e`) 3. Change all `((VAR++))` → `VAR=$((VAR + 1))` 4. Add explicit `|| true` to nlm/gbrain/curl commands that may fail non-fatally 5. Initialize all counters before the loop: `OK=0; FAIL=0; SKIP=0` 6. Test with `--dry-run` if the script supports it 7. Run the actual cron job to verify `last_status: "ok"`

### Real-World Impact

This bug caused 4 NotebookLM sync cron jobs to fail silently for weeks: - `update-decision-science-notebook.sh` — died on first concept - `update-financial-strategy-notebook.sh` — died on first concept (unbound var + no init) - `update-cooking-science-notebook.sh` — died on syntax error (orphaned if block) - `update-jazz-theory-notebook.sh` — died on misplaced auth block

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/bash-set-e-arithmetic-trap/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
