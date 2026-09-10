---
date: 2026-07-19
type: concept
title: Migrate To Gws
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/migrate-to-gws
description: Migrate Gmail script from IMAP/Himalaya to gws CLI.
---

# Migrate To Gws

> Migrate Gmail script from IMAP/Himalaya to gws CLI.

## Overview

- **When to Use** — - You have a Python script that uses imaplib and Himalaya config to read Gmail. - You want to replace it with the officially supported gws CLI for better reliability and OAuth handling. - The script is part of a cron job or hourly triage workflow.
- **Prerequisites** — - Google Workspace CLI (gws) installed and authenticated (`gws auth status` shows Authenticated). - Python 3.8+ with json, os, re, subprocess, sys, time modules (standard library). - Access to the script to be migrated (e.g., `~/.hermes/scripts/inbox-triage.py`). - Optionally, a test environment or ability to run the script manually.
- **How to Run** — Follow the Procedure steps using the `terminal` tool to edit the script, then run it with `python3 <script>` to verify output. Optionally, use `skill_view` to review this skill before starting.

## Further detail

### Quick Reference

- `gws auth status` - `gws gmail users messages list --params '{"userId": "me", "q": "is:unread newer_than:1d"}' --format json` - `gws gmail users messages get --params '{"userId": "me", "id": "<ID>"}' --format json` - `gws gmail users messages modify --params '{"userId": "me", "id": "<ID>", "removeLabelIds": ["UNREAD"], "addLabelIds": ["TRASH"]}' --format json` - `python3 <script>` - `skill_view name=migrate-to-gws`

### Procedure

1. Backup the original script: `cp <script> <script>.bak`. 2. Open the script in an editor (or use `write_file`/`patch` via Hermes tools). 3. Remove IMAP/Himalaya specific imports and configuration blocks (imaplib, email, config path parsing, credential resolution). 4. Keep the constants for newsletters, notifications, urgent keywords, signal routes, self‑tuning functions (they remain unchanged). 5. Replace the `run_triage()` function body with the GWS‑based implementation: a. Load state from STATE_FILE. b. Determine `since_date` as yesterday. c. Call `gws gmail users messages list` with query

### Pitfalls

- The gws CLI uses different command paths: `gmail users messages list` instead of `gmail list`. Ensure you use the correct subcommand. - The internalDate field is epoch milliseconds; the original script used the Date header. If you need a formatted date, convert internalDate to ISO string. - The TRASH label may be named differently in some Gmail domains (e.g., `[Gmail]/Trash`). Using the label name `TRASH` works with gws as it maps to the system Trash label. - Do not forget to remove the UNREAD label when trashing; otherwise the message stays in inbox. - The self‑tuning and Bayesian trust log

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/migrate-to-gws/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
