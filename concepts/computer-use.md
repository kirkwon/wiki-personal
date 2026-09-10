---
date: 2026-07-19
type: concept
title: Computer Use
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- computer-use
- desktop
- automation
- gui
- cross-platform
- uncategorized
sources:
- hermes://skill/computer-use
description: 'Drive the user''s desktop in the background — clicking, typing,

  scrolling, dragging — without stealing the cursor, keyboard focus,

  or switching virtual desktops / Spaces. Cross-platform: macOS,

  Windows, Linux. Works with any tool-capable model. Load this skill

  whenever the `computer_use` tool is available.'
---

# Computer Use

> Drive the user's desktop in the background — clicking, typing,
scrolling, dragging — without stealing the cursor, keyboard focus,
or switching virtual desktops / Spaces. Cross-platform: macOS,
Windows, Linux. Works with any tool-capable model. Load this skill
whenever the `computer_use` tool is available.

## Overview

- **The canonical workflow** — **Step 1 — Capture first.** Almost every task starts with:
- **Capture modes** — | `mode` | Returns | Best for | |---|---|---| | `som` (default) | Screenshot + numbered overlays + AX index | Vision models; preferred default | | `vision` | Plain screenshot | When SOM overlay interferes with what you want to verify | | `ax` | AX tree only, no image | Text-only models, or when you don't need to see pixels |
- **Actions** — All actions accept optional `capture_after=True` to get a follow-up screenshot in the same tool call. All actions that target an element accept `modifiers=[…]` for held keys.

## Further detail

### Background rules (the whole point)

1. **Never `raise_window=True`** unless the user explicitly asked you to bring a window to front. Input routing works without raising. 2. **Scope captures to an app** (`app="Chrome"`) — less noisy, fewer elements, doesn't leak other windows the user has open. 3. **Don't switch virtual desktops / Spaces.** cua-driver drives elements on any virtual desktop / Space regardless of which one is visible. 4. **The user can be on the same machine.** They might be typing in another window. Don't grab focus. Don't pop modals to the front.

### Drag & drop

Prefer element indices:

### Scroll

Scroll the viewport under an element (most common):

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/computer-use/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
