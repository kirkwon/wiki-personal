---
date: 2026-06-13

type: concept
title: Ergodicity
related:
  - tail-event-thinking
  - margin-of-safety-financial
  - leverage-and-randomness
  - base-rate-neglect
ingested_via: put_page
ingested_at: '2026-06-13T17:08:28.103Z'
source_kind: put_page
tags:
  - concept
  - decision-making
  - mental-model
  - probability
  - risk
  - strategy
---

# Ergodicity

**Also known as:** Ensemble vs Time Averages, Non-Ergodicity, Ruin Probability

A mathematical property of systems where time averages equal ensemble averages. When a system is non-ergodic (most real-world systems), what works for a group does NOT work for an individual over time.

## Core Idea

Most strategic advice is based on **ensemble averages** — what works across many people or many attempts. But individuals live in **time averages** — a single sequence of decisions over time. In non-ergodic systems (most of finance, entrepreneurship, career decisions), ensemble advice is dangerously misleading.

## The Key Insight

```
Ensemble average: 100 people each try once → 70 succeed
Time average: 1 person tries 100 times → they go bankrupt on attempt 15
```

The difference is **ruin probability**. If there's any chance of total loss (ruin), the ensemble average is irrelevant to the individual. The optimal strategy for the individual is the one that minimizes ruin, not the one that maximizes expected value.

## Connection to Strategic Framework

Ergodicity refines **Step 2 (Asymmetric Upside)** and **Step 4 (Resource Positioning)**:
- An opportunity may look like asymmetric upside in expectation but be non-ergodic in practice
- Kelly Criterion is the mathematical correction for non-ergodicity (optimal growth ≠ maximum EV)
- If a decision has a path to ruin, it's non-ergodic and should be filtered differently

## Practical Test

Ask: "If I made this decision 100 times in sequence, would I be better off or bankrupt?"
- If any single iteration can cause unrecoverable loss → non-ergodic, apply Kelly
- If losses are always recoverable → ergodic, expected value works

## Related
- Kelly Criterion — optimal bet sizing for non-ergodic systems
- Tail Event Thinking — rare events that cause ruin
- Margin of Safety — buffer against non-ergodicity
- Leverage and Risk — leverage amplifies non-ergodicity
