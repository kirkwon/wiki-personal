---
type: concept
title: Reinforcement Learning Alignment
description: "Reinforcement Learning Alignment"
created: 2026-05-03
updated: 2026-05-03
tags:
- ai
- ai-safety
- machine-learning
- decision-making
sources:
- the-alignment-problem
- Reinforcement Learning Alignment
related: [the-alignment-problem---brian-christian-tom-griffiths, reward-hacking, the-genie-problem, decision-making-frameworks]
---
# Reinforcement Learning Alignment

Reinforcement learning alignment refers to the challenge of ensuring that behaviors learned through RL match human values and intentions. In [[the-alignment-problem---brian-christian-tom-griffiths]], this is explored through gaming and real-world applications where reward functions can be mispecified or gamed.

Key issues include:
- **Reward hacking**: Agents find unintended shortcuts to maximize rewards without actually achieving the intended outcome.
- **Misalignment between learned behavior and human values**: What the model optimizes for may diverge from what humans actually want.
- **Difficulty of specifying correct objectives**: Human values are complex, contextual, and often difficult to formalize.

This connects to [[decision-quality-vs-outcome-quality]] and [[thinking-in-bets---annie-duke]] in that specifying the right objective function is itself a decision problem under uncertainty.