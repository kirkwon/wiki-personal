---
date: 2026-07-19
type: concept
title: Google Workspace
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Google
- Gmail
- Calendar
- Drive
- Sheets
- Docs
- Contacts
- Email
- OAuth
- productivity
sources:
- hermes://skill/google-workspace
description: Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Hermes.
  Uses Hermes-managed OAuth2 setup, prefers the Google Workspace CLI (`gws`) when
  available for broader API coverage, and falls back to the Python client libraries
  otherwise.
---

# Google Workspace

> Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Hermes. Uses Hermes-managed OAuth2 setup, prefers the Google Workspace CLI (`gws`) when available for broader API coverage, and falls back to the Python client libraries otherwise.

## Overview

- **References** — - `references/gmail-search-syntax.md` — Gmail search operators (is:unread, from:, newer_than:, etc.)
- **Scripts** — - `scripts/setup.py` — OAuth2 setup (run once to authorize) - `scripts/google_api.py` — compatibility wrapper CLI. It prefers `gws` for operations when available, while preserving Hermes' existing JSON output contract.
- **First-Time Setup** — The setup is fully non-interactive — you drive it step by step so it works on CLI, Telegram, Discord, or any platform.

## Further detail

### Usage

All commands go through the API script. Set `GAPI` as a shorthand:

### Output Format

All commands return JSON. Parse with `jq` or read directly. Key fields:

### Rules

1. **Never send email or create/delete events without confirming with the user first.** Show the draft content and ask for approval. 2. **Check auth before first use** — run `setup.py --check`. If it fails, guide the user through setup. 3. **Use the Gmail search syntax reference** for complex queries — load it with `skill_view("google-workspace", file_path="references/gmail-search-syntax.md")`. 4. **Calendar times must include timezone** — always use ISO 8601 with offset (e.g., `2026-03-01T10:00:00-06:00`) or UTC (`Z`). 5. **Respect rate limits** — avoid rapid-fire sequential API calls. Batch

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/google-workspace/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
