---
date: 2026-07-19
type: concept
title: Github Pr Workflow
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- GitHub
- Pull-Requests
- CI/CD
- Git
- Automation
- Merge
- github
sources:
- hermes://skill/github-pr-workflow
description: 'GitHub PR lifecycle: branch, commit, open, CI, merge.'
---

# Github Pr Workflow

> GitHub PR lifecycle: branch, commit, open, CI, merge.

## Overview

- **Prerequisites** — - Authenticated with GitHub (see `github-auth` skill) - Inside a git repository with a GitHub remote
- **1. Branch Creation** — This part is pure `git` — identical either way:
- **2. Making Commits** — Use the agent's file tools (`write_file`, `patch`) to make changes, then commit:

## Further detail

### Test Plan

- [ ] Unit tests pass

### 5. Auto-Fixing CI Failures

When CI fails, diagnose and fix. This loop works with either auth method.

### 6. Merging

**With gh:**

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/github/github-pr-workflow/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
