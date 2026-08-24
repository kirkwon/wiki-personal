---
date: 2026-06-21

type: concept
title: "Verifiable Planning"
category: concepts
tags: [concept, ai, planning, verification, formalization, reliability]
sources: ["arxiv:2510.04542"]
summary: "Making AI planning decisions verifiable by encoding rules as executable code — correctness becomes decidable rather than probabilistic."
base_confidence: 0.50
lifecycle: draft
lifecycle_changed: "2026-06-21"
tier: core
provenance:
  extracted: 0.55
  inferred: 0.45
  ambiguous: 0.0
relationships:
  - target: "[[concepts/code-world-models]]"
    type: related_to
  - target: "[[concepts/llm-as-compiler]]"
    type: related_to
  - target: "[[concepts/strategic-decision-framework]]"
    type: related_to
  - target: "[[papers/code-world-models-general-game-playing]]"
    type: derived_from
created: 2026-07-26
updated: 2026-07-26
---

# Verifiable Planning

**Verifiable planning** is the principle that AI-generated plans should be checkable for correctness against formal constraints. When rules are encoded as executable code, the question "is this move legal?" becomes a decidable computation rather than a probabilistic judgment.^[extracted]

## The Verification Advantage

The CWM paper's deepest insight is that **formalization enables verification**:^[extracted]

> "Contingent on the generated code being correct, this completely eliminates the problem of illegal moves."

This is a categorical improvement over probabilistic approaches:
- **Probabilistic LLM:** "This move is probably legal (95% confidence)"
- **Verified CWM:** "This move IS legal (the code returned True)"

## The Verification Hierarchy

| Level | What's Verified | Residual Risk |
|-------|----------------|---------------|
| 1. Move legality | Action conforms to rules | None (if code is correct) |
| 2. State validity | Resulting state is reachable | None |
| 3. Code correctness | CWM accurately reflects rules | **Translation errors** (LLM misunderstanding rules) |
| 4. Heuristic quality | Value function is reasonable | Approximation errors |

The residual risk concentrates at **Level 3** — did the LLM correctly translate the rules? This is a single point of failure that can be addressed with:^[inferred]

- Unit tests on the generated CWM
- Property-based testing (play random games, check invariants)
- Cross-validation (generate CWM twice, check consistency)
- Human review of edge cases

## Application to Strategic Decision-Making

The verifiable planning principle extends beyond games to any [[concepts/strategic-decision-framework|strategic decision]]:^[inferred]

- **Investment rules** → code as portfolio constraints → verify all trades comply
- **Risk management** → code as risk model → verify exposure limits
- **Game-theoretic equilibrium** → code as payoff matrix → verify Nash conditions

The pattern: **if a decision rule can be expressed in natural language, it can be formalized, and if it can be formalized, it can be verified.**^[inferred]

## Connection to Formal Methods

Verifiable planning bridges AI and formal methods:^[inferred]

- **Model checking** — verify properties hold across all states
- **Theorem proving** — prove the CWM satisfies game rules
- **Abstract interpretation** — over-approximate legal states

## Cross-References

- [[concepts/code-world-models]] — Where this concept originates
- [[concepts/llm-as-compiler]] — The architectural pattern enabling it
- [[concepts/strategic-decision-framework]] — Application to broader decision-making
- [[papers/code-world-models-general-game-playing]] — Source paper
