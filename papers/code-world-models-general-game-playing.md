---
date: 2026-06-21

type: paper
title: "Code World Models for General Game Playing"
authors: ["Lehrach, W.", "Hennes, D.", "Lazaro-Gredilla, M."]
institution: Google DeepMind
year: 2025
arxiv_id: "2510.04542"
doi: "https://doi.org/10.48550/arxiv.2510.04542"
cited_by: 11
category: references
tags: [paper, ai, game-theory, llm, planning, mcts, deepmind, code-generation]
sources: ["arxiv:2510.04542"]
summary: "LLMs translate game rules into executable Python (Code World Models), enabling MCTS to handle 9/10 games better than direct LLM move prediction."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-06-21"
tier: core
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
relationships:
  - target: "[[concepts/code-world-models]]"
    type: derived_from
  - target: "[[concepts/llm-as-compiler]]"
    type: derived_from
  - target: "[[concepts/verifiable-planning]]"
    type: derived_from
  - target: "[[papers/alphazero]]"
    type: related_to
  - target: "[[concepts/game-theory-and-strategic-analysis]]"
    type: related_to
created: 2026-07-26
updated: 2026-07-26
---

# Code World Models for General Game Playing

> **Core thesis:** Instead of using LLMs as direct game-playing policies, use them as *compilers* — translating natural language game rules into executable Python programs (Code World Models), then hand off to classical planners (MCTS) for deep search.

## The Problem: System 1 vs System 2 in Game Playing

LLMs deployed as direct move generators ("intuitive players") suffer three failure modes:

1. **No deep lookahead** — LLMs predict one move at a time from pattern recognition, lacking multi-step tactical search ("System 2" deliberation)
2. **Illegal moves** — the model hallucinates actions that violate game rules, since it relies on implicit understanding rather than formal constraints
3. **Poor generalization** — on novel games outside training data, the pattern-matching approach breaks down

This mirrors the broader limitation of LLMs in any domain requiring **verifiable, multi-step reasoning**: the model can recognize patterns but cannot reliably execute formal logic chains.^[inferred]

## The CWM Architecture

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Natural Lang │────▶│      LLM        │────▶│  Executable  │
│  Game Rules   │     │  (translator)   │     │  Python CWM  │
└──────────────┘     └────────┬────────┘     └──────┬───────┘
                              │                      │
                     ┌────────┴────────┐    ┌───────▼───────┐
                     │  Heuristic      │    │  MCTS Planner │
                     │  Value/Policy   │───▶│  (search)     │
                     │  Functions      │    └───────┬───────┘
                     └─────────────────┘            │
                                              ┌─────▼─────┐
                                              │ Best Move │
                                              └───────────┘
```

The CWM provides five executable functions:
- **State transitions** — apply(move, state) → new_state
- **Legal move enumeration** — legal_moves(state) → [moves]
- **Termination checks** — is_terminal(state) → bool
- **Reward functions** — reward(state) → float
- **Observation functions** — observe(state, player) → observation (for imperfect information games)

## Three Key Advantages

### 1. Verifiability
Formal code specification → planners algorithmically enumerate valid actions → **illegal moves eliminated** (contingent on correct code generation). This is the deepest insight: by making the world model executable, correctness becomes a decidable property.

### 2. Strategic Depth
LLM semantic reasoning + heuristic generation ⊕ MCTS exhaustive search = deep lookahead. The LLM provides the *evaluation function*; MCTS provides the *search*. This division of labor exploits each component's strength.

### 3. Generalization
Framing as "data-to-code translation" rather than "direct move generation" generalizes to unseen games. The LLM doesn't need to have *played* the game — it needs to *understand the rules* and express them as code. This is a fundamentally different capability.^[inferred]

## Results

| Metric | CWM Method | Gemini 2.5 Pro (direct) |
|--------|-----------|------------------------|
| Games won/matched (of 10) | **9/10** | Baseline |
| Novel games (of 4) | Generalized | Struggled |
| Perfect info games (5) | Strong | Mixed |
| Imperfect info games (5) | Strong | Mixed |

Tested across 10 games (5 perfect information, 5 imperfect information), 4 of which were novel creations for the paper.

## Implications Beyond Games

The CWM pattern — **LLM as compiler → executable model → classical solver** — generalizes to any domain where:
1. Rules can be expressed in natural language
2. Those rules can be formalized as executable code
3. A classical solver exists for the resulting formal problem

Candidate domains:^[inferred]
- Financial modeling (rules → simulation → optimization)
- Legal reasoning (statutes → logic program → solver)
- Logistics (constraints → optimizer)
- [[concepts/strategic-decision-framework|Strategic decision-making]] (scenarios → game tree → equilibrium solver)

## Connection to AlphaZero

[[papers/alphazero|AlphaZero]] used neural networks to provide value/policy *heuristics* to MCTS, but the game rules were hand-coded. CWM extends this: the LLM *generates both the rules engine and the heuristics*, making the system fully autonomous for novel games.^[inferred]

## Open Questions

- How robust is the LLM-generated code? What happens when the CWM has bugs?
- Can this approach handle games with continuous action spaces?
- Does the CWM pattern apply to multi-agent games with negotiation/bluffing?
- What is the scaling law — does larger LLM = better CWM generation?

## References

Lehrach, W., Hennes, D., Lazaro-Gredilla, M., et al. (2025). Code World Models for General Game Playing. *arXiv*. [https://doi.org/10.48550/arxiv.2510.04542](https://doi.org/10.48550/arxiv.2510.04542)
