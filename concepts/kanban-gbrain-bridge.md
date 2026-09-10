---
date: 2026-07-19
type: concept
title: Kanban Gbrain Bridge
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/kanban-gbrain-bridge
description: Documents how Kanban multi-agent workflows interact with GBrain knowledge
  base.
---

# Kanban Gbrain Bridge

> Documents how Kanban multi-agent workflows interact with GBrain knowledge base.

## Overview

- **Overview** — Kanban multi-agent workflows generate outputs that should persist in GBrain for future reference. This skill documents the patterns for bidirectional integration.
- **Save Task Outputs to GBrain** — After completing work, save detailed findings to GBrain for future reference:
- **Retrieve Context from GBrain Before Work** — Query GBrain for relevant context before starting:

## Further detail

### Link to Project Pages

Kanban tasks should link to GBrain project pages:

### Agent Memory via GBrain

From the `gbrain` skill, Hermes stores agent preferences in `agents/hermes/`: - `agents/hermes/preferences` — Language, clarify style, learning goals - `agents/hermes/learning-goals` — LLM workflows, guardrails - `agents/hermes/memory-strategy` — Hybrid approach documentation

### Pitfalls (from gbrain-content-ops skill)

- **Never use** `gbrain put --content /dev/stdin < file` (stores literal "/dev/stdin" as body) - **Use `gbrain import`** from filesystem (Method 1 from gbrain-content-ops) - **Verify actual slug** after import (prefix stripping: `concepts/foo.md` → slug `foo`) - **Query with `gbrain search`** before `gbrain get` (list truncates at 50 lines) - **If update needed**: Delete + reimport (gbrain put may skip updates)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/kanban-gbrain-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
