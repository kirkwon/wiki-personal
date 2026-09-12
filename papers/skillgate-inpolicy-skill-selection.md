---
date: 2026-08-23
type: media
title: "SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents"
created: 2026-08-23
updated: 2026-08-23
tags: [model, agents, skills, methodology]
sources: [https://arxiv.org/abs/2608.18852]
---

# SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents

**Authors:** Qingyao Li, Wenxiang Jiao, Shuai Shao, Kangning Zhang, Yuan Lu, Yi Guo, Weiwen Liu, Weinan Zhang, Yong Yu (9 authors)
**Submitted:** 19 Aug 2026 (v1) · cs.AI
**arXiv:** [2608.18852](https://arxiv.org/abs/2608.18852) · 17 pp., 6 figs., 6 tables
**Code:** [DeepExperience/SkillGate](https://github.com/DeepExperience/SkillGate) · **Model:** [simonlqy/SkillGate-9B](https://huggingface.co/simonlqy/SkillGate-9B)

## Core Problem: Selector Credit Starvation

Skill libraries are instruction files read on demand — *which skill to read* is now a mid-episode policy decision, but outcome-rewarded RL over the candidate slate **cannot train it**. Structural reason: under broadcast, sequence-level advantage, the few tokens naming the chosen skill carry a vanishing share of the loss, and the credit they inherit is increasingly **wrong-signed as trajectories lengthen** — a correct choice is punished whenever the execution after it fails. All three properties verified on a completed run's own training artifacts, each worsening monotonically with horizon.

## Method

SkillGate partitions the token support into two disjoint credit channels:
- **Outcome credit** reaches only execution tokens.
- A separate **action-local advantage** reaches exactly the skill-naming tokens, positive only when the trajectory's single read is the correct one.

## Results

Five agentic benchmarks, 16-candidate slate: a 9B policy lifts **40.8% → 53.2%** trial success — ahead of the identical budget spent on outcome reward alone — while cutting exposure to misleading candidates by two-thirds and reading fewer skills.

## Why It Matters for β (Co-Failure Rate)

Selection–execution co-failure is the confound: a correct skill choice penalized by downstream execution failure is exactly a wrong-signed credit signal. The disjoint-credit-channel fix is a general template for **de-confounding β estimates** whenever attribution must split a decision from its execution.

## Caveats

- Trains the selection policy itself (RL) — heavier than router heuristics; needs the two-channel trainer infrastructure.
- Single-read assumption ("a trajectory's single read") — unclear how it extends to multi-skill episodes ^[inferred from abstract]

## Connections

- [[concepts/skill-utility-gating]] — the training-side gate; utility scores are the inference-side gate
- [[concepts/scaffold-optimization]] — skill selection as a learnable scaffold parameter
- [[concepts/co-failure-ceiling]] — credit starvation is a selection–execution co-failure artifact
