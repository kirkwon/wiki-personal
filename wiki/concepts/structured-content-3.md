---
type: note
title: Knowledge Pipeline Architecture — Structured Content
description: "Knowledge Pipeline Architecture — Structured Content"
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
--

# Knowledge Pipeline Architecture — Structured Content

## Title
Knowledge Pipeline Architecture: Automated Data Ingestion

## Learning Objectives
1. Understand the end-to-end pipeline architecture for knowledge ingestion
2. See the classification of data sources as historical vs ongoing
3. Identify the technical components and scripts involved in each stage
4. Understand the scheduling and monitoring mechanisms

## Section 1: Data Sources — Historical vs Ongoing

**Key Concept**: Classification of data sources by update frequency

**Content**: 
- **Historical (one-time)**: Evernote exports, Pinterest exports, Obsidian/Logseq vault exports
- **Ongoing (continuous)**: Apple Notes, wiki kb.md updates

**Visual Element**: Two columns with icons - historical (archive box) and ongoing (clock with circular arrows)

**Text Labels**: "Historical Loads" | "Ongoing Loads"

## Section 2: Directory Structure

**Key Concept**: Organized data ingestion workspace

**Content**: 
```
~/data-ingestion/
├── sources/          # Raw exports (place exports here)
├── staging/          # Unified processed files
│   ├── index.json    # File manifest with metadata
│   └── hashes/       # SHA256 hashes for change detection
├── scripts/          # Processing automation
│   ├── detect_changes.py
│   ├── convert_to_unified.py
│   ├── enrich_with_wisdom.py (optional)
│   └── import_to_gbrain.py
├── logs/             # Execution logs for each stage
└── config.yaml       # Pipeline configuration
```

**Visual Element**: Directory tree diagram with folders and files

**Text Labels**: "sources/" | "staging/" | "scripts/" | "logs/" | "config.yaml"

## Section 3: Pipeline Stages

**Key Concept**: Six-stage ETL pipeline for knowledge ingestion

**Content**: 
1. **detect_changes.py**: Hash-based detection of new/modified files
2. **convert_to_unified.py**: Format normalization (txt/json/yaml/md → unified YAML)
3. **enrich_with_wisdom.py**: Optional wisdom extraction using extract-wisdom skill (Ollama phi3, ~0.5-1s/file)
4. **update_index.py**: Rebuild index.json with file metadata and content hashes
5. **record_hash.py**: Store file hashes for incremental synchronization
6. **gbrain import --no-embed**: Import unified files into GBrain knowledge graph (using redirect `<` not --content)
7. **gbrain embed --stale**: Background vector embedding generation

**Visual Element**: Horizontal flow diagram with 7 connected stages

**Text Labels**: "Detect Changes" | "Convert Formats" | "Extract Wisdom" | "Update Index" | "Record Hash" | "GBrain Import" | "Background Embed"

## Section 4: Schedule & Automation

**Key Concept**: Automated execution via cron jobs

**Content**: 
- **Ongoing loads**: Cron every 15-30 minutes for Apple Notes and wiki updates
- **One-time loads**: Manual execution after placing historical exports in sources/
- **Monitoring**: Per-stage logging with alerts on processing backlogs
- **Health checks**: Periodic `gbrain doctor --json` to monitor link density and brain score

**Visual Element**: Calendar/cron tab visualization with time intervals

**Text Labels**: "*/15 * * * *" | "0 */6 * * *" | "0 2,3,9 * * *" | "Daily 3AM" | "Weekly Mon 9AM"

## Section 5: Technical Notes

**Key Concept**: Important implementation details

**Content**: 
- GBrain put: use redirect `<` NOT `--content` (treats path as string, not file content)
- Orphan linker v9: 60% hit rate for automatic knowledge graph connections
- String split parsing works for link extraction (regex approach failed)
- Dream synthesis phase requires BOTH:
  - `gbrain config set dream.synthesize.enabled true`
  - `gbrain config set dream.synthesize.session_corpus_dir /path/to/corpus`

**Visual Element**: Callout boxes or warning icons with technical details

**Text Labels**: "Redirect `<` not --content" | "Orphan linker: 60% hit rate" | "Dream needs both flags"