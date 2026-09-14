---
type: note
title: Effort Router - Two-Tier Reasoning Effort Classifier
links:
  - adaptive-rl-metascheduling-runtime
  - reinforcement-learning-adaptive-resource-scheduling
  - pattern-analysis
captured_at: '2026-07-19T07:26:57.462Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:26:57.740Z'
source_kind: put_page
tags:
  - bandit
  - effort-routing
  - llm-optimization
  - reasoning-effort
  - thompson-sampling
created: 2026-07-19
source: brain/ (retired 2026-09-13)
---
# Effort Router — Two-Tier Reasoning Effort Classifier

A reasoning-effort classification system for LLM calls, built for Hermes Agent. Maps task descriptions to reasoning_effort levels (low/medium/high/max) to minimize token cost while maintaining task success.

**Built:** 2026-07-19
**Location:** ~/.hermes/skills/decision/effort-router/

## Origin

Sebastian Raschka's article on Controlling Reasoning Effort in LLMs (magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms) describes a two-knob framework: model size and reasoning effort are separate axes that overlap. A smaller model at high effort can match a larger model at low effort. The cheapest point shifts by task type. Hermes treated every task the same — no effort routing. This system fills that gap.

## Architecture

Two tiers with cold-start fallback:

### Tier 1: Rule-Based Router
- Deterministic keyword classifier (stdlib regex, first-match-wins)
- ~34 microseconds latency, no model calls
- Categories: LOW (read/list/cron/digest), HIGH (email/deploy/commit/review/debug), MAX overrides, else MEDIUM
- Logs every classification to JSONL — this is Tier 3's training data contract

### Tier 3: Learned Router (Thompson Sampling Bandit)
- Per-cluster Beta-Bernoulli bandit over 4 effort arms
- TF-IDF + MiniBatchKMeans task clustering
- Cost-aware: score = beta_sample / effort_cost_weight (prefers cheaper arms at similar success probability)
- Non-stationary: decay_all() shrinks Beta params toward prior for drift handling
- Cold-starts from Tier 1 rules — never breaks when untrained

### Tier 2: A/B Bridge
- ABRouter splits traffic 50/50 between rule-based (control) and learned (treatment)
- Logs outcomes to determine which implementation wins

## Key Connections

- **Related to:** adaptive-rl-metascheduling-runtime — both use RL for runtime resource optimization. The metascheduling paper applies RL to hardware task scheduling; effort router applies Thompson sampling to LLM inference effort.
- **Related to:** reinforcement-learning-adaptive-resource-scheduling — same family of adaptive resource allocation. Effort routing IS resource scheduling where the resource is reasoning compute.
- **Related to:** pattern-analysis — task pattern clustering (TF-IDF + KMeans) is a form of digital-life pattern analysis applied to LLM workloads.

## Implementation Notes

The stochastic testing required statistical thresholds, not strict equality asserts (Thompson sampling has exploration noise from uniform Beta priors on unexplored arms). See build-tiered-effort-router skill for the 5 pitfalls encountered.

## Files

- scripts/effort_router.py — Tier 1 rule-based classifier
- scripts/bandit_router.py — Thompson sampling core
- scripts/task_vectorizer.py — TF-IDF + KMeans clustering
- scripts/learned_router.py — Integrated router with cold-start
- scripts/ab_router.py — A/B testing harness
- scripts/retrain.py — Batch retrain from JSONL logs
- tests/ — 67 tests (43 Tier 1, 24 Tier 3), all green
