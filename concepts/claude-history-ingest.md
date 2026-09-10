---
date: 2026-08-02
type: concept
title: Claude History Ingest
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/claude-history-ingest
description: Ingest Claude Code conversation history into the Obsidian wiki. Use this
  skill when the user wants to mine their past Claude conversations for knowledge,
  import their ~/.claude folder, extract insights from previous coding sessions, or
  says things like "process my Claude history", "add my conversations to the wiki",
  "what have I discussed with Claude before". Also triggers when the user mentions
  their .claude folder, Claude projects, session data, past conversation logs, local-agent-mode
  sessions, or audit logs.
---

# Claude History Ingest

> Ingest Claude Code conversation history into the Obsidian wiki. Use this skill when the user wants to mine their past Claude conversations for knowledge, import their ~/.claude folder, extract insights from previous coding sessions, or says things like "process my Claude history", "add my conversations to the wiki", "what have I discussed with Claude before". Also triggers when the user mentions their .claude folder, Claude projects, session data, past conversation logs, local-agent-mode sessions, or audit logs.

## Overview

- **Before You Start** — 1. **Resolve config** — follow the Config Resolution Protocol in `llm-wiki/SKILL.md` (walk up CWD for `.env` → `~/.obsidian-wiki/config` → prompt setup). This gives `OBSIDIAN_VAULT_PATH` and `CLAUDE_HISTORY_PATH` (defaults to `~/.claude`) 2. Read `.manifest.json` at the vault root to check what's already been ingested 3. Read `index.md` at the vault root to know what the wiki already contains 4. **Project Scoping** — read `WIKI_SKIP_PROJECTS` from config (comma-separated substrings). Exclude any project directory whose name contains one of them from **every** step below (scan, delta, sampling,
- **Claude Code Data Layout** — Claude Code stores data in two locations. Scan **both**.
- **Step 1: Survey and Compute Delta** — Scan both data locations and compare against `.manifest.json`:

## Further detail

### Step 2: Ingest Memory Files First

Memory files are already structured with YAML frontmatter:

### Step 3: Parse Conversation JSONL

**Always check for a pre-extracted file first** (see Pre-extraction section above).  For each conversation `~/.claude/projects/<proj>/<uuid>.jsonl`, look for its counterpart at `~/.claude/extracted/<proj>/<uuid>.json`.  If found, read that instead — it is already filtered to user + assistant text turns and costs 50–200× fewer tokens than the raw JSONL.

### Step 3b: Parse Audit Logs (desktop sessions only)

For each `audit.jsonl` found under `local-agent-mode-sessions/`, read it line by line. Each line is a JSON record of one agent action:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/claude-history-ingest/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
