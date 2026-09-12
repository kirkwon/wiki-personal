---
date: 2026-08-23
type: media
title: "Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection"
created: 2026-08-23
updated: 2026-08-23
tags: [model, methodology, agents]
sources: [https://arxiv.org/abs/2608.20169]
---

# Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

**Authors:** Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki (University of Tokyo)
**Submitted:** 20 Aug 2026 (v1) · cs.CL primary, cs.AI, cs.LG cross-listed
**arXiv:** [2608.20169](https://arxiv.org/abs/2608.20169)
**Code:** [Agent4Science-UTokyo/Task-CoEvolve](https://github.com/Agent4Science-UTokyo/Task-CoEvolve) (announced in arXiv comments field; contents not yet audited)

## Core Method

Harness optimization iteratively rewrites scaffold/harness code against a validation set. Task-CoEvolve cuts its dominant cost — re-evaluating the full fixed validation set every iteration — via two mechanisms:

1. **Disagreement-weighted task selection.** Tasks where candidate harnesses *disagree* (one succeeds, one fails) are the informative ones for ranking candidates; consistently-solved and consistently-failed tasks are sampled out. Implemented as variance-weighted sampling over past Bernoulli outcomes, concentrating on the capability frontier, adapting as the harness evolves.
2. **Inclusion-probability score estimation.** Full-set scores are estimated from the sampled subset by accounting for each task's sampling probability (Horvitz-Thompson-style correction), keeping iterations comparable despite different subsets being evaluated.

## Results

- **Terminal-Bench 2.1:** matches the final performance of full-set search while reducing evaluations during optimization by **80%**.
- Online text classification: consistently outperforms fixed-subset baselines.

## Why It Matters for β (Co-Failure Rate)

The disagreement signal is operationally the co-success/co-failure table between candidates — the same quantity [[concepts/co-failure-ceiling|β]] estimation needs. Tasks where all candidates co-fail are explicitly non-informative for *ranking* and get sampled out; the sampler's logs therefore yield a cheap, continuously-updated β estimate across scaffold variants as a byproduct.

## Caveats

- Frontier-focused sampling down-weights consistently-solved tasks → **regression blindness on easy tasks**. Pair with a small fixed easy-task probe if capability loss must be caught (see [[papers/phantom-gains-self-improvement-null]]: self-training corrupts baseline-solved problems).
- Evidence base: one agent benchmark + one text-classification setting, single group.

## Connections

- [[concepts/scaffold-optimization]] — makes the scaffold-optimization loop's evaluation stage ~5× cheaper
- [[concepts/co-failure-ceiling]] — disagreement sampling ≈ cheap β estimator over scaffold variants
- [[papers/ornith-1-self-improving-coding]] — the scaffold-co-optimization model this evaluates around
