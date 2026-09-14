---
type: note
title: Autoresearch Core Harnesses
related:
  - awesome-autoresearch
  - autoresearch-pattern
  - karpathy-autoresearch-loop
ingested_via: put_page
ingested_at: '2026-06-30T06:05:28.590Z'
source_kind: put_page
tags:
  - autoresearch
  - comparison
  - harnesses
  - infra
  - tools
created: 2026-06-30
---
# Core Autoresearch Harnesses — Analysis

Analysis of the 5 most influential autoresearch harness/infra projects from the awesome-autoresearch curated list.

---

## 1. karpathy/autoresearch — The Original

**Repo:** https://github.com/karpathy/autoresearch
**Influence:** The canonical reference. Spawned 500+ forks and adaptations across every ML subfield.

### Architecture
Three immutable/mutable files:
- `prepare.py` — data prep (chmod 444)
- `train.py` — **only editable file** (agent mutates this)
- `eval.py` — fixed evaluator, measures `val_bpb`

### Key innovation
The **single-file mutation + git keep/revert** combo is the core pattern. Every other project is a variant of this.

### Integration potential
High. The three-file pattern is trivially portable to any codebase. Would need to adapt `prepare.py` and `eval.py` for our domain (not ML training).

### Verdict
⭐ Essential reading. Basis for all other harnesses.

---

## 2. RightNow-AI/autokernel — GPU Kernel Optimization

**Repo:** https://github.com/RightNow-AI/autokernel
**Domain:** GPU kernel optimization (CUDA, Triton)

### Architecture
Generalizes autoresearch to kernel code:
- Agent edits `.cu` or `.py` kernel files
- Benchmarks each change for speed
- Keeps only verified performance wins
- Correctness gate (must pass tests before acceptance)

### Key innovation
**Domain transfer** — shows the pattern works on systems code, not just ML training. The correctness gate prevents overfitting to benchmarks.

### Integration potential
High for any performance-sensitive code (but needs CUDA GPU). The correctness-gate pattern is reusable even without the GPU component.

### Verdict
⭐⭐ Highly recommended for systems optimization. The benchmark + correctness double-gate is a best practice.

---

## 3. RUC-NLPIR/Arbor — Generalist Autonomous Research

**Repo:** https://github.com/RUC-NLPIR/Arbor
**Paper:** arXiv:2606.11926
**Published:** June 2026

### Architecture
Generalist autonomous research agent that:
- Proposes hypotheses from code + research context
- Edits code and runs real experiments
- Keeps only improvements that survive held-out evaluation
- Grows a **persistent hypothesis tree** across branches

### Key results
| Metric | Arbor | Claude Code | Codex |
|--------|-------|-------------|-------|
| Throughput (same compute) | **2.5×** | 1× | 1× |
| MLE-Bench Lite Any-Medal | **86.36%** | — | — |
| BrowseComp | ✓ SOTA | — | — |
| Terminal-Bench 2.0 | ✓ SOTA | — | — |

### Key innovation
**Hypothesis tree** — unlike flat keep/discard loops, Arbor maintains branches of competing hypotheses that persist across sessions. This enables compounding discovery rather than forgetting.

### Integration potential
Very high. The hypothesis tree pattern is general and could be applied to any research domain. The paper is fresh (June 2026).

### Verdict
⭐⭐⭐ Most advanced harness. The hypothesis tree is the next evolution beyond flat keep/discard.

---

## 4. recursive-org/first-steps-toward-automated-ai-research — Multi-Thread Recursive Research

**Repo:** https://github.com/recursive-org/first-steps-toward-automated-ai-research

### Architecture
Proposes, implements, validates, and composes improvements across **many parallel research threads** with shared knowledge transfer.

### Key results
| Benchmark | System | Human/Community |
|-----------|--------|----------------|
| NanoChat val_bpb | **0.9109** | 0.9372 (community) |
| NanoGPT Speedrun (wall time) | **77.5s** | 79.7s (2-year human record) |
| SOL-ExecBench kernel opt | **0.754** | 0.699 |

### Key innovation
**Cross-thread composition** — improvements found in one thread inform others. This amortizes the cost of research across parallel explorations.

### Integration potential
High for any multi-problem domain. The cross-thread knowledge transfer is the unique value.

### Verdict
⭐⭐ Beats the 2-year human-optimized nanoGPT record. Shows autoresearch can surpass sustained human effort.

---

## 5. mco-org/squad — Multi-Agent SQLite Orchestration

**Repo:** https://github.com/mco-org/squad
**Already reviewed in depth** (prior session — see `sources/squad-multi-agent-messaging.md` if saved).

### Architecture
Multi-AI-agent orchestration through **SQLite** instead of sockets/daemons:
- `squad send` / `squad receive` for messaging
- Task lifecycle: create → claim → complete/skip/requeue
- Roles: manager, worker, inspector
- Compatible with Claude Code, Gemini CLI, Codex, OpenCode

### Key innovation
**SQLite as transport** — simpler, more durable, and easier to debug than socket-based orchestration. Maps directly to our `/queue` requirements.

### Integration potential
High. Squad's task lifecycle (create → claim → complete) is identical to our queue pattern. The cross-review (inspector role) catches 20-30% more bugs.

### Verdict
⭐⭐ Already integrated into our thinking about `/queue`. The SQLite transport pattern is proven.

---

## Comparison Matrix

| | Original | AutoKernel | Arbor | Recursive | Squad |
|---|---|---|---|---|---|
| **Mutation target** | `train.py` | kernel code | any code | any code | agent messages |
| **Eval type** | val_bpb | benchmark+test | held-out | cross-thread | inspector review |
| **Persistence** | git revert | git revert | hypothesis tree | shared knowledge | SQLite |
| **Parallelism** | serial | serial | branch tree | multi-thread | multi-agent |
| **GPU needed** | yes | yes | no | yes | no |
| **Runs on macOS** | partial (MPS) | no (CUDA) | yes | partial | yes |
| **Unique value** | canonical pattern | correctness gate | hypothesis tree | cross-thread transfer | SQLite transport |

## Integration Recommendations

1. **Adopt the shared knowledge pattern** from recursive-org for our multi-agent symphony setup
2. **Explore Arbor's hypothesis tree** as an alternative to flat keep/discard in our research workflows
3. **Use the correctness + benchmark double-gate** from AutoKernel for any performance optimization
4. **Squad's SQLite transport** is already informing our `/queue` design
