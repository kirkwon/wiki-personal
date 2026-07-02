---
type: concept
title: Co-Failure Ceiling
created: 2026-06-28
updated: 2026-06-28
tags: [methodology, improvement, model]
sources: [papers/co-failure-ceiling]
---

# Co-Failure Ceiling

The fundamental upper bound on how much any multi-model strategy (routing, voting, cascades, mixture-of-agents) can improve accuracy. For any policy that outputs one member model's answer: **accuracy ≤ 1 − β**, where **β** is the rate at which all models are simultaneously wrong on the same query.

## Why It Matters

- **Correlation is not diversity.** Standard reporting of average pairwise error correlation ρ cannot identify β — different error distributions can have identical ρ but wildly different all-wrong rates ^[inferred]
- The all-wrong tail is systematically **underpriced by 2.5×** (observed β=0.052 vs Gaussian copula β=0.023 on open-ended math across 67 models)

## Practical Rules

1. **Estimate β before building a multi-model system** — Clopper-Pearson bound on a small sample gives the ceiling
2. If β < 1 − accuracy_of_best_model, **routing/voting cannot improve much**
3. Gains come from **diversity in failure patterns**, not model count ^[inferred]
4. **Free-response format** exposes larger co-failure tails than multiple-choice

## Impact on P3 Strategy

Validates the **single-model improvement** approach used by [[papers/ornith-1-self-improving-coding|Ornith-1.0]]: rather than building expensive ensembles, invest in making the single model better via [[concepts/scaffold-optimization]].

## Connections

- [[papers/co-failure-ceiling]] — the full paper page with empirical data
- [[concepts/scaffold-optimization]] — the alternative strategy (improve the single model, not the ensemble)
- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — validates that scaffold optimization beats raw ensemble scaling
