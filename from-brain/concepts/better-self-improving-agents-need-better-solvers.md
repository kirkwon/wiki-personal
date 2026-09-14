---
type: note
title: >-
  Better self‑improving agents need better solvers, not bigger update‑writing
  models
created: 2026-08-10
---
# Better self‑improving agents need better solvers, not bigger update‑writing models

**Source:** arXiv:2605.30621 – https://arxiv.org/abs/2605.30621

## Summary

This paper challenges the common intuition that the strongest model should occupy the “evolver” seat in a self‑improving agent loop (the model that writes prompts, memories, tools, and skills). The authors argue that the two roles—**writing useful harness updates** and **benefiting from those updates during task execution**—are largely independent.

### Key Insights

1. **Decoupling the roles**  
   - A cheaper, smaller model (e.g., Qwen3.5‑9B) can often produce updates (prompt templates, memory entries, skill definitions) that are *good enough* to improve performance.  
   - The expensive, larger model (e.g., Claude Opus 4.6) does not necessarily yield substantially better updates.

2. **Where the large model shines**  
   - The large model’s strength is better utilized as the **solver/agent** that actually carries out the task using the updates produced by the evolver.  
   - Weak models often fail to correctly invoke or follow the newly introduced skills, causing the update to provide little benefit.  
   - Very strong models may already be near their performance ceiling, so the incremental gain from a harness update is limited.

3. **The sweet spot**  
   - A **mid‑tier model**—capable enough to reliably load and follow new procedures, yet not so capable that the harness has nothing left to teach—provides the best overall improvement when paired with a competent evolver.

### Implications for Hermes

- **Evolver seat**: Consider using a smaller, cheaper model (or even a prompt‑engineering‑focused variant) to generate skill updates, memory entries, or tool configurations for Hermes.  
- **Solver seat**: Keep the stronger model (e.g., the current Claude‑based Hermes) as the agent that executes tasks, invokes skills, and applies the updates produced by the evolver.  
- **Experimentation**: Run A/B tests where the evolver is Qwen3.5‑9B (or another open‑weight model) and the solver is Claude Opus 4.6, measuring task success rate, latency, and quality metrics.

### Related Concepts in the LLm‑wiki/GBrain

- `[[self-improving-agent-loop]]` – the general framework where an agent updates its own harness.  
- `[[skill-update-pipeline]]` – how Hermes can autonomously generate and test new skills.  
- `[[model-routing]]` – strategies for assigning different models to different roles (evolver vs. solver).  
- `[[experiment-evolver-vs-solver-model-size]]` – proposed experiment to test this hypothesis with Hermes.

---

*Added to LLm‑wiki on 2026‑06‑08. The note will be synced to GBrain via the existing LLm‑wiki → GBrain delta‑sync cron (every 3 h).*
