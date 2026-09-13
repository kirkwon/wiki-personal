---
type: concept
title: Agent Browser
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - devops
---

# agent-browser

>

## Usage

# agent-browser

Fast browser-automation CLI (v0.31.1, `/opt/homebrew/bin/agent-browser`). Chrome via CDP — no Playwright/Puppeteer dependency. Accessibility-tree snapshots with compact `@eN` refs let you interact in ~200-400 tokens instead of parsing raw HTML.

## When to use agent-browser vs Hermes browser_* tools

| Need | Use |
|------|-----|
| Simple navigation + single-page read, one-off | **Hermes `browser_navigate` / `browser_snapshot`** (fewer moving parts) |
| CLI-native speed, scriptable, repeatable | **agent-browser** |
| Reuse Chrome login session (`--profile`, `--cdp`) | **agent-browser** |
| JS eval / structured extraction (`eval --stdin`) | **agent-browser** |
| HAR / network recording | **agent-browser** |
| Multi-session parallel browsers | **agent-browser** |
| Vision screenshot + annotate (`--annotate`) | **agent-browser** |

Rule of thumb: reach for Hermes `browser_*` for a quick one-shot page read. Reach for agent-browser the moment you need auth reuse, JS eval, network capture, or a repeatable script.

## The core loop

```bash
agent-browser open <url>        # 1. Open a page
agent-browser snapshot -i       # 2. See interactive elements (refs @e1, @e2, ...)
agent-browser click @e3         # 3. Act on a ref
agent-browser snapshot -i       # 4. Re-snapshot after ANY page change
```

Refs are reassigned on every snapshot. **They go stale the moment the page changes** — after navigations, form submits, dynamic re-renders, dialog opens. Always re-snapshot before the next ref interaction.

## Global flags (put before the command)

```bash
--session <name>        # isolated browser session (own cookies/tabs/refs)
--cdp <port>            # connect to an already-running Chrome via CDP port
--auto-connect          # auto-discover + connect to running Chrome (reuse its auth)
--profile <name|path>   # launch Chrome with a profile (login state survives). e.g. Default
--restore [name]        # auto-save/restore cookies+localStorage; defaults to --session key
--restore-save auto     # save policy: auto (default) | always | never
--headers <json>        # HTTP headers scoped to the URL origin (e.g. bearer token)
--headed                # show the window (default is headless)
--json                  # machine-readable output
--state <path>          # load saved auth state (cookies + storage) from JSON
```

### Auth / session reuse (most common reason to pick agent-browser)

```bash
# Connect to a Chrome that is already running (BEST for logged-in SPAs):
agent-browser --cdp 9222 open https://app.example.com/dashboard

# Launch a fresh Chrome using your real profile (cookies + localStorage):
agent-browser --profile Default open https://app.example.com/dashboard

# Persist a session across runs (repeatable cron jobs):
SESSION="$(agent-browser session id --scope worktree --prefix my-app)"
agent-browser --session "$SESSION" --restore open https://app.example.com
# ... do work ...
# state auto-saved under the session key; next run restores it
```

...(truncated)