---
type: concept
title: "Always-On Evaluation Protocol (AOEP)"
created: 2026-07-06
updated: 2026-07-06
tags: [agent-systems, methodology, technology]
sources: [papers/always-on-agents-survey]
summary: An evaluation protocol for always-on agents that scores state mutation and recovery (governance obligations) rather than answer quality. AOEP-v0 uses an event-stream + snapshot schema with deterministic invariant checks instead of holistic LLM judges.
---

# Always-On Evaluation Protocol (AOEP)

## What It Is

AOEP is an evaluation protocol designed for always-on agents that tests **governance obligations** — whether state mutations satisfy structural invariants — rather than downstream task accuracy.^[papers/always-on-agents-survey]

The key insight: existing benchmarks measure whether an agent answers correctly, but never whether it *governs its state correctly*. AOEP shifts from "what does the agent know?" to "does the agent's state satisfy its declared governance obligations?"

## AOEP-v0 Design

### Event-Stream + Snapshot Schema

AOEP-v0 uses two complementary data structures:

- **Event stream**: a chronological log of all state mutations (writes, updates, deletions, rollbacks, permission changes) — analogous to write-ahead logging in databases
- **Snapshots**: point-in-time state captures that allow checking whether derived state is consistent with the event stream — analogous to snapshot isolation

This combination enables **deterministic invariant checks**: test whether a deleted value is unretrievable across all derived tiers, whether an action is licensed by the current authority epoch, whether consolidation preserved retrieval handles, whether rollback restored the correct prior state.

### Obligation Types

AOEP-v0 evaluates two classes of obligations:

| Type | Definition | Example Check |
|---|---|---|
| **Obligation pass** | System satisfies a positive governance requirement | Deleted fact is unretrievable from all stores |
| **Negative-invariant pass** | System does not violate a declared constraint | No action executes under lapsed authority |

### Pilot Results

| System Type | Obligations Passed / Total |
|---|:---:|
| Governed reducer (explicit governance state) | **15/15** |
| Raw stores (vector DBs, key-value, graph) | **~7/15** |
| Mem0-style wrappers (memory augmented with minimal governance) | **~4/15** |

**Interpretation:** The gap between governed reducers and raw stores is not a retrieval problem — it's a missing governance state problem. Mem0-style wrappers that add memory augmentation without governance infrastructure actually score *worse* than raw stores on some obligations because their consolidation layer drops provenance.

## Why Not Holistic Judges

AOEP uses **deterministic checks** instead of LLM-as-a-judge holistic evaluation because:

1. Governance obligations are structural — they either hold or they don't (a deletion either propagated or it didn't)
2. Holistic judges have well-documented position bias, length bias, and self-preference that make binary governance checks unreliable
3. The four questions an always-on agent must answer (what persists, which is authoritative, how it changes, how it's revoked) require verifiable answers, not estimated ones

## Limitations and Status

AOEP-v0 is deliberately **small and representational** — a pilot illustrating the approach rather than a benchmark. The survey notes that no shared benchmark exists for rollback recovery, authority enforcement, or cross-surface governance, which is precisely the gap AOEP aims to fill.

## Connections

- [[papers/always-on-agents-survey]] — the source paper proposing AOEP
- [[concepts/state-governance-lifecycle]] — the lifecycle and five invariants that AOEP tests against
- [[concepts/persistent-state-systems]] — the system model AOEP evaluates
- [[concepts/loop-engineering]] — AOEP's deterministic invariant checks mirror loop-engineering's SHA-256 hash verification as a mechanical gate
