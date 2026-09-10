---
date: 2026-08-02
type: concept
title: Claude Code
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- Coding-Agent
- Claude
- Anthropic
- Code-Review
- Refactoring
- PTY
- Automation
- software-development
sources:
- hermes://skill/claude-code
description: Delegate coding to Claude Code CLI (features, PRs).
---

# Claude Code

> Delegate coding to Claude Code CLI (features, PRs).

## Overview

- **Symphony Bridge** — The `hermes-claude` bridge script (`~/.local/bin/hermes-claude`) provides a Symphony-compatible wrapper for automated dispatch:
- **Prerequisites** — - **Install:** `npm install -g @anthropic-ai/claude-code` - **Auth:** run `claude` once to log in (browser OAuth for Pro/Max, or set `ANTHROPIC_API_KEY`) - **Console auth:** `claude auth login --console` for API key billing - **SSO auth:** `claude auth login --sso` for Enterprise - **Check status:** `claude auth status` (JSON) or `claude auth status --text` (human-readable) - **Health check:** `claude doctor` — checks auto-updater and installation health - **Version check:** `claude --version` (requires v2.x+) - **Update:** `claude update` or `claude upgrade`
- **Two Orchestration Modes** — Hermes interacts with Claude Code in two fundamentally different ways. Choose based on the task.

## Further detail

### PTY Dialog Handling (CRITICAL for Interactive Mode)

Claude Code presents up to two confirmation dialogs on first launch. You MUST handle these via tmux send-keys:

### CLI Subcommands

| Subcommand | Purpose | |------------|---------| | `claude` | Start interactive REPL | | `claude "query"` | Start REPL with initial prompt | | `claude -p "query"` | Print mode (non-interactive, exits when done) | | `cat file \| claude -p "query"` | Pipe content as stdin context | | `claude -c` | Continue the most recent conversation in this directory | | `claude -r "id"` | Resume a specific session by ID or name | | `claude auth login` | Sign in (add `--console` for API billing, `--sso` for Enterprise) | | `claude auth status` | Check login status (returns JSON; `--text` for human-readable) |

### Parallel Claude Instances

Run multiple independent Claude tasks simultaneously:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/claude-code/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
