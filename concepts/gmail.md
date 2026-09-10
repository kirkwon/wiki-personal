---
date: 2026-07-19
type: concept
title: Gmail
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gmail
- email
- imap
- triage
- automation
- productivity
sources:
- hermes://skill/gmail
description: CLI tools for Gmail — search, read, list, send, and automated email triage
  with body-level urgency detection.
---

# Gmail

> CLI tools for Gmail — search, read, list, send, and automated email triage with body-level urgency detection.

## Overview

- **When to Use This Skill** — Use `gmail.py` when: - You want to see what's in your inbox without opening Gmail - You need to find a specific email (search by sender, subject, or text) - You want to read the full body of an email
- **Triage System (inbox-triage.py)** — **Schedule:** Hourly cron **Script:** `~/.hermes/scripts/inbox-triage.py` **State:** `~/.hermes/scripts/triage-state.json` (tracks seen IDs)
- **Keyword Maintenance** — Edit these lists in `~/.hermes/scripts/inbox-triage.py`:

## Further detail

### Architecture

**As of 2026-06-27:** Google Workspace OAuth is now the primary authentication path. Token at `~/.hermes/google_token.json` (auto-refreshing, desktop app credentials). The `gmail.py` script still works via IMAP credentials, but Google Workspace API access is preferred for cron jobs and automated workflows. Load the `google-workspace` skill for API-based access.

### Related Files

- Script: `~/.hermes/scripts/gmail.py` - Script: `~/.hermes/scripts/inbox-triage.py` - State: `~/.hermes/scripts/triage-state.json` - Skill: `inbox-triage` (file inbox triage + email footnote) - Reference: `references/google-workspace-oauth-setup.md` — OAuth setup with local callback server (bypasses localhost:1 hanging bug in bundled setup.py)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/gmail/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
