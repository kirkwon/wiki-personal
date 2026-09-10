---
date: 2026-07-19
type: concept
title: Hermes Skill Development Workflow
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- skills
- automation
- safety
- testing
- deployment
- cron
- user-local
- software-development
sources:
- hermes://skill/hermes-skill-development-workflow
description: Use when creating, testing, installing, and scheduling user-local Hermes
  Agent skills with safety policies, dry-run testing, rollback capability, and cron
  job deployment. Covers full lifecycle from initial design through automated execution.
---

# Hermes Skill Development Workflow

> Use when creating, testing, installing, and scheduling user-local Hermes Agent skills with safety policies, dry-run testing, rollback capability, and cron job deployment. Covers full lifecycle from initial design through automated execution.

## Overview

- **When to Use** — Use this skill when: - Creating automation skills for file organization, maintenance, or scheduled tasks - Designing skills that modify files or system state (requires safety policies) - Testing skills with dry-run mode and rollback capability before full execution - Installing user-local skills to `~/.hermes/skills/` - Scheduling skills as cron jobs for automated execution - Integrating safety policies into existing skills
- **Workflow Overview** — ---
- **Phase 0: Quick Capture with /learn (v0.18.0+)** — Before going through the full design → author → test workflow, consider whether `/learn` is sufficient:

## Further detail

### Overview

One or two paragraphs: what and why.

### When to Use

- Bulleted triggers - "Don't use for:" counter-triggers

### Process

Numbered steps or phases.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/hermes-skill-development-workflow/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
