---
type: concept
title: Gbrain Decide
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - uncategorized
---

# gbrain-decide

>

## Usage

# gbrain-decide

Decision-support skill over Kirk's GBrain. Runs inside the existing
conversation — no standalone CLI habit. Built per the premortem
`premortem-2026-08-17-gbrain-decision-engine.md` (revised plan v1).

## When to invoke

Trigger when Kirk:

- Faces a choice between options and wants GBrain-informed guidance
- Is about to commit resources (time, money, engineering effort) and asks
  "what do I know about this"
- Wants to revise a prior decision and needs to find what superseded what
- Asks "what did I decide about X" / "what do I know about X" where X is
  decision-relevant (not a plain fact lookup)

**Do NOT trigger** when the question is a plain factual lookup — use
`gbrain query`/`gbrain search` directly instead. This skill exists for
*decision framing*, not encyclopedic retrieval.

## Phase 1 — Retrieve (date-forward, insight-first)

### Step 1.1 — Run the primary query

```bash
gbrain query "<question>" --recency on --salience on --limit 20
```

Use the decision question itself as the query text (not a keyword
abbreviation). `--recency on` and `--salience on` are explicit here per
the revised plan — do not omit them and rely on auto-detection for
decision queries.

### Step 1.2 — Pull graph context for the top decision-ish hit

Take the single most decision-relevant result from Step 1.1 (prefer pages
with `type: decision` or under `decisions/` in their slug). For that slug,
pull three things:

```bash
gbrain backlinks <slug>
gbrain graph <slug> --depth 2        # follows supersedes edges
gbrain timeline <slug>               # temporal ordering
```

If `graph --depth 2` surfaces a page that supersedes the slug you started
from, pivot to that page and pull its backlinks + timeline too.

### Step 1.3 — Rank and filter

Apply these rules in order:

1. **Decision pages outrank topical stubs.** Pages with `type: decision`
   or whose slug starts with `decisions/` outrank topically-similar stubs
   and index/hub pages.
2. **Discard empty stubs.** If a result's body is empty or it's a pure
   index/MOC hub page with no substantive content, remove it from ranking
   even if it scores high.
3. **Every citation MUST show its date.** When you cite a page, include its
   date (from frontmatter `date:` / `created:` or the page's timeline). Do
   not cite undated pages without noting that.
4. **Flag stale items.** Pages >12 months old get flagged "⚠ verify
   supersession" unless a `supersedes` edge resolves recency in your favor.
5. **Prefer lonely insight notes.** When a hub/MOC page and a sparse
   "random tuesday" lesson note both match, prefer the lesson note — it
   usually carries the actual judgment.
6. **Self-citation cap: 0.** Never cite anything under a `generated/`
   prefix. If a top result is under `generated/`, discard it and note the
   gap.
7. **Stub gate.** If >50% of your top-10 results are stubs/index pages,
   **stop**. Say "retrieval failed the stub gate — top-N is mostly empty
   pages" and ask Kirk rather than synthes

...(truncated)