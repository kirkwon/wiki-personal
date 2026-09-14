---
type: concept
title: Debugging Hermes Tui Commands
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Debugging Hermes Tui Commands

> Debug Hermes TUI slash commands: Python, gateway, Ink UI.

## Overview

- **Overview** — Hermes slash commands span three layers — Python command registry, tui_gateway JSON-RPC bridge, and the Ink/TypeScript frontend. When a command misbehaves (missing from autocomplete, works in CLI but not TUI, config persists but UI doesn't update), the bug is almost always one layer being out of sync with another.
- **When to Use** — - A slash command exists in one part of the codebase but doesn't work fully - A command needs to be added to both backend and frontend - Command autocomplete isn't working for specific commands - Command behavior is inconsistent between CLI and TUI - A command persists config but doesn't apply live in the TUI
- **Architecture Overview** — Command definitions must be registered consistently across Python and TypeScript to work properly. The Python `COMMAND_REGISTRY` is the source of truth for: CLI dispatch, gateway help, Telegram BotCommand menu, Slack subcommand map, and autocomplete data shipped to Ink.

## Further detail

### Investigation Steps

1. **Check if the command exists in the TUI frontend:**

### Fix: Missing Command Autocomplete

If a command exists in the TUI but doesn't show in autocomplete:

### Common Issues

1. **Command shows in TUI but not in autocomplete.** The command is defined in the TUI codebase but missing from `COMMAND_REGISTRY` in `hermes_cli/commands.py`. Autocomplete data ships from Python.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/debugging-hermes-tui-commands/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
