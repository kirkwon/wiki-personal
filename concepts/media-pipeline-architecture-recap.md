---
type: concept
title: Media Pipeline Architecture Recap
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Media Pipeline Architecture Recap
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- pipeline
- architecture
- media
- books
- videos
- gbrain
- llm-wiki
- notebooklm
- marp
- infographics
- knowledge
sources:
- hermes://skill/media-pipeline-architecture-recap
description: 'Architectural and process changes to media pipelines: 8 ingestion pipelines
  feeding GBrain (24,041 pages, 94,651 links). Books → unified_books → GBrain → LLM-wiki
  → NotebookLM → MARP. YouTube (698), email triage with Q01-Q06 signal routing, academic
  papers (239), session backfill, and Symphony Kanban dispatch. Plus: inbox self-tuning
  triage, nightly dream cycle (2K links/night), 5 NotebookLM auto-syncs, 28 cron jobs
  (89% no_agent). Multi-format documentation: SVG architecture diagram, Mermaid diagrams,
  HTML dashboard.'
---

# Media Pipeline Architecture Recap

> Architectural and process changes to media pipelines: 8 ingestion pipelines feeding GBrain (24,041 pages, 94,651 links). Books → unified_books → GBrain → LLM-wiki → NotebookLM → MARP. YouTube (698), email triage with Q01-Q06 signal routing, academic papers (239), session backfill, and Symphony Kanban dispatch. Plus: inbox self-tuning triage, nightly dream cycle (2K links/night), 5 NotebookLM auto-syncs, 28 cron jobs (89% no_agent). Multi-format documentation: SVG architecture diagram, Mermaid diagrams, HTML dashboard.

## Overview

- **Executive Summary** — This week saw major architectural hardening across 5 media pipelines. Key changes: - **Book reconciliation** — 107/107 books matched via synthetic ISBN (SHA-256 hash) - **YouTube batch** — 640/641 videos processed with real transcripts + LLM summaries - **Cron optimization** — 4 agent→no_agent conversions (89% token reduction) - **Skills dashboard** — Interactive HTML dashboard created from unified book data - **Infographic pipeline** — Full visual documentation suite generated - **LLM-wiki sync** — GBrain delta sync every 15min via no_agent script
- **Architecture Diagram** — ---
- **June 2026 Updates (v2.0.0)** — Since the May 2026 recap, the architecture has evolved significantly:

## Further detail

### System Health (June 17, 2026)

| Component | Count | Status | Details | |-----------|-------|--------|---------| | GBrain pages | 24,041 | ✅ 100% embedded | Postgres, text-embedding-3-large | | GBrain chunks | 38,358 | ✅ 100% | | | GBrain links | 94,651 | ✅ 1,258 tags | 4.9 links/page avg | | Books unified | 107 | ✅ 100% skill coverage | 11 balanced categories | | YouTube real content | 698 | ✅ 98.2% PASS quality | Title validation active | | Academic papers | 239 | ✅ In GBrain | Linked citations | | LLM wiki pages | 488+ | ✅ Synced every 3h | Delta sync script | | NotebookLM notebooks | 41 | ✅ 5 auto-synced | Daily/weekly

### Key Lessons (June 2026)

1. **Phase-based processing** — extract → summarize → import beats monolithic scripts for large batches 2. **Signal routing** — routing incoming data to permanent questions (Q01-Q06) creates a queryable knowledge layer 3. **Self-tuning reduces noise** — domain weight decay based on engagement keeps the signal-to-noise ratio high 4. **Nightly dreams scale the graph** — automated link discovery grows connections 5x faster than manual 5. **NotebookLM syncs need monitoring** — 2/5 notebooks errored (Cooking Science, Jazz Theory) — needs investigation 6. **Cron hygiene** — 89% no_agent ratio keeps

### Related Skills

| Skill | Purpose | |-------|---------| | `unified-book-library-management` | Book processing + book-processor.py CLI | | `youtube-video-ingestion` | YouTube transcript + LLM pipeline | | `gbrain-to-notebooklm` | Selective GBrain → NotebookLM migration | | `llm-wiki` | Karpathy-style wiki with GBrain sync | | `marptalk` | MARP presentations + TTS video | | `book-skills-dashboard` | HTML dashboard generator | | `query-escalation-pipeline` | 3-tier research escalation | | `notebooklm-cli` | Full nlm CLI reference | | `baoyu-infographic` | 21×21 infographic generator | | `gbrain-operations` | GBr

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/media-pipeline-architecture-recap/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
