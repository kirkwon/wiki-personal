---
type: concept
title: Finacumen Self Evolving Memory Harness
sha256: pending
authors:
  - Pianran Guo
  - Pengcheng Zhou
  - Yuchen Jian
  - Shuhua Chen
arxiv_id: 2606.17642v1
ingested: '2026-06-28T00:00:00.000Z'
pdf_path: raw/papers/2606.17642.pdf
published: '2026-06-16T00:00:00.000Z'
source_url: 'https://arxiv.org/abs/2606.17642'
affiliations:
  - Beijing University of Posts and Telecommunications
  - Queen Mary University of London
ingested_via: put_page
ingested_at: '2026-06-28T22:58:50.141Z'
source_kind: put_page
tags:
  - agent
  - causal
  - finance
  - memory-harness
  - multimodal-reasoning
  - papers
  - self-evolving
created: 2026-06-28
---
# FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness

**arXiv:2606.17642v1** [cs.AI] 16 Jun 2026

## Abstract

FinAcumen is a financial reasoning agent framework centered on **selective experience memory** for tool-augmented multimodal reasoning. It accumulates financially grounded reasoning experience from prior trajectories, distilling successful strategies and failure-derived cautionary rules into a **persistent memory bank**.

During inference, retrieved experiences condition reasoning **only when semantic relevance exceeds a calibrated threshold**, while irrelevant memory is explicitly suppressed through a fallback mechanism. A deterministic financial tool environment further grounds numerical computation, retrieval, visual decoding, and answer verification.

Across four financial multimodal reasoning benchmarks, FinAcumen consistently improves a **frozen 8B vision-language model** over finance-specialized models and approaches leading proprietary general-purpose models.

**Code:** https://anonymous.4open.science/r/FinAcumen

---

## Key Contributions

### 1. Self-Evolving Experience Memory Harness

The core innovation. Unlike static fine-tuning or simple reflection, FinAcumen:

- **Accumulates** experience from prior reasoning trajectories (both successes and failures)
- **Distills** successful strategies into reusable reasoning patterns
- **Encodes** failure-derived cautionary rules (what NOT to do)
- **Persists** across episodes in a memory bank (not stateless like ReAct)
- **Selectively activates** memory only when semantic relevance exceeds a threshold (τ-gated)

This directly maps to the **self-evolving memory harness** concept from the OCR'd research screenshot. The memory bank IS the harness — it adapts based on what worked and what failed.

### 2. Selective Memory Retrieval (τ-gated)

Critical design choice: memory is NOT always activated. FinAcumen uses a **calibrated threshold** (τ) to decide whether retrieved experience is relevant enough to condition current reasoning. This prevents irrelevant memories from degrading performance — a problem in naive memory-augmented systems.

- If `similarity(query, memory) > τ`: activate memory, condition reasoning
- If `similarity(query, memory) ≤ τ`: suppress memory, use fallback reasoning

### 3. Deterministic Financial Tool Environment

Grounds the agent in reality:
- Numerical computation (deterministic, not LLM-guessed)
- Retrieval (grounded in real financial documents)
- Visual decoding (chart/table parsing)
- Answer verification (checks intermediate conclusions)

### 4. Benchmarks (4 financial multimodal reasoning datasets)

| Benchmark | Challenge | Modality |
|:---|:---|:---|
| **BizBench** (SEC-NUM) | SEC quantity grounding, dense distractors, exact match | Text + tables |
| **FinMMR** | Multimodal numerical reasoning, visual noise, 0.2% tolerance | Charts + text |
| **FinMME** | Broad-spectrum chart evaluation | Charts |
| **FinTMMBench** | Temporal-aware multimodal RAG | Time-indexed records |

---

## Relevance to Our Stack

This paper directly informs **three** of our active research projects:

### P2: Self-Evolving Memory Harness
FinAcumen IS the self-evolving memory harness concept made concrete. The τ-gated selective activation maps to our memory tier system:

| FinAcumen Concept | Our Stack Equivalent |
|:---|:---|
| Experience memory bank | T2 WARM (MEMORY.md) + T4 COLD (gbrain) |
| τ-gated activation | Memory promotion rules (currently manual) |
| Failure-derived cautionary rules | Not yet implemented (gap) |
| Trajectory distillation | Not yet implemented (P3 LoRA prerequisite) |
| Fallback mechanism | T1 HOT always-loaded context |

### P4: Financial Reasoning Models
FinAcumen uses a **frozen 8B VLM** and achieves results competitive with finance-specialized models — **confirming the "harness > model size" finding** from our NotebookLM synthesis. No fine-tuning needed; the memory harness provides all the improvement.

### P3: SKILL.md → LoRA Adapters
FinAcumen's trajectory distillation is the precursor to LoRA training. If we collect FinAcumen-style reasoning trajectories from skill executions, we can distill them into LoRA adapters.

---

## Key Findings (from paper)

1. **Frozen 8B + harness beats finance-specialized models** — confirms harness > SFT
2. **Selective memory activation is critical** — naive memory injection degrades performance
3. **Failure-derived rules are as important as success patterns** — learning what NOT to do
4. **Deterministic tool environment grounds reasoning** — prevents numerical hallucination

---

## Connections

- [[2606.09498]] — Same paradigm (harness improvement loop), different domain (coding vs. finance)
- [[memory-tiering]] — FinAcumen's memory bank is a formalization of the tier concept
- [[causal-ai-hedge-agent]] — FinAcumen's financial reasoning is directly applicable
- [[self-harness-paradigm]] — Three-stage improvement loop

---

*Ingested 2026-06-28 from https://share.google/j3dOWNYVW80dgz38y → https://arxiv.org/pdf/2606.17642v1*
