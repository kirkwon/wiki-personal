---
date: 2026-07-19
type: concept
title: Git Operations
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- git
- version-control
- operations
- commit
- branch
- software-development
sources:
- hermes://skill/git-operations
description: Perform common Git operations — commit, push, pull, branch, merge, rebase,
  stash, log, diff, and status. Use whenever the user asks about git, commits, branches,
  or repository operations. Covers everyday workflows and error recovery.
---

# Git Operations

> Perform common Git operations — commit, push, pull, branch, merge, rebase, stash, log, diff, and status. Use whenever the user asks about git, commits, branches, or repository operations. Covers everyday workflows and error recovery.

## Overview

- **Quick Reference** — | Task | Command | |------|---------| | Status | `git status` | | Diff | `git diff` (unstaged), `git diff --cached` (staged) | | Log | `git log --oneline -10` | | Commit | `git commit -m "type: message"` | | Push | `git push origin <branch>` | | Pull | `git pull --rebase` | | Branch | `git checkout -b <name>` | | Stash | `git stash push -m "message"`, `git stash pop` |
- **Error Recovery** — | Error | Fix | |-------|-----| | Merge conflict | `git status` → edit conflicted files → `git add` → `git commit` | | Wrong branch committed | `git reset HEAD~1` → stash → switch branch → apply | | Push rejected | `git pull --rebase` first, then push | | Detached HEAD | `git stash` → `git checkout <branch>` → `git stash pop` | | `failed to push some refs` | Remote has new commits — `git pull --rebase` first |
- **Retry Discipline** — - **Do NOT retry `git` commands blindly.** If a git command fails, read the error message, understand why, and fix the root cause before retrying. - **Common causes of git failure**: wrong branch, uncommitted changes, merge conflicts, authentication, network issues. Each has a specific fix. - **If `git push` fails**, check if you need to pull first (`git pull --rebase`), not retry the same push. - **If `git merge` conflicts**, fix the conflicts, don't abort and retry the same merge.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/git-operations/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
