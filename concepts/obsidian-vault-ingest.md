---
date: 2026-07-19
type: concept
title: Obsidian Vault Ingest
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- obsidian
- ingestion
- knowledge-base
- migration
- vault
- note-taking
sources:
- hermes://skill/obsidian-vault-ingest
description: Ingest content from an Obsidian vault into an llm-wiki knowledge base,
  preserving structure while enforcing llm-wiki conventions and cross-referencing.
---

# Obsidian Vault Ingest

> Ingest content from an Obsidian vault into an llm-wiki knowledge base, preserving structure while enforcing llm-wiki conventions and cross-referencing.

## Overview

- **When to Use** — - You have an existing Obsidian vault you want to integrate into your llm-wiki - You're migrating from a traditional Obsidian setup to the llm-wiki system - You want to incorporate reference materials, notes, or research from another vault - You're consolidating multiple knowledge sources into a unified llm-wiki
- **How It Works** — 1. **Orientation**: First reads target llm-wiki's SCHEMA.md, index.md, and recent log 2. **Source Analysis**: Scans the source vault for markdown files 3. **Content Processing**: For each file: - Extracts existing frontmatter or creates new - Determines appropriate type (entity/concept/comparison/query) - Validates and maps tags to target SCHEMA taxonomy - Ensures proper wikilinking (≥2 outbound links to target wiki) - Adds provenance tracking to raw source 4. **Integration**: Writes processed content to target wiki - Updates index.md with new entries - Appends detailed action to log.md 5. **R
- **Prerequisites** — - Target llm-wiki must exist and be initialized (run llm-wiki skill first if needed) - Source vault path must be accessible - Python 3.6+ with standard library (no external dependencies)

## Further detail

### Conventions Preserved

From source vault: - Original content depth and detail - Existing internal wikilinks (converted to llm-wiki format if needed) - Heading structure and formatting - Lists, tables, code blocks - Image references (if assets are also ingested)

### Handling Updates (Re-ingestion)

When re-ingesting the same source vault:

### Obsidian-Specific Features Preserved

The skill maintains compatibility with Obsidian:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/note-taking/obsidian-vault-ingest/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
