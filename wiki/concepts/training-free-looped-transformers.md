---
type: paper
description: "Training-Free Looped Transformers"
tags: [paper, transformers, inference, ode, looping]
created: 2026-06-15
status: filed
---

# Training-Free Looped Transformers

**arXiv:** [2605.23872](https://arxiv.org/abs/2605.23872) — May 2026  
**Authors:** Lizhang Chen, Jonathan Li, Chen Liang, Ni Lao, Qiang Liu  
**Verdict:** Filed for reference. Not implementing now.

## Summary
Inference-time wrapper that loops a mid-stack block of layers from a frozen pretrained model. Treats transformer blocks as ODE Euler steps → damped sub-steps instead of naive repetition. Gains of +1-2 pp on academic benchmarks across 7 model families.

## Why Filed (Not Implemented)
No code released, incremental benchmark gains, compute overhead doesn't justify benefit for current agentic/causal workloads. See llm-wiki concept note for full analysis.

## Related
- [[causal-pipeline-results-real-data]]
- [[loop-engineering]]
