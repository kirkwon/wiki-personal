---
date: 2026-07-19
type: concept
title: Hermes Antigravity Bridge
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- antigravity
- agy
- bridge
- delegation
- coding
- autonomous-ai-agents
sources:
- hermes://skill/hermes-antigravity-bridge
description: Dispatch coding tasks from Hermes to Google Antigravity CLI (agy) via
  the hermes-antigravity bridge wrapper. Use when delegating coding/build tasks to
  Antigravity. Migrated from hermes-gemini-bridge on 2026-06-19.
---

# Hermes Antigravity Bridge

> Dispatch coding tasks from Hermes to Google Antigravity CLI (agy) via the hermes-antigravity bridge wrapper. Use when delegating coding/build tasks to Antigravity. Migrated from hermes-gemini-bridge on 2026-06-19.

## Overview

- **When to Use** — - User wants to build/create an app or tool via Antigravity - Task is primarily coding (not research, not file organization) - You want agy to scaffold, then Hermes to refine - Kanban/Symphony tasks assigned to `gemini-*` assignees (now routed to agy)
- **Prerequisites (one-time setup)** — 1. **Install agy**: `curl -fsSL https://antigravity.google/cli/install.sh | bash` (installs to `~/.local/bin/agy`; SHA512-verified by the installer itself) 2. **Authenticate**: run `agy` interactively → browser OAuth → sign in. Token persists in macOS keychain ("Antigravity Safe Storage"). gcloud ADC is NOT used. 3. **Autonomous execution**: set `toolPermission: "always-proceed"` in `~/.gemini/antigravity-cli/settings.json` (required for unattended writes).
- **Legacy Gemini Bridge Interface (superseded)** — This skill replaced `hermes-gemini-bridge` (migrated 2026-06-19). The old `hermes-gemini` wrapper binary still exists at `~/.local/bin/hermes-gemini`; its interface for reference:

## Further detail

### ⚠️ CRITICAL PITFALL: agy print-mode flag contamination

**Verified 2026-06-19 on agy v1.0.10.** This is the single most important thing to know about this bridge.

### agy vs Gemini CLI flag map

| hermes-gemini (Gemini CLI) | hermes-antigravity (agy) | Notes | |---|---|---| | `-p "prompt"` | `agy -p "prompt"` | BARE — no other inline flags | | `-m gemini-2.5-pro` | (settings.json `model`) | Cannot pass via flag in print mode | | `-y` (YOLO) | `toolPermission: always-proceed` | Setting, not flag | | `-s` (sandbox) | `enableTerminalSandbox` setting | | | `--include-directories=<path>` | cwd / `--add-dir` (slash cmd only) | Bridge uses cwd | | `--skip-trust` | n/a | Trust via `trustedWorkspaces` setting |

### Available agy models (display names)

List with `agy models`. Set default via settings.json `"model"` key.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-antigravity-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
