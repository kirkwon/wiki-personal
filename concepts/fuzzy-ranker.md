---
type: concept
title: Fuzzy Ranker
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Fuzzy Ranker
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- fuzzy-match
- ranking
- search
- rapidfuzz
- difflib
- python
- pattern
- software-development
sources:
- hermes://skill/fuzzy-ranker
description: Use when implementing relevance scoring for search results with fuzzy/partial
  matching. Combines base scores with fuzzy similarity (rapidfuzz with difflib fallback),
  applies system-specific boosts, and deduplicates by title. Produces 0-100 scores
  suitable for ranking.
---

# Fuzzy Ranker

> Use when implementing relevance scoring for search results with fuzzy/partial matching. Combines base scores with fuzzy similarity (rapidfuzz with difflib fallback), applies system-specific boosts, and deduplicates by title. Produces 0-100 scores suitable for ranking.

## Overview

- **When to Use** — - Merging results from multiple search systems - Scoring title-to-query relevance with tolerance for typos/partial matches - Deduplicating results that appear across multiple systems - Building a meta-search or federated search tool
- **Testing** — Expected: - Exact match → score near 100 - Fuzzy match → score lower (fuzzy contributes ~60% to total) - Deduplication → 1 result (books wins with higher base score)
- **Pitfalls** — 1. **rapidfuzz not installed** — always provide the difflib fallback or your skill breaks on clean installs 2. **Sorting after deduplication** — if you deduplicate first (alphabetically), you lose the score-based prioritization 3. **Fuzzy score dominates 60%** — if base scores are meaningful, tune this weight; 40/60 split works well for title-heavy matching 4. **Case sensitivity** — always `.lower()` both query and title before fuzzy comparison 5. **Empty title** — handle `result.get('title', '')` gracefully; empty title gets fuzzy_score 0

## Further detail

### Success Metrics

| Metric | Target | How to Measure | |--------|--------|----------------| | Exact query match | Score = 100 | `calculate_global_score({'title': 'X', 'score': 80}, 'X')` → 100 | | Typo tolerance | Score > 70 | `calculate_global_score({'title': 'Dul Proces'}, 'dual process')` → >70 | | Deduplication | 0 duplicates | Count unique titles in ranked output | | Fallback availability | Always works | Test without rapidfuzz installed |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/fuzzy-ranker/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
