---
date: 2026-07-19
type: concept
title: Agent Folder Structure
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/agent-folder-structure
description: Optimize project folders for AI agent navigation speed. INDEX.md maps
  at folder roots, one-concern-per-folder, numbered names for reading order, symlinked
  external deps, and a project-local activity log. Cuts retrieval time 2-10x with
  no model change.
---

# Agent Folder Structure

> Optimize project folders for AI agent navigation speed. INDEX.md maps at folder roots, one-concern-per-folder, numbered names for reading order, symlinked external deps, and a project-local activity log. Cuts retrieval time 2-10x with no model change.

## Overview

- **When to Use** — - An agent regularly takes >30s or opens >3 wrong files to find something in a project - A workspace grew organically (content-type folders) and the agent gets lost - Starting a new multi-session project where the agent needs fast, reliable context retrieval - User says: "the agent keeps opening the wrong file" or "why does it take so long to find X?"
- **The Problem** — Humans organize folders by **content type** (articles/, research/, assets/). The brain cross-references automatically. Agents can't — they search from scratch every time, with no map of what's current vs. archived, or which file is the starting point. They burn capability on *navigation* instead of the actual task.
- **Agent Discipline: Tool Usage & Communication** — Within a well-structured project, agents should minimize tool calls and leverage the built-in maps and logs. When information gathering is necessary:

## Further detail

### Folder Map

| Folder | Purpose | Updated | |---|---|---| | `01.Core/` | Main working files | 2026-07-02 | | `02.Research/` | Source material, analysis | 2026-07-01 | | `03.Scripts/` | Automation, data pipeline | 2026-06-28 | | `04.Archive/` | Completed/superseded — do not use unless asked |

### Canonical Files

| File | Purpose | |---|---| | `01.Core/01. Current Plan.md` | The active plan — start here | | `02.Research/01. Key Findings.md` | Synthesized research |

### Where To Go

- **New session?** → `01.Core/01. Current Plan.md` - **Need data?** → `03.Scripts/01. Data Pipeline.md` - **Historical context?** → `04.Archive/` (only if explicitly asked) - **Writing/blogging?** → `10.Blog/`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/agent-folder-structure/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
