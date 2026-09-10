---
date: 2026-08-02
type: concept
title: Authenticated Extraction
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/authenticated-extraction
description: 'Extract data from authenticated web apps by reusing Chrome''s active
  login session. Three approaches: --cdp (connect to running Chrome, best for SPAs),
  --profile (launch with user profile), manual CDP cookie extraction (for httpx replay).
  Solves "scrape data from a site I''m logged into."'
---

# Authenticated Extraction

> Extract data from authenticated web apps by reusing Chrome's active login session. Three approaches: --cdp (connect to running Chrome, best for SPAs), --profile (launch with user profile), manual CDP cookie extraction (for httpx replay). Solves "scrape data from a site I'm logged into."

## Overview

- **Three approaches (best → worst)** — | # | Approach | When | Auth fidelity | |---|----------|------|---------------| | 1 | `--cdp PORT` | Chrome already running, logged in | **Best** — live session, full SPA state | | 2 | `--profile Default` | Chrome NOT running; want persisted login | Good — cookies + localStorage | | 3 | Manual CDP cookie extraction | Need raw cookies for httpx replay | Variable — see pitfalls |
- **Approach 1: `--cdp PORT` (BEST for SPAs)** — Connect to a Chrome that is already running with your active login sessions. This preserves cookies, localStorage, sessionStorage, and in-memory SPA state.
- **Approach 2: `--profile Default` (when Chrome is closed)** — Launch a fresh Chrome using your real user profile. Cookies and localStorage survive, so login state persists. **Chrome must NOT already be running with the same profile** (profile directory lock).

## Further detail

### Approach 3: Manual CDP cookie extraction (for httpx replay)

When you need cookies as a raw string for a Python httpx client (not browser automation). This is the pattern used to reverse-engineer the NotebookLM API.

### Session persistence (repeat workflows / cron jobs)

For recurring extraction (e.g. daily cron), persist the browser session so you don't re-login each run:

### Pitfalls

- **Google CookieMismatch blocks HTTP cookie replay.** Google services (and some others) reject requests where the `Cookie` header doesn't match the exact browser fingerprint. Extracted cookies replayed via httpx can get 401/403 with `CookieMismatch`. For Google properties, **prefer approach 1 (`--cdp`)** and extract data via `eval` inside the live browser — never replay cookies over HTTP. - **SPA auth state lives in localStorage, not cookies.** Cookie-only extraction (approach 3) misses JWTs stored in `localStorage` and attached by a JS interceptor. Always dump `localStorage` too (see `extrac

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/authenticated-extraction/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
