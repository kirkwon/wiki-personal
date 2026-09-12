---
date: 2026-07-19
type: concept
title: Llm Wiki
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- wiki
- knowledge-base
- research
- notes
- markdown
- rag-alternative
sources:
- hermes://skill/llm-wiki
description: 'Karpathy''s LLM Wiki: build/query interlinked markdown KB.'
---

# Llm Wiki

> Karpathy's LLM Wiki: build/query interlinked markdown KB.

## Overview

- **When This Skill Activates** — Use this skill when the user: - Asks to create, build, or start a wiki or knowledge base - Asks to ingest, add, or process a source into their wiki - Asks a question and an existing wiki is present at the configured path - Asks to lint, audit, or health-check their wiki - References their wiki, knowledge base, or "notes" in a research context
- **Wiki Location** — **Location:** Set via `WIKI_PATH` environment variable (e.g. in `~/.hermes/.env`).
- **Architecture: Three Layers** — **Layer 1 — Raw Sources:** Immutable. The agent reads but never modifies these. **Layer 2 — The Wiki:** Agent-owned markdown files. Created, updated, and cross-referenced by the agent. **Layer 3 — The Schema:** `SCHEMA.md` defines structure, conventions, and tag taxonomy.

## Further detail

### Resuming an Existing Wiki (CRITICAL — do this every session)

When the user has an existing wiki, **always orient yourself before doing anything**:

### Initializing a New Wiki

When the user asks to create or start a wiki:

### Domain

[What this wiki covers — e.g., "AI/ML research", "personal health", "startup intelligence"]

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/llm-wiki/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[mlx-local-models]]
