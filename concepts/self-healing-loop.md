---
date: 2026-07-19
type: concept
title: Self Healing Loop
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/self-healing-loop
description: Implements a Loop Engineering (meta-loop) architecture for Hermes skills
  to detect failures, perform root cause analysis, apply fixes, and document learnings
  in GBrain.
---

# Self Healing Loop

> Implements a Loop Engineering (meta-loop) architecture for Hermes skills to detect failures, perform root cause analysis, apply fixes, and document learnings in GBrain.

## Overview

- **Prerequisites** — - Hermes agent with access to `terminal`, `file`, `memory`, `delegate_task`, `gbrain` (if available). - Basic scripting ability (Python or shell).
- **⚠️ Critical: Run Outer-Loop Scripts as `no_agent: true`** — Outer-loop analysis scripts are **pure Python** — they read JSON logs, detect patterns, and apply hardcoded fixes. They contain **zero LLM calls** of their own. Running them as agent-driven cron jobs (`no_agent: false`) wastes **200K+ tokens/day** (one agent session per 15-min tick × 96 ticks/day × 2 jobs = ~192 agent sessions/day, each spinning up a model to read a 4-word prompt and call `terminal` once).
- **Example Implementation** — See `references/outer-loop-template.py` for a clean, working template implementing the full detect → investigate → fix → validate → document cycle with all pitfalls addressed.

## Further detail

### Register as a Cron Job

**Replace the script path with your actual outer loop script.** Scripts must be in `~/.hermes/scripts/`.

### Verification

After deploying, you can test by inducing a failure in the target skill and verifying that: - The inner loop logs the failure. - The outer loop detects the pattern. - A fix is applied and validated. - A note is added to `~/.hermes/logs/self-healing-notes.md`. - For wrapper/script fixes, verify the script returns appropriate exit codes (0 or 1 for success/threshold breach, other codes for failures). - **The job runs silently (zero stdout) when no stagnation is detected** — check the cron output file to confirm no "No stagnation detected" spam.

### Notes

- This skill is a template; you will need to adapt the paths, error detection logic, and fix actions to your specific skill. - The outer loop script can be written in any language; the example is in Python for simplicity. - Ensure the `hermes` CLI is available in the environment where the script runs. - If GBrain is not available, you can still store notes locally and periodically sync. - **`no_agent: true` is mandatory for outer-loop scripts** — they are pure Python, and running them as agent sessions wastes ~200K tokens/day per job. See the "Critical" section above.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/self-healing-loop/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
