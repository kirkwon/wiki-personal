---
date: 2026-08-02
type: concept
title: Email Triage
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- email
- gmail
- triage
- filtering
- cron
- productivity
- software-development
sources:
- hermes://skill/email-triage
description: Smart inbox triage with five-layer filtering — server-side Gmail categories,
  priority surfacing, batch collapsing, recruiter auto-detection, and auto-learning
  tuning. Produces morning-briefing-style summaries instead of raw email dumps.
---

# Email Triage

> Smart inbox triage with five-layer filtering — server-side Gmail categories, priority surfacing, batch collapsing, recruiter auto-detection, and auto-learning tuning. Produces morning-briefing-style summaries instead of raw email dumps.

## Overview

- **When to Use** — - Setting up or maintaining inbox triage cron jobs - User complains that triage is "dumping 50 emails" without real filtering - User wants triage output to look like the morning briefing (less spam, prioritized) - Migrating from GWS-based email access to gmail_list.py - Need to reduce email noise in Telegram cron deliveries - Building iterative/self-tuning email filters (recruiter detection, trusted senders)
- **Architecture: Server-Side First** — **Key insight:** Gmail's own category classification is the most effective noise filter. Use it server-side via Gmail search rather than fetching everything and filtering client-side.
- **Related Files** — - `~/.hermes/scripts/gmail_triage.py` — canonical triage module (v3, underscore for import) - `~/.hermes/scripts/gmail-triage.py` — thin wrapper (delegates to canonical) - `~/.hermes/scripts/gmail-triage.sh` — shell wrapper for cron entry point - `~/.hermes/scripts/triage-tuning-sync.py` — sent-mail analysis for trusted sender discovery - `~/.hermes/scripts/triage-tuning.json` — auto-learned tuning state (recruiter domains, trusted senders) - `~/gmail-reader/gmail_list.py` — Gmail CLI (OAuth-based) - `~/.local/bin/gmail` — symlink/wrapper to gmail_list.py - See `references/server-side-filterin

## Further detail

### References

- `gmail` skill — covers the old gmail.py IMAP + inbox-triage.py architecture (manually authored, may be stale) - `gws-email-triage` skill — deprecated GWS-based approach (manually authored) - `himalaya-email-setup` skill — Himalaya CLI configuration (separate concern, for send-only)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/email-triage/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
