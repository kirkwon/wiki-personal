---
date: 2026-06-28

source_url: https://github.com/deepreinforce-ai/Ornith-1
hf_url: https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B
publisher: deepreinforce-ai
ingested: 2026-06-28
tags: [models, ornith, coding-agent, self-improving, rl, scaffold, qwen35, gemma4, terminal-bench, swebench]
created: 2026-07-26
updated: 2026-07-26
---

# Ornith-1.0: Self-Improving Open-Source Models for Agentic Coding

**Publisher:** Deep Reinforce AI
**GitHub:** https://github.com/deepreinforce-ai/Ornith-1
**HuggingFace:** deepreinforce-ai/Ornith-1.0-{9B,35B,397B}
**License:** MIT
**Published:** 2026-06-21 (HF), 2026-06-25 (last modified)
**Blog:** https://deep-reinforce.com/ornith.html

## Model Family

| Model | Architecture | Base | Params | Format | Best For |
|:---|:---|:---|:---:|:---|:---|
| Ornith-1.0-9B | Dense | Qwen 3.5 | 9B | bf16, GGUF | Single-GPU, local inference |
| Ornith-1.0-9B-GGUF | Dense | Qwen 3.5 | 9B | Q8_0 | Ollama / llama.cpp |
| Ornith-1.0-35B | MoE | Qwen 3.5 MoE | 35B | bf16, FP8 | Multi-GPU serving |
| Ornith-1.0-397B | MoE | Qwen 3.5 MoE | 397B | bf16, FP8 | Datacenter-scale |

All models are **image-text-to-text** (multimodal/vision capable).

---

## Core Innovation: Self-Improving Training Framework

Ornith-1.0 employs **RL to jointly optimize scaffolds and solution rollouts**. Instead of just learning to produce better answers, the model learns to generate better *scaffolds* (the prompts, tool configurations, and search strategies) that drive those answers.

> "Ornith-1.0 employs RL to learn to generate not only solution rollouts, but also the scaffold that drive those rollouts. By jointly optimizing the scaffold and the resulting solution, the model discovers better search trajectories and generates higher-quality solutions."

This is a **meta-learning** approach: the model improves its own *process* of arriving at solutions, not just the solutions themselves.

---

## Benchmark Results: Ornith-1.0-9B

### Agentic Coding (the key differentiator)

| Benchmark | Ornith-9B | Qwen3.5-9B | Qwen3.5-35B | Gemma4-12B | Gemma4-31B |
|:---|:---:|:---:|:---:|:---:|:---:|
| Terminal-Bench 2.1 (Terminus-2) | **43.1** | 21.3 | 41.4 | 21.0 | 42.1 |
| Terminal-Bench 2.1 (Claude Code) | **40.6** | 18.9 | 38.9 | — | — |
| SWE-bench Verified | **69.4** | 53.2 | 70.0 | 44.2 | 52.0 |
| SWE-bench Pro | **42.9** | 31.3 | 44.6 | 27.6 | 35.7 |
| SWE-bench Multilingual | **52.0** | 39.7 | 60.3 | 32.5 | 51.7 |
| NL2Repo | **27.2** | 16.2 | 20.5 | 10.3 | 15.5 |
| SWE Atlas - QnA | **17.9** | 9.2 | 13.2 | — | — |
| SWE Atlas - RF | **16.6** | 4.3 | 10.2 | — | — |
| SWE Atlas - TW | **15.3** | 4.4 | 9.8 | — | — |

**Key finding:** Ornith-9B **doubles** Qwen3.5-9B on Terminal-Bench (43.1 vs 21.3) and matches/beats Qwen3.5-35B (4x larger) on most coding benchmarks. It also beats Gemma4-31B (3x larger) on SWE-bench.

---

## Hermes Integration

The README explicitly includes Hermes Agent integration:

```bash
# Ornith works with Hermes Agent as a custom endpoint
# options: { baseURL: "http://localhost:8000/v1", apiKey: "EMPTY" }
```

Ornith exposes an OpenAI-compatible API via vLLM, making it drop-in compatible with Hermes's custom provider.

---

## Relevance to Our Stack

### Direct Connections

| Concept | Connection |
|:---|:---|
| **Self-Harness paradigm** (arXiv:2606.09498) | Ornith's scaffold optimization IS self-harness — the model improves its own harness via RL |
| **P3: Skill→LoRA** | Ornith's joint scaffold+solution optimization is exactly the trajectory distillation P3 needs |
| **P0: Skill Subspace** | Ornith's scaffold generation could benefit from skill routing (which scaffold for which task) |
| **FinAcumen** (arXiv:2606.17642) | Both use self-evolving harness; Ornith for coding, FinAcumen for finance |
| **Local model comparison** | Ornith-9B is 2x the Qwen3.5-9B it's built on — for coding tasks, use Ornith |

### What We Can Use

1. **Scaffold optimization for P3:** Ornith's approach of jointly optimizing the scaffold (skill text/instructions) and the solution (execution trace) is the training methodology for P3-T5 (LoRA training). Instead of just distilling traces, we co-optimize the skill instructions AND the model weights.

2. **Terminal-Bench as evaluation target:** The benchmarks Ornith targets (Terminal-Bench, SWE-bench) are the same coding-agent benchmarks the Self-Harness paper uses. We should use these for P3-T7 evaluation.

3. **Ornith-9B as the LoRA base:** Since Ornith is already optimized for agentic coding via RL, it's a better starting point for skill-specific LoRA adapters than raw Qwen3.5. The scaffold optimization pre-trains the model to follow structured instructions.

4. **Self-improving loop architecture:** Ornith's RL loop (generate scaffold → generate solution → evaluate → improve both) is the concrete implementation of the abstract Self-Harness loop (weakness mining → harness proposal → proposal validation).

### What Our Live Benchmark Missed

Our earlier speed test showed Ornith-9B as 2.3x slower than Gemma4. But we tested on **general tasks** (instruction following, simple reasoning). Ornith is optimized for **agentic coding** — it would likely perform much better on actual coding tasks (Terminal-Bench style). The thinking tokens that slowed it down are its *advantage* for complex coding problems.
