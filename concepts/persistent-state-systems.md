---
type: concept
title: "Persistent-State Systems"
created: 2026-07-06
updated: 2026-07-06
tags: [agent-systems, technology, cognitive-science]
sources: [papers/always-on-agents-survey]
summary: An always-on agent is not a memory-augmented LLM but a persistent-state system whose state includes retrievable memory, task ledgers, permissions, tool state, provenance records, and shared state — all governed over a lifecycle, not just accumulated and retrieved.
---

# Persistent-State Systems

## Definition

A **persistent-state system** is an agent that carries state across tasks and is analyzed not by what it remembers but by how that state is *governed* — admitted, attributed, scoped, mutated, recovered, and revoked over a lifecycle.^[papers/always-on-agents-survey]

The reframing from "memory-augmented LLM" to "persistent-state system" expands the unit of analysis:

| Traditional "Memory" View | Persistent-State View |
|---|---|
| What can the agent recall? | What state does the agent carry and how is it governed? |
| Accumulate and retrieve | Observe → write → validate → organize → retrieve → act → update → forget → audit → rollback |
| Store the interaction, retrieve later | Admit at the write boundary under a scope and authority label |
| Most similar to the query | The authoritative record; authority only narrows |
| Append a newer entry | Mutate with provenance; mark prior truth superseded |
| Delete the row, hope it propagates | Cascade deletion, verify completeness, log the rollback |
| Downstream task accuracy | Score the governance obligation directly |

## Why the Distinction Matters

An episodic assistant that answers a question and forgets it can be wrong without making the error durable. An always-on agent **inherits what it wrote yesterday**. Its competence and its liabilities both compound — the substrate that lets it carry knowledge forward is the same substrate that lets a stale preference, a poisoned trace, or a lapsed permission govern an action taken months later.

Classical cognitive architectures (Soar, ACT-R) separated procedural, episodic, and semantic stores within a single decision cycle, and the complementary-learning-systems tradition explained why fast capture and slow consolidation must be on different timescales. Modern agent frameworks ported these modules into LLM systems but **ported the storage without the governance**: the cognitive theories assumed type boundaries and decay schedules enforced by biology, whereas an LLM agent mixes fast and slow updates in flat text with no runtime enforcement of who wrote what, with what authority, recoverable by whom.

## Relationship to Existing Work

The persistent-state systems concept is the foundational framing of the [[papers/always-on-agents-survey]]. It connects to:

- [[concepts/state-governance-lifecycle]] — the ten-stage lifecycle over which persistent state is governed, including the five invariants and forward/return arc asymmetry
- [[concepts/six-state-axes]] — the six dimensions (authority, scope, mutability, provenance, recoverability, actionability) along which persistent state is characterized
- [[concepts/self-maintaining-knowledge-base]] — self-maintaining KBs are persistent-state systems applied to documentation; the drift-detect-approve loop is a governance lifecycle instance
- [[concepts/loop-engineering]] — loop engineering's critic/doer separation is a governance primitive: the critic enforces that the doer's state changes pass validation before becoming durable
