---
type: concept
title: Hermes Mimo Bridge
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Hermes Mimo Bridge

> Dispatch coding tasks from Hermes to Mimo (Mimocode) CLI. Autonomous coding agent with Xiaomi Mimo models. Supports one-shot execution, file attachment, session management, and thinking blocks. Use for code review, refactoring, and surgical code changes.

## Overview

- **When to Use** — - User explicitly says "use mimo", "mimocode" - Task is **code review** (Mimo is most thorough — line numbers, severity levels) - Task is **refactoring** (context-aware, understands project structure) - Task needs a **different model family** (Xiaomi Mimo vs Google Gemini vs Claude) - Kanban/Symphony tasks assigned to `mimo-*` assignees
- **Prerequisites** — - Binary: `~/.mimocode/bin/mimo` (v0.1.0+) - **Auth required**: run `mimo auth login` interactively (one-time) - Verify: `mimo providers whoami` should show logged-in user
- **Mimo CLI Interface** — Mimo supports inline flags without derailing (unlike agy's print-mode quirk):

## Further detail

### ⚠ Pitfalls

1. **Auth hangs silently** — if not authenticated, `mimo run` hangs waiting for login with no output. Always check `mimo providers whoami` first. 2. **`mimo-auto` may fail** — `ProviderModelNotFoundError` on empty modelID. Use explicit model like `xiaomi/mimo-v2.5-pro`. 3. **PATH not sourced in Hermes** — use full path `~/.mimocode/bin/mimo` or the bridge (which handles this automatically). 4. **Detects existing code** — Mimo reads files before responding. If a function already exists, it may produce replacement code. Be explicit about intent.

### Symphony Integration

Mimo is integrated via `AGENT_REGISTRY`:

### Logging

- Bridge log: `~/.hermes/mimo-bridge.log` - Mimo binary: `~/.mimocode/bin/mimo` - Sessions: `mimo session list`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-mimo-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
