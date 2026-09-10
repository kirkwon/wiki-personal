---
date: 2026-07-19
type: concept
title: Agents Guideline
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge-management
sources:
- hermes://skill/agents-guideline
description: Guideline for writing and using AGENTS.md as a linear run book for Hermes
  agents.
---

# Agents Guideline

> Guideline for writing and using AGENTS.md as a linear run book for Hermes agents.

## Overview

- **Purpose** — AGENTS.md is a linear, non-static run book followed at session start and updated as the project evolves. It should be read top-to-bottom at the beginning of each main session and treated as a procedural checklist, not a reference document.
- **Core Principles (from observed AGENTS.md patterns)** — - Linear: read top-to-bottom, each step assumes prior steps done - Action-oriented: commands, checks, decisions, not just reference - Session-start ritual: review AGENTS.md first in every main session - Evolving: after meaningful work, append a line summarizing what was done (e.g., `[agent] added X skill`) - No reference dump: keep procedural, avoid bibliography or config reference - Visuals encouraged: embed charts, diagrams, tables when helpful - Status symbols: use 🟢/🟡/🔴 to indicate completion state - Conciseness: favor leverage-first output; skip low-value explanations unless requested - C
- **Standard Section Structure** — Based on the observed AGENTS.md in clawd/, include these sections:

## Further detail

### Memory System

You wake up fresh each session. These files are your continuity: - **Daily notes:** `memory/YYYY-MM-DD.md` (create `memory/` if needed) — raw logs of what happened - **Long-term:** `MEMORY.md` — your curated memories, like a human's long-term memory

### Safety

- Don't exfiltrate private data. Ever. - Don't run destructive commands without asking. - `trash` > `rm` (recoverable beats gone forever) - When in doubt, ask.

### Response Status Convention

Every response that completes a unit of work must end with a status line: - 🟢 = work is finished - 🟡 = non-routine follow-up remains (name it) - 🔴 = blocked on user input Keep it under 100 chars. Nothing after it.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/agents-guideline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
