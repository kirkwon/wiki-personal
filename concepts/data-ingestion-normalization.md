---
date: 2026-07-19
type: concept
title: Data Ingestion Normalization
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- data
- ingestion
- deduplication
- normalization
- data-engineering
sources:
- hermes://skill/data-ingestion-normalization
description: Normalize and deduplicate data during ingestion from multiple sources
  or evolving naming conventions.
---

# Data Ingestion Normalization

> Normalize and deduplicate data during ingestion from multiple sources or evolving naming conventions.

## Overview

- **When to Use** — - Same entity appears multiple times under different names (e.g., "Schwab DWT 401k" vs "Schwab 401(k) - Davis Wright Tremaine LLP") - Legacy files coexist with newer parsed files in the same data directory - Account/device identifiers changed over time but represent the same thing - Data sources use inconsistent naming conventions
- **Pitfalls** — - **Legacy files not moved**: If you only add normalization without moving legacy files, both will still load and you'll get duplicate timestamps. The more recent file by date wins, but this can cause confusion if timestamps are identical.
- **Verification** — After adding normalization:

## Further detail

### References

- `references/portfolio-deduplication-case.md` — A concrete example from portfolio data with debugging steps - `references/financial-statement-metadata-extraction.md` — Pattern for extracting `institution`, `account_type`, and `retirement_source` from broker statement PDFs to prevent naming inconsistencies

### Application: Book Library Skill Reconciliation

Reconcile placeholder or generic skills in book library JSON files with real named skills from a master skills database. This is an application of the data deduplication pattern where the "duplicate" is a placeholder skill that needs to be replaced with a real one.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/data-engineering/data-ingestion-normalization/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
