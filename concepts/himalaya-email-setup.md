---
date: 2026-07-19
type: concept
title: Himalaya Email Setup
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Email
- Gmail
- Himalaya
- SMTP
- IMAP
- configuration
- productivity
sources:
- hermes://skill/himalaya-email-setup
description: Configure Himalaya for Gmail SMTP/IMAP access to send emails via Hermes,
  including app password and OAuth2 setup.
---

# Himalaya Email Setup

> Configure Himalaya for Gmail SMTP/IMAP access to send emails via Hermes, including app password and OAuth2 setup.

## Overview

- **When to Use This Skill** — - You want to send emails from Hermes (e.g., session reports, notifications) using your Gmail account. - You prefer a lightweight, local CLI tool over the Google Workspace skill or direct API calls. - You need to set up Himalaya for the first time or reconfigure it after authentication issues.
- **Prerequisites** — - Himalaya CLI installed (`~/.local/bin/himalaya` or in your `$PATH`). - A Gmail account (e.g., `kirkwon@gmail.com`). - If using 2‑Factor Authentication (recommended), generate an **App Password**: 1. Go to your Google Account → Security → App Passwords. 2. Select app: **Mail**, device: **Other** (name it `himalaya`). 3. Copy the 16‑character password.
- **Using Himalaya in Hermes** — Once configured, you can send emails from Hermes using the `himalaya` skill or directly via the terminal tool.

## Further detail

### Troubleshooting

| Issue | Solution | |-------|----------| | `cannot find default account configuration` | Config is in v0.x format. Check: does it use `imap.host` / `smtp.mechanism`? If so, rewrite in v1.x format. Also ensure `default = true` is set under the account section. Also: the `backend.*` schema from docs.rs is WRONG for v1.2.0 — use `imap.server` + `imap.sasl.*` instead. | | Binary lacks `+oauth2`/`+keyring` features | Check `himalaya --version` for feature flags. Common Homebrew/nix builds omit these. Without them, `*.keyring` config keys are silently ignored. Must use `password.raw` with an App Pa

### Notes

- Himalaya stores its configuration in `~/.config/himalaya/config.toml` (you can override with `--config`). - The `himalaya message send` command expects a fully formatted email (with headers) on stdin. The `write` subcommand helps build this. - For best reliability in automated scripts, use the App Password method unless you specifically need two‑way sync.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/himalaya-email-setup/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
