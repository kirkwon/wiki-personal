---
date: 2026-07-19
type: concept
title: Image To Wiki Ingestion
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/image-to-wiki-ingestion
description: 'Reusable image-to-wiki ingestion methodology. Extracts structured content
  from images using glm-ocr (sole extraction engine — handles both text and layout
  in one pass) plus Apple Vision for confidence gating, then writes a properly formatted
  wiki concept page with frontmatter, cross-links, and GBrain sync. Delegates the
  actual extraction to the wiki-raw-ingest image_ingest.py script. Trigger when ingesting
  images, infographics, charts, diagrams, screenshots, or document scans into the
  wiki. Key phrases: "ingest image to wiki", "image ingestion", "ocr to wiki", "extract
  image content", "vision to markdown".'
---

# Image To Wiki Ingestion

> Reusable image-to-wiki ingestion methodology. Extracts structured content from images using glm-ocr (sole extraction engine — handles both text and layout in one pass) plus Apple Vision for confidence gating, then writes a properly formatted wiki concept page with frontmatter, cross-links, and GBrain sync. Delegates the actual extraction to the wiki-raw-ingest image_ingest.py script. Trigger when ingesting images, infographics, charts, diagrams, screenshots, or document scans into the wiki. Key phrases: "ingest image to wiki", "image ingestion", "ocr to wiki", "extract image content", "vision to markdown".

## Overview

- **The Core Problem** — Images contain: 1. **Text content** (words, numbers, code) 2. **Spatial structure** (layout, hierarchy, relationships)
- **When to Use This Skill** — - A user sends an image and asks to ingest it to the wiki - Infographics, charts, diagrams, dense visual content - Document scans or screenshots with embedded text - Any image where both text and layout matter
- **Confidence Gate (Proof Gate)** — OCR confidence determines the ingestion gate — this mirrors the PM Loop's Improve / Accept / Escalate proof gate from the very infographic that inspired this pipeline:

## Further detail

### Why glm-ocr (Simplified 2026-07-05)

Original design was a dual-path pipeline (Apple Vision OCR + Ollama VLM with a 3-model fallback chain). Benchmarking collapsed it:

### Output Structure

Each ingested image produces a wiki page at `~/wiki-personal/concepts/<slug>.md`:

### Integration with Agentic Loops

This pipeline implements 5 modifications derived from benchmarking:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/image-to-wiki-ingestion/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
