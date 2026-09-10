---
date: 2026-08-02
type: concept
title: Context Reduction Architecture
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/context-reduction-architecture
description: Use when designing agent systems or auditing context bloat.
---

# Context Reduction Architecture

> Use when designing agent systems or auditing context bloat.

## Overview

- **The Problem** — One monolithic prompt eats 100% of context every turn. Every procedure, role, and instruction sits in the system prompt regardless of whether it's needed. Token costs scale linearly with prompt size, not with work done.
- **Layer 4 — GraphWork (Hermes extension)** — **File:** GRAPH.md — DAG topology as state summary **Purpose:** Cross-session continuity without re-reading chat history.
- **Audit Checklist (When Context Is Too High)** — 1. **Is the law file >3K tokens?** Move job-specific procedures to skills. 2. **Are you pasting prompts?** Convert to a skill with trigger description. 3. **Are you doing heavy work inline?** Delegate to a subagent. 4. **Is cross-session state in chat history?** Move to GRAPH.md. 5. **Are procedures in memory?** Move to skills. Memory is for facts, not procedures. 6. **Are there unused skills loaded?** Check description triggers aren't too broad.

## Further detail

### Decision Framework

| Situation | Layer | Action | |-----------|-------|--------| | Universal rule | Law (AGENTS.md) | Keep it here, pay every turn | | Repeatable procedure | Skill | Create SKILL.md, lazy-loaded | | Heavy work (>5K tokens) | Subagent | delegate_task, summary return | | Multi-session project state | GraphWork | GRAPH.md topology | | Stable facts/preferences | Memory | Compact declarative entries | | One-off task | None | Just do it inline |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/development-patterns/context-reduction-architecture/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
