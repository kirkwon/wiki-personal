---
date: 2026-07-19
type: concept
title: Hermes Desktop Plugins
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- desktop
- plugins
- ui
- extension
- uncategorized
sources:
- hermes://skill/hermes-desktop-plugins
description: Write desktop app plugins that add UI panes and commands.
---

# Hermes Desktop Plugins

> Write desktop app plugins that add UI panes and commands.

## Overview

- **When to Use** — - The user asks for a new desktop UI element (a pane, a statusbar widget, a dashboard, a command) without modifying the app itself. - You want to surface data you compute (via gateway RPC) inside the app.
- **Prerequisites** — - The Hermes desktop app (it loads plugins; the CLI/gateway alone does not). - Write access to `$HERMES_HOME/desktop-plugins/` (usually `~/.hermes/desktop-plugins/`).
- **How to Run** — 1. Create `$HERMES_HOME/desktop-plugins/<name>/plugin.js` from `templates/plugin.js` (relative to this skill directory) — that's `~/.hermes/...` by default, or `~/.hermes/profiles/<profile>/...` under a named profile. Keep `<name>` equal to the plugin `id`. 2. The desktop app watches that directory: the plugin loads within a few seconds of the file landing, and every later save hot-reloads it in place. No reload step. (Fallback if it doesn't appear: ⌘K → **Reload desktop plugins**.) 3. If loading fails the app shows a toast naming the error — fix the file and save again.

## Further detail

### Quick Reference

The ONLY import surface is `@hermes/plugin-sdk` (plus `react` / `react/jsx-runtime`, which resolve to the app's own React — write UI with `jsx()` calls, not JSX syntax; the file is not compiled).

### Procedure

1. Pick a short kebab-case `id`; the folder name must match. 2. Start from `templates/plugin.js`; keep the default export shape (`{ id, name, register(ctx) }`). 3. For a pane, register `area: 'panes'` with a `placement` hint and a `render` returning your component — the app places it into a sensible zone automatically; the user can drag it anywhere afterwards. 4. Fetch data with `host.request` and/or subscribe with `host.onEvent`; never poll faster than a few seconds. 5. Write the file with your file tools, then ask the user to run **Reload desktop plugins** from ⌘K.

### Pitfalls

- NEVER hardcode colors or backgrounds (`#000`, `black`, `rgb(...)`). Panes already sit on the app's editor background — leave the background alone and use theme variables for everything else: `var(--ui-text-secondary)`, `var(--ui-text-quaternary)`, `var(--ui-stroke-secondary)`, `var(--ui-accent)`. For canvas drawing, resolve them once with `getComputedStyle(canvas).getPropertyValue('--ui-accent')`. - Reference only what you imported — a component you forgot to import (e.g. `StatusDot`) is a ReferenceError at render. Double-check every identifier in your `jsx()` calls appears in the import lin

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/hermes-desktop-plugins/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
