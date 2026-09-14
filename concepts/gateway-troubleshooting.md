---
type: concept
title: Gateway Troubleshooting
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Gateway Troubleshooting
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gateway
- troubleshooting
- telegram
- messaging
- hermes
- network
- diagnostics
- devops
sources:
- hermes://skill/gateway-troubleshooting
description: Diagnose and repair Hermes messaging-platform gateway issues (Telegram,
  Discord, Slack, WhatsApp, Signal, etc.) without crashing the host. Covers the config-vs-network
  disambiguation technique, read-only watchdog patterns, retry-storm suppression,
  and the silent-polling-death trap. CRITICAL — embeds the gateway-restart crash hazard
  and the safe-restart protocol. Load when the user reports a gateway/bot/platform
  outage, messages not delivered, bot not responding, or platform connectivity issues.
---

# Gateway Troubleshooting

> Diagnose and repair Hermes messaging-platform gateway issues (Telegram, Discord, Slack, WhatsApp, Signal, etc.) without crashing the host. Covers the config-vs-network disambiguation technique, read-only watchdog patterns, retry-storm suppression, and the silent-polling-death trap. CRITICAL — embeds the gateway-restart crash hazard and the safe-restart protocol. Load when the user reports a gateway/bot/platform outage, messages not delivered, bot not responding, or platform connectivity issues.

## Overview

- **⚠️ THE CARDINAL RULE — Gateway Restarts Can Crash the Machine** — **`hermes gateway restart` is a high-risk command on this user's setup.** It has crashed the machine before. The user said, verbatim: *"be careful this crashed my machine last time."*
- **Command Reference (correct forms — these trip up every new session)** — | Task | WRONG | CORRECT | |------|-------|---------| | Restart gateway | `hermes restart gateway` | `hermes gateway restart` | | Send a test message | `hermes send telegram "msg"` | `hermes send --to telegram "msg"` | | Send to specific chat | `hermes send telegram:12345 "msg"` | `hermes send --to telegram:12345 "msg"` | | Gateway subcommands | — | `hermes gateway {run,start,stop,restart,status,install,uninstall,list,setup}` |
- **The Diagnostic Discipline** — Gateway outages have two failure domains. **Always disambiguate which one you're in before acting:**

## Further detail

### The Silent-Polling-Death Trap ⚠️

**Polling threads can die without logging an error.** When this happens, "no recent errors in the log" is a FALSE POSITIVE for health — the thread is dead, so it can't log errors.

### The `hermes status` Config-vs-Liveness Trap ⚠️

**`hermes status` is a CONFIG check, not a LIVENESS check.** It reports what is *configured* (env vars, config.yaml entries), not what is *actually running*. A line like "Browser automation ✓ active via Camofox" means "CAMOFOX_URL is set" — NOT "the Camofox daemon is reachable."

### Read-Only Watchdog Pattern

When the route is flapping (intermittent connectivity), use a background script that watches the log without touching the gateway process. See `scripts/tg-watchdog.sh`:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/gateway-troubleshooting/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
