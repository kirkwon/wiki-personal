---
date: 2026-07-19
type: concept
title: Dispatch
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/dispatch
description: Route tasks to the best-suited coding assistant. Supports explicit targeting
  by assistant name, auto-routing by tags/keywords, and parallel fan-out.
---

# Dispatch

> Route tasks to the best-suited coding assistant. Supports explicit targeting by assistant name, auto-routing by tags/keywords, and parallel fan-out.

## Overview

- **Agent Registry** — | Assistant | Binary | Specialty | Tags | |-----------|--------|-----------|------| | **claude** | `~/.local/bin/claude --print` | Complex refactors, architecture, multi-file changes, API work | `backend`, `refactor`, `architecture`, `api` | | **opencode** | `/opt/homebrew/bin/opencode run` | PR review, general coding, frontend | `review`, `frontend`, `general` | | **goose** | `~/.local/bin/goose run -t` | MCP-heavy automation, research, data | `research`, `data`, `automation`, `mcp` | | **antigravity** / **agy** | `~/.local/bin/agy --print --print-timeout 300s` | Gemini models, prototyping, s
- **Dispatch Mechanisms** — Three approaches for dispatching work, each with different trade-offs:
- **Response Format** — All results are returned as a brief with: - Assistant used - Exit code and duration - Key output (first 2000 chars) - Error summary (if any)

## Further detail

### Anti-Patterns

- **Don't dispatch trivial work** — `ls`, `cd`, reading files. Do that yourself. - **Don't dispatch to a tool that isn't installed** — check the agent registry first. - **Don't parallelize dependent work** — use sequential dispatch for task chains. - **Don't dispatch without context** — include the file paths, error messages, and constraints the assistant needs. - **Timeout awareness** — CLI assistants can take 2-5 minutes. Use background dispatch for long tasks.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/dispatch/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
