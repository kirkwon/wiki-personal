---
date: 2026-08-23
type: entity
title: "AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement"
created: 2026-08-23
updated: 2026-08-23
tags: [model, agents, benchmark, methodology]
sources: [https://arxiv.org/abs/2608.20318]
---

# AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement

**Authors:** Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na (10 authors)
**Submitted:** 20 Aug 2026 (v1) · cs.AI primary, cs.CL, cs.LG
**arXiv:** [2608.20318](https://arxiv.org/abs/2608.20318) · CC BY 4.0 · task suite, evaluators, and every scored submission released

## Core Design

Recursive self-improvement (RSI) operationalized as: **can an agent design training algorithms?** — distinct from collecting data or tuning hyperparameters. 10 frozen research repositories spanning 10 training-algorithm families; per task the agent gets 4 hours on one B300 to rewrite the training algorithm; its code is rerun from scratch for up to 12 hours and scored by a hidden fixed evaluator against the repository's original algorithm under identical procedure. Incommensurable metrics mapped to one scale: 0 = uninformative model, 0.1 = the shipped algorithm, 1.0 = task optimum.

## Results

- 29 configurations of 6 systems: **mean score 0.166; best system 0.250** — the strongest closes under a fifth of the distance from shipped-algorithm to optimum.
- Most submissions never change how the model learns; the minority that do average **0.226 vs 0.126** for the rest.
- More reasoning effort mostly buys the *willingness* to touch learning: takes that minority from 8% → 64% of submissions and mean score 0.094 → 0.196.

## Why It Matters

The **learn-vs-execute separation** is the exact attribution axis for self-improvement stacks: "changed how the model learns" (weights/objective — the LoRA side) vs "changed how the run executes" (scaffold/harness side). Any P3/P0 experiment claiming self-improvement should be classifiable on this axis, and the measured floor (best ≈ 0.25) calibrates expectations for agent-designed training changes.

## Caveats

- Single-benchmark snapshot; frontier systems will move the numbers.
- 4h/1-B300 budget is far below what an organization can spend — the score is a floor for capability, not a ceiling ^[inferred]

## Connections

- [[concepts/self-harness-paradigm]] — the RSI question this benchmark makes measurable
- [[concepts/scaffold-optimization]] — execute-side vs learn-side of the same improvement axis
- [[papers/ornith-1-self-improving-coding]] — a learn-side result this benchmark would score
