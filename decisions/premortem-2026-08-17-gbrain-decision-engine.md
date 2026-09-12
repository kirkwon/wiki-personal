---
date: 2026-08-17
type: note
title: "Premortem: GBrain Decision Engine"
created: '2026-08-17'
status: active
tags: [premortem, gbrain, decision-engine]
---

# Premortem — GBrain Decision Engine (2026-08-17)

## Context
- **What:** Query/advisory layer over GBrain (19.8K pages): `gbrain-decide` CLI → hybrid query + graph traversal + type-based ranking boosts → cited synthesis → decision write-back loop.
- **Who:** Kirk, solo. Used via CLI + agent sessions.
- **Success:** Used ≥2x/week, changes a real decision by month 2.
- **Known debt:** 658 broken-link stubs, 3,034 stale internal links, unnormalized frontmatter across 8 pipelines, local-only 768d ollama embeddings, Firecrawl credits dead.

## Raw Failure Reasons
1. Stale/untrustworthy knowledge (superseded decisions, deprecated tech)
2. Retrieval quality ceiling (local embeddings, topically-similar-but-insight-free results)
3. Low adoption (displaced by main agent + GBrain bridge already in flow)
4. Write-back pollution loop (engine outputs crowd out primary sources)
5. Data-quality debt (stubs/links/frontmatter break the ranking boosts; never paid down)

## Investigator Deep-Dives (summaries)

### 1. Stale knowledge
Retrieval relevance ≠ temporal validity. GBrain has no supersession metadata; the ranking boost actively demoted a 2025 page that superseded a 2023 "closed, do not revisit" decision. Write-back loop adds pages but never marks predecessors stale → average trustworthiness declines as corpus grows.
- **Assumption:** A well-ranked page is a current page.
- **Warning signs:** answers citing >12mo-old decisions without dates; stale-link count growing after syncs.

### 2. Retrieval ceiling
Hard-won lessons live in sparse, un-linked, poorly-titled notes ("random tuesday"); 768d embeddings encode topical similarity, not decision-relevance. RRF promotes hub/MOC/index pages over lonely insight notes. Engine answers "what did I write about X" but never "what should I learn from what I wrote."
- **Assumption:** Hybrid retrieval suffices to surface decision-relevant knowledge.
- **Warning signs:** >50% of top-10 results are stubs/index pages in week-1 evals; Kirk greps vault manually within 2 min of using the engine.

### 3. Adoption
The competitor is the path of least resistance: Kirk's main Telegram agent already has GBrain bridged. Mid-decision at work, habit routes questions to the agent in his hand. Decision archive stalled at 11 entries (9 from first two weeks); CLI untouched for 47 days by January. Fourth consecutive "should pick that back up" project.
- **Assumption:** Kirk will change interaction habits for a dedicated tool.
- **Warning signs:** <15 invocations with zero repeat lookups by day 30; Kirk asks the main agent a decision question in any post-launch week.

### 4. Write-back pollution
Generated digests are cleaner and more query-shaped than messy primary notes, so they match *better* in embedding space. By month 4, index ~22% generated content; engine retrieves its own outputs, inherits its own synthesis errors, primary sources buried on page 3. Cleanup requires hand-triaging thousands of chunks.
- **Assumption:** Generated content is a neutral addition, not a competitor that displaces primary material.
- **Warning signs:** self-citation rate >15% on factual queries; digests outranking their own sources in monthly spot-checks.

### 5. Data-quality debt
Defrag stubs inherit `type: project` frontmatter, so type boosts fire on empty pages and outrank real decisions. Boosts fire on ~60% of actual decisions due to 4 frontmatter conventions across pipelines. Saturday cleanup script runs on 40 pages, then stalls. Firecrawl dead = can't re-ingest source data.
- **Assumption:** Advisory quality can layer on known-bad hygiene that a solo operator has already demonstrated he won't pay down.
- **Warning signs:** >10% of queries surfacing a stub in top-5 within 2 weeks; normalization script unmerged after 10 days.

## Synthesis

### Most Likely Failure: **Adoption**
Not technical. The main agent + GBrain bridge already covers 90% of the need at near-zero friction. A dedicated CLI loses to the tool already in hand.

### Most Dangerous Failure: **Write-back pollution**
Contaminates the underlying 19.8K-page asset — the one thing this project must never damage. Effectively irreversible at scale (manual triage of thousands of chunks).

### The Hidden Assumption
That *retrieval relevance ≈ decision value*. Every failure mode reduces to it: relevance without recency (stale), without insight-density (retrieval ceiling), without provenance (pollution), without hygiene (debt). The engine as drafted retrieves pages; Kirk needs it to retrieve *judgment*.

### Revised Plan (v1)
1. **Don't build a CLI — build an agent skill.** Ship `gbrain-decide` as a skill invoked BY the main agent (Hermes + this agent) inside the conversation Kirk already has. Zero habit change. Kills the adoption failure.
2. **Date-forward answers, day 1.** Every cited page shows its date; decision pages >12 months old get flagged "verify supersession." Kills the stale failure.
3. **Write-back with quarantine.** Engine outputs go to a separate `generated/` prefix excluded from retrieval by default; only human-edited decision pages enter the corpus. Cap self-citation at 0. Kills the pollution failure.
4. **Insight-first ranking eval before building boosts.** Week-1 eval: 20 real decision questions, hand-labeled. Gate: <30% stubs/index pages in top-10, and at least one true "lesson" note surfaced per question. If the eval fails, fix embeddings/ranking FIRST — no advisory layer on a failing retriever.
5. **Debt paydown scoped to the eval, not the corpus.** Only clean pages that the eval shows pollute results (likely the typed stubs). Don't boil the ocean.
6. **Supersession edges.** When write-back logs a decision, add a `supersedes` link to the prior decision page (gbrain link supports typed links). Cheap, and encodes the temporal graph.

### Pre-Launch Checklist
- [ ] Run 20-question retrieval eval; pass stub-rate gate before any engine work
- [ ] Confirm `generated/` prefix exclusion in retrieval path
- [ ] Date display + >12mo flag in answer template
- [ ] `supersedes` link creation in the write-back script
- [ ] Wire skill trigger into main agent (both Hermes + Autoclaw), not a standalone CLI
