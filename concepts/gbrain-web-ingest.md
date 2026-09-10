---
date: 2026-08-02
type: concept
title: Gbrain Web Ingest
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/gbrain-web-ingest
description: Safely load web pages into GBrain avoiding pitfalls.
---

# Gbrain Web Ingest

> Safely load web pages into GBrain avoiding pitfalls.

## Overview

- **Why This Matters** — - Using `gbrain put --content /dev/stdin < file` stores the literal string '"/dev/stdin"' as the note body – a common mistake. - `gbrain import` on a single file requires a directory; it also strips the top‑level directory from the slug. - Web pages often need cleaning (scripts, ads) before storage; raw HTML is noisy.
- **Recommended Workflow** — 1. **Fetch clean markdown** Use `web_extract` (fast, no LLM summarization) or the Jina Reader via `curl -s https://r.jina.ai/<URL>` for a markdown‑ified version.
- **Pitfalls & How to Avoid Them** — | Pitfall | Symptom | Fix | |---------|---------|-----| | Using `--content /dev/stdin` | Body becomes the literal string '"/dev/stdin"' | Use heredoc or pipe without `--content` (e.g., `cat file | gbrain put slug`). | | `gbrain import` on a single file | "Found 0 markdown files" error | Either wrap the file in a directory (`mkdir -p /tmp/brain && cp file /tmp/brain/ && gbrain import /tmp/brain/`) or use `gbrain put` directly. | | Slug mismatch after import | `gbrain get` returns page_not_found even though `gbrain list` shows it | `gbrain import` strips the top‑level directory from the slug. Us

## Further detail

### Integration with Other Skills

- Pair with the **agent-reach** skill when you need to fetch content from social platforms that require login (use the appropriate backend from `agent-reach doctor --json`). - Use the **gbrain-content-ops** skill for general GBrain put/get patterns and for troubleshooting slug mismatches. - If you need to ingest many URLs in batch, consider a small loop in `execute_code` that calls `web_extract` for each URL and runs the heredoc put pattern.

### References

- See `gbrain-content-ops` skill for deep details on GBrain put/get, import behavior, and slug handling. - The `agent-reach` skill’s `references/web.md` describes the Jina Reader method (`https://r.jina.ai/URL`).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/gbrain-web-ingest/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
