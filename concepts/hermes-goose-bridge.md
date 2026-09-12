------

# Hermes Goose Bridge

> Dispatch coding tasks from Hermes to Goose CLI (Block / Linux Foundation). Open-source, model-agnostic agent with MCP extensions, headless mode, recipe system. Use for general-purpose automation, research, and coding tasks requiring provider diversity.

## Overview

- **When to Use** — - Task needs **model diversity** (Goose can run Claude, Gemini, Ollama, etc.) - Task benefits from **MCP extensions** (70+ tools: web search, databases, etc.) - Task is **general-purpose** (not just code — research, writing, automation) - User explicitly says "use goose" - Kanban/Symphony tasks assigned to `goose-*` assignees
- **Prerequisites** — - Binary: `~/.local/bin/goose` (v1.12.1+) - Provider configured in `~/.config/goose/config.yaml` - For autonomous runs: `GOOSE_MODE=auto` (set automatically by the bridge)
- **Goose Headless Mode** — Goose's `run` command with `--no-session` is the headless execution path:

## Further detail

### Provider Configuration

Goose supports multiple LLM providers. Current setup (`~/.config/goose/config.yaml`):

### Symphony Integration

Goose is integrated into the Symphony multi-agent dispatcher via the `AGENT_REGISTRY` in `symphony_runner.py`:

### Goose vs Other Agents

| Feature | Goose | Antigravity (agy) | Mimo | |---------|-------|-------------------|------| | License | Apache 2.0 (open) | Closed | Proprietary | | Language | Rust | Go | — | | Models | Any (BYOK) | Gemini family | Xiaomi Mimo | | MCP | 70+ extensions | Plugins | ACP | | Headless | `goose run --no-session` | `agy -p` (bare only) | `mimo run` | | Best for | General-purpose, MCP-heavy | Coding (Gemini) | Code review, refactoring |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-goose-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
