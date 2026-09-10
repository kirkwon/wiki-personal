---
date: 2026-07-19
type: concept
title: Macos Computer Use
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- computer-use
- macos
- desktop
- automation
- gui
- apple
sources:
- hermes://skill/macos-computer-use
description: 'Drive the macOS desktop in the background — screenshots, mouse, keyboard,

  scroll, drag — without stealing the user''s cursor, keyboard focus, or

  Space. Works with any tool-capable model. Load this skill whenever the

  `computer_use` tool is available.'
---

# Macos Computer Use

> Drive the macOS desktop in the background — screenshots, mouse, keyboard,
scroll, drag — without stealing the user's cursor, keyboard focus, or
Space. Works with any tool-capable model. Load this skill whenever the
`computer_use` tool is available.

## Overview

- **The canonical workflow** — **Step 1 — Capture first.** Almost every task starts with:
- **Capture modes** — | `mode` | Returns | Best for | |---|---|---| | `som` (default) | Screenshot + numbered overlays + AX index | Vision models; preferred default | | `vision` | Plain screenshot | When SOM overlay interferes with what you want to verify | | `ax` | AX tree only, no image | Text-only models, or when you don't need to see pixels |
- **Actions** — All actions accept optional `capture_after=True` to get a follow-up screenshot in the same tool call.

## Further detail

### Background rules (the whole point)

1. **Never `raise_window=True`** unless the user explicitly asked you to bring a window to front. Input routing works without raising. 2. **Scope captures to an app** (`app="Safari"`) — less noisy, fewer elements, doesn't leak other windows the user has open. 3. **Don't switch Spaces.** cua-driver drives elements on any Space regardless of which one is visible.

### Text input patterns

- `type` sends whatever string you give it, respecting the current layout. Unicode works. - For shortcuts use `key` with `+`-joined names: - `cmd+s` save - `cmd+t` new tab - `cmd+w` close tab - `return` / `escape` / `tab` / `space` - `cmd+shift+g` go to path (Finder) - Arrow keys: `up`, `down`, `left`, `right`, optionally with modifiers.

### Drag & drop

Prefer element indices:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/apple/macos-computer-use/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
