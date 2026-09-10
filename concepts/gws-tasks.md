---
date: 2026-07-19
type: concept
title: Gws Tasks
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gws
- google-workspace
- tasks
- task-management
- cli
- communication
sources:
- hermes://skill/gws-tasks
description: Manage Google Tasks using the Google Workspace CLI (gws) for task and
  tasklist operations.
---

# Gws Tasks

> Manage Google Tasks using the Google Workspace CLI (gws) for task and tasklist operations.

## Overview

- **When to Use This Skill** — - You need to list or manage your Google Task lists - You want to view, add, or modify tasks in specific lists - You're setting up automation for task management - You prefer CLI over web UI for task operations
- **Prerequisites** — - Google Workspace CLI (`gws`) installed and in PATH - Valid Google OAuth credentials configured (run `gws auth status` to verify) - The `tasks` and `tasklists` services must be enabled in your OAuth scopes - Required scopes: `https://www.googleapis.com/auth/tasks` - Check with: `gws auth status`
- **Core Concepts** — The GWS CLI follows this pattern:

## Further detail

### Workflow: Getting Your Tasks

1. **Verify GWS access and scopes** (run this first — most failures are auth):

### Example Cron Job: Daily Task Digest

Make it executable and schedule it (Hermes cron preferred over crontab).

### Integration with Knowledge Workflow

To save tasks to your knowledge base (GBrain/Obsidian):

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/communication/gws-task-management/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
