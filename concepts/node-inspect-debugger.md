---
date: 2026-07-19
type: concept
title: Node Inspect Debugger
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- debugging
- nodejs
- node-inspect
- cdp
- breakpoints
- ui-tui
- software-development
sources:
- hermes://skill/node-inspect-debugger
description: Debug Node.js via --inspect + Chrome DevTools Protocol CLI.
---

# Node Inspect Debugger

> Debug Node.js via --inspect + Chrome DevTools Protocol CLI.

## Overview

- **Overview** — When `console.log` isn't enough, drive Node's built-in V8 inspector programmatically from the terminal. You get real breakpoints, step in/over/out, call-stack walking, local/closure scope dumps, and arbitrary expression evaluation in the paused frame.
- **When to Use** — - A Node test fails and you need to see intermediate state - ui-tui crashes or behaves wrong and you want to inspect React/Ink state pre-render - tui_gateway child processes (`_SlashWorker`, PTY bridge workers) misbehave - You need to inspect a value in a closure that `console.log` can't reach without patching - Perf: attach to a running process to capture a CPU profile or heap snapshot
- **Quick Reference: `node inspect` REPL** — Launch paused on first line:

## Further detail

### Attaching to a Running Process

When the process is already running (e.g. a long-lived dev server or the TUI gateway):

### Programmatic CDP (scripting from terminal)

When you want to automate — set many breakpoints, capture scope state, script a repro — use `chrome-remote-interface`:

### Debugging Hermes ui-tui

The TUI is built Ink + tsx. Two common scenarios:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/node-inspect-debugger/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
