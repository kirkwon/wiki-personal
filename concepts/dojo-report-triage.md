---
date: 2026-08-02
type: concept
title: Dojo Report Triage
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-report-triage
description: 'Triage a daily Dojo eval report: dedup queue, reset stale breakers,
  reclassify noise.'
---

# Dojo Report Triage

> Triage a daily Dojo eval report: dedup queue, reset stale breakers, reclassify noise.

## Overview

- **When to Use** — - A daily/weekly Dojo eval report arrives via cron and you need to process it. - The fix queue has grown large with many `pending` entries. - Circuit breakers show `half-open` with 0% success rates. - The report recommends `add_retry_handling` for many skills (usually noise). - You want to verify all circuits are green before closing a session.
- **Prerequisites** — - Dojo eval has run recently (`~/.hermes/dojo-eval/` exists with fresh data). - `read_file` access to state files under `~/.hermes/dojo-eval/`. - `terminal` tool for probing whether flagged tools actually work. - `execute_code` for batch JSON edits to state files.
- **Pitfalls** — - **Never reset a breaker before probing the tool.** If the tool is genuinely broken, it re-trips immediately and pollutes the audit trail. - **Don't action items one-by-one.** Group by root cause — most reports are 1-3 shared root causes manifesting as N symptoms. - **The fix-router never deduplicates.** Left unchecked, 10 unique fixes become 35+ entries across 4 daily runs, all `pending`, never drained. - **`unknown:retry_loop` (100+ count) is almost always model-level.** When the retry count is very high and spans different skills, it's the model retrying bad tool calls — not skill code loo

## Further detail

### Verification

After triage, all three checks must pass:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-report-triage/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
