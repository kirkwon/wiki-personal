---
date: 2026-07-19
type: concept
title: Gws Email Send
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- communication
sources:
- hermes://skill/gws-email-send
description: Send email with attachment via Google Workspace CLI.
---

# Gws Email Send

> Send email with attachment via Google Workspace CLI.

## Overview

- **When to Use** — - You need to send a file (e.g., a report) to an email address via Gmail. - You have Google Workspace CLI installed and a Google Cloud OAuth client configured. - You prefer a non-interactive, scriptable method after initial auth setup. - Himalaya is not usable due to missing TTY for interactive prompts.
- **Prerequisites** — - macOS (tested on macOS 26.1) or any OS where `gws` is available. - Google Workspace CLI (`gws`) installed and in PATH. - A Google Cloud OAuth client (client ID and secret) saved as `~/.config/gws/client_secret.json` or available via environment variables `GOOGLE_WORKSPACE_CLI_CLIENT_ID` and `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET`. - Access to a browser to complete the initial OAuth consent flow (only required once unless tokens expire).
- **How to Run** — Invoke through the `terminal` tool with the appropriate command, or use the provided procedure steps. The skill assumes you have the file to attach, recipient, subject, and body ready.

## Further detail

### Quick Reference

- `gws auth status` – Check authentication. - `gws auth login --services gmail` – Authenticate (opens browser for consent). - `gws gmail +send --to <addr> --subject "<subj>" --body "<body>" --attach <file>` – Send email with attachment.

### Procedure

1. **Verify GWS installation**

### Pitfalls

- **Interactive auth required**: The first `gws auth login` needs a browser; cannot be fully automated without user interaction. - **Token expiration**: Refresh tokens may expire or be revoked; re‑run step 3 if `gws auth status` shows `"token_valid": false`. - **Attachment size**: Gmail limits attachments to 25 MB; larger files must be shared via Drive link. - **Scoped tokens**: Ensure the OAuth client includes the `https://www.googleapis.com/auth/gmail.modify` scope; otherwise sending will fail. - **CLI version**: Older versions of `gws` may use different subcommand syntax; verify with `gws g

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/communication/gws-email-send/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
