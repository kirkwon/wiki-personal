---
date: 2026-08-18
type: entity
title: E2-Explainer — Causal Explanations of MAS Communication Topologies
created: 2026-08-18
updated: 2026-08-18
tags: [agent-systems, methodology, causal-inference]
sources: [https://arxiv.org/abs/2608.12921]
---

# E2-Explainer: Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference

**Authors:** Junzhi Li, Peng He, Qirui Ji, Wei Wang, Lixiang Liu, Chuxiong Sun
**Submitted:** 13 Aug 2026 (v2 updated 14 Aug 2026)
**arXiv:** [2608.12921](https://arxiv.org/abs/2608.12921)
**Code:** none found (checked 2026-08-18)

## Core Method

Formulates **topology explanation as causal attribution**: identify compact communication subgraphs supported by edge-level evidence of task preservation. Evidence comes from a **Granger-style masking objective** — mask each communication channel, measure the change in task outcome and response stability. Budgeted critical subgraphs are then **distilled into an amortized explainer** for cheap post-hoc explanation at deployment.

## Key Result

The identified critical subgraphs **execute directly**: pruning redundant communication edges substantially cuts communication cost while maintaining competitive task performance (reasoning + coding benchmarks).

## Relevance to Our Stack

- **Skill saliency by intervention**: the masking objective is a do-operator — transferable to ablating skills in a stack and measuring outcome delta, vs observational embedding similarity. ^[inferred]
- **Amortized explainer = routing signal**: expensive masking evaluations distilled into a cheap predictor of load-bearing channels is structurally the same problem as skill routing/selection in the Skill Subspace. ^[inferred]
- **Pruning result generalizes the redundancy prediction**: semantically adjacent components may be causally redundant — prune without performance loss.

## Connections

- [[concepts/co-failure-ceiling]] — analog rule: gains come from causal complementarity, not component count
- [[concepts/scaffold-optimization]] — scaffold *compression*: minimal subgraph that preserves outcome
- [[papers/causal-discovery-effect-constraints]] — same-week causal-inference thread; that one estimates structure from observations, this one intervenes (masking)
