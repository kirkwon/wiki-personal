---
date: 2026-08-18
type: media
title: Interpretable Causal Discovery via Causal-Effect Constraints
created: 2026-08-18
updated: 2026-08-18
tags: [model, methodology, causal-inference]
sources: [https://arxiv.org/abs/2608.12640]
---

# Interpretable Causal Discovery via Causal-Effect Constraints

**Authors:** Cixuan Zhang, Guy Van den Broeck, Benjie Wang (UCLA StarAI)
**Submitted:** 12 Aug 2026 (v1)
**arXiv:** [2608.12640](https://arxiv.org/abs/2608.12640)
**Venue:** UAI 2026 — [PMLR v337, pp. 8071–8089](https://proceedings.mlr.press/v337/zhang26c.html)
**Code:** [MLS-Framework](https://github.com/ZCX031116/MLS-Framework) — Python, unlicensed, 0 stars (verified 2026-08-18)

## Core Method

**Conditional causal discovery**: compute the posterior over causal graphs G and parameters B *conditional on an event* — e.g., "this causal effect is large" or "these variables co-occur in a tail event." Standard Bayesian causal discovery collapses when the conditioning event has small posterior mass; the paper adapts **rare-event estimation (adaptive multilevel splitting)** to drive a particle population into the constrained region while maintaining samples that approximate the conditional posterior.

## Structure

- §4.1 Conditional causal discovery as a **score-level problem**
- §4.2 **Adaptive multilevel splitting** for rare posterior events
- §4.3 Particle initialization · §4.4 Inner Metropolis–Hastings over joint (G, B)
- §5 Validation: synthetic d=4, d=8 (single- and multi-effect conditioning)
- §6 Case study: **Sachs protein dataset (d=11)** — pathway-level summaries for scientific exploration
- §A.8 pseudo-code · CC BY 4.0

## Why It Matters for β (Co-Failure Rate)

Current β estimation is frequency counting (Clopper-Pearson on observed all-wrong rates). This paper reframes the same inferential target as conditional causal discovery: **posterior over causal structure given the observed event that components co-failed**. That distinguishes *shared-cause* co-failure (structural, fixable by removing the common dependency) from *coincidental* co-occurrence — exactly what naive co-occurrence rates conflate. Co-failures are tail events, which is precisely the rare-posterior-mass regime the method was built for. Validated scale (d=4–11 nodes) brackets stack-component counts.

## Caveats

- No license on the repo — reimplement from §A.8 pseudo-code if shipping anything derived.
- Demonstrated on Bayesian networks over tabular variables, not token-level agent scaffolds — the transfer to β is a method-level analogy, not a validated result. ^[inferred]

## Connections

- [[concepts/co-failure-ceiling]] — the β quantity this method could upgrade from statistics to causal estimation
- [[concepts/scaffold-optimization]] — potential diagnostic: which scaffold components causally co-fail
- [[papers/co-failure-ceiling]] — the empirical β paper (statistical ceiling); this is the causal follow-on
