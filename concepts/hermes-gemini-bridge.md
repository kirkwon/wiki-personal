------

# Hermes Gemini Bridge

> Dispatch coding tasks from Hermes to Gemini CLI via the hermes-gemini bridge wrapper. Use when delegating coding/build tasks to Gemini.

## Overview

- **When to Use** — - User wants to build/create an app or tool - Task is primarily coding (not research, not file organization) - You want Gemini to scaffold, then Hermes to refine
- **Workflow** — 1. **Hermes receives coding task** 2. **Hermes calls bridge:** `hermes-gemini -p <project> "<task>"` 3. **Gemini scaffolds** the code (Superpowers auto-triggers: brainstorm → plan → TDD → verify) 4. **Hermes reviews output** — check for: hardcoded paths, wrong output format assumptions, missing error handling 5. **Hermes refines** — fix integration issues, test against real data 6. **Hermes commits** — `hermes-code-sync` to push to GitHub
- **How It Works** — The bridge: 1. Takes a task description and project directory 2. Adds context (project path, gbrain output format notes, error handling reminder) 3. Calls `gemini -m <model> --include-directories=<output> -y --skip-trust -p "<enriched prompt>"` 4. Gemini creates files directly in the target directory 5. As a fallback, moves any new files from `~/clawd/` to the target directory

## Further detail

### Key Flags

| Flag | Description | |------|-------------| | `-p PATH` | Project/output directory | | `-m MODEL` | Model: gemini-2.5-pro (default), gemini-2.5-flash | | `-y` | YOLO mode (default: true) | | `--no-yolo` | Disable YOLO (interactive approval) | | `-s` | Sandbox mode | | `-o DIR` | Override output directory | | `-v` | Verbose output | | `--no-skips` | Don't skip workspace trust check |

### Output Location

Files are created in the `-p` directory (or current dir if not specified). The bridge uses `--include-directories=` to grant Gemini workspace access.

### Logging

All invocations logged to: `~/.hermes/gemini-bridge.log`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-gemini-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
