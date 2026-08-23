---
date: 2026-06-28
type: entity
title: Tmax — A Simple Recipe for Terminal Agents
created: 2026-06-28
updated: 2026-06-28
tags: [model, agent-systems, methodology]
sources: [papers/2606.23321]
---

# Tmax: A Simple Recipe for Terminal Agents

**arXiv:** [2606.23321](https://arxiv.org/abs/2606.23321) (cs.CL)
**Authors:** Hamish Ivison, Junjie Oscar Yin, Rulin Shao, Teng Xiao, Nathan Lambert, Hannaneh Hajishirzi
**Submitted:** 22 Jun 2026
**Code & Data:** [github.com/hamishivi/tmax](https://github.com/hamishivi/tmax)
**License:** CC BY 4.0

## Key Results

| Metric | Tmax (9B) | Prior Open Models | Frontier |
|--------|:---------:|:-----------------:|:--------:|
| Terminal-Bench 2.0 | **27%** | Lower | ~40% |

## Core Approach

- **Data generation taxonomy**: combines difficulty control, personas, and verifier diversification for cheap large-scale environment creation
- **Largest open terminal dataset**: >2.5× larger than previous releases
- **Simple RL recipe**: outcome-only reward, no complex intermediate supervision
- **Base**: 9B parameters, open-weight

## Relevance to Our Stack

- Directly comparable to [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — both target Terminal-Bench, both use RL for terminal agents
- Tmax uses outcome-only RL (simpler); Ornith uses scaffold RL (more sophisticated)
- **Key comparison**: Ornith-9B achieves 43.1 on Terminal-Bench 2.1 (later version); Tmax achieves 27% on Terminal-Bench 2.0 — compatible benchmarks but different versions ^[ambiguous]
- The data generation taxonomy (difficulty control + personas + verifier diversification) is a reusable pattern for P3 trace generation

## Connections

- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — same task domain, different RL approach (scaffold vs outcome-only)
- [[concepts/scaffold-optimization]] — Tmax's simple RL vs Ornith's scaffold RL comparison
- P3-T1 (Trace Collection) — Tmax's data taxonomy is directly applicable to trace generation strategies
