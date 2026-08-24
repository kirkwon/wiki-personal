---
date: 2026-06-28
type: note
title: Wiki Log
created: 2026-06-28
updated: 2026-06-28
tags: [meta]
---

- 2026-06-29: WIKI_DASHBOARD name="projects-overview" tool=bases view=table+cards filter="projects/ excluding TEMPLATE+DASHBOARD, live view by status/priority/staleness"
- 2026-08-23: INGEST source="arxiv-monitor-afd36d5e0d2e" pages_created=7 pages_updated=2 mode=append
  - Created: [[papers/task-coevolve-harness-optimization]] (arXiv:2608.20169 — disagreement-weighted validation sampling, Terminal-Bench 2.1 @ 80% fewer evals), [[papers/phantom-gains-self-improvement-null]] (2608.20290 — frozen-control null for self-improvement audits), [[papers/ai4ai-bench-rsi]] (2608.20318 — agent-designed training algorithms, best 0.25 vs optimum 1.0), [[papers/skillgate-inpolicy-skill-selection]] (2608.18852 — selector credit starvation + disjoint credit channels), [[papers/tmi-task-model-induction]] (2608.20319 — computer-use traces → task models → +30% skills), [[papers/break-it-down-skill-transfer]] (2608.20274 — subtask-level + text skills transfer; task-level skills harm), [[concepts/skill-utility-gating]] (convergent theme: self-generated skills need measured utility before reuse)
  - Updated: [[concepts/co-failure-ceiling]] (β measurement discipline: SkillGate selection–execution de-confounding, Task-CoEvolve disagreement logs as cheap β, Phantom Gains measured-null requirement), [[concepts/scaffold-optimization]] (Task-CoEvolve link)
  - Note: papers 2608.20169/2608.20290/2608.20319 were flagged by the Aug 22 monitor run but that run's persistence stage did not execute — pages created today from today's re-verification (abstracts pulled via arXiv REST API this session)
  - FinSkillBench (2608.18099, orig. Jun 9) cross-listed into q-fin Aug 20 — noted in [[concepts/skill-utility-gating]] evidence table; no separate page (not a fresh submission)
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
