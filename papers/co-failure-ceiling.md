---
date: 2026-06-28
type: media
title: Co-Failure Ceiling — When Combining Language Models Helps
created: 2026-06-28
updated: 2026-06-28
tags: [model, comparison, methodology, agent-systems]
sources: [raw/papers/2606.27288]
---

# Co-Failure Ceiling: When Does Combining Language Models Help?

**Title:** *When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models*
**Author:** Josef Chen
**Submitted:** 25 Jun 2026
**arXiv:** [2606.27288](https://arxiv.org/abs/2606.27288)
**Subjects:** cs.AI, cs.LG

## Core Finding

Multi-model LLM systems (routing, voting, cascades, mixture-of-agents) show **gains capped by co-failure rate β** — the fraction of queries where **every model in the ensemble is wrong simultaneously**.

> For any policy whose output is one member model's answer: **accuracy ≤ 1 − β**

This is the **Co-Failure Ceiling**: a fundamental upper bound on what any multi-model strategy can deliver, determined solely by the joint failure distribution of the ensemble.

## Why Correlations Are Misleading

Standard practice reports **average pairwise error correlation ρ** as a diversity metric. This paper proves ρ **cannot identify β**:

- Different error distributions can have identical ρ but **wildly different all-wrong rates**
- A tetrachoric-calibrated single-factor model underprices the all-wrong tail by **2.5×**
- This means ensembles appear more diverse (and more powerful) than they actually are

## Empirical Results

### β Across Tasks (67 models, 21 providers)

| Task | β (observed) | β (Gaussian copula) | Underpricing |
|------|:-----------:|:-------------------:|:-----------:|
| Open-ended math | **0.052** | 0.023 | **2.5×** |
| Execution-graded code | **0.079** | — | — |
| GPQA-Diamond (free-response) | **0.127** | — | — |

### Key Takeaways

1. **Low-ρ heterogeneous ensembles** (models that fail on different questions) beat **high-ρ Self-MoA** at matched quality — but the ceiling still applies
2. Over the whole pool, **combining rarely beats the single best model** without a strong query-level routing signal
3. Free-response tasks expose **larger co-failure tails** than multiple-choice — format matters more than subject
4. Five-judge panel agreement κ=0.73–0.92 for free-response grading, introducing measurement uncertainty

## Practical Guidance

### Before Building a Multi-Model System

1. **Estimate β** via Clopper-Pearson on a small sample — gives an upper bound on accuracy gain
2. If β is already small (e.g., < 1 − accuracy_of_best_model), routing/voting **cannot improve much**
3. Gains come from **diversity in failure patterns**, not model count
4. **Invest in query-level routing signal** before adding more models

### Applying β to P3 Evaluation

- [[papers/ornith-1-self-improving-coding|Ornith-9B]] vs ensemble: if Ornith's single-model accuracy on SWE-bench (69.4) is close to β for code tasks (β=0.079, ceiling=92.1%), then ensembles offer at most ~23% relative improvement
- For P3-T7 evaluation, report β alongside single-model accuracy to contextualize ensemble gains
- The "checkable tasks" finding supports Ornith's approach: improving the single model (via scaffold optimization) is often more effective than ensembling

## Connections

- [[concepts/scaffold-optimization]] — contrasts with ensemble ceiling: improving the single model's scaffold vs adding more models
- [[concepts/co-failure-ceiling]] — the formalized concept
- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — single-model approach validated by this paper's findings
- P3-T7 evaluation: report β to contextualize ensemble vs single-adapter trade-offs
