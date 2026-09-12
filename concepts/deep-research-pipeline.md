------

# Deep Research Pipeline

> 18-step deep research pipeline with source ranking, citation verification, contradiction detection, and compounding vault loop.

## Overview

- **When to Use** — - Deep-dive research requiring multiple sources, critical analysis, and cited output - Academic literature reviews with source quality ranking - Multi-perspective analysis where citation verification matters - Any research where the compounding vault benefit is desired
- **Pipeline Steps** — | Step | Name | Dispatch | |------|------|----------| | 0 | **vault_prefetch** | **`vault-synergy.py`** ⭐ (queries GBrain BEFORE fetch) | | 1 | decompose | `permanent-questions` skill | | 2 | width_sweep | `arxiv` + `web-researcher` skills | | 3 | **source_ranker** | **`source-ranker.py`** ⭐ | | 4-6 | loci → depth → reconcile | `research-agent` skill | | 7 | **contradiction_graph** | **`contradiction-graph.py`** ⭐ | | 8 | corpus_critic | `web-researcher` (adversarial search) | | 9 | evidence_digest | `extract-wisdom` + `analyze-paper` | | 10 | triple_draft | `delegate_task` (3 parallel drafts)
- **Tier Profiles** — | Tier | Steps | Trigger keywords | |------|-------|-----------------| | light | 1,2,10,15,16 | "compare", "overview", "what is", "summary" | | full | all 17 | Default | | premier | all 17 | Explicit deep analysis request | | dissertation | all + 1.5 | "dissertation", "thesis", "systematic review" |

## Further detail

### The Compounding Loop

Every run feeds the vault. Future runs query before fetching. Rankings accumulate. Smarter each time.

### Project Artifacts

- **Location**: `~/clawd/30.Research-Pipeline/` - **INFRASTRUCTURE.md**: Complete artifact audit (read this first for orientation) - **GRAPH.md**: DAG topology — 10/10 nodes ✅ - **decisions/**: Decision log (9 architectural decisions) - **GAP-ANALYSIS.md**: All phases marked complete - **ARCHITECTURE.md**: Full 16-step × Hermes skill mapping - **PIPELINE.md**: Dispatcher specification (all gaps removed) - **Source**: Adapted from [Hyperresearch](https://github.com/jordan-gibbs/hyperresearch) (MIT)

### References

| File | Purpose | |------|---------| | `references/academic-api-quickref.md` | arXiv + OpenAlex API patterns (tested) | | `references/multi-backend-search.md` | Multi-backend parallel search (DDG + arXiv + GBrain): venv dependency, arXiv fielded queries, Jaccard relevance scoring, cross-validation | | `references/adapting-external-architectures.md` | How to adapt external systems to Hermes | | `references/hyperresearch-architecture.md` | Original architecture notes | | `references/full-run-playbook.md` | Step-by-step playbook from first complete run (cite-check fix cycle, parallelization stra

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/deep-research-pipeline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[storm-research]]
