---
date: 2026-06-28
type: note
title: Wiki Log
created: 2026-06-28
updated: 2026-06-28
tags: [meta]
---

- 2026-06-29: WIKI_DASHBOARD name="projects-overview" tool=bases view=table+cards filter="projects/ excluding TEMPLATE+DASHBOARD, live view by status/priority/staleness"
- 2026-08-18: INGEST source="arxiv-monitor-afd36d5e0d2e" pages_created=2 pages_updated=1 mode=append
  - Created: [[papers/causal-discovery-effect-constraints]] (arXiv:2608.12640, UAI 2026, UCLA StarAI — conditional causal discovery via adaptive multilevel splitting; β upgrade path), [[papers/e2-explainer-mas-topologies]] (arXiv:2608.12921 — Granger-style edge masking for MAS topology explanation; skill saliency via intervention)
  - Updated: [[concepts/co-failure-ceiling]] — added "Upgrade Path: From Statistics to Causal Estimation" section (β as conditional posterior over causal structure)
  - gbrain synced: 2 pages created (source=wiki), 6 typed links established (extends/related_to), graph verified
  - Code located: MLS-Framework (github.com/ZCX031116/MLS-Framework) — Python, unlicensed, 0 stars, pushed 2026-06-29
  - β flag: 2608.12640 separates shared-cause co-failure from coincidental co-occurrence; rare-event regime matches co-failure tails
- 2026-06-28: INGEST source="ornith-1-paper+conversation" pages_created=4 pages_updated=1 mode=append
  - Created: [[papers/ornith-1-self-improving-coding]], [[concepts/scaffold-optimization]], [[papers/co-failure-ceiling]], [[concepts/co-failure-ceiling]]
  - Updated: [[concepts/self-harness-paradigm]] — added Ornith and scaffold optimization connections
  - Ornith-1.0: RL joint scaffold+solution optimization, 2× Terminal-Bench vs Qwen3.5-9B
  - Co-Failure Ceiling (arXiv:2606.27288): β captures all-model-wrong rate, measurably 2.5× underpriced by Gaussian copula
  - P3 implication: pivot from trace distillation to co-optimization of skill instructions + LoRA weights

- 2026-06-28: INGEST source="paperswithcode-share-google" pages_created=6 pages_updated=0 mode=append
  - Created: [[papers/tmax-terminal-agents]], [[papers/fastcontext-coding-agent-explorer]], [[papers/quest-deep-research-agents]], [[papers/osworld2-computer-use-benchmark]], [[papers/evoevolution-long-context-embeddings]], [[papers/vibethinker-3b-reasoning]]
  - gbrain links established connecting all 6 papers to ornith-1, scaffold-optimization, and co-failure-ceiling
  - Batch extracted from Papers With Code "All Time Trending" collection at share.google/kr8DV5XTVPWiKRHJn
  - Key themes: terminal agents (Tmax vs Ornith), subagent architectures (FastContext), synthetic training data (QUEST), computer-use benchmarking (OSWorld 2.0), evolvable embeddings (EvoEmbedding), small-model reasoning (VibeThinker)

- 2026-07-15: ARCHITECTURE EXTENSION source="hermes-architecture-notebooklm" pages_created=4 pages_updated=1 mode=append
  - Created: [[concepts/documentation-master]], [[concepts/decision-master]], [[concepts/productivity-master]], [[concepts/learning-loop]]
  - Extended: [[concepts/knowledge-master]] (replaced stub with full architectural spec)
  - Updated: [[concepts/self-health-loop]] — autonomous health monitoring and repair
  - Created: [[sources/p6-hermes-architecture-layers-domain-masters.md]] — NotebookLM source document
  - Domain Master layer concept: specialized cognitive subsystems for documentation, decision, productivity, knowledge
  - Learning Loop layer concept: three-tier improvement (Execution → Harness → Meta)
  - Self-Health Loop concept: continuous system monitoring with automatic/semi-auto/escalated repair tiers
  - Integration: All layers connect to existing Hermes Cognitive Stack via feedback loops

- [2026-07-26T10:04:09] LINT issues_found=5 slug_mismatches_fixed=14 frontmatter_fixed=4 stale=844 missing_summary=5781 yaml_parse_remaining=5 flagged_pages=8 notes=ran_gbrain_frontmatter_fix+manual_yaml_fixes

- [2026-08-02T17:10:00Z] KNOWLEDGE_MAINTENANCE stubs_created=137 frontmatter_fixed=15+24(wiki-personal) queue_restarted=1 sync_wiki-personal=full_extracted edges_extracted=12261

- 2026-08-21: QUERY query="Tell me about wiki/sources/cl4r1t4s-leaked-system-prompts" result_pages=1 mode=normal escalated=false
- 2026-08-21: QUERY query="ontology vs semantic networks — comparison" result_pages=3 mode=normal escalated=false
