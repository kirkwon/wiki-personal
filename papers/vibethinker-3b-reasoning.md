---
type: entity
title: VibeThinker-3B — Verifiable Reasoning in Small Language Models
created: 2026-06-28
updated: 2026-06-28
tags: [model, methodology]
sources: [papers/2606.16140]
---

# VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models

**arXiv:** [2606.16140](https://arxiv.org/abs/2606.16140) (cs.AI)
**Authors:** Sen Xu, Shixi Liu, Wei Wang, Jixin Min, Yingwei Dai, Zhibin Yin, Yirong Chen, Xin Zhou, Junlin Zhang
**Submitted:** 15 Jun 2026
**Code:** [github.com/WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker)
**License:** CC0

## Key Results

| Benchmark | Score | Note |
|-----------|:-----:|------|
| **AIME26** | **94.3** | Improves to **97.1** with claim-level test-time scaling |
| **LiveCodeBench v6** | **80.2%** Pass@1 | Code generation |
| **LeetCode** (unseen) | **96.1%** acceptance | Strong OOD generalization |
| **IFEval** | **93.4** | Instruction following unaffected |

**Matches or exceeds**: DeepSeek V3.2, GLM-5, Gemini 3 Pro — all **orders of magnitude larger**.

## Methodology: Spectrum-to-Signal Post-Training

1. **Curriculum-based SFT** — staged training with increasing difficulty
2. **Multi-domain RL** — rewards across diverse reasoning domains
3. **Offline self-distillation** — knowledge transfer without runtime overhead

## Parametric Compression–Coverage Hypothesis

> "Verifiable reasoning is compressible into compact reasoning cores, while open-domain knowledge and general-purpose competence require broad parameter coverage over facts, concepts, and long-tail scenarios."

**Implication**: Small models are not just deployment-efficient substitutes — they represent a **complementary path** toward frontier capability in parameter-dense regimes.

## Relevance to Our Stack

- **Pairs with our Gemma4-agent-12b evaluation**: VibeThinker-3B matches models orders of magnitude larger at 3B params — supports our finding that small models (Gemma4-12B, 6.8GB) can handle complex agentic tasks
- **The Parametric Compression–Coverage Hypothesis** explains why our Gemma4-agent-12b had perfect instruction following despite smaller size — reasoning compresses, knowledge doesn't
- **Test-time scaling** (97.1 AIME with claim-level scaling) is relevant to P3's evaluation strategy
- Could be a candidate for skill-specific adapters (P3-T6) — a 3B reasoning specialist paired with a larger general model

## Connections

- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — both push small models to frontier; Ornith for coding, VibeThinker for reasoning
- [[concepts/scaffold-optimization]] — VibeThinker's curriculum SFT + multi-domain RL is a form of scaffold optimization
- P3-T5 (LoRA Training) — VibeThinker's post-training pipeline (curriculum SFT → multi-domain RL → distillation) is a reference architecture
- Local model deployment — 3B models are deployable alongside our Gemma4-agent-12b without memory conflict
