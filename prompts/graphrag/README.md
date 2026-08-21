---
date: 2026-06-30

type: concept
title: "GraphRAG Search Strategy Prompts"
source: "Microsoft GraphRAG — extracted from github.com/ChristopherLyon/graphrag-workbench"
tags:
  - graphrag
  - prompts
  - search-strategies
  - knowledge-graph
  - entity-extraction
---

# GraphRAG Search Strategy Prompts

Extracted from [graphrag-workbench](https://github.com/ChristopherLyon/graphrag-workbench) — a Next.js frontend for Microsoft's GraphRAG framework. The prompts below are Microsoft's research-backed query strategies for knowledge graph interaction.

## Prompt Index

| # | Prompt | Purpose |
|---|--------|---------|
| 1 | `basic_search_system_prompt.txt` | Simple entity/relationship retrieval |
| 2 | `local_search_system_prompt.txt | Context-aware local graph search |
| 3 | `global_search_knowledge_system_prompt.txt` | Global knowledge aggregation |
| 4 | `global_search_map_system_prompt.txt` | Map-phase for global search (parallel) |
| 5 | `global_search_reduce_system_prompt.txt` | Reduce-phase for global search (merge) |
| 6 | `drift_search_system_prompt.txt` | Drift exploration — follow information trails |
| 7 | `drift_reduce_prompt.txt` | Reduce drift search results |
| 8 | `extract_graph.txt` | Extract entities + relationships from text |
| 9 | `extract_claims.txt` | Extract claims/assertions with confidence |
| 10 | `summarize_descriptions.txt` | Summarize entity descriptions |
| 11 | `community_report_graph.txt` | Generate community graph reports |
| 12 | `community_report_text.txt` | Generate community text summaries |
| 13 | `question_gen_system_prompt.txt` | Generate follow-up questions |

## Search Strategies

### Basic Search
Direct entity lookup with relationship context. Good for: "What do we know about X?"

### Local Search
Context-aware retrieval that considers the entity's neighborhood in the graph. Weighs direct relationships, community membership, and recent activity.

### Global Search (Map-Reduce)
Two-phase: **Map** — parallel queries across community summaries → **Reduce** — synthesize into coherent answer. Good for broad questions across the entire knowledge corpus.

### Drift Search
Follows information trails through the graph, surfacing connected but non-obvious entities. The drift prompt uses a "reduce" step to collapse branching paths. Good for exploratory research questions.

## Relevance to Current Stack

These prompts map to GBrain's existing capabilities:

| GraphRAG Strategy | GBrain Equivalent | Gap |
|-------------------|-------------------|-----|
| Basic search | `gbrain query` | None — already covered |
| Local search | Retrieval Reflex + graph traversal | None — already covered |
| Global search (map-reduce) | Dream cycle (nightly synthesis) | Dream is batch, not query-time |
| Drift search | `gbrain brainstorm` / `gbrain lsd` | Close — brainstorm is bisociation, drift is trail-following |
| Entity extraction | Skillpack ingestion + dream cycle | GraphRAG's extraction is more structured |
| Community reports | Concept-synthesis T1/T2 tiering | Concept-synthesis is per-concept, not per-community |

## Key Takeaways

1. **Drift search** is the most novel — GBrain has no equivalent trail-following query mode. The drift prompts (`drift_search_system_prompt.txt`, `drift_reduce_prompt.txt`) could inspire a new query mode in the knowledge-metabolism skill.

2. **Community reports** (graph + text) produce hierarchical cluster summaries that concept-synthesis doesn't. Could be adapted as a Phase 5 for the concept-synthesis skillpack.

3. **Extract claims** is unique — GBrain doesn't extract claims with confidence scores from ingested content. This could fill a gap in the extraction pipeline.

## Source
- Repo: github.com/ChristopherLyon/graphrag-workbench (MIT)
- Microsoft GraphRAG: github.com/microsoft/graphrag
