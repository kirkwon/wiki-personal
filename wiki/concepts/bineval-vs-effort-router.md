---
type: note
title: BINEVAL vs Effort Router - Pre-Task vs Post-Task Evaluation
links:
  - effort-router
  - raschka-reasoning-effort
  - blind-evaluation
  - model-selection-and-validation-frameworks
  - system-reassessment
  - inversion-premortem
  - pre-mortem-analysis
captured_at: '2026-07-19T07:34:56.137Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:34:56.429Z'
source_kind: put_page
tags:
  - bineval
  - effort-routing
  - evaluation
  - premortem
  - reward-signal
  - task-lifecycle
created: 2026-07-19
source: brain/ (retired 2026-09-13)
---
# BINEVAL vs Effort Router — Pre-Task vs Post-Task Evaluation

Comparison of two evaluation systems in the Hermes stack. They solve different problems at different stages of the task lifecycle and are complementary, not interchangeable.

**Created:** 2026-07-19 (during premortem and triaging work)

## The Core Distinction

- **Effort Router** runs *before* a task — allocates compute by predicting effort needed
- **BINEVAL** runs *after* a task — evaluates output quality via binary question decomposition

They operate on orthogonal axes: resource allocation vs quality measurement. Using one for the other's job is a category error.

## Side-by-Side

| Dimension | BINEVAL | Effort Router |
|-----------|---------|---------------|
| **Lifecycle stage** | Post-task (evaluates output) | Pre-task (allocates resource) |
| **Question answered** | "How good was this?" | "How hard should the model try?" |
| **Output** | Continuous score [0,1] from binary aggregation | Discrete category {low, medium, high, max} |
| **Method** | Decompose criteria into 5-10 yes/no questions, aggregate | Rule-based keyword match then Thompson sampling bandit |
| **Learns?** | No — training-free, questions fixed per criterion | Yes — Tier 3 bandit learns from outcome feedback |
| **Optimizes** | Evaluation variance, interpretability, debuggability | Token cost efficiency |
| **Source** | Cho et al. 2026 (arxiv 2606.27226) | Raschka two-knob framework + Thompson sampling |

## Where Each Lives in the Stack

**BINEVAL** (7 skills, post-production evaluation):
- meta-critic — reward signal decomposition for RL
- critical-review — 7 dimensions to binary sub-questions
- grill-me — stress-test pass/fail gating
- impl-validator — spec compliance checks
- autoresearch — single float to BINEVAL sub-metrics
- judgment-equation — heuristic trust to binary questions

**Effort Router** (pre-production resource allocation):
- Cron system — set reasoning_effort on scheduled jobs
- delegate_task — route by funnel phase (Explore low, Sieve medium, Execute high)
- Dispatch skill — pre-classify before routing to agent

## The One Real Intersection

The single point where they touch: the effort router's outcome signal.

Currently the bandit rewards on a crude success/failure binary. BINEVAL could enrich that signal by decomposing success into:
- Did the output meet spec? (yes/no)
- Was it complete on first pass? (yes/no)
- Did it require retries? (yes/no)
- Did it introduce regressions? (yes/no)

A BINEVAL-decomposed reward gives the bandit a richer gradient — it learns WHY low effort failed, not just that it failed.

Conversely, the effort router could control how many BINEVAL questions get asked: a quick cron summary gets 3 binary checks (low evaluation effort); a production deploy gets 10 (high evaluation effort). Same two-knob principle applied to the evaluation layer itself.

## Correct Architecture (Sequential, Not Interchangeable)

```
Effort Router (BEFORE)
    → Task runs at chosen effort level
        → BINEVAL (AFTER)
            → reward signal feeds back to bandit
```

Using BINEVAL to decide effort is circular (need output to evaluate it). Using effort router to evaluate quality is a category error (does not assess artifacts, allocates budget).

## Connection to Premortem and Triaging

This comparison emerged during premortem and triaging work. The relevance:

- **Premortem:** When stress-testing a plan before execution, the effort router decides how much reasoning to spend ON the premortem itself. A high-stakes deploy premortem should run at high effort; a routine cron premortem at low. BINEVAL then evaluates whether the premortem surfaced real risks (binary: did it identify a failure mode that would have occurred?).
- **Triaging:** When triaging tasks by priority, the effort router determines execution cost per task. BINEVAL evaluates whether triage decisions were correct (binary: was the task actually as urgent as classified?). Together they enable cost-aware triage — not just "what matters most" but "what matters most per token spent."

The triage-premortem-effort loop:
```
Triaging (priority) → Effort Router (cost) → Premortem (risk check) → BINEVAL (was risk check thorough?)
```

## Related Concepts

- effort-router — the pre-task resource allocator
- raschka-reasoning-effort — the conceptual origin (two-knob framework)
- blind-evaluation — BINEVAL benefits from blind scoring (reduces judge bias)
- model-selection-and-validation-frameworks — both systems are validation frameworks at different lifecycle stages
- system-reassessment — this comparison IS a system reassessment (evaluating how evaluation tools relate)
