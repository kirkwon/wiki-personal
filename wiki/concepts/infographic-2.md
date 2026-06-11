---
type: note
title: Infographic Prompt
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
-

# Infographic Prompt

## Layout: bento-grid
# bento-grid

Modular grid layout with varied cell sizes, like a bento box.

## Structure

- Grid of rectangular cells
- Mixed cell sizes (1x1, 2x1, 1x2, 2x2)
- No strict symmetry required
- Hero cell for main point
- Supporting cells around it

## Best For

- Multiple topic overview
- Feature highlights
- Dashboard summaries
- Portfolio displays
- Mixed content types

## Visual Elements

- Clear cell boundaries
- Varied cell backgrounds
- Icons or illustrations per cell
- Consistent padding/margins
- Visual hierarchy through size

## Text Placement

- Main title at top
- Cell titles within each cell
- Brief content per cell
- Minimal text, maximum visual
- CTA or summary in prominent cell

## Recommended Pairings

- `craft-handmade`: Friendly overviews (default)
- `corporate-memphis`: Business summaries
- `pixel-art`: Retro feature grids


## Style: corporate-memphis
# corporate-memphis

Flat vector people with vibrant geometric fills

## Color Palette

- Primary: Bright, saturated - purple, orange, teal, yellow
- Background: White or light pastels
- Accents: Gradient fills, geometric patterns

## Visual Elements

- Flat vector illustration
- Disproportionate human figures
- Abstract body shapes
- Floating geometric elements
- No outlines, solid fills
- Plant and object accents

## Typography

- Clean sans-serif
- Bold headings
- Professional but friendly
- Minimal decoration

## Best For

Business presentations, tech products, marketing materials, corporate training


## Base Template
Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: {{LAYOUT}}
- **Style**: {{STYLE}}
- **Aspect Ratio**: {{ASPECT_RATIO}}
- **Language**: {{LANGUAGE}}

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- If content involves sensitive or copyrighted figures, create stylistically similar alternatives
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use the specified language for all text content

## Layout Guidelines

{{LAYOUT_GUIDELINES}}

## Style Guidelines

{{STYLE_GUIDELINES}}

---

Generate the infographic based on the content below:

{{CONTENT}}

Text labels (in {{LANGUAGE}}):
{{TEXT_LABELS}}


## Structured Content
# Personal Knowledge Ecosystem — Structured Content

## Title
Personal Knowledge Ecosystem: System Overview

## Learning Objectives
1. Understand the scale and structure of the personal knowledge wiki (3,000+ pages across 6 domains)
2. See the automated pipeline architecture that ingests, processes, and syncs knowledge
3. Identify the tooling layer (3 CLI tools, 12 cron jobs) that maintains the ecosystem
4. Understand the integration with external systems for research and synthesis

## Section 1: Knowledge Wiki — The Core

**Key Concept**: A Wikipedia-style personal knowledge base organized into 6 categories

**Content**: 
- 3,048+ total markdown files
- 1,794 concept pages — interconnected ideas and frameworks
- 352 entity pages — people, organizations, tools, and concepts
- 410 source documents — historical imports from Evernote, Pinterest, Obsidian
- ~764 YouTube Watch Later videos
- 108 book summary text files
- 515-line wiki index
- 1,251-line activity log
- Last updated: 2026-04-29

**Visual Element**: Wikipedia-style article preview with title, summary, and metadata

**Text Labels**: "3,048+ Pages" | "1,794 Concepts" | "352 Entities" | "6 Domains"

## Section 2: Knowledge Domains

**Key Concept**: Six specialized areas of knowledge

**Content**: 
- Cooking & Gastronomy: wok techniques, seafood preparation, recipes
- Photography: equipment, shooting techniques, post-processing
- Personal Finance: investing strategies, accounting, wealth building
- Decision Science: cognitive biases, game theory, rational frameworks
- Jazz/Music Theory: bebop harmony, improvisation, modal jazz
- Botany & Urban Ecology: plant species, gardening, ecological systems

**Visual Element**: Six circular badges or icons arranged in a hexagon or grid

**Text Labels**: "Cooking" | "Photography" | "Finance" | "Decision Science" | "Jazz" | "Botany"

## Section 3: Automated Ingestion Pipeline

**Key Concept**: End-to-end pipeline for knowledge acquisition

**Content**: 
- **Sources**: Evernote (historical), Pinterest (historical), Obsidian/Logseq exports (historical), Apple Notes (ongoing)
- **Staging**: ~/data-ingestion/ with format normalization
- **Processing**: 
  1. detect_changes.py — hash-based file change detection
  2. convert_to_unified.py — txt/json/yaml/md → unified YAML format
  3. enrich_with_wisdom.py — optional Ollama phi3 extraction (~0.5-1s/file)
  4. update_index.py — rebuild file manifest with metadata
  5. record_hash.py — store SHA256 hashes for incremental sync
  6. gbrain import --no-embed — load unified files (using redirect `<`)
  7. gbrain embed --stale — background vector embedding generation
- **Destination**: GBrain knowledge graph with semantic search

**Visual Element**: Left-to-right flow diagram with 7 stages and two source columns

**Text Labels**: "Source → Convert → Enrich → Index → Embed → Search"

## Section 4: Search & Access Layer

**Key Concept**: Multiple ways to query and interact with the knowledge base

**Content**: 
- **knowledge-connect**: Unified search across 4 systems (wiki, GBrain, NotebookLM, sources)
- **gbrain search**: Semantic vector search in the knowledge graph
- **NotebookLM**: Research synthesis and audio overviews from GBrain exports
- **Wiki Browser**: Direct markdown navigation and editing
- **CLI Tools**: 
  - knowledge-connect — search and query interface
  - book-pipeline — manage book ingestion workflow
  - gbrain-notebooklm-bridge — sync between GBrain and NotebookLM

**Visual Element**: Four quadrants or tabs with icons for each access method

**Text Labels**: "knowledge-connect" | "gbrain search" | "NotebookLM" | "Wiki Browser"

## Section 5: Automation & Maintenance

**Key Concept**: Scheduled jobs and custom tools that keep the system running

**Content**: 
- **12 Cron Jobs**: 
  - */15 * * * * — Apple Notes sync, pipeline monitoring
  - 0 */6 * * * — AI/ML model updates, embedding refresh
  - 0 2,3,9 * * * — dream synthesis, backup verification, health checks
  - 0 6,9 * * 1 — weekly GBrain doctor, link analysis
  - 0 21 * * 0 — conversation log compression and review
- **Custom CLI Tools** (3):
  - knowledge-connect — unified search
  - book-pipeline — book ingestion management
  - gbrain-notebooklm-bridge — GBrain ↔ NotebookLM synchronization
- **Maintenance Tasks**:
  - Daily 3AM: GBrain export backup
  - Weekly Mon 9AM: Vault defrag (fix broken links)
  - Weekly Sun 9PM: Conversation review and log compression
  - Per-stage logging with alerts on backlogs

**Visual Element**: Cron schedule table or clock-face visualization

**Text Labels**: "12 Cron Jobs" | "3 CLI Tools" | "Daily/Weekly Tasks"

## Section 6: System Health & Metrics

**Key Concept**: Current status and performance indicators

**Content**: 
- GBrain Health Score: 75/100 (needs vector extension for optimal performance)
- Link density: monitoring via gbrain doctor --json
- Brain score: knowledge graph connectivity metric
- Pipeline status: 4 active pipelines (Books, Videos, GBrain Export, NotebookLM Sync)
- Storage: ~2.2GB of markdown and metadata
- Last health check: 2026-05-10

**Visual Element**: Gauge or meter showing health score, plus status indicators

**Text Labels**: "Health: 75/100" | "Link Density: Monitoring" | "Brain Score: Tracking" | "Pipelines: 4 Active"

## Section 7: Technical Infrastructure

**Key Concept**: Underlying technologies and host environment

**Content**: 
- Host: macOS (26.1) on Apple Silicon
- Primary AI: Hermes Agent (openrouter/owl-alpha)
- Knowledge Graph: GBrain (PGLite + pgvector extension)
- Vector Embeddings: Ollama nomic-embed-text (local)
- Automation: Python 3.11+, bash scripts, cron
- File Management: unify-document-formats, extract-wisdom skill
- Backup Strategy: PGLite snapshots, directory exports
- Development: VS Code, git, GitHub (kirkwon/hermes-code repo)

**Visual Element**: Stack diagram or technology radar

**Text Labels**: "macOS 26.1" | "Hermes Agent" | "GBrain + Vector" | "Python/Bash" | "unify-document-formats"

## Aspect Ratio: landscape (16:9)
## Language: en
