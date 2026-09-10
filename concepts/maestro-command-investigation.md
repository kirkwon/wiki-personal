---
date: 2026-07-19
type: concept
title: Maestro Command Investigation
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- maestro
- cli
- investigation
- delegation
- maestro-integration
- autonomous-ai-agents
sources:
- hermes://skill/maestro-command-investigation
description: Process for investigating missing CLI commands in Maestro CLI and handling
  delegation results from Maestro integration
---

# Maestro Command Investigation

> Process for investigating missing CLI commands in Maestro CLI and handling delegation results from Maestro integration

## Overview

- **Overview** — This skill documents the process for investigating when a referenced CLI command (like Maestro's `/fortify`) doesn't exist in the available CLI, and how to handle delegation results from Maestro integration workflows.
- **When to Use This Skill** — - When a referenced CLI command doesn't exist in the available command list - When processing delegation results from Maestro integration (like deleg_0ac926b1 for Maestro /fortify) - When needing to verify if a CLI feature exists or needs to be implemented - When working with Maestro CLI and needing to understand available commands
- **Handling Missing Commands in Delegation Workflows** — When a delegated command like `/fortify` doesn't exist:

## Further detail

### Example: Processing deleg_0ac926b1 (Maestro /fortify)

From ACTIVITY.md:

### Verification Steps

After investigation, always verify: 1. ✅ CLI location confirmed 2. ✅ Available commands enumerated 3. ✅ Code searched for command references 4. ✅ Build status checked (if applicable) 5. ✅ Delegation status documented in ACTIVITY.md 6. ✅ Next steps determined and recorded

### Related Skills

- `hermes-agent` - For general Hermes CLI usage and configuration - `hermes-mimo-bridge` - For MCP-based delegation to other CLI tools - `autonomous-ai-agents/claude-code` - For delegating to Claude Code CLI - `autonomous-ai-agents/codex` - For delegating to OpenAI Codex CLI

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/maestro-command-investigation/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
