---
date: 2026-07-19
type: concept
title: Gbrain Graph Enrichment
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gbrain
sources:
- hermes://skill/gbrain-graph-enrichment
description: 'Systematic GBrain knowledge graph enrichment and maintenance. Covers
  timeline

  population, bulk entity linking (books→authors, papers→citations),

  backlink verification, health checks, and export/sync workflows.'
---

# Gbrain Graph Enrichment

> Systematic GBrain knowledge graph enrichment and maintenance. Covers timeline
population, bulk entity linking (books→authors, papers→citations),
backlink verification, health checks, and export/sync workflows.

## Overview

- **Contract** — This skill guarantees: - Timeline entries are added to capture temporal relationships (70 → 100+ entries) - Entity links are created systematically (books→authors, papers→citations) - Graph integrity is maintained (backlink verification, dead link checks) - Health is assessed (gbrain doctor, filing rules, resolver checks) - Export/sync workflows are documented and repeatable
- **When To Use** — - User wants to "populate timeline" or "add timeline events" - Books have `author:` fields but missing person page links - Papers need citation network built - User says "build link graph", "populate links", or "enrich graph" - After bulk imports, need to verify graph integrity - Before major exports, need health check - User wants to export GBrain to markdown/wiki
- **Timeline** — **1926-05-26** | Born in Alton, Illinois **1959-08-17** | Kind of Blue released **1991-09-28** | Died in Santa Monica, California

## Further detail

### Related Skills

**Related Skills:** - `gbrain`: Install, configure, and operate GBrain CLI - `gbrain-minions`: Durable job queue for GBrain - `gbrain-skillify`: Turn failures into durable skills - `connector`: Analyze GBrain knowledge graph for semantic connections - `defrag`: Weekly Obsidian vault maintenance (file-based) - `paper-import-gbrain`: Proper paper import with correct frontmatter

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gbrain/gbrain-graph-enrichment/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
