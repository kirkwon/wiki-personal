---
date: 2026-07-19
type: concept
title: Codex
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Coding-Agent
- Codex
- OpenAI
- Code-Review
- Refactoring
- autonomous-ai-agents
sources:
- hermes://skill/codex
description: Delegate coding to OpenAI Codex CLI (features, PRs).
---

# Codex

> Delegate coding to OpenAI Codex CLI (features, PRs).

## Overview

- **When to use** — - Building features - Refactoring - PR reviews - Batch issue fixing
- **Prerequisites** — - Codex installed: `npm install -g @openai/codex` - OpenAI auth configured: either `OPENAI_API_KEY` or Codex OAuth credentials from the Codex CLI login flow - **Must run inside a git repository** — Codex refuses to run outside one - Use `pty=true` in terminal calls — Codex is an interactive terminal app
- **One-Shot Tasks** — For scratch work (Codex needs a git repo):

## Further detail

### Key Flags

| Flag | Effect | |------|--------| | `exec "prompt"` | One-shot execution, exits when done | | `--sandbox workspace-write` (`-s`) | Sandboxed but auto-approves file changes in the workspace (the recommended auto-build mode) | | `--dangerously-bypass-approvals-and-sandbox` | No sandbox, no approvals (fastest, most dangerous; `--yolo` still works as a hidden alias) | | `--sandbox danger-full-access` | No Codex sandbox; useful when the host service context breaks bubblewrap |

### Hermes Gateway Caveat

When invoking the Codex CLI from a Hermes gateway/service context (for example, Telegram-driven agent sessions), Codex `workspace-write` sandboxing may fail even when the same command works in the user's interactive shell. A typical symptom is bubblewrap/user-namespace errors such as `setting up uid map: Permission denied` or `loopback: Failed RTM_NEWADDR: Operation not permitted`.

### PR Reviews

Clone to a temp directory for safe review:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/codex/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
