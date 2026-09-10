---
date: 2026-07-19
type: concept
title: Using Git Worktrees
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- git
- worktree
- isolation
- parallel
- kanban
- software-development
sources:
- hermes://skill/using-git-worktrees
description: Set up isolated workspaces via git worktrees for parallel agent sessions.
  Use before executing implementation plans, starting feature work that needs isolation,
  or running parallel Kanban tasks on separate branches.
---

# Using Git Worktrees

> Set up isolated workspaces via git worktrees for parallel agent sessions. Use before executing implementation plans, starting feature work that needs isolation, or running parallel Kanban tasks on separate branches.

## Overview

- **When to Use** — - Starting feature work that should be isolated from the current branch - Before executing implementation plans from `writing-plans` or `plan` - Running parallel Kanban tasks on the same repo simultaneously - Before delegating work to subagents that might conflict - Any multi-agent workflow where sessions need isolated branches
- **Core Principle** — Detect existing isolation first. Then create a worktree only if needed. Never fight the harness — if the environment already provides isolation, use it.
- **Step 0: Detect Existing Isolation** — **Before creating anything, check if you're already isolated:**

## Further detail

### Step 2: Project Setup

Auto-detect and install dependencies in the new worktree:

### Step 3: Verify Clean Baseline

**If tests fail:** Report failures, ask whether to proceed or investigate pre-existing issues.

### Parallel Agent Pattern (Hermes-specific)

The primary value for Hermes: **run multiple delegated agents simultaneously without branch conflicts.**

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/using-git-worktrees/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
