---
date: 2026-07-19
type: concept
title: Kanban Orchestrator
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- kanban
- multi-agent
- orchestration
- routing
- devops
sources:
- hermes://skill/kanban-orchestrator
description: Decomposition playbook + anti-temptation rules for an orchestrator profile
  routing work through Kanban. The "don't do the work yourself" rule and the basic
  lifecycle are auto-injected into every kanban worker's system prompt; this skill
  is the deeper playbook when you're specifically playing the orchestrator role.
---

# Kanban Orchestrator

> Decomposition playbook + anti-temptation rules for an orchestrator profile routing work through Kanban. The "don't do the work yourself" rule and the basic lifecycle are auto-injected into every kanban worker's system prompt; this skill is the deeper playbook when you're specifically playing the orchestrator role.

## Overview

- **Profiles are user-configured — not a fixed roster** — Hermes setups vary widely. Some users run a single profile that does everything; some run a small fleet (`docker-worker`, `cron-worker`); some run a curated specialist team they've named themselves. There is **no default specialist roster** — the orchestrator skill does not know what profiles exist on this machine.
- **Pre-Dispatch Checklist** — Run this **before** creating any kanban tasks. Each item here was paid for in failed runs.
- **When to use the board (vs. just doing the work)** — Create Kanban tasks when any of these are true:

## Further detail

### The anti-temptation rules

Your job description says "route, don't execute." The rules that enforce that:

### Common patterns

**Fan-out + fan-in (research → synthesize):** N research-style cards with no parents, one synthesis card with all of them as parents.

### Pitfalls Corrected

- **Corruption Risk:** If a kanban tool times out or blocks, do not force-repair the file via shell commands. Archive the corrupted database (`.corrupt`) and run `hermes kanban init` to reset. The audit trail persists in `task_events`, so state can often be reconstructed. - **Decomposition Latency:** If `hermes kanban decompose` timed out, it is often due to context bloat. Ensure task bodies are concise. If it persists, use manual `hermes kanban create` calls to define the task graph. - **Profile Descriptions:** The deconsumer LLM routes based on profile descriptions, not names. Always define

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/kanban-orchestrator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
