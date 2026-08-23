---
date: 2026-06-28
type: entity
title: QUEST — Training Frontier Deep Research Agents with Fully Synthetic Tasks
created: 2026-06-28
updated: 2026-06-28
tags: [model, agent-systems, methodology]
sources: [papers/2605.24218]
---

# QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks

**arXiv:** [2605.24218](https://arxiv.org/abs/2605.24218) (cs.CL)
**Authors:** Jian Xie, Tianhe Lin, Zilu Wang, et al. (OSU NLP Group)
**Submitted:** 22 May 2026
**Project Page:** [osu-nlp-group.github.io/QUEST](https://osu-nlp-group.github.io/QUEST/)

## What It Is

A family of open deep research agents (2B–35B) trained with **fully synthetic tasks**, approaching/surpassing frontier closed-source agents across 8 deep research benchmarks.

## Training Recipe

1. **Mid-training** — general capability foundation
2. **Supervised fine-tuning** — on synthetic rubric-tree data
3. **Reinforcement learning** — with verifiable rewards

| Component | Detail |
|-----------|--------|
| Training data | Only **8K synthesized tasks** — no human annotation |
| Data pipeline | **Unified rubric trees** — applies to different task types |
| Verifiability | Rubric trees enable automatic reward computation |
| Context mgmt | Built-in mechanism for long-horizon reasoning |

## Key Capabilities

- Fact-seeking
- Citation grounding
- Long-horizon reasoning
- Report synthesis
- Generalizes across diverse task types (unlike prior open agents)

## Relevance to Our Stack

- **Synthetic data pipeline** for P3: QUEST's rubric-tree approach is directly applicable to trace generation — instead of collecting real execution traces, generate synthetic ones with verifiable rewards
- Open-source at all scales (2B–35B) means deployable locally
- The "8K synthetic tasks beating frontier" claim validates the synthetic data approach for agent training

## Connections

- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — both use RL for agent training; QUEST uses synthetic rubric trees, Ornith uses scaffold RL
- P3-T4 (Dataset Curation) — QUEST's rubric-tree pipeline is directly applicable
- [[concepts/scaffold-optimization]] — QUEST's synthetic task design IS a form of scaffold engineering
