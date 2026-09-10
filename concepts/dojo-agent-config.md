---
date: 2026-07-19
type: concept
title: Dojo Agent Config
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-agent-config
description: Configure Hermes agent delegation and approvals to prevent Dojo circuit
  breaker trips.
---

# Dojo Agent Config

> Configure Hermes agent delegation and approvals to prevent Dojo circuit breaker trips.

## Overview

- **When to Use** — Use this skill when the Hermes Dojo evaluation repeatedly shows open circuit breakers for core tools such as `execute_code`, `tool_call`, `skill_manage`, `browser_navigate`, `web_search`, or `vision_analyze`, and preliminary triage (via `dojo-circuit-breaker-triage`) indicates the failures stem from agent/delegation misconfiguration rather than intrinsic tool bugs.
- **Goal** — Ensure that Hermes agents (especially subagents spawned by the Dojo cron job) have the correct roles, allowed toolsets, and delegation depth so they can execute the tools needed for self‑healing without hitting policy blocks. This prevents circuit breakers from tripping in the first place.
- **Prerequisites** — - Access to `~/.hermes/config.yaml` (read/write). - Ability to run `hermes config get` /config get` / `hermes config set`. - Familiarity with the delegation configuration section. - The `dojo-circuit-breaker-triage` skill for verifying breaker state after changes.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-agent-config/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
