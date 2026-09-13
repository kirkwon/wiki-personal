---
type: concept
title: Hermes Desktop Plugins
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - productivity
---

# hermes-desktop-plugins

Write desktop app plugins that add UI panes and commands.

## Usage

# Hermes Desktop Plugins Skill

Write plugins for the Hermes desktop app: statusbar items, layout panes,
command-palette commands, keybinds, routes, and themes. A plugin is a single
plain-JavaScript ESM file the app loads at runtime — no build step, no repo
changes. A plugin can also talk to its own Python backend namespace
(`ctx.rest`/`ctx.socket` → `/api/plugins/<id>`); the general Python plugin
system (`~/.hermes/plugins/`) is otherwise documented separately.

Full human reference (every export, area payloads, backend, security):
`website/docs/developer-guide/desktop-plugin-sdk.md`.

## When to Use

- The user asks for a new desktop UI element (a pane, a statusbar widget, a
  dashboard, a command) without modifying the app itself.
- You want to surface data you compute (via gateway RPC) inside the app.

## Prerequisites

- The Hermes desktop app (it loads plugins; the CLI/gateway alone does not).
- Write access to `$HERMES_HOME/desktop-plugins/` (usually
  `~/.hermes/desktop-plugins/`).

## How to Run

1. Create `$HERMES_HOME/desktop-plugins/<name>/plugin.js` from
   `templates/plugin.js` (relative to this skill directory) — that's
   `~/.hermes/...` by default, or `~/.hermes/profiles/<profile>/...` under a
   named profile. Keep `<name>` equal to the plugin `id`.
2. The desktop app watches that directory: the plugin loads within a few
   seconds of the file landing, and every later save hot-reloads it in
   place. No reload step. (Fallback if it doesn't appear: ⌘K →
   **Reload desktop plugins**.)
3. If loading fails the app shows a toast naming the error — fix the file
   and save again.

## Quick Reference

The ONLY import surface is `@hermes/plugin-sdk` (plus `react` /
`react/jsx-runtime`, which resolve to the app's own React — write UI with
`jsx()` calls, not JSX syntax; the file is not compiled).

- `host.state.*` — readonly reactive atoms: `activeSessionId`, `cwd`,
  `gateway`, `model`, `profile`, `viewport`. Read with `.get()` in handlers,
  `useValue(atom)` in components.
- `host.request(method, params)` — gateway JSON-RPC (sessions, config,
  skills, cron — everything the app uses).
- `host.onEvent(type, fn)` — live gateway events (`'*'` for all). Returns a
  disposer.
- `host.notify({ kind, message })`, `host.navigate(path)`, `host.logs(...)`,
  `host.status()`, `haptic('tap')`.
- `ctx.register({ id, area, order?, render?, data? })` — contribute UI.
  Key areas: `'statusBar.right'`/`'statusBar.left'` (chips),
  `'panes'` (layout zones — set `title` and
  `data: { placement, dock?, width?, height? }`; the pane auto-joins a
  matching zone), `PALETTE_AREA` (⌘K commands), `KEYBINDS_AREA` (rebindable
  actions).
- Pane placement: `placement: 'left'|'right'|'bottom'|'main'` is the
  semantic role — the pane stacks (tabs) with existing panes of that role.
  To land on a specific EDGE instead, add `dock: { pane, pos }` — the same
  gesture as dragging onto a pane's drop chip. `pane` is any pane id
  (`workspace` is the main thread; also `s

...(truncated)