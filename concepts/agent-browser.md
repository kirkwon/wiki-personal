---
type: concept
title: Agent Browser
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Agent Browser

> Use when automating a website — fill forms, click flows, extract data, log in, scrape, run JS. Core routing skill: choose agent-browser CLI vs Hermes built-in browser_* tools. Covers the snapshot-ref loop, auth/session reuse, JS eval, and structured extraction.

## Overview

- **When to use agent-browser vs Hermes browser_* tools** — | Need | Use | |------|-----| | Simple navigation + single-page read, one-off | **Hermes `browser_navigate` / `browser_snapshot`** (fewer moving parts) | | CLI-native speed, scriptable, repeatable | **agent-browser** | | Reuse Chrome login session (`--profile`, `--cdp`) | **agent-browser** | | JS eval / structured extraction (`eval --stdin`) | **agent-browser** | | HAR / network recording | **agent-browser** | | Multi-session parallel browsers | **agent-browser** | | Vision screenshot + annotate (`--annotate`) | **agent-browser** |
- **The core loop** — Refs are reassigned on every snapshot. **They go stale the moment the page changes** — after navigations, form submits, dynamic re-renders, dialog opens. Always re-snapshot before the next ref interaction.
- **eval --stdin — structured data extraction** — Prefer `eval --stdin` (heredoc) for any JS with quotes or special chars. **Wrap multi-statement scripts in an IIFE** to avoid `Identifier 'x' has already been declared` errors when the script is evaluated more than once on the same page:

## Further detail

### Related skills

- **web-api-reverse-engineer** — HAR recording → discover endpoints → build Python client - **authenticated-extraction** — reuse Chrome login sessions; CDP cookie extraction - **crawl4ai** — local markdown extraction (no interaction needed) - **web-fallback** — search/extract with Exa+Jina fallback (no browser needed)

### Pitfalls

- **Refs go stale after ANY page change.** Click that navigates, form submit, SPA re-render, tab switch, dialog open — all invalidate refs. Re-snapshot (`snapshot -i`) before the next ref interaction. This is the #1 failure mode. - **`--profile` requires Chrome NOT already running with that profile.** Chrome locks the profile directory. If Chrome is open with `Default`, `--profile Default` will fail or launch a fresh temp profile. Use `--cdp <port>` (connect to the running instance) instead. - **Profile mode may render blank in headless for some SPAs.** If a `--profile` launch shows an empty p

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/agent-browser/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[agent-self-introspection]]
