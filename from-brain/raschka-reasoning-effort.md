---
type: note
title: Controlling Reasoning Effort in LLMs (Raschka)
links:
  - effort-router
  - reinforcement-learning
captured_at: '2026-07-19T07:27:27.131Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:27:27.324Z'
source_kind: put_page
tags:
  - inference
  - llm-optimization
  - model-routing
  - reasoning-effort
created: 2026-07-19
---
# Controlling Reasoning Effort in LLMs (Raschka)

Sebastian Raschka's article on the two-knob framework for LLM reasoning effort optimization. Published at magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms.

## Core Insight

Model size and reasoning effort are separate axes that overlap. A smaller model at high effort can match a larger model at low effort. The cheapest point on this surface shifts by task type.

## The Two Knobs

1. **Model size** — which model to call (parameter count)
2. **Reasoning effort** — how many reasoning tokens to allow (low/medium/high/max)

These are not redundant. A 7B model at max effort can outperform a 70B model at low effort on some tasks, at a fraction of the cost. The optimization surface is non-trivial.

## Key Observations

- GPT-5's "Auto" mode for effort selection was "more miss than hit" per Raschka — the automatic router often picked the wrong level
- The "holy grail" is automatic effort classification — routing each task to the cheapest effort level that succeeds
- Inputs to a good classifier: task type (deterministic vs exploratory vs precision), failure cost (external side effects vs read-only), historical success rate, token/compute budget

## Connection to Effort Router

This article is the conceptual origin of the [[effort-router]] system. The effort router implements the three-tier approach Raschka describes:

1. **Tier 1 (rule-based):** keyword classification — the minimum viable router
2. **Tier 2 (cheap-model classifier):** a small model classifies each task — Raschka's direct suggestion
3. **Tier 3 (learned router):** multi-armed bandit (Thompson sampling) that learns the cheapest effort level per task type — the actual optimization

The effort router cold-starts from rules (Tier 1) and learns over time (Tier 3), which addresses GPT-5's Auto-mode failure: instead of a one-shot classifier, it continuously learns from observed outcomes.

## Related

- [[reinforcement-learning]] — the learned router is an RL problem (multi-armed bandit over effort levels)
