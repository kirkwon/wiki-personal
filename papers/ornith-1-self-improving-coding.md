---
date: 2026-06-28
type: media
title: "Ornith-1.0: Self-Improving Open-Source Models for Agentic Coding"
created: 2026-06-28
updated: 2026-06-28
tags: [model, agent-systems, improvement, methodology]
sources: [raw/models/ornith-1.md]
dates:
  - date: "2026-06-21"
    event: "Published by Deep Reinforce AI"
---

# Ornith-1.0: Self-Improving Open-Source Models for Agentic Coding

**Publisher:** Deep Reinforce AI
**GitHub:** https://github.com/deepreinforce-ai/Ornith-1
**HuggingFace:** deepreinforce-ai/Ornith-1.0-{9B,35B,397B}
**Blog:** https://deep-reinforce.com/ornith.html
**License:** MIT
**Published:** 2026-06-21

A family of RL-trained coding agents that improve their own *scaffolds* (prompts, tool configs, search strategies) — not just their outputs.

## What It Actually Is (Corrected from Prior Misunderstanding)

| Attribute | Before (what we thought) | After (what it actually is) |
|-----------|-------------------------|-----------------------------|
| Publisher | "maxwell1500" (anonymous) | **Deep Reinforce AI** |
| Purpose | Generic Qwen 3.5 fine-tune | **Agentic coding specialist** |
| Training | Unknown | **RL jointly optimizing scaffolds + solutions** |
| Terminal-Bench 2.1 | Untested | **43.1** (vs Qwen3.5-9B's 21.3 — **2x**) |
| SWE-bench Verified | Untested | **69.4** (matches Qwen3.5-35B, 4× larger) |
| Vision | Thought text-only | Image-text-to-text (multimodal) |
| Hermes | Unknown | Explicit Hermes integration in README ^[inferred] |

## Model Family

| Model | Architecture | Base | Params | Best For |
|-------|-------------|------|-------:|----------|
| Ornith-1.0-9B | Dense | Qwen 3.5 | 9B | Single-GPU, local inference |
| Ornith-1.0-35B | MoE | Qwen 3.5 MoE | 35B | Multi-GPU serving |
| Ornith-1.0-397B | MoE | Qwen 3.5 MoE | 397B | Datacenter-scale |

All models are **image-text-to-text** (multimodal/vision capable).

## The Key Innovation: Scaffold Optimization

Ornith doesn't just learn to code better — it learns to generate better **scaffolds** (the prompts, tool configurations, and search strategies that drive answers). This is RL applied to the *meta-process*, not just the output. The model improves its own harness.

> "Ornith-1.0 employs RL to learn to generate not only solution rollouts, but also the scaffold that drives those rollouts."

This is a concrete instantiation of the [[concepts/self-harness-paradigm]]: the Weakness Mine → Harness Propose → Proposal Validate loop, implemented as RL weight updates rather than manual iteration.

## Benchmark Results: Ornith-1.0-9B

| Benchmark | Ornith-9B | Qwen3.5-9B | Qwen3.5-35B | Gemma4-12B | Gemma4-31B |
|-----------|:---------:|:-----------:|:-----------:|:----------:|:----------:|
| Terminal-Bench 2.1 (Terminus-2) | **43.1** | 21.3 | 41.4 | 21.0 | 42.1 |
| Terminal-Bench 2.1 (Claude Code) | **40.6** | 18.9 | 38.9 | — | — |
| SWE-bench Verified | **69.4** | 53.2 | 70.0 | 44.2 | 52.0 |
| SWE-bench Pro | **42.9** | 31.3 | 44.6 | 27.6 | 35.7 |
| SWE-bench Multilingual | **52.0** | 39.7 | 60.3 | 32.5 | 51.7 |

**Key finding:** Ornith-9B **doubles** Qwen3.5-9B on Terminal-Bench and matches/beats Qwen3.5-35B (4× larger) on most coding benchmarks.

## Connections

- [[concepts/scaffold-optimization]] — the core innovation formalized as its own concept
- [[concepts/self-harness-paradigm]] — Ornith is a concrete RL-based implementation of this loop
- [[projects/causal-ai-hedge-agent]] — P3 Skill→LoRA workstream directly benefits from scaffold co-optimization
- [[concepts/co-failure-ceiling]] — understanding ensemble limits informs when to route to Ornith vs fallback models

## Timeline

**2026-06-21** | Published by Deep Reinforce AI
