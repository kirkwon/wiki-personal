---
type: concept
title: Socratic Sieve
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Socratic Sieve
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- strategy
- decision-making
- socratic
- bayesian-rogue
- sieve
- funnel
- risk-analysis
sources:
- hermes://skill/socratic-sieve
description: Phase 2 of the Bayesian Rogue funnel. Takes 3+ candidate options (from
  bayesian-rogue-explore or user-provided) and stress-tests them through Socratic
  questioning, assumption mapping, failure mode analysis, and leverage identification
  to produce a ranked recommendation with explicit trade-offs. Use whenever a decision
  has 3+ options and the user needs help choosing — especially for high-stakes, irreversible,
  or resource-intensive decisions.
---

# Socratic Sieve

> Phase 2 of the Bayesian Rogue funnel. Takes 3+ candidate options (from bayesian-rogue-explore or user-provided) and stress-tests them through Socratic questioning, assumption mapping, failure mode analysis, and leverage identification to produce a ranked recommendation with explicit trade-offs. Use whenever a decision has 3+ options and the user needs help choosing — especially for high-stakes, irreversible, or resource-intensive decisions.

## Overview

- **When to Use** — - You have 3+ options (from `bayesian-rogue-explore` or provided by the user) and need to choose - High-stakes or resource-intensive decisions where the wrong choice is expensive - The user is stuck between approaches and needs structured disambiguation - Before committing to execution (feeds into `leverage-executor`)
- **When NOT to Use** — - Only 1 option exists (just evaluate it directly) - The decision is trivially reversible (use `leverage-executor` and iterate) - The user has already decided and wants execution (skip to `leverage-executor`)
- **Contrast Table (Practitioner-Verified)** — | Do This | Not This | Why | |---------|----------|-----| | Map full assumption chains (foundational → derivative → boundary → hidden) | List only the obvious assumptions | Derivative assumptions carry hidden biases; the chain reveals where logic breaks | | Run failure mode analysis BEFORE recommendation | Run it after you've already decided | Failure analysis before = genuine risk assessment; after = rationalization | | Quantify resource requirements realistically | Assume "it'll take about X" without decomposition | Underestimating resources is the #1 execution failure cause | | Question whe

## Further detail

### Pitfalls

- ❌ Treating the sieve as confirmation rather than adversarial test — the point is to *break* options, not validate them - ❌ Skipping the hidden assumption layer — this is where the most dangerous biases live - ❌ Equal weighting when stakes differ — a foundational assumption failure is fatal; a derivative failure is manageable - ❌ Presenting a single "winner" without showing the trade-offs — the user needs to see *why* the losers lost - ❌ Forgetting the kill condition — every recommendation needs an exit criterion - ❌ Running the sieve when only 1 real option exists — if there's no genuine cho

### Integration with the Funnel

The sieve receives options from `bayesian-rogue-explore` and hands its recommendation to `leverage-executor`. It can also run standalone on user-provided options.

### References

- `references/worked-example-hermes-improvement.md` — full worked example applied to "How should I improve Hermes?"

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/strategy/socratic-sieve/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
