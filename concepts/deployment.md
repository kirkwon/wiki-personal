---
type: concept
title: Deployment
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Deployment
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/deployment
description: Deploy scripts, cron jobs, services, and configurations. Use this skill
  whenever the user needs to schedule a recurring task with cron, install a script,
  set up a background service, create a launchd plist, deploy code to production,
  manage environment variables, set up a systemd service, or automate a deployment
  workflow. Covers Hermes cron jobs, launchd services, background processes, environment
  configuration, and deployment verification patterns. Trigger on phrases like "deploy
  this", "set up cron", "schedule this", "run on startup", "background service", "launchd",
  "systemd", "auto-start", "production deploy", "env vars", "environment setup", "install
  as service", "daemonize", "always-on".
---

# Deployment

> Deploy scripts, cron jobs, services, and configurations. Use this skill whenever the user needs to schedule a recurring task with cron, install a script, set up a background service, create a launchd plist, deploy code to production, manage environment variables, set up a systemd service, or automate a deployment workflow. Covers Hermes cron jobs, launchd services, background processes, environment configuration, and deployment verification patterns. Trigger on phrases like "deploy this", "set up cron", "schedule this", "run on startup", "background service", "launchd", "systemd", "auto-start", "production deploy", "env vars", "environment setup", "install as service", "daemonize", "always-on".

## Overview

- **Environment Context** — - **Host:** macOS (26.1) - **Hermes gateway:** runs as a managed service - **Python:** 3.11.14 (use `python3`, avoid system Python 3.8 for new scripts) - **Package manager:** `uv` preferred over `pip` (PEP 668 enforced) - **Cron system:** built into Hermes (not OS cron) — use `cronjob` tool - **Scripts dir:** `~/.hermes/scripts/` - **Working dir:** `~/clawd/` (project root)
- **3. Background Processes (Servers, Daemons, Watchers)** — Use `terminal(background=True)` for long-lived processes:
- **Related** — - `references/token-optimization.md` — Hermes token cost optimization checklist (10 config cuts applied 2026-07-01)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/deployment/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
