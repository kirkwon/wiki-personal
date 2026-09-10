---
date: 2026-07-19
type: concept
title: Gws Email Triage
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- communication
sources:
- hermes://skill/gws-email-triage
description: Process Gmail inbox using Google Workspace CLI for triage and action
  extraction.
---

# Gws Email Triage

> Process Gmail inbox using Google Workspace CLI for triage and action extraction.

## Overview

- **When to Use This Skill** — - You want to automatically scan your unread Gmail for actionable items - You need to extract email content for your knowledge base (GBrain/Obsidian) - You're setting up a cron job for regular email processing - You prefer GWS over Himalaya for email operations (more reliable automation) - You want to flag/label processed emails automatically
- **Prerequisites** — - macOS (or Linux/Windows with GWS installed) - Google Workspace CLI (`gws`) installed and in PATH - Valid Google OAuth credentials configured (run `gws auth status` to verify) - The `gmail.modify` scope must be enabled in your OAuth client (for labeling/marking as read) - Basic familiarity with your email processing workflow
- **How to Run** — Invoke through the `terminal` tool or run the commands directly in your shell. The skill provides a reusable workflow for: 1. Fetching unread emails 2. Extracting key information (sender, subject, snippet) 3. Optionally processing content for knowledge capture 4. Marking emails as processed (read/labelled)

## Further detail

### Quick Reference

- `gws gmail +triage` – Show summary of unread emails - `gws gmail +read --id <ID>` – Read full email content (use --format json/table/yaml/csv) - `gws gmail modify --id <ID> --remove-label UNREAD` – Mark as read - `gws gmail modify --id <ID> --add-label ^Processed` – Add custom label

### Example Cron Job Setup

To run this daily at 9 AM:

### Pitfalls

- **Scope Missing**: If `gmail.modify` isn't in your OAuth scopes, you can read but not modify labels. Re-run `gws auth login --services gmail` to ensure proper scopes. - **Rate Limits**: Gmail API has limits; avoid polling too frequently (<5 min intervals may cause issues). - **JSON Parsing**: The `+triage` output is JSON; use `jq` for reliable field extraction. - **Label Names**: GWS uses `^LabelName` syntax for labels (note the caret prefix). - **Token Expiry**: Refresh tokens can expire; check `gws auth status` periodically if automation fails. - **Large Attachments**: The `+read` command

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/communication/gws-email-triage/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
