---
date: 2026-07-19
type: concept
title: Gbrain Timeline Enrichment
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/gbrain-timeline-enrichment
description: Enrich gbrain entity pages with structured timeline data.
---

# Gbrain Timeline Enrichment

> Enrich gbrain entity pages with structured timeline data.

## Overview

- **When to Use** — - "timeline coverage is low" / gbrain doctor shows `timeline_coverage` WARN - "add timelines to entity pages" - "enrich gbrain with date metadata" - After a `gbrain extract all` run produces 0 timeline entries despite pages having dates in body text
- **Prerequisites** — - `gbrain` CLI installed (`~/.bun/bin/gbrain`) - PostgreSQL `gbrain` database accessible via `psql -d gbrain` - Wiki sources synced: `gbrain sync --source <source> --full` - Entity pages with `type: entity|person|company|book|paper` in frontmatter
- **How to Run** — 1. Scan for candidates: invoke `scripts/scan_candidates.py` through the `terminal` tool — outputs top 50 entity pages sorted by enrichment value. 2. Read top candidates with `read_file` and manually extract dates/events from body text. 3. Add `## Timeline` body sections using `scripts/add_timeline_sections.py`. 4. Sync and extract: `gbrain sync --source <source> --full` then `gbrain extract timeline`. 5. If extract yields 0 entries (idempotent skip), force-insert via `scripts/insert_timelines_sql.py`.

## Further detail

### Procedure

1. **Scan for candidates** — invoke `python3 scripts/scan_candidates.py` through the `terminal` tool. This walks all wiki bases, finds entity-type pages, checks for date patterns (ISO, full month, abbreviated, quarter, year) and event keywords (born, died, founded, published, released, etc.), and outputs a ranked list. Saves JSON to `/tmp/timeline_candidates.json`.

### Pitfalls

- **Frontmatter `dates:` field does NOT work** — gbrain's timeline extractor reads body text lines, not YAML frontmatter. The regex `TIMELINE_LINE_RE` at `link-extraction.ts:1105` scans body lines only. Do not waste time adding `dates:` arrays to frontmatter. - **`gbrain extract timeline` is idempotent and skips re-processed pages** — even after `--full` sync re-imports pages, the extract command may report "0 entries created" because it uses a hash/skip mechanism. Bypass with direct SQL insertion. - **CLI `timeline-add` fails on path-prefixed slugs** — wiki-personal slugs are `wiki/entities/r

### Verification

Expected: count increased by the number of entries inserted; the page query returns dated entries with summaries.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/gbrain-timeline-enrichment/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
