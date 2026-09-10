---
date: 2026-07-19
type: concept
title: Gws Calendar
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gws
- google-workspace
- calendar
- cli
- scheduling
- communication
sources:
- hermes://skill/gws-calendar
description: Manage Google Calendar via the Google Workspace CLI (gws) — list calendars,
  query events with time windows, handle multi-calendar setups. Use when google_api.py
  calendar calls fail or when you need raw Calendar API access via gws.
---

# Gws Calendar

> Manage Google Calendar via the Google Workspace CLI (gws) — list calendars, query events with time windows, handle multi-calendar setups. Use when google_api.py calendar calls fail or when you need raw Calendar API access via gws.

## Overview

- **When to Use This Skill** — - `$GAPI calendar list` returns `invalid_grant` or auth errors (common — see Credential Separation below) - You need to enumerate ALL calendars (primary, shared, family) — `google_api.py` only covers primary - You need raw Calendar API params (custom `timeMin`/`timeMax`, field filtering) - Building a morning briefing or daily review cron that needs reliable calendar data
- **Credential Separation (Critical)** — `gws` and `google_api.py` do **NOT** share credentials, despite what the `google-workspace` skill implies:
- **Prerequisites** — - `gws` CLI installed and in PATH (`which gws`) - Valid `gws` auth (`gws auth status` should show Calendar scope) - Calendar API enabled in the Google Cloud project backing `gws`

## Further detail

### Core Command Pattern

Unlike `google_api.py`'s wrapper syntax, `gws` passes raw API params as JSON:

### Listing All Calendars

Users often have multiple calendars (shared, family, work). **Always discover all calendar IDs first** before querying events:

### Listing Events (with time window)

**Required params:** - `calendarId` — `"primary"` or a specific ID from `calendarList list`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/communication/gws-calendar/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
