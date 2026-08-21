---
date: 2026-06-29

type: log
tags: [autoresearch, research, synthesis, phase2, process]
---

# Phase 2 Complete: awesome-autoresearch Research Synthesis

**Date:** 2026-06-29
**Preceding:** Phase 1 import (wiki source + concept notes + GBrain + cron + curation skill)

## What was created

### 4 synthesis pages in wiki + GBrain

#### 1. Core Harnesses Analysis
**File:** `wiki/synthesis/autoresearch-core-harnesses-analysis.md`

Analyzed the 5 most influential autoresearch harness/infra projects:
- **karpathy/autoresearch** — The canonical three-file pattern. Basis for all other harnesses.
- **RightNow-AI/autokernel** — GPU kernel optimization with correctness + benchmark double-gate.
- **RUC-NLPIR/Arbor** — Generalist autonomous research with persistent hypothesis tree. 2.5× Claude Code throughput.
- **recursive-org/first-steps-toward-automated-ai-research** — Multi-thread recursive research that beats 2-year human nanoGPT record.
- **mco-org/squad** — SQLite-based multi-agent orchestration (already reviewed in prior session for /queue design).

Each rated on: architecture, key innovation, integration potential, verdict.

#### 2. Finance/Trading Cross-Reference
**File:** `wiki/synthesis/autoresearch-finance-trading-crosslink.md`

All 32 finance/trading entries classified and APS-scored (Applies to our Stack, 1-5):
- **APS 5:** autoresearch-skfolio (portfolio optimization), AutoResearch DEX (DeFi), delu-agent (live 24/7 trading)
- **APS 4:** AutoHypothesis (stock selection), ml-vs-leadlag-jp-stock (PCA vs ML strategy)
- Cross-linked to existing wiki concepts: [[factors]], [[mean-variance-myopia-under-stochastic-volatility]], [[asymmetry-hunter]], [[pca-random-matrix-theory-equity-markets]], [[causal-ai-hedge-agent]]
- Strategy clusters: crypto (6), prediction markets (5), equities (5), generic (5)

#### 3. Evaluation/Red Teaming Patterns
**File:** `wiki/synthesis/autoresearch-evaluation-red-teaming-patterns.md`

All 23 evaluation entries mapped to 6 reusable patterns:
1. Attack→Fix→Verify loop (penetration testing as autoresearch)
2. Prompt/Skill optimization via eval loop (directly applicable to our skills)
3. Agent behavior evaluation (meta-evaluation)
4. Benchmark novelty & integrity (current agents <10% human-level on open-ended tasks)
5. Integrity forensics (Anti-Autoresearch detects 39 hack patterns across 7 families)
6. Domain-specific evaluation benchmarks

Key reusable techniques extracted: blind multi-judge Borda, failure classification gates, three-layer audit stack, evidence gates, harness overfit detection.

#### 4. Software Optimization Clusters
**File:** `wiki/synthesis/autoresearch-software-optimization-clusters.md`

All 52 software entries clustered into 15 technique × domain groups:
- Top impact stories: 588× SQLite, 91.9% RISC-V CoreMark, 62% ClickHouse granule reduction (hidden 3-year bug found)
- 5 macOS-compatible projects identified for immediate testing
- 4 reusable protocols extracted: benchmark+correctness double-gate, profile-first, scout-promote, quality guard

### GBrain pages created (6)
| Slug | Type | Tag | Chunks |
|------|------|-----|--------|
| autoresearch-core-harnesses | synthesis | autoresearch,synthesis | 2 |
| autoresearch-finance-trading | synthesis | autoresearch,synthesis,finance | 3 |
| autoresearch-evaluation-patterns | synthesis | autoresearch,synthesis,eval | 2 |
| autoresearch-software-optimization | synthesis | autoresearch,synthesis,optimization | 2 |
| awesome-autoresearch-phase1-log | log | autoresearch,log | 1 |

### Auto-links resolved
GBrain auto-linker created links between synthesis pages and existing concept pages (autoresearch-pattern, karpathy-autoresearch-loop) plus finance concepts (factors, pca-random-matrix-theory, etc.)

## What was learned
1. **Only 32/684 entries (4.7%) are finance/trading** — the list is dominated by infra (132) and discussions (146)
2. **DEX trading shows the strongest published results** — 0.421 → 8.176 composite over 230 experiments
3. **Arbor's hypothesis tree** is the most architecturally interesting harness — it solves the forgetting problem of flat keep/discard
4. **The integrity forensics field is nascent but critical** — Anti-Autoresearch already documents 39 known hack patterns
5. **Top software optimizations are CPU-bound, not GPU** — SQLite (588×), ClickHouse (62%), Liquid (53%) are all CPU workloads

## Metrics
- 4 synthesis pages (18.5 KB total)
- 6 GBrain pages created (11 chunks)
- 23 auto-links resolved between new and existing pages
- 684 entries analyzed, cross-referenced, and clustered
