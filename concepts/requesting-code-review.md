---
date: 2026-07-19
type: concept
title: Requesting Code Review
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- code-review
- security
- verification
- quality
- pre-commit
- auto-fix
- software-development
sources:
- hermes://skill/requesting-code-review
description: 'Pre-commit review: security scan, quality gates, auto-fix.'
---

# Requesting Code Review

> Pre-commit review: security scan, quality gates, auto-fix.

## Overview

- **When to Use** — - After implementing a feature or bug fix, before `git commit` or `git push` - When user says "commit", "push", "ship", "done", "verify", or "review before merge" - After completing a task with 2+ file edits in a git repo - After each task in subagent-driven-development (the two-stage review)
- **Step 1 — Get the diff** — If empty, try `git diff` then `git diff HEAD~1 HEAD`.
- **Step 2 — Static security scan** — Scan added lines only. Any match is a security concern fed into Step 5.

## Further detail

### Step 3 — Baseline tests and linting

Detect the project language and run the appropriate tools. Capture the failure count BEFORE your changes as **baseline_failures** (stash changes, run, pop). Only NEW failures introduced by your changes block the commit.

### Step 4 — Self-review checklist

Quick scan before dispatching the reviewer:

### Step 5 — Independent reviewer subagent

Call `delegate_task` directly — it is NOT available inside execute_code or scripts.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/requesting-code-review/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
