---
type: concept
title: Codex History Ingest
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Codex History Ingest

> Ingest Codex CLI conversation history into the Obsidian wiki. Use this skill when the user wants to mine their past Codex sessions for knowledge, import their ~/.codex folder, extract insights from previous coding sessions, or says things like "process my Codex history", "add my Codex conversations to the wiki", or "what have I discussed in Codex before". Also triggers when the user mentions .codex sessions, rollout files, session_index.jsonl, or Codex transcript logs.

## Overview

- **Before You Start** — 1. **Resolve config** — follow the Config Resolution Protocol in `llm-wiki/SKILL.md` (walk up CWD for `.env` → `~/.obsidian-wiki/config` → prompt setup). This gives `OBSIDIAN_VAULT_PATH` and `CODEX_HISTORY_PATH` (defaults to `~/.codex`) 2. Read `.manifest.json` at the vault root to check what has already been ingested 3. Read `index.md` at the vault root to understand what the wiki already contains
- **Codex Data Layout** — Codex stores local artifacts under `~/.codex/`.
- **Step 1: Survey and Compute Delta** — Scan `CODEX_HISTORY_PATH` and compare against `.manifest.json`:

## Further detail

### Step 2: Parse Session Index First

`session_index.jsonl` typically has entries like:

### Step 3: Parse Rollout JSONL Safely

Each `rollout-*.jsonl` line is an event envelope with:

### Step 4: Cluster by Topic

Do not create one wiki page per session.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/codex-history-ingest/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[conversation-logging-review]]
