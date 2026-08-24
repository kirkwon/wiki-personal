---
created: 2026-08-23
updated: 2026-08-23
---


# Scaffold Optimization

The principle of **co-optimizing the meta-process (scaffolds) alongside the final outputs**, rather than optimizing outputs alone. This is distinct from standard fine-tuning or RLHF, which targets output quality directly.

## Definition

A *scaffold* is the structure that guides an agent's reasoning and tool use: system prompts, tool descriptions, search strategies, chain-of-thought templates, and error-handling rules. *Scaffold optimization* is the practice of learning better scaffolds — not just better answers.

| Approach | Optimizes | Example |
|----------|-----------|---------|
| Standard fine-tuning | Output tokens | Next-token prediction loss |
| RLHF | Output quality | Reward model on final answer |
| Scaffold optimization | **The process** | RL on both scaffold parameters + solution rollouts |

## Proven Implementation: Ornith-1.0

[[papers/ornith-1-self-improving-coding|Ornith-1.0]] by Deep Reinforce AI is the first open-source model to jointly optimize scaffolds and solutions via RL. Key results:

- **2× improvement** on Terminal-Bench vs the base model (Qwen3.5-9B: 21.3 → Ornith-9B: 43.1)
- Matches Qwen3.5-35B (4× larger) on SWE-bench
- The model learns to generate better prompts, tool configs, and search strategies — not just better code

## Strategic Significance for P3 (Skill→LoRA)

This shifts the P3 strategy from **execution trace distillation** to **co-optimization**:

1. **Before (distillation approach):** Collect execution traces → filter good ones → fine-tune LoRA on traces alone
2. **After (co-optimization approach):** Jointly optimize skill instructions (the scaffold) + model weights (the LoRA adapter) via RL. The skill becomes a learnable parameter of the training loop.

This is the key insight from Ornith: **the scaffold and the model can be co-optimized**, producing gains that neither achieves alone.

## Relationship to Self-Harness Paradigm

Scaffold optimization is the RL-automated version of the [[concepts/self-harness-paradigm]]:

| Self-Harness Stage | Scaffold Optimization Equivalent |
|-------------------|----------------------------------|
| Weakness Mine | RL discovers failure modes via reward signal |
| Harness Propose | Model generates improved scaffold |
| Proposal Validate | Reward evaluates both scaffold + solution quality |

## Related Concepts

- [[concepts/self-harness-paradigm]] — the manual methodology that scaffold optimization automates
- [[concepts/co-failure-ceiling]] — when scaffold/ensembling stops helping, measured by β
- [[concepts/loop-engineering]] — the meta-skill of building and optimizing improvement loops
- [[papers/task-coevolve-harness-optimization]] — 80% cheaper validation for the scaffold-optimization loop (2026-08-23)
- [[concepts/skill-utility-gating]] — quality gate for the skill side of the scaffold

Sources: [[papers/ornith-1-self-improving-coding]]
