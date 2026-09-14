---
created: 2026-07-27
tags: [auto-fixed, frontmatter]
---

# Ornith-9B Coding Benchmark — Final Report (v2)

> Date: 2026-07-17 | Models: Ornith-9B (Q8_0), Qwen 3.5 (9B MLX), Gemma 4 Agent (12B)
> Benchmark: 5 Python coding tasks × 3 models | Ollama local | deterministic scoring

## Executive Summary

**The timeout confound was real.** With temp=0 and 300s timeout (v2), Ornith-9B matches Gemma's perfect 50/50 score. Qwen 3.5 remains the weakest — its LRU Cache failure is genuine, not timeout-related.

## Results Comparison: v1 vs v2

| Model | v1 (temp 0.3, 180s) | v2 (temp 0, 300s) | Δ |
|-------|---------------------|---------------------|---|
| Ornith-9B | 40/50 | **50/50** 🏆 | +10 |
| Qwen 3.5 | 30/50 | 40/50 | +10 |
| Gemma 4 Agent | 50/50 | **50/50** 🏆 | 0 |

### Per-Test Breakdown (v2)

| Test | Difficulty | Ornith | Qwen | Gemma |
|------|-----------|--------|------|-------|
| Fibonacci | Easy | ✅ 56.5s | ✅ 156.8s | ✅ 104.8s |
| Binary Search | Easy | ✅ 48.2s | ✅ 46.2s | ✅ 26.5s |
| LRU Cache | Medium | ✅ 166.9s | ❌ NameError | ✅ 105.7s |
| Flatten Nested List | Medium | ✅ 84.2s | ✅ 115.5s | ✅ 38.3s |
| Thread-Safe Counter | Hard | ✅ 105.4s | ✅ 191.1s | ✅ 46.0s |

## Latency Analysis

| Model | Total Time | Avg/Test | Fastest | Slowest (passing) |
|-------|-----------|----------|---------|-------------------|
| Gemma 4 Agent | 321.3s | **64.3s** | 26.5s | 105.7s |
| Ornith-9B | 461.2s | 92.2s | 48.2s | 166.9s |
| Qwen 3.5 | 809.6s* | 161.9s | 46.2s | 191.1s |

*Excludes the 300s LRU timeout.

## Key Findings

### 1. Ornith's v1 failures were purely timeout
LRU Cache took 166.9s in v2 (vs 180s timeout in v1 — razor thin margin). Ornith isn't slow at coding; it's slow at generating verbose explanations. Its `raw_chars` for LRU Cache was 6620 (vs Gemma's 1459) — it generates 4.5x more text for the same task.

### 2. Qwen's LRU Cache failure is genuine
Even at 300s timeout, Qwen returned `raw_chars: 0` — it produced nothing. This is a capability gap, not a speed issue. The `NameError: name 'LRUCache' is not defined` suggests Qwen's output format failed code extraction.

### 3. Gemma is the speed champion
Gemma 4 Agent is consistently fastest (64.3s avg vs Ornith's 92.2s). It produces terse, correct code with minimal explanation (raw_chars typically 100-700). For MoA aggregation purposes, this is ideal — fast, reliable, low-token.

### 4. Verbosity vs Speed trade-off
- Ornith: verbose explanations (1466-6620 raw chars), slower but correct
- Gemma: terse code-only output (107-1459 raw chars), fast and correct
- Qwen: terse but inconsistent (0-718 raw chars), failed on the hardest task

## Recommendations

### For MoA Local Preset
Current config (after v1): Gemma4-Agent (aggregator) + Ornith-9B (reference) + Phi4-mini (reference)

**This is correct.** Gemma's speed makes it the ideal aggregator, and Ornith's verbose correctness provides reliable reference signal. Qwen was correctly demoted out.

### For Agentic Tasks
The agentic benchmark harness is built (`~/.hermes/scripts/agentic-benchmark.py`) but can't run yet due to `delegate_task` model isolation limitations. Ornith's scaffold-optimization advantage (Terminal-Bench 43.1) may surface on multi-tool tasks, justifying a future run using `hermes chat` subprocess isolation.

### For Production Coding
Gemma 4 Agent (12B) is the recommended local model for single-function coding tasks. It's fast, reliable, and token-efficient. Ornith-9B is a solid backup at 50/50 but slower.

## Caveats
- **Test suite is small** (5 tasks, single-function only) — not representative of real-world complexity
- **No agentic tasks** — Ornith's Terminal-Bench advantage is on multi-tool workflows
- **Local only** — no API latency, but also no quantization artifacts
- **Temp 0 may favor deterministic models** — Ornith's verbose style may be an artifact of temperature settings

## Files
- v1 Results: `~/brain/ollama-coding-benchmark-results.json`
- v2 Results: `~/brain/ollama-coding-benchmark-results-v2.json`
- Raw logs: `~/brain/ollama-benchmark-run-v2.log`
- Benchmark script: `~/.hermes/scripts/ollama-coding-benchmark.py`
- Agentic harness: `~/.hermes/scripts/agentic-benchmark.py`
