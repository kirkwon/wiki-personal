---
date: 2026-07-19
type: concept
title: Email Sending
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/email-sending
description: Send emails via SMTP (smtplib) and transactional email APIs (SendGrid,
  Mailgun via curl). Covers Gmail App Passwords, environment-variable credential management,
  and error handling for auth failures, connection issues, and rate limits. All tools
  use terminal (python3, curl).
---

# Email Sending

> Send emails via SMTP (smtplib) and transactional email APIs (SendGrid, Mailgun via curl). Covers Gmail App Passwords, environment-variable credential management, and error handling for auth failures, connection issues, and rate limits. All tools use terminal (python3, curl).

## Overview

- **Tools Used** — | Tool | Purpose | |------|---------| | `terminal` | Run python3, curl |
- **1. Environment Variables for Credentials** — **Never hardcode email credentials.** Always load them from environment variables. Define these in the shell session before sending, or set them persistently in `~/.zshrc` / `~/.bashrc`.
- **3. Gmail App Passwords via SMTP** — Gmail requires an **App Password** (not your regular Google password) when using SMTP. Generate one at: https://myaccount.google.com/apppasswords

## Further detail

### 4. SendGrid via curl API

SendGrid uses a REST API with a Bearer token. Set the API key in `SENDGRID_API_KEY`.

### 5. Mailgun via curl API

Mailgun uses Basic auth with `api:YOUR_API_KEY`.

### 7. Quick Reference — Cheat Sheet

| Task | Command | |------|---------| | **SMTP plain text** | `python3 -c '...smtplib...'` (see §2) | | **SMTP HTML** | `python3 -c '...add_alternative(..., subtype="html")...'` | | **SMTP attachment** | `python3 -c '...add_attachment(...)...'` | | **Gmail App Password** | `GMAIL_USER` + `GMAIL_APP_PASS` → smtp.gmail.com:587 | | **SendGrid** | `curl -H "Authorization: Bearer ${SENDGRID_API_KEY}" ...` | | **Mailgun** | `curl --user "api:${MAILGUN_API_KEY}" ...` | | **Check env vars** | `: "${VAR:?VAR not set}"` | | **Catch auth failure** | `except smtplib.SMTPAuthenticationError` | | **Catch co

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/email-sending/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
