---
type: note
title: Personal Knowledge Ecosystem — System Overview
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
--

# Personal Knowledge Ecosystem — System Overview

## What We've Built

### Core Components
1. **Wiki-based Second Brain**: 3,048+ markdown files across 6 knowledge domains
2. **Automated Knowledge Ingestion Pipeline**: 
   - Sources: Evernote, Pinterest, Obsidian exports (historical)
   - Ongoing: Apple Notes, wiki updates
   - Staging: ~/data-ingestion/ with format unification
   - Processing: detect changes → convert → optional wisdom extract → index → record hash
   - Import: gbrain import --no-embed (using redirect `<`)
   - Embedding: gbrain embed --stale (background vectors)
3. **GBrain Knowledge Graph**: Semantic storage with vector embeddings
4. **Search & Access Layer**: 
   - knowledge-connect (unified 4-system search)
   - gbrain search (semantic vector search)
   - NotebookLM integration (research & synthesis)
   - Direct wiki browser
5. **Automation & Monitoring**:
   - 12 scheduled cron jobs (various schedules)
   - 3 custom CLI tools: knowledge-connect, book-pipeline, gbrain-notebooklm-bridge
   - Per-stage logging & alerting
   - Weekly maintenance: defrag, log compression, backups
   - Health monitoring: gbrain doctor --json (current score: 75/100)

### Knowledge Domains (6)
- Cooking & Gastronomy (wok techniques, recipes)
- Photography (equipment, techniques, processing)
- Personal Finance (investing, accounting, strategy)
- Decision Science (biases, game theory, frameworks)
- Jazz/Music Theory (harmony, bebop, improvisation)
- Botany & Urban Ecology (plant species, gardening, ecology)

### Scale Metrics (Verbatim)
- 3,048+ total markdown files in wiki
- 1,794 concept pages
- 352 entity pages
- 410 source documents (historical imports)
- ~764 YouTube Watch Later videos
- 108 book summary text files
- 515-line wiki index
- 1,251-line activity log
- 4 knowledge pipelines (Books, Videos, GBrain Export, NotebookLM Sync)
- 12 scheduled cron jobs
- 3 active CLI tools
- GBrain health score: 75/100 (needs vector extension)

### Technical Infrastructure
- macOS (26.1) host environment
- Hermes Agent as primary AI assistant
- GBrain (PGLite + vector) as knowledge graph
- NotebookLM for research synthesis
- Python/bash scripts for automation
- Cron for scheduling (15min → weekly intervals)
- Extract-wisdom skill (Ollama phi3, ~0.5-1s/file)
- Unify-document-formats for format normalization