---
date: 2026-07-06
type: concept
title: "Six State Axes"
created: 2026-07-06
updated: 2026-07-06
tags: [agent-systems, methodology, technology]
sources: [papers/always-on-agents-survey]
summary: Six dimensions for characterizing persistent agent state — authority, scope, mutability, provenance, recoverability, and actionability — each with associated invariants that tie them to the governance lifecycle.
---

# Six State Axes

## Definition

The six state axes are dimensions along which persistent state in an always-on agent can be characterized. Each axis carries governance obligations that must be enforced across the [[concepts/state-governance-lifecycle|lifecycle]].^[papers/always-on-agents-survey]

They define what the agent must know about every piece of state it carries:

| Axis | Question | Corpus Count (of 435) |
|---|---|:---:|
| **Authority** | Who may read, write, delete, or act on this state? | **72** (rarest) |
| **Scope** | Where may this state legitimately apply? | Moderately studied |
| **Mutability** | How does this state change under new evidence? | Partially studied |
| **Provenance** | Where did this state come from, through what transformations? | Partially studied |
| **Recoverability** | Can a change to this state be undone? | 27 (rollback) |
| **Actionability** | Can this state drive an external effect? | Moderately studied |

## The Six Axes in Detail

### 1. Authority

**Who may read, write, delete, or act on a piece of state?**

Authority is the rarest axis in the corpus at 72/435 — not an accident of coding, but a structural consequence of the accumulate-and-retrieve paradigm having no reason to represent it. An always-on agent that never checks who licensed a fact will treat a preference that was true last month (changed yesterday) as still authoritative today, and will let any stored fact influence any action.

**Invariant: Authority monotonicity** — authority can narrow over time but never silently widen. A permission granted for task X does not automatically extend to task Y. The validate stage must enforce this at write/promotion time.

Key works: Lahjouji and Colaco 2026 (privacy survey), Shah et al. 2026 (deletion verification), Qin et al. 2026 (AirGuard runtime authority control).

### 2. Scope

**Where may this state legitimately apply?**

Scope defines the boundary within which a record is authorized to influence actions. Without scope gating, accumulated state drifts — routine interactions gradually expand the agent's effective action scope without any single step looking like an attack.

**Invariant: Scope non-expansion** — a record's applicability cannot grow beyond its admission boundary without explicit re-licensing.

Key works: Xu et al. 2026b (RBI-Eval — agents integrate sensitive memory even when unwarranted), Ibrahim and Li 2026 (compositional authorization framework).

### 3. Mutability

**How does this state change when new evidence contradicts it?**

Mutability governs whether state is append-only, versioned, or mutable — and what happens when a new observation contradicts an existing record. A preference that was true last month and changed yesterday is still retrievable today; the question is whether the agent treats it as superseded or current — a mutability-and-provenance decision no retriever makes.

**Invariant link: Provenance preservation** — when state mutates, the prior version must be marked superseded (not silently overwritten), with a traceable chain.

Key works: Park 2026 (graph-native versioned memory satisfying AGM belief-revision postulates), Wang 2026b (bitemporal operator algebra for contradiction resolution).

### 4. Provenance

**Where did this state come from, and through what transformations?**

Provenance tracks the lineage of every piece of state — who authored it, under what authority, through what consolidation steps. This is critical for audit, rollback, and contamination detection.

**Invariant: Provenance preservation** — source attribution survives consolidation. Summarization that scores well on aggregate recall while dropping retrieval handles (names, identifiers, dates, keys) violates this invariant.

Key works: Ouyang and Hou 2026 (MemLineage — lineage-guided enforcement), Jin and Li 2026b (typed memory to prevent provenance-role collapse), Dalugoda 2026 (append-only signed delegation-provenance chain).

### 5. Recoverability

**Can a change to this state be undone?**

Recoverability covers rollback, checkpoint-restore, and the ability to revert to a prior state. The 27/435 figure undercounts the problem: even among those works, none reports the quantities an operator actually needs (recovery success rate, state loss on recovery, latency and compute costs).

**Invariant: Rollback traceability** — every mutation has a recoverable prior state with a logged chain. Three subclasses: internal-state rollback, workflow rollback (compensation), and external-effect rollback (undoing irreversible side effects).

Key works: Chang and Geng 2025 (Saga model import), Zheng et al. 2026d (semantic rollback attacks in checkpoint-restore), Nakajima 2026 (event-sourced runtime with deterministic replay), Shawn et al. 2026 (anytime-valid betting gate for commit decisions).

### 6. Actionability

**Can this state drive an external effect?**

Actionability captures whether stored state can trigger or license external actions — tool calls, payments, deletions, messages. This is the axis where governance gaps are most consequential: state that crosses from passive storage into action without proper authority and scope checks creates the failure modes the survey catalogs (poisoned traces governing actions, lapsed permissions executing tools).

The actionability axis is where the [[concepts/state-governance-lifecycle|lifecycle]] forward arc and return arc meet: retrieve feeds act, but act without validated authority/scope/recoverability is the governance failure.

## Cross-Axis Composition

The survey's central argument is that these six axes are not independently satisfiable — they interact:

- Authority + recoverability → who may rollback tool-originated state after authority lapses (the thinnest corpus area)
- Provenance + actionability → can a poisoned trace's lineage be traced and its downstream actions reverted?
- Scope + mutability → when scope narrows, do all in-scope mutations preserve the narrowed boundary?

No current system composes all six. The frontier program (Table 21 in the survey) targets integration across all axes and invariants with unified evaluation.

## Connections

- [[papers/always-on-agents-survey]] — the source survey defining these axes
- [[concepts/persistent-state-systems]] — the system model these axes characterize
- [[concepts/state-governance-lifecycle]] — the lifecycle stages these axes govern
- [[concepts/always-on-evaluation-protocol-aoep]] — the protocol that tests invariant satisfaction across these axes
