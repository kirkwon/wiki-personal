---
date: 2026-07-19
type: concept
title: Arxiv
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Research
- Arxiv
- Papers
- Academic
- Science
- API
- research
sources:
- hermes://skill/arxiv
description: Search arXiv papers by keyword, author, category, or ID.
---

# Arxiv

> Search arXiv papers by keyword, author, category, or ID.

## Overview

- **Quick Reference** — | Action | Command | |--------|---------| | Search papers | `curl "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5"` | | Get specific paper | `curl "https://export.arxiv.org/api/query?id_list=2402.03300"` | | Read abstract (web) | `web_extract(urls=["https://arxiv.org/abs/2402.03300"])` | | Read full paper (PDF) | `web_extract(urls=["https://arxiv.org/pdf/2402.03300"])` |
- **Searching Papers** — The API returns Atom XML. Parse with `grep`/`sed` or pipe through `python3` for clean output.
- **Search Query Syntax** — | Prefix | Searches | Example | |--------|----------|---------| | `all:` | All fields | `all:transformer+attention` | | `ti:` | Title | `ti:large+language+models` | | `au:` | Author | `au:vaswani` | | `abs:` | Abstract | `abs:reinforcement+learning` | | `cat:` | Category | `cat:cs.AI` | | `co:` | Comment | `co:accepted+NeurIPS` |

## Further detail

### Sort and Pagination

| Parameter | Options | |-----------|---------| | `sortBy` | `relevance`, `lastUpdatedDate`, `submittedDate` | | `sortOrder` | `ascending`, `descending` | | `start` | Result offset (0-based) | | `max_results` | Number of results (default 10, max 30000) |

### BibTeX Generation

After fetching metadata for a paper, generate a BibTeX entry:

### Reading Paper Content

After finding a paper, read it:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/arxiv/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
