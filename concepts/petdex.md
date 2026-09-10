---
date: 2026-07-19
type: concept
title: Petdex
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- petdex
- mascot
- display
- cli
- tui
- desktop
- productivity
sources:
- hermes://skill/petdex
description: Install and select animated petdex mascots for Hermes.
---

# Petdex

> Install and select animated petdex mascots for Hermes.

## Overview

- **When to Use** — - The user wants a desktop/terminal mascot or asks about "pets" / petdex. - The user wants to change, preview, or disable the active pet. - Diagnosing why a pet isn't showing (terminal graphics support, config).
- **Prerequisites** — - Network access to `petdex.dev` for the gallery/manifest (read-only, no auth). - Pillow (a core Hermes dependency) for sprite decoding — already installed. - For full-fidelity terminal rendering: a graphics-capable terminal (kitty, Ghostty, WezTerm, iTerm2, or sixel). Otherwise a truecolor Unicode half-block fallback is used automatically.
- **How to Run** — Use the `terminal` tool to run `hermes pets <subcommand>`.

## Further detail

### Quick Reference

| Goal | Command | | --- | --- | | Browse the gallery | `hermes pets list` (add a substring to filter: `hermes pets list cat`) | | List installed pets | `hermes pets list --installed` | | Install a pet | `hermes pets install <slug>` (add `--select` to make it active) | | Set the active pet | `hermes pets select <slug>` (omit slug for a picker) | | Resize the pet everywhere | `hermes pets scale <factor>` (e.g. `0.5`, clamped 0.1–3.0) | | Preview/animate in terminal | `hermes pets show [slug] [--cycle] [--state run]` | | Disable the pet | `hermes pets off` | | Remove a pet | `hermes pets remove

### Procedure

1. Find a pet: `hermes pets list <query>` and note its `slug`. 2. Install + activate: `hermes pets install <slug> --select`. 3. Preview it: `hermes pets show` (Ctrl+C to stop). 4. Confirm setup: `hermes pets doctor` — shows the resolved pet, configured render mode, detected terminal graphics protocol, and effective mode.

### Configuration

Under `display.pet` in `config.yaml`:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/petdex/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
