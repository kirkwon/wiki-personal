---
date: 2026-07-19
type: concept
title: Academic Graph Import
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- research
sources:
- hermes://skill/academic-graph-import
description: 'Import academic works (papers, books) into a knowledge base (GBrain),

  link them to existing author entities, and build a research citation graph.

  Handles discovery (arXiv, DOI, Semantic Scholar), page creation with proper

  frontmatter, and entity linkage (person → wrote → paper).'
---

# Academic Graph Import

> Import academic works (papers, books) into a knowledge base (GBrain),
link them to existing author entities, and build a research citation graph.
Handles discovery (arXiv, DOI, Semantic Scholar), page creation with proper
frontmatter, and entity linkage (person → wrote → paper).

## Overview

- **Contract** — This skill guarantees: - Paper pages are created with proper frontmatter (type: paper, authors, year, DOI/arXiv ID) - Papers are linked to their authors via `wrote` link type - Timeline entries are added for import date - Papers are searchable via `gbrain search` and `gbrain query` - Works for both individual imports and bulk operations
- **Paper Queue** — Two-layer queue structure under `~/papers/`:
- **When To Use** — - User has academic authors in their knowledge base (GBrain person pages) - User wants to import research papers (from arXiv, DOI, Semantic Scholar, or manual entry) - User says "import papers for [author]" or "build research graph" - User wants to link papers to their authors (person → wrote → paper) - User mentions arXiv, DOI, or academic paper discovery

## Further detail

### Paper Page Template

⚠️ **CRITICAL: Type Field Override Issue (HISTORICAL — FIXED 2026-06-13)**

### Abstract

Abstract text...

### Relevance to Hermes Architecture

Why this paper matters...

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/academic-graph-import/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
