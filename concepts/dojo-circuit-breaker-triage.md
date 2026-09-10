---
date: 2026-07-19
type: concept
title: Dojo Circuit Breaker Triage
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-circuit-breaker-triage
description: Triage dojo eval reports and reset stale circuit breakers.
---

# Dojo Circuit Breaker Triage

> Triage dojo eval reports and reset stale circuit breakers.

## Overview

- **When to Use** — - A daily Dojo eval report lands and you need to triage it. - Circuit breakers are stuck open/half-open after a fix was applied. - The Dojo report flags tools as "create skill" or "investigate retry loops" and you need to check if those are real or hallucinated. - You want to verify all circuits are green after a repair session. - A tool is failing by design (safety guard) and the breaker should be whitelisted/closed, not investigated.
- **Prerequisites** — - `read_file` access to `~/.hermes/dojo-eval/circuit-breakers.json`. - `terminal` tool for probing whether tools are actually broken. - `search_files` for checking error logs in `~/.hermes/logs/errors.log`.
- **How to Run** — 1. Read the Dojo report (delivered via cron or pasted by user). 2. Read the current breaker state file (see Quick Reference). 3. For each flagged tool, classify: real bug, deprecated, by-design, transient, or false positive. 4. For each classification, apply the matching action (see Procedure). 5. Verify all remaining circuits are `closed` via the state dump.

## Further detail

### Pitfalls

- **Don't reset a breaker before fixing the tool.** If you reset a real bug to closed, it immediately re-trips on the next call, and now the `notes` trail is polluted. Fix root cause first. - **Dojo "create skill" recommendations are often stale.** Always check `search_files` for an existing skill before creating one. The Dojo flagged `git-operations` as missing, but it existed at `skills/software-development/git-operations/`. After 2026-07-06 tuning, the analyzer now walks category subdirectories and skips existing skills, so this false positive is reduced but not eliminated for nested struct

### Verification

After triage, this command should show all `closed`:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-circuit-breaker-triage/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
