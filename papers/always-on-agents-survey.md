---
date: 2026-07-06
type: media
title: "Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents"
created: 2026-07-06
updated: 2026-07-06
tags: [agent-systems, methodology, technology, cognitive-science]
sources: [raw/papers/arxiv-2606.30306.md]
summary: Survey of 435 works reframing always-on agents as persistent-state systems governed over a lifecycle. Finds structural asymmetry — forward arc (retrieve 269, write 200) dominates, return arc (rollback 27, authority 72) is sparse. Proposes AOEP-v0 evaluation protocol where governance gaps are not reading problems.
dates:
  - date: "2026-06-29"
    event: "Published on arXiv (2606.30306)"
---

# Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents

**Authors:** Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
**arXiv:** [2606.30306](https://arxiv.org/abs/2606.30306)
**Date:** 2026-06-29
**Corpus:** 435 works (2023-01 through 2026-06)

## Core Thesis

An agent that carries state across tasks is a fundamentally different kind of system than one that resets. The survey reframes always-on agents from **"accumulate-and-retrieve"** to **"govern-over-a-lifecycle"** — persistent state is not memory alone but retrievable memory plus task ledgers, permissions, tool and credential state, standing commitments, provenance records, shared/social state, and trigger conditions.

Memory is the most studied component, but treating the whole union as "memory" hides the governance obligations that make always-on agents distinct.

## The Four Contributions

1. **Persistent-state framing** — always-on agents as [[concepts/persistent-state-systems]] governed over a lifecycle along [[concepts/six-state-axes]], tied by [[concepts/state-governance-lifecycle|five invariants]]
2. **Layered stack reading** — literature as a persistent-state stack (substrate → memory-form → state-movement → application) rather than a memory taxonomy
3. **Corpus coding** — 435 works measured for lifecycle-stage and state-axis coverage, revealing structural asymmetry
4. **AOEP-v0 protocol** — [[concepts/always-on-evaluation-protocol-aoep]] — event-stream + snapshot schema that scores state mutation and recovery rather than answer quality

## Key Finding: Structural Asymmetry

| Lifecycle Stage | Corpus Count (of 435) |
|---|---:|
| Retrieve | 269 |
| Write | 200 |
| Authority (state axis) | 72 |
| Rollback | 27 |

The **forward arc** (retrieve, write) is crowded; the **return arc** (rollback, authority) is sparse — an order-of-magnitude gap. The works studied store and retrieve more thoroughly than they revoke, recover, attribute, and bound stored state. Even this is generous: the rollback count aggregates internal-state, workflow, and external-effect rollback, with the hardest subclass (external-effect rollback) rarer than the aggregate suggests.

## Five Invariants

The five invariants tie the [[concepts/state-governance-lifecycle|lifecycle stages]] to the [[concepts/six-state-axes|state axes]]:

1. **Authority monotonicity** — authority can narrow over time but never silently widen
2. **Scope non-expansion** — a record's applicability cannot grow beyond its admission boundary
3. **Deletion propagation** — a delete must cascade to all derived tiers, not just the primary store
4. **Provenance preservation** — source attribution survives consolidation, not dropped when a summary scores well
5. **Rollback traceability** — every state mutation has a recoverable prior state with a logged chain

No current system enforces all five. The "validate" lifecycle stage has no native abstraction — vector stores promote whatever is written, with no authority check at admission time.

## AOEP-v0 Pilot Results

| System Type | Score (obligations passed / total) |
|---|:---:|
| Governed reducer | 15/15 |
| All raw stores (average) | 7/15 |
| Mem0-style wrappers | 4/15 |

**The gap is missing governance state, not missing retrieval.** Tested memory wrappers fail obligations that require explicit governance state: permission epochs, deletion ledgers, trust tiers, conflicts, and rollback records.

## Why Bigger Context Is Not Enough

The governance gaps documented are **not reading problems**:

- Larger context and better retrieval answer "what did I record?" — they do not answer what *should* persist, which record is *authoritative*, how a record should *change* under contradiction, or how a user can *revoke* it
- Long-context studies show capacity ≠ comprehension — models underuse information in the middle of long windows even when present
- Personalization research shows accumulated user state drifts, contradicts itself, and can be poisoned; routine interactions gradually weaken confirmation boundaries and expand action scope without any single step looking like an attack
- The four questions an always-on agent must answer — what persists, which is authoritative, how it changes, how it's revoked — are decisions about authority, mutability, and recoverability, not context length

## Benchmark Gap (Table 14)

Six benchmark families each measure part of the requirement space but **none jointly tests governance across the lifecycle**:

- Memory QA, Long-context/RAG, Memory-guided action, State/belief mutation, Tool-security, Personalization/proactive
- Each family has disjoint blind spots — no benchmark exercises deletion propagation, authority scoping, rollback recovery, and provenance preservation together

## Five Frontier Programs (Table 21)

| Program | Corpus Gap | Missing Instrument |
|---|---|---|
| Lifecycle-complete evaluation | Rollback 27/435; recovery never measured | Recovery-success and recovery-cost metrics on hosted systems |
| Controlled compounding | Consolidation drops retrieval handles; contagion has no safe threshold | Write-acceptance gate keyed to later addressability |
| Authority, privacy, deletion, cross-surface | Authority 72/435; no single-policy cross-surface benchmark | One agent, all surfaces, one declared policy |
| Shared-memory governance | No distributed rollback; revocation cascades unmodeled | Authority-scoped rollback of tool-originated state |
| Adjacent-discipline bridging | Governance axes thin in every part | Native correctness calculi imported, not rederived |

## Disciplinary Bridges

The governance backbone needs deliberate import from five established disciplines:

- **Databases/distributed systems** — transactional correctness, snapshot isolation, write-ahead logging, point-in-time recovery, consistency models (Saga model imported by Chang and Geng 2025)
- **Classical knowledge representation** — belief revision (AGM/Hansson postulates), contradiction resolution as write-time concurrency control (Park 2026, Wang 2026b)
- **Formal methods/runtime verification** — past-time temporal logic monitors (Bollig 2026), SMT-compiled tool-use policies via Z3 (Winston et al. 2026), capability-containment proofs (Metere et al. 2026)
- **Access control / capability security** — privilege lattices, capability-scoped rehydration, delegation-provenance chains
- **HCI / fairness auditing** — regulatory interfaces, structured audit protocols

## Corpus Methodology

- Sources: arXiv (cs.AI, cs.CL, cs.LG, cs.CR), Semantic Scholar, OpenReview, ACL Anthology
- Time window: 2023-01 through 2026-06 with foundational anchors admitted regardless of date
- Collection: seeded from agent-memory surveys → backward/forward citation chasing (2 hops) → targeted term-set sweeps (iterative until duplicate saturation)
- Inclusion: persistent-state mechanism, relevant benchmark, failure mode, foundational anchor, or boundary case
- Coding reliability: blind second coding on 236-work sample; pooled per-cell agreement 0.82 lifecycle (κ=0.58), 0.74 axes (κ=0.44) — moderate agreement supporting directional claims far better than exact counts

## Connections

- [[concepts/persistent-state-systems]] — the core definition this survey establishes
- [[concepts/always-on-evaluation-protocol-aoep]] — the proposed evaluation protocol
- [[concepts/state-governance-lifecycle]] — the lifecycle, invariants, and forward/return arc asymmetry
- [[concepts/six-state-axes]] — the six characterization dimensions
- [[concepts/self-maintaining-knowledge-base]] — this survey's governance lifecycle directly applies to the drift-detect-approve-verify loop in self-maintaining KBs
- [[concepts/loop-engineering]] — the validate gate gap parallels loop-engineering's insight that independent validation prevents circular reasoning; the survey's "validate" stage is the missing gate
- [[concepts/self-harness-paradigm]] — the AOEP-v0 approach (test obligations mechanically, not holistically) mirrors the proposal-validate stage's mechanical gatekeeping

## Timeline

**2026-06-29** | Published on arXiv (2606.30306)
