---
date: 2026-07-19
type: concept
title: Hermes Subagent Terminal Diagnostic
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/hermes-subagent-terminal-diagnostic
description: Fix subagents that echo commands without executing them.
---

# Hermes Subagent Terminal Diagnostic

> Fix subagents that echo commands without executing them.

## Overview

- **When to Use** — - `delegate_task` subagents return planning text ("I'll run these commands...") instead of command output - Subagents echo the command string back verbatim without showing stdout/stderr - Multiple subagents dispatched with `toolsets: ["terminal"]` all fail identically - Terminal works in the main session but not in delegated subagents - After switching profiles or models, subagent execution breaks
- **Prerequisites** — - Hermes profile configs at `~/.hermes/profiles/<name>/config.yaml` - Main config at `~/.hermes/config.yaml` - `read_file` and `search_files` tools for config inspection - `delegate_task` tool for verification testing
- **How to Run** — 1. Check the active profile config for two conditions (both must be satisfied). 2. Fix the config via `patch`. 3. Run a minimal echo-test subagent to confirm execution. 4. `/reset` the session for changes to take effect.

## Further detail

### Quick Reference

- Two config keys gate terminal: `toolsets` (must include `terminal`) and `agent.disabled_toolsets` (must NOT include `terminal`) - Profile config path: `~/.hermes/profiles/<profile>/config.yaml` - Subagents inherit parent toolset — no separate subagent toolset config - Minimal test: dispatch a subagent with `echo "OK_$(date +%s)"` and check for literal stdout - Config changes require `/reset` — toolsets load at session start

### Procedure

1. **Identify the active profile.** Check the session's system prompt or `hermes status` for the running profile name (e.g., `web_content_retriever`, `default`).

### Pitfalls

- **Two conditions, not one:** Removing `terminal` from `disabled_toolsets` is insufficient if `terminal` is also missing from the `toolsets` list. Both must be correct. The `toolsets` list is the allowlist; `disabled_toolsets` is a denylist on top. - **Inheritance is silent:** Subagents do not report "terminal tool unavailable" — they attempt to help without it, producing command text that looks like output. The failure mode mimics a model intelligence problem but is actually a tooling problem. - **Model vs toolset misdiagnosis:** When subagents echo commands, the instinct is to blame the mod

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/hermes-subagent-terminal-diagnostic/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
