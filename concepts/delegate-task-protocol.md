---
date: 2026-07-19
type: concept
title: Delegate Task Protocol
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- delegation
- subagents
- parallel
- multi-agent
- orchestration
- software-development
sources:
- hermes://skill/delegate-task-protocol
description: Structured fan-out pattern for synchronous subagent delegation — when
  to parallelize, how to split prompts, and anti-patterns to avoid. Covers both delegate_task
  (in-session) and cron-based fan-out patterns.
---

# Delegate Task Protocol

> Structured fan-out pattern for synchronous subagent delegation — when to parallelize, how to split prompts, and anti-patterns to avoid. Covers both delegate_task (in-session) and cron-based fan-out patterns.

## Overview

- **When to Fan Out (vs. Sequential)** — | Fan Out ✅ | Keep Sequential ❌ | |------------|-------------------| | Subtasks are independent — no output dependency | Task B needs output from Task A | | Subtasks use different toolsets (terminal vs. web) | Subtasks share mutable state | | Subtasks would serialize a long chain of calls | A subtask may need clarification from user | | Research + synthesis (research in parallel → synthesize) | Any task requiring `clarify` tool |
- **Structural Template** — **context field rules:** - Pass file paths, URLs, IDs — NOT a text dump of everything - Include the goal statement and any hard constraints (e.g., "do not modify X", "output format: YAML") - If context is identical for all subagents, write it once and reference it
- **Model Override: NOT Supported Per-Call (Critical Constraint)** — `delegate_task` does **not** accept a `model` parameter. All children use the **same model**, resolved at spawn time via `_resolve_delegation_credentials(cfg, parent_agent)` (source: `tools/delegate_tool.py:2459-2467`):

## Further detail

### Capacity Limits (Enforced by Config)

- `max_concurrent_children: 3` — never exceed 3 parallel subagents - `max_spawn_depth: 1` — no nested fan-out (children are leaves) - For nested orchestration: use `cronjob` with `workdir` instead

### Pitfalls & Environment-Specific Workarounds

- **Python Version Mismatch**: Modern GUI and browser automation tools (`playwright`, `pyobjc`) often require Python 3.9+. If the local environment is locked to 3.8.5 (e.g., legacy Anaconda), these tools will fail to import or install. - **The "Container-First" Rule**: Never attempt to force system-level `pip` installs of GUI automation toolchains into a locked or legacy environment. It often corrupts host shared objects (e.g., `libexpat`) and leads to dynamic linking errors (`ImportError`). - **Orchestration Pattern**: When the host environment is too rigid for GUI tools, do not push. Use the

### Cron-Based Fan-Out (Background Parallelism)

For long-running tasks that outlive a session:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/delegate-task-protocol/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
