---
type: concept
title: Self-Distilled Agentic Reinforcement Learning (SDAR)
created: '2026-05-13T00:00:00.000Z'
sources: []
updated: '2026-05-13T00:00:00.000Z'
source: brain/ (retired 2026-09-13)
---

# Self-Distilled Agentic Reinforcement Learning (SDAR)

**arXiv:** 2605.15155 | **Published:** 2026-05-13
**Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Affiliation:** ZJU-REAL (Zhejiang University)
**GitHub:** https://github.com/ZJU-REAL/SDAR (⭐73)
**HuggingFace:** https://huggingface.co/papers/2605.15155 (83 upvotes, #3 Paper of the Day May 15, 2026)

## Summary

SDAR enhances reinforcement learning for **multi-turn LLM agent training** by integrating **self-distillation** through a **sigmoid gate** that selectively strengthens positive token-level guidance while mitigating negative teacher rejections.

## Core Problem

- **RL** is key for post-training LLM agents but provides only **coarse trajectory-level rewards**, insufficient for long-horizon tasks.
- **On-Policy Self-Distillation (OPSD)** adds dense **token-level guidance** using a teacher with **privileged context**.
- However, applying OPSD to **multi-turn agents** is challenging:
  - Multi-turn instability compounds supervision errors.
  - **Negative teacher rejections** may stem from imperfect skill retrieval/usage — not actual poor actions — requiring asymmetric treatment.

## Solution: SDAR

SDAR treats **OPSD as a gated auxiliary objective**, with **RL as the primary optimization backbone**.

### Key Mechanism

Maps detached token-level signals into a **sigmoid gate**:
- ✅ **Strengthens distillation** on **positive-gap tokens** (teacher-endorsed).
- 🔇 **Softly attenuates** influence from **negative teacher rejections**.

This avoids instability from naive GRPO+OPSD hybrids while preserving beneficial dense supervision.

## Results

Evaluated on **Qwen2.5** and **Qwen3** model families across three benchmarks:

| Benchmark | Improvement over GRPO |
|-----------|----------------------|
| **ALFWorld** | **+9.4%** |
| **Search-QA** | **+7.0%** |
| **WebShop-Acc** | **+10.2%** |

✅ **Consistently outperforms** hybrid RL–OPSD baselines across model scales.
✅ **Avoids instability** seen in naive GRPO + OPSD approaches.

## Key Takeaways

- **SDAR** effectively combines RL and self-distillation for **multi-turn LLM agents**.
- Uses a **sigmoid gate** to filter teacher signals — boosting useful guidance, suppressing noise.
- Delivers **significant gains** (+7–10%) over GRPO on standard agent benchmarks.
- Offers a **stable, scalable alternative** to naive RL+OPSD hybrids.
- Open-source code available: https://github.com/ZJU-REAL/SDAR

## Relevance to Agentic AI

This paper directly applies to the multi-agent orchestration work:
- **Multi-turn agent training** — relevant for Symphony/Kanban agent dispatch
- **Self-distillation** — could improve agent quality without additional human labels
- **Sigmoid gating** — a clean pattern for filtering noisy teacher signals in production agent systems
- **GRPO baseline** — connects to the RL training pipeline for agent optimization
