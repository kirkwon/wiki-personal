---
date: 2026-07-19
type: concept
title: Inbox Triage
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- file-organization
- automation
- para-system
- cron-job
- email
- triage
- productivity
sources:
- hermes://skill/inbox-triage
description: Automatically categorize and organize files in Downloads/ inbox into
  PARA structure and delegate email triage to gws-email-triage skill.
---

# Inbox Triage

> Automatically categorize and organize files in Downloads/ inbox into PARA structure and delegate email triage to gws-email-triage skill.

## Overview

- **When to Use This Skill** — Use this skill when: - Your Downloads/ inbox has accumulated 50+ loose files - You want to maintain a clean PARA structure automatically - You want to prevent file backlogs before they grow unmanageable - You need to regularly process your email for actionable items (via gws-email-triage) - Running as a scheduled task (cron job: daily or weekly for files, hourly for email via gws-email-triage)
- **Part 2: Email Triage (Delegated to gws-email-triage)** — Email triage functionality has been moved to the dedicated `gws-email-triage` skill for better modularity and maintenance. This separation allows each component to evolve independently while maintaining a unified workflow.
- **Safety Policy** — This skill follows **conservative-by-default** principles:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/inbox-triage/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
