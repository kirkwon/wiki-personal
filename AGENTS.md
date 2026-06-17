# Wiki Personal — Vault Configuration

This file overrides obsidian-wiki framework defaults for this vault. Read this before running any wiki-* skill.

## Vault Structure

```
~/wiki-personal/
├── AGENTS.md              ← This file (override config)
├── CLAUDE.md              ← Generic agent instructions (legacy)
├── purpose.md             ← Wiki purpose & scope (read for domain context)
├── schema.md              ← Frontmatter schema & conventions (read before writing)
├── log.md                 ← Change log (every skill must update this)
├── broken_links_report.md ← Lint output
│
├── concepts/              ← Abstract ideas, frameworks, mental models
├── papers/                ← Academic paper notes (not a standard category)
│
├── wiki/                  ← Curated knowledge hub
│   ├── index.md           ← Wiki master index (equivalent to root index.md)
│   ├── log.md             ← Wiki-level changelog
│   ├── concepts/          ← Wiki sub-concepts
│   ├── entities/          ← People, tools, libraries, companies
│   ├── synthesis/         ← Cross-cutting analyses
│   ├── sources/           ← Source origin tracking
│   ├── queries/           ← Saved graph queries
│   └── comparisons/       ← Side-by-side analyses
│
├── questions/             ← Permanent research questions (Q01-Q06)
│   ├── index.md           ← Question index
│   └── syntheses/         ← Cross-question syntheses
│
├── raw/                   ← Unprocessed source materials (equiv to _raw/)
│   ├── books/
│   ├── papers/
│   ├── sources/           ← Articles, videos, transcripts
│   └── ingested/          ← Already processed (archived)
│
├── _archive/              ← Superseded/archived pages
├── .manifest.json         ← Ingest tracking (created by setup)
└── .obsidian/             ← Obsidian app config
```

## Category Overrides

Override the standard obsidian-wiki category paths for this vault:

- **entities/** → `wiki/entities/` (nested under wiki/)
- **synthesis/** → `wiki/synthesis/` (nested under wiki/)
- **sources/** → `wiki/sources/` (nested under wiki/)
- **_raw/** → `raw/` (different name, same purpose)
- **index.md** → `wiki/index.md` (master index is nested)
- **log.md** → `wiki/log.md` (wiki-level changelog, in addition to root log.md)
- **skills/** → not created yet; create on demand via wiki-ingest
- **references/** → not created yet; create on demand via wiki-ingest
- **journal/** → not created yet; create on demand via wiki-ingest
- **_archive/** → `_archive/` at root

The root `concepts/` dir is the canonical location. `wiki/concepts/` is a sub-hierarchy for wiki-internal organization — prefer root `concepts/` for new concept pages unless they're tightly scoped to wiki content.

## Frontmatter Convention

From `schema.md`, every page uses:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | note
tags: [tag1, tag2]
sources: [raw/articles/source-name.md]
# Optional:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

**Provenance markers:** On synthesis pages, append `^[raw/articles/source-file.md]` at the end of paragraphs whose claims come from a specific source.

## Domain Context

Primary domains: cooking & gastronomy, photography, personal finance, general knowledge & second brain (mental models, cognitive biases, productivity).

## Conventions

- Filenames: lowercase, hyphens, no spaces
- Use `[[wikilinks]]` for cross-references (minimum 2 outbound links per page)
- Bump `updated` date on every edit
- Every new page must be added to `wiki/index.md`
- Every action must be appended to `log.md`
- Create a page when an entity/concept appears in 2+ sources or is central to one
- Split pages at ~200 lines
- Tag taxonomy must be followed (see `schema.md` for full list)
