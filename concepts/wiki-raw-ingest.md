---
date: 2026-07-19
type: concept
title: Wiki Raw Ingest
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/wiki-raw-ingest
description: 'Ingest raw content into the wiki-personal vault — process markdown files,
  web articles, papers, images, and other sources into properly formatted wiki concepts.
  Handles frontmatter generation, cross-linking, tag assignment, and GBrain sync.
  Batch-process directories of raw markdown. Dual-path image ingestion: Apple Vision
  OCR + Ollama VLM hybrid. Trigger on phrases like "ingest to wiki", "raw ingest",
  "import content", "batch import", "wiki ingestion", "add to vault", "ingest image
  to wiki".'
---

# Wiki Raw Ingest

> Ingest raw content into the wiki-personal vault — process markdown files, web articles, papers, images, and other sources into properly formatted wiki concepts. Handles frontmatter generation, cross-linking, tag assignment, and GBrain sync. Batch-process directories of raw markdown. Dual-path image ingestion: Apple Vision OCR + Ollama VLM hybrid. Trigger on phrases like "ingest to wiki", "raw ingest", "import content", "batch import", "wiki ingestion", "add to vault", "ingest image to wiki".

## Overview

- **Ingestion Pipeline** — 1. **Validate** — Check file exists and has content 2. **Clean** — Strip frontmatter, clean markdown, remove boilerplate 3. **Categorize** — Assign domain and type tags 4. **Cross-link** — Add [[wiki-links]] to related concepts 5. **Write** — Save to `~/wiki-personal/concepts/<slug>.md` 6. **Sync** — `gbrain sync wiki-personal` for GBrain indexing
- **Best Practices** — - Remove duplicate content before importing - Add at least 3 cross-links per concept - Tag with domain + type - Verify with `cli.py stats` after import
- **Image Ingestion (Single-Engine Pipeline)** — Images contain text *and* spatial structure. The pipeline uses two tools, but each has a distinct role — no fallback chain:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/wiki-raw-ingest/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
