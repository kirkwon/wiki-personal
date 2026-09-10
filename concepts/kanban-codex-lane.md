---
date: 2026-07-19
type: concept
title: Kanban Codex Lane
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- kanban
- codex
- worktrees
- autonomous-agents
- prediction-market-bot
- autonomous-ai-agents
sources:
- hermes://skill/kanban-codex-lane
description: Use when a Hermes Kanban worker wants to run Codex CLI as an isolated
  implementation lane while Hermes keeps ownership of task lifecycle, reconciliation,
  testing, and handoff.
---

# Kanban Codex Lane

> Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, reconciliation, testing, and handoff.

## Overview

- **Overview** — This skill defines the lightweight Hermes+Codex dual-lane convention for Kanban workers. Hermes is always the task owner: it calls `kanban_show`, decides whether Codex is appropriate, creates or selects an isolated workspace, starts and monitors Codex, reconciles any diff, runs verification, and writes the final `kanban_complete` or `kanban_block` handoff. Codex is an input lane only. Codex output is not a task completion signal, not a trusted reviewer, and not allowed to write durable Kanban state directly.
- **When to Use** — Use the Codex lane when all of these are true:
- **Ownership Rules** — 1. Hermes owns the Kanban lifecycle. Codex must never call `kanban_complete`, `kanban_block`, `kanban_create`, gateway messaging, or any Hermes board CLI as a substitute for the worker. 2. Hermes owns final acceptance. Treat Codex commits/diffs as untrusted patches until reviewed and verified. 3. Hermes owns test execution. Codex may run tests, but those runs are advisory; repeat required verification from Hermes with the repo's canonical wrapper. 4. Hermes owns safety. If Codex changes safety boundaries, risk gates, live trading behavior, or secrets handling, reject the lane even if tests pas

## Further detail

### Required Worktree and Branch Pattern

Never run Codex directly in a shared dirty checkout. Use a branch/worktree name that ties the lane to the Kanban task and keeps untrusted edits isolated.

### Codex Capability Checks

Run these before spawning Codex. Missing Codex is a normal reason to skip the lane, not a task blocker if Hermes can do the task directly.

### Mode Selection

Use `codex exec` for bounded one-shot edits where Codex should exit on its own:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/kanban-codex-lane/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
