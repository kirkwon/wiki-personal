---
date: 2026-07-19
type: concept
title: Notebooklm Research Pipeline
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/notebooklm-research-pipeline
description: End-to-end research pipeline using nlm CLI -- create a NotebookLM notebook,
  run deep/fast research, import sources, query for synthesis, and generate multi-modal
  outputs (infographic, audio, report).
---

# Notebooklm Research Pipeline

> End-to-end research pipeline using nlm CLI -- create a NotebookLM notebook, run deep/fast research, import sources, query for synthesis, and generate multi-modal outputs (infographic, audio, report).

## Overview

- **Prerequisites** — - `nlm` CLI installed and authenticated - Run `nlm auth status` to verify. If expired, run `nlm login` (opens Chrome, ~10s) - **Auth check in scripts:** `AUTH_STATUS=$(nlm auth status 2>&1); if ! echo "$AUTH_STATUS" | grep -qi "Authenticated"; then nlm login; fi` - **Always add `|| true` to nlm pipe commands** when using `set -euo pipefail` — `nlm alias get` and `nlm notebook list` can fail gracefully
- **Run DIAGNOSTICS (see below) immediately after any create command.** — nlm mindmap create my-research --confirm
- **⚠️ DIAGNOSTICS — Verify Artifacts Actually Created** — **This is the critical step the pipeline was missing.** The CLI `create` commands can silently fail — they return a success exit code even when the server rejects or ignores the request. Always verify:

## Further detail

### Pitfalls

- **Session expires ~20 min**: If any command returns "Cookies have expired" or "authentication may have expired", run `nlm login` - **`source add` has no `--confirm`**: Only generation and delete commands accept it. - **Deep research can return empty**: If `research status` shows `no_research` with `Sources found: 0`, deep mode failed silently. Do NOT re-poll or `--force` the same dead task. Instead, start a **new** research task with `--mode fast --force`. Fast mode almost always succeeds when deep mode fails — it returns ~10 sources in 30 seconds vs deep's 40-80 in 5 minutes. Example: `nlm

### Command Quick Reference

| Command | Key Flags | |---------|-----------| | `nlm notebook create` | "Title" | | `nlm notebook query` | "question", --conversation-id, --source-ids | | `nlm source add` | --url, --text, --title, --drive | | `nlm research start` | "query", --notebook-id (required), --mode fast/deep, --force | | `nlm research status` | --task-id, --max-wait | | `nlm research import` | notebook-id task-id, --indices | | `nlm audio create` | --format deep_dive/brief/critique/debate, --length short/default/long, --confirm | | `nlm report create` | --format "Briefing Doc"/"Study Guide"/"Blog Post"/"Create Your

### Bulk Ingest Existing Markdown Directory into a Notebook

**When to use:** You have a directory of `.md` research docs (e.g. `08.Research-Docs/`) and want them in a NotebookLM notebook as sources — not creating a new notebook from scratch, not running deep research, just getting existing documents into NLM for synthesis.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/notebooklm-research-pipeline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
