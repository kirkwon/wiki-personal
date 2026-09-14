---
type: concept
title: Always-On Evaluation Protocol
ingested_via: put_page
ingested_at: '2026-07-06T07:41:28.480Z'
source_kind: put_page
tags:
  - always-on-agents
  - aoep
  - benchmarking
  - evaluation
  - governance
  - invariants
created: 2026-07-06
source: brain/ (retired 2026-09-13)
---
# Always-On Evaluation Protocol (AOEP)

## Definition

AOEP (Always-On Evaluation Protocol) is a two-pass evaluation framework designed to assess always-on agents along governance dimensions that standard single-turn benchmarks cannot capture. Introduced as v0 in Ding et al. (2026), "Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents" (arXiv:2606.30306).

## Design: Event Stream + State Snapshot

AOEP-v0 operates on two input traces collected from an agent's execution:

1. **Event Stream** — ordered log of all agent actions, state writes, reads, and external interactions over the evaluation period
2. **State Snapshot** — point-in-time dump of the agent's full state (object state, governance envelope, external commitments) at regular intervals

These traces are then evaluated against the agent's declared invariants and obligation set.

## Two-Pass Architecture

### Pass 1: Obligation Pass
**Question**: Did the agent fulfill all committed obligations?

- Check every obligation in the External Commitments layer
- Verify scheduled actions were executed on time
- Verify promises and deadlines were met
- Score: fraction of obligations satisfied / total obligations committed

### Pass 2: Negative-Invariant Pass
**Question**: Did the agent violate any declared invariants?

- Replay the event stream against the five governance invariants (consistency, completeness, non-contradiction, auditability, bounded obligation)
- Flag any state transition that produced a violation
- Score: 1.0 if zero violations; otherwise severity-weighted violation count

## Pilot Results

Key finding: **The governance gap is structural, not incidental.**

Agents that score high on standard benchmarks (MMLU, HumanEval, AgentBench) routinely fail the AOEP obligation pass. This is not a matter of imperfect implementation — the architectures themselves lack the return arc machinery (Update, Forget, Audit, Rollback) needed to maintain governance invariants over time.

### Implications

- Single-turn benchmarks are necessary but insufficient for always-on agent evaluation
- The obligation pass catches a distinct failure mode: agents that are competent but unreliable
- The negative-invariant pass catches another: agents that accumulate silent corruption
- Both passes must be used together for meaningful always-on evaluation

## Connections

- Extends [[always-on-agents-survey|Always-On Agents Survey]] (source paper)
- Governs [[persistent-state-systems|Persistent State Systems]] via the [[state-governance-lifecycle|State Governance Lifecycle]]
