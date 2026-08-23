---
date: 2026-07-06
type: concept
title: "State Governance Lifecycle"
created: 2026-07-06
updated: 2026-07-06
tags: [agent-systems, methodology, technology]
sources: [papers/always-on-agents-survey]
summary: "The ten-stage lifecycle (observe→write→validate→organize→retrieve→act→update→forget→audit→rollback) over which persistent agent state is governed, with five invariants that tie lifecycle stages to state axes. A structural asymmetry exists: the forward arc dominates, the return arc is sparse."
---

# State Governance Lifecycle

## The Ten Stages

Persistent state in an always-on agent moves through ten stages, each with distinct governance obligations:^[papers/always-on-agents-survey]

| Stage | Governance Question | Current Gap |
|---|---|---|
| **Observe** | What enters the agent's attention? | Mostly addressed |
| **Write** | What gets admitted to durable state? | No authority/scope gating at admission |
| **Validate** | Does the write satisfy invariants? | **No native abstraction** — vector stores promote whatever is written |
| **Organize** | How is state consolidated without losing governance? | Summarization drops provenance; structural organization introduces governance complexity |
| **Retrieve** | What gets surfaced to the agent? | Well-studied (269/435 works) |
| **Act** | Does the action stay within state-licensed authority? | Partially addressed |
| **Update** | How does state change under contradiction? | Mutability rarely scoped |
| **Forget** | Is deletion complete and verifiable? | Supposedly forgotten info resurfaces under multi-hop queries |
| **Audit** | Can operators inspect the state lineage? | Sparse formal audit mechanisms |
| **Rollback** | Can state be reverted to a prior point? | Only 27/435 works expose any rollback |

## Five Invariants

Five structural invariants tie the lifecycle stages to the [[concepts/six-state-axes|state axes]]:

1. **Authority monotonicity** — a record's authority level can narrow over time (a permission granted for task A does not automatically extend to task B) but never silently widen. Enforced at the validate/write boundary.

2. **Scope non-expansion** — a record admitted for scope X cannot legitimately be applied at scope Y unless explicitly re-licensed. Prevents the "accumulated state drift" failure where routine interactions gradually expand an agent's effective action scope.

3. **Deletion propagation** — when a record is deleted, all derived representations (summaries, embeddings, caches, skill libraries) must also be updated. The survey documents that supposedly forgotten information resurfaces under multi-hop and aliased queries because deletion is applied only to primary stores.

4. **Provenance preservation** — every record carries attribution (who wrote it, under what authority, through what transformations) that survives consolidation. Summarization that scores well on aggregate recall while silently dropping source attribution violates this invariant.

5. **Rollback traceability** — every state mutation has a recoverable prior state, logged in an auditable chain. Rollback is itself categorized: internal-state rollback (reverting a stored fact), workflow rollback (compensating a partially executed multi-step task), and external-effect rollback (undoing an already-committed side effect like a payment).

## Forward Arc vs Return Arc Asymmetry

The 435-work corpus coding reveals a **structural asymmetry** between two arcs of the lifecycle:

### Forward Arc (crowded)
- Retrieve: 269 works
- Write: 200 works

### Return Arc (sparse)
- Rollback: 27 works (aggregate of three mechanically distinct operations)
- Authority: 72/435 works

This is an order-of-magnitude gap that no plausible reclassification of borderline cells could close. The return arc — revoking, recovering, attributing, and bounding stored state — is the governance frontier.

## The Validate Gap

The **validate** stage is the most critical gap: no current system enforces authority monotonicity at the promotion/writing boundary. Vector stores accept whatever is written. This means poisoned traces, stale preferences, and lapsed permissions enter durable state without any gate — and then influence actions months later.

This parallels [[concepts/loop-engineering]]'s insight: without a critic independent of the doer, the system cannot reliably catch its own errors at admission time.

## The Organize Tradeoff

Two families of consolidation exist, each with governance costs:

| Approach | Governance Tradeoff |
|---|---|
| **Summarization** | Compact but loses provenance, retrieval handles, and provenance chains |
| **Structural organization** (knowledge graphs, hierarchical memory) | Preserves more structure but introduces governance complexity (multi-hop reasoning paths, authority propagation across edges) |

Neither family has a built-in mechanism for checking whether consolidation preserved the five invariants.

## Connections

- [[papers/always-on-agents-survey]] — the source survey defining this lifecycle
- [[concepts/persistent-state-systems]] — the system model this lifecycle governs
- [[concepts/six-state-axes]] — the six characterization dimensions the invariants operate on
- [[concepts/always-on-evaluation-protocol-aoep]] — the protocol that tests whether a system satisfies these invariants
- [[concepts/self-maintaining-knowledge-base]] — the detect-drift→propose-fix→human-approve loop is an instance of the governance lifecycle applied to documentation
- [[concepts/loop-engineering]] — the validate gap directly parallels loop-engineering's critic/doer separation as essential for correct state admission
