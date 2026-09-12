------

# Notebooklm Cli

> Full command reference and workflow guide for Google NotebookLM via the 'nlm' CLI. Covers authentication, notebook/source management, deep research, querying, and multi-modal content generation (audio, reports, infographics, video, mind maps, slides, quizzes, flashcards, data tables).

## Overview

- **Fleet Cataloging (Multi-Notebook Inventory)** — The commands above cover single-notebook operations. For inventorying an **entire fleet** — all notebooks with source counts, domain classification, verification, and privacy-conscious documentation — see `references/fleet-cataloging-workflow.md`. It includes the batch enumeration script (one `python3 << 'EOF'` heredoc in terminal, NOT execute_code), the three-system stack routing table (NotebookLM → gbrain → wiki), and the privacy rules for publishing a methodology blog without leaking source content or personal metadata.
- **Authentication (ALWAYS DO THIS FIRST)** — Sessions last 24-48 hours (Google Session ID expiry). Before ANY operation, verify auth:
- **Notebook Management** — **Pitfall:** Do NOT use `nlm chat start` — it opens an interactive REPL that agents cannot control. Use `nlm notebook query` for one-shot Q&A.

## Further detail

### Alias System

Create memorable names for UUIDs to simplify all subsequent commands:

### Source Management

**IMPORTANT: You CANNOT add local files by path.** The CLI does NOT support:

### Bulk Source Cleanup Workflow

When managing multiple notebooks with many sources, duplicates and misplaced sources can accumulate. Use this systematic cleanup approach.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/notebooklm-cli/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[notebooklm-research-pipeline]]

[[notebooklm-downloader]]
