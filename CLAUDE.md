# CLAUDE.md — Wiki Pipeline Guide

> For any AI agent processing content in this wiki.
> Generic: any agent should be able to digest raw sources into wiki entries.

## Structure

```
wiki-personal/
├── CLAUDE.md          ← This file (agent instructions)
├── purpose.md         ← Wiki purpose & scope
├── schema.md          ← Frontmatter schema reference
├── log.md             ← Change log
├── raw/               ← Source materials (unprocessed)
│   ├── books/         ─ Book notes and summaries
│   ├── papers/        ─ Academic papers
│   ├── sources/       ─ Articles, videos, transcripts
│   └── ingested/      ─ Already processed (archived)
├── wiki/              ← Curated knowledge
│   ├── concepts/      ─ Abstract ideas, frameworks, mental models
│   ├── entities/      ─ People, places, things, organizations
│   ├── sources/       ─ Curated source pages
│   └── queries/       ─ Saved gbrain queries
└── .obsidian/         ─ Obsidian vault config
```

## Raw → Wiki Pipeline

When ingesting raw content into the wiki, follow these rules:

### 1. Frontmatter Requirements
Every wiki page MUST have frontmatter:
```yaml
---
type: concept|entity|source|note
title: Human-Readable Title
created: YYYY-MM-DD        # Date the page was created
updated: YYYY-MM-DD        # Date last modified
tags: [tag1, tag2]
sources: []                # Optional: links to source material
---
```

### 2. Timestamp Every New Entry
- `created:` MUST be set to the date of creation (not date of raw source)
- `updated:` MUST be updated whenever content changes
- Use format: `YYYY-MM-DD` (ISO 8601 date only)

### 3. Entity Pages
- Go in `wiki/entities/<slug>.md`
- Slug: lowercase, hyphens for spaces (e.g., `andrej-karpathy.md`)
- Must include `created:` and `type: entity` in frontmatter

### 4. Concept Pages
- Go in `wiki/concepts/<slug>.md`
- Link to related entities with `[[entity-slug]]` wikilinks
- Must include `created:` and `type: concept` in frontmatter

### 5. Source Pages
- Go in `wiki/sources/<slug>.md`
- Include original URL or reference
- Tag with domain areas

### 6. gbrain Timeline Integration
After creating/updating any entity or concept page, add a gbrain timeline entry:
```bash
gbrain timeline-add wiki-personal/<type>/<slug> <created-date> "Summary of event"
```
This ensures gbrain timeline coverage stays high.

## Sync to gbrain
After changes, sync the wiki-personal source:
```bash
gbrain sync --source wiki-personal
```

## Schema Reference
See `schema.md` for complete frontmatter schema documentation.
