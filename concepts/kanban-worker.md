---
type: concept
title: Kanban Worker
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Kanban Worker
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- kanban
- multi-agent
- collaboration
- workflow
- pitfalls
- devops
sources:
- hermes://skill/kanban-worker
description: Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle
  itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from
  agent/prompt_builder.py); this skill is what you load when you want deeper detail
  on specific scenarios.
---

# Kanban Worker

> Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from agent/prompt_builder.py); this skill is what you load when you want deeper detail on specific scenarios.

## Overview

- **Workspace handling** — Your workspace kind determines how you should behave inside `$HERMES_KANBAN_WORKSPACE`:
- **Tenant isolation** — If `$HERMES_TENANT` is set, the task belongs to a tenant namespace. When reading or writing persistent memory, prefix memory entries with the tenant so context doesn't leak across tenants:
- **Good summary + metadata shapes** — The `kanban_complete(summary=..., metadata=...)` handoff is how downstream workers read what you did. Patterns that work:

## Further detail

### Claiming cards you actually created

If your run produced new kanban tasks (via `kanban_create`), pass the ids in `created_cards` on `kanban_complete`. The kernel verifies each id exists and was created by your profile; any phantom id blocks the completion with an error listing what went wrong, and the rejected attempt is permanently recorded on the task's event log. **Only list ids you captured from a successful `kanban_create` return value — never invent ids from prose, never paste ids from earlier runs, never claim cards another worker created.**

### Block reasons that get answered fast

Bad: `"stuck"` — the human has no context.

### Blocked Task Diagnostics (for orchestrators / humans debugging)

When a task shows `blocked` status, you need to determine WHY before you can unblock it.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/kanban-worker/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
