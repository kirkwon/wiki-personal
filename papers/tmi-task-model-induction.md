---
date: 2026-08-23
type: media
title: "Inducing Task Models from Computer-Use Traces (TMI)"
created: 2026-08-23
updated: 2026-08-23
tags: [model, agents, skills, methodology]
sources: [https://arxiv.org/abs/2608.20319]
---

# Inducing Task Models from Computer-Use Traces (TMI)

**Authors:** Yucheng Jiang, Zora Zhiruo Wang, Ruishi Chen, Diyi Yang (Stanford)
**Submitted:** 20 Aug 2026 (v1) · cs.CL primary, cs.AI
**arXiv:** [2608.20319](https://arxiv.org/abs/2608.20319)
**Code:** [Yucheng-Jiang/task-model-induction](https://github.com/Yucheng-Jiang/task-model-induction) (from monitor verification; contents not yet audited)

## Core Method

**Task Model Induction (TMI)** turns passively recorded computer-use traces (screenshots + mouse/keyboard events) into symbolic, auditable task models:

1. **Latent task discovery** — disentangles concurrent, interleaved activity in an unconstrained trace into distinct latent tasks.
2. **Task model induction** — for each latent task: a hierarchical **objective model** (recursive goal decomposition) paired with a **procedure model** (control flow that organized the execution).

## Results

- **Intrinsic:** recovers interleaved tasks with **0.974 agreement** vs ground-truth groupings; reconstructs **74.9%** of observed execution steps — far more than the strongest workflow-induction baseline.
- **Extrinsic:** skills derived from TMI task models improve held-out task accuracy by **30.0%** over the strongest baseline.

## Why It Matters

A concrete automated skill-acquisition pipeline from computer-use telemetry — the missing "trace → skill" front-end for any P3 trace-collection stage. Task disentanglement of interleaved sessions matters for failure attribution: without it, failures from concurrent tasks get credited to the wrong skill, contaminating co-failure statistics ^[inferred].

## Caveats

- "Controlled human and agent trajectories" — the 0.974/74.9% numbers are on controlled traces; unconstrained wild traces will be noisier ^[inferred]
- +30% extrinsic is over the strongest *workflow-induction* baseline, not over hand-authored skill libraries ^[inferred from abstract wording]

## Connections

- [[concepts/skill-utility-gating]] — mined skills need utility gates before reuse (see Break It Down, Pass It On)
- [[concepts/scaffold-optimization]] — procedure models are executable scaffolds mined from execution
- [[concepts/co-failure-ceiling]] — task disentanglement is a prerequisite for clean skill-level β
