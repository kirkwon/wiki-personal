---
type: concept
title: Speculative Decoding
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
--

# Speculative Decoding & Multi-Token Prediction

## Overview

Speculative decoding accelerates LLM inference by pairing a **smaller draft model** with a **larger target model**. The draft model quickly proposes multiple tokens; the target model verifies them in parallel, accepting the longest matching prefix.

## Key Papers

### 1. Fast Inference from Transformers via Speculative Decoding
- **Authors**: Leviathan et al.
- **Venue**: ICLR 2023 Oral
- **Key Contribution**: Introduced draft-target speculative decoding for autoregressive models
- **Link**: https://arxiv.org/abs/2211.17192

### 2. EAGLE: Extrapolation Algorithm for Greater Language-model Efficiency
- **Authors**: Li et al.
- **Venue**: ICLR 2024
- **Key Contribution**: Feature-level speculation, attaches drafting head to target model
- **Link**: https://arxiv.org/abs/2305.15034

### 3. EAGLE-3: Instance-adaptive Speculative Decoding
- **Authors**: Li et al.
- **Venue**: 2025
- **Key Contribution**: Multi-layer fused features, dynamic draft tree, context-aware speculation
- **Link**: https://nvidia.github.io/TensorRT-Model-Optimizer/reference/generated/modelopt.torch.speculative.html

### 4. FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction
- **Authors**: Yuxuan Cai et al. (Tencent)
- **Venue**: arXiv:2509.18362
- **Key Contribution**: 2.03× speedup, outperforms vanilla MTP by 82%, shared-weight MTP head
- **Link**: https://arxiv.org/abs/2509.18362

### 5. Accelerating SGLang with Multiple Token Prediction
- **Authors**: Eigen AI Team / LMSYS
- **Venue**: LMSYS Blog, July 2025
- **Key Contribution**: +60% throughput on DeepSeek V3, MTP + EP + PD disaggregation
- **Link**: https://lmsys.org/blog/2025-07-17-mtp/

### 6. Accelerating Large Language Model Decoding with Speculative Sampling
- **Authors**: Chen et al.
- **Venue**: NeurIPS 2023
- **Key Contribution**: Randomized acceptance for better generalization
- **Link**: https://arxiv.org/abs/2301.02373

## Performance Differences

| Approach | Speedup | Acceptance Rate | Notes |
|----------|---------|-----------------|-------|
| Speculative Decoding (draft-target) | 1.2–1.8× | 70–80% (1st token) | Small draft + large target |
| EAGLE-3 | 2.0–2.5× | Higher (context-aware) | Feature-level, no separate draft model |
| FastMTP | **2.03×** | 81% (1st), 56% (2nd), 36% (3rd) | Shared-weight MTP head |
| MTP + SGLang | **+60% throughput** | avg 2.44 (4-token) | DeepSeek V3, H200 GPUs |

## Key Insight

**Acceptance rate drives everything.** At τ=2.44 average acceptance, you skip 2.44 decode steps per verification. FastMTP achieves this through:
- Shared-weight MTP head (vs independent modules)
- Language-aware vocabulary compression (16k Chinese, 32k English)
- Self-distillation training (389K samples, <3% parameters fine-tuned)

## Tags

speculative-decoding, MTP, draft-model, target-model, inference-speed, LLM-optimization
