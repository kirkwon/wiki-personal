---
date: 2026-07-19
type: concept
title: Webhook Subscriptions
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- webhook
- events
- automation
- integrations
- notifications
- push
- devops
sources:
- hermes://skill/webhook-subscriptions
description: 'Webhook subscriptions: event-driven agent runs.'
---

# Webhook Subscriptions

> Webhook subscriptions: event-driven agent runs.

## Overview

- **Setup (Required First)** — The webhook platform must be enabled before subscriptions can be created. Check with:
- **Commands** — All management is via the `hermes webhook` CLI command:
- **Prompt Templates** — Prompts support `{dot.notation}` for accessing nested payload fields:

## Further detail

### Security

- Each subscription gets an auto-generated HMAC-SHA256 secret (or provide your own with `--secret`) - The webhook adapter validates signatures on every incoming POST - Static routes from config.yaml cannot be overwritten by dynamic subscriptions - Subscriptions persist to `~/.hermes/webhook_subscriptions.json`

### How It Works

1. `hermes webhook subscribe` writes to `~/.hermes/webhook_subscriptions.json` 2. The webhook adapter hot-reloads this file on each incoming request (mtime-gated, negligible overhead) 3. When a POST arrives matching a route, the adapter formats the prompt and triggers an agent run 4. The agent's response is delivered to the configured target (Telegram, Discord, GitHub comment, etc.)

### Troubleshooting

If webhooks aren't working:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/webhook-subscriptions/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
