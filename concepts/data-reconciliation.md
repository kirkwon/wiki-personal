---
date: 2026-07-19
type: concept
title: Data Reconciliation
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- data-engineering
sources:
- hermes://skill/data-reconciliation
description: Techniques for matching, merging, and reconciling datasets that lack
  unique identifiers.
---

# Data Reconciliation

> Techniques for matching, merging, and reconciling datasets that lack unique identifiers.

## Overview

- **Core Problem** — When datasets lack unique identifiers (ISBNs, UUIDs, etc.), matching records across sources requires composite-key strategies and fuzzy matching.
- **References** — - See: `references/book-reconciliation-2026-05-14.md` for session-specific detail - CLI tool: `reconcile_books_skills.py` in the book_summaries project
- **Prompt Architecture Notes** — - **C1 Confabulation equilibrium:** When reconciliation produces "unmatched" records, the model's default is to force-match them with plausible-sounding fuzzy hits. Named restraint: "An unmatched record stays unmatched. A 0.74 similarity score does NOT round up to a match. Report unmatched records explicitly — a false match is worse than no match because it creates data integrity errors that propagate downstream." - **C4 Absent self-model (match confidence):** Fuzzy matching threshold (0.75) is the threshold gate — but the model may lower it under pressure to "get to zero unmatched." Maintain

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/data-engineering/data-reconciliation/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
