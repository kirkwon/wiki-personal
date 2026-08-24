---
date: 2026-08-23
type: entity
title: "Phantom Gains: Auditing Self-Improvement Against a Measured Null"
created: 2026-08-23
updated: 2026-08-23
tags: [model, methodology, evaluation]
sources: [https://arxiv.org/abs/2608.20290]
---

# Phantom Gains: Auditing Self-Improvement Against a Measured Null

**Authors:** Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi
**Submitted:** 20 Aug 2026 (v1) · cs.AI primary, cs.CL
**arXiv:** [2608.20290](https://arxiv.org/abs/2608.20290)
**Code:** [chengxuphd/phantom-gains](https://github.com/chengxuphd/phantom-gains) (code + evaluation artifacts)

## Core Method

Audits three rounds of rank-32 LoRA self-training on Qwen3-8B by pushing a **frozen, untrained control through the identical pipeline**. Identifies **seven measurement failures**, each of which inverts a reported finding when the control is absent. Several are standard practice:

- A per-problem gain/loss ledger built on a **single greedy decode** manufactures capability changes on the untrained model, largely an inference-**batching artifact** (phantom expansion rate 0.280 on the frozen control).
- The natural threshold repair does not survive replication — its null stays non-zero.

**Replacement protocol:** pool every baseline evaluation into one reference (per-problem exact [Fisher] tests under FDR control), which detects nothing on any held-out replicate and is stable under multiple-testing rule, error rate, and pool size.

## Findings

- **External distillation improves problems the base model rarely reaches; three forms of self-training do not.** A regression rejects the asymmetry as a by-product of distillation's larger overall gain (p < 10⁻⁸).
- On problems the base model never reaches: evidence inconclusive.
- **Self-training corrupts problems solved at baseline** at rates well above the measured floor.
- Teacher effect on low-base-rate problems estimated at β = 1.91 [1.25, 2.56] ^[secondary — from the arXiv monitor's full-text read, not in the abstract]
- Nulls cost no new experiments: build them from baseline replicates a multi-arm study already owns — "though not from as few as most possess."

## Why It Matters for β (Co-Failure Rate)

Every transition-level statistic — including co-failure rates — needs a **separately measured null** built from baseline replicates. Naive β computed from single-run ledgers inherits exactly the phantom-transition artifacts documented here. Hard constraint on P3 evaluation design: adapter-vs-baseline deltas are untrustworthy without a frozen control pushed through the same pipeline.

## Caveats

- Single base model (Qwen3-8B), single rank (32), math-domain evaluation (AIME-style) — transfer to agent/terminal domains is plausible but unverified ^[inferred]
- Pooled-baseline Fisher testing requires many baseline draws per problem; plan the replicate budget upfront.

## Connections

- [[concepts/co-failure-ceiling]] — β estimators need the measured-null discipline this paper formalizes
- [[concepts/scaffold-optimization]] — gates every self-improvement claim the loop makes
- [[concepts/skill-utility-gating]] — companion theme: self-generated artifacts need audit before trust
- [[papers/task-coevolve-harness-optimization]] — pairs as the cost-reducer this paper's audit makes affordable
