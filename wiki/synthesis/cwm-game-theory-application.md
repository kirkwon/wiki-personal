---
date: 2026-06-21

type: note
title: "CWM Pattern Applied to Game Theory in Agent Systems"
category: wiki
tags: [synthesis, game-theory, code-world-models, planning, verification, agent-architecture]
sources: ["arxiv:2510.04542"]
summary: "How the Code World Models insight (LLM-as-compiler → classical solver) maps onto game-theoretic problems in agent skills: autoresearch, meta-critic, structured execution."
base_confidence: 0.50
lifecycle: draft
lifecycle_changed: "2026-06-21"
tier: supporting
provenance:
  extracted: 0.30
  inferred: 0.70
  ambiguous: 0.0
relationships:
  - target: "[[concepts/code-world-models]]"
    type: derived_from
  - target: "[[concepts/game-theory-and-strategic-analysis]]"
    type: related_to
  - target: "[[concepts/verifiable-planning]]"
    type: derived_from
  - target: "[[concepts/llm-as-compiler]]"
    type: related_to
created: 2026-07-26
updated: 2026-07-26
---

# CWM Pattern Applied to Game Theory in Agent Systems

## The Insight

Lehrach et al. (2025) showed that LLMs play games better when they *compile the rules into code* and hand off to classical planners, rather than directly predicting moves. This is not just a game-playing result — it's an **architectural principle for any system where an LLM makes strategic decisions in a rule-governed domain.**^[inferred]

## The Game Theory Mapping

| Game Element | CWM Equivalent | Agent System Analog |
|-------------|----------------|-------------------|
| Game rules | Executable CWM code | Skill constraints, acceptance criteria |
| Legal moves | `legal_moves(state)` | Allowed actions per skill protocol |
| Move evaluation | MCTS + LLM heuristics | Critic pass + automated checks |
| Win condition | `is_terminal()` + `reward()` | Success/failure assertions |
| Opponent moves | Hidden in imperfect info games | Unpredictable external environment |
| Game tree search | MCTS exploration | Multi-scenario planning |

## Where Game Theory Lives in the Agent System

### 1. Autoresearch: Experiment as Game Against Nature

The propose→test→ratchet cycle is a **game against nature**. The agent proposes; nature responds with outcomes.^[inferred]

**CWM application:** Encode experiment success criteria as executable evaluation scripts (already supported via `Evaluation: Command` in program.md). This eliminates the confabulation equilibrium where the agent games the metric — the evaluation is deterministic, not probabilistic.

**Skill updated:** `autoresearch/SKILL.md` — added Game Theory Connection section

### 2. Meta-Critic: Strategy Selection Game

The meta-critic selects critique strategies to maximize information gain — a **multi-armed bandit** with the artifact as adversary.^[inferred]

**CWM application:** Critique dimensions that can be expressed as executable assertions (linters, test suites, type checkers) are strictly more reliable than natural-language dimensions (style, elegance). Prioritize executable dimensions; use NL dimensions as heuristic pruning.

**Skill updated:** `meta-critic/SKILL.md` — added Game Theory Connection section

### 3. Structured Execution: Adversarial Critic Game

The strategic filter includes an adversarial critic pass where the critic tries to break the scorer's decision — a **2-player zero-sum game**.^[inferred]

**CWM application:** Formalize acceptance criteria as executable assertions. Instead of "critic, is this sound?" → "critic, does it pass these 12 assertions?" Converts probabilistic critique into verifiable critique.

**Skill updated:** `structured-execution/SKILL.md` — added Game Theory Connection section

## The Meta-Pattern

```
For any agent skill involving strategic decisions:

1. Identify the "game" — who are the players, what are the moves, what's the payoff?
2. Ask: can the rules be formalized as executable code?
3. If yes → encode as CWM, use classical verification (assertions, tests)
4. If no → use LLM judgment, but mark as probabilistic and require cross-validation
```

This creates a **reliability hierarchy**:^[inferred]

```
Most reliable: Executable CWM + classical solver (deterministic)
              ↓
             Executable assertions + LLM critique (verifiable)
              ↓
             LLM critique with anti-hallucination contract (probabilistic)
              ↓
Least reliable: Raw LLM judgment (unverifiable)
```

## Connection to Existing Game Theory Knowledge

- [[concepts/game-theory-and-strategic-analysis]] — General framework
- [[concepts/game-theory-in-life]] — Life applications
- [[concepts/behavioral-game-theory]] — How agents actually behave
- [[concepts/prisoners-dilemma]] — Cooperation/defection dynamics
- [[concepts/minimax-algorithm]] — Minimizing maximum loss (classical planning)
- [[papers/alphazero]] — Neural network heuristics + MCTS (predecessor to CWM)

## Open Questions

- Can the CWM pattern formalize **multi-agent games** where agents negotiate or bluff?
- How does the pattern handle **continuous action spaces** (financial markets)?
- What's the equivalent of MCTS for **non-zero-sum games** (collaborative scenarios)?
- Can we build a "CWM compiler" that translates any skill's decision criteria into executable assertions?

## References

- Lehrach, W., et al. (2025). [Code World Models for General Game Playing](https://doi.org/10.48550/arxiv.2510.04542). arXiv.
