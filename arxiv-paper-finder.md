---
type: concept
title: Arxiv Paper Finder
created: 2026-09-05
updated: 2026-09-05
tags:
  - Skill
  - uncategorized
---

# arxiv-paper-finder

Find recent arXiv papers (last 90 days) matching Hermes agent use cases — agentic AI, CLI/terminal agents, tool use, self-evolution, memory/context management. Use when the user asks what papers to read, surf, or apply.

## Usage

# arXiv Paper Finder — Agent Research Surface

## When to use
User wants paper recommendations to read/surface — especially papers applicable to Hermes agent design (CLI agents, tool use, memory, context, self-evolution, evaluation).

## Prerequisites
- `uv` ≥ 0.5 on $PATH
- network access to arXiv API

## Invocation

```bash
# one-shot run
uv run --with arxiv==2.2.0 python ~/.hermes/skills/arxiv-paper-finder/scripts/surf.py

# narrow by query (space-joined, AND semantics via arxiv.query)
uv run --with arxiv==2.2.0 python ~/.hermes/skills/arxiv-paper-finder/scripts/surf.py --query "self-evolving agent CLI" --days 60 --max 8
```

### Optional flags
| flag | default | meaning |
|---|---|---|
| `--query` | (none — broad agentic + CLI surface) | extra query terms ANDed onto the base filters |
| `--days` | `90` | recency window |
| `--max` | `6` | papers to surface per run |
| `--category` | (auto: cs.AI cs.CL cs.MA cs.LG cs.SE) | comma-separated arXiv categories |
| `--dry-run` | off | print the search payload without fetching details |

## What this surfaces
For each paper:
- title, authors (last author only if >6), arxiv ID, date
- 1–2 line relevance note (why Hermes cares)
- direct arxiv abstract link

Surfacing only — no download, no full-text. User can read further via `web_extract` or `arxiv` skill.

## Design notes
- Broad default is intentional: the value is a curated shortlist, not an exhaustive scan.
- Recency bias toward last 90 days unless user asks for a specific older paper.
- Category list is opinionated toward agent-relevant cs.* buckets; tell the user if you want cs.CV / cs.IR etc.
- Skips withdrawn/corrupted entries silently.

## Pitfalls
- arXiv API rate limits raw queries; the script caps at 100 per call and sleeps 3s between detail calls.
- If `uv` isn't on PATH, fall back to the user's system python with `pip install arxiv` and run the same script.
- Title-only display on narrow queries to avoid spam; expand to full relevance note only when count ≤ max.

### Session notes
Per-run curation detail (selected papers, applicability reasoning, triage) lives in
`references/2026-09-04-hermes-surface.md` below — re-run the skill when you want a fresh shortlist.

### Gotchas verified this session (arxiv 2.2.0 + `uv run`)
These are real API surface quirks, not transient environment failures. Encode them here so a future session doesn't re-discover them.

1. **`Result` has no `.submitted` attribute.** The `arxiv.Result` object does not expose `.submitted`. Use `getattr(r, "published", None) or getattr(r, "submitted", None)` to get a date, and guard for `None`. If you write `r.submitted` directly you get `AttributeError` at runtime.
2. **Timezone mismatch on date comparison.** arXiv dates are offset-aware (UTC). Compare against `datetime.now(timezone.utc)`, not `datetime.now()` (naive) or `datetime.utcnow()` (deprecated). A naive-vs-aware comparison raises `TypeError: can't compare offset-naive and offset-aware datetimes` and silently skips 

...(truncated)