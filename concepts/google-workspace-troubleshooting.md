---
date: 2026-07-19
type: concept
title: Google Workspace Troubleshooting
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
- Troubleshooting
- OAuth
- productivity
sources:
- hermes://skill/google-workspace-troubleshooting
description: Troubleshooting and compatibility fixes for Google Workspace OAuth setup
  on older Python versions and systems with dependency issues.
---

# Google Workspace Troubleshooting

> Troubleshooting and compatibility fixes for Google Workspace OAuth setup on older Python versions and systems with dependency issues.

## Overview

- **References** — - `references/token-diagnostics.md` — Fast, dependency-free OAuth token validity check (direct HTTP refresh + curl variant + decision tree) - `references/gmail-imap-fallback.md` — Read-only IMAP fallback when OAuth is down (for cron/autonomous jobs) - `references/redirect-uri-fix.md` — Fix for `redirect_uri_mismatch` OAuth error - `scripts/gmail_imap_scan.py` — Reusable IMAP scanner for degraded-mode inbox scans
- **Verification Steps** — After applying fixes, verify the setup:
- **Advanced Protection Issues** — **Problem:** "Error 403: access_denied" during OAuth flow

## Further detail

### Fallback Approach

If Google Workspace setup continues to fail, consider the simpler `himalaya` skill for email-only access:

### Debug Tips

1. **Check Python version**: `python3 --version` (3.8 requires type hint fixes; < 3.9 also breaks on transitive `urllib3` — see above) 2. **Test imports**: `python3 -c "import googleapiclient; print('OK')"` 3. **Manual test**: Run setup script with `--auth-url` to see if it generates the OAuth URL 4. **Network issues**: Ensure internet connectivity for pip installs 5. **Token expired mid-job (autonomous/cron)**: see "IMAP Fallback for Read-Only Access" below — no user present to re-auth, but read access is recoverable.

### IMAP Fallback for Read-Only Access (2026-07-07)

**Problem:** An autonomous job (cron, heartbeat) loads `google-workspace` to fetch mail, but the OAuth token at `~/.hermes/google_token.json` has expired or been revoked (`invalid_grant: Token has been expired or revoked`). There is no user present to walk through Steps 2–4 of the OAuth flow. The job must still produce *something* useful — typically a degraded morning briefing with weather + calendar, even if Gmail is dark.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/google-workspace-troubleshooting/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
