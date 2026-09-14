---
type: concept
title: Ollama Model Benchmark
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Ollama Model Benchmark

> Benchmark Ollama-hosted LLMs on coding tasks to compare performance and correctness.

## Overview

- **Purpose** — Benchmark Ollama-hosted LLMs on coding tasks to compare performance and correctness.
- **When to Use** — - You want to evaluate claims like "Ornith > Qwen > Gemma for coding". - You need to select a local model for code generation based on empirical results. - You wish to reproduce a standardized coding benchmark locally. - Selecting which model to slot into a local MoA (Mixture of Agents) coding council.
- **Steps** — 1. **Ensure Ollama is running** and the target models are pulled. Verify with `curl http://127.0.0.1:11434/api/tags` — confirm all target models appear. 2. **Run the benchmark script** (lives at `~/.hermes/scripts/ollama-coding-benchmark.py`). A full 3-model × 5-test run takes 30-45 minutes. Run in the background with `notify_on_complete=true` so you're not blocked:

## Further detail

### Pitfalls & Tips

- **Diagnosing zero-score failures — three distinct modes:** Before declaring a model "bad at coding," inspect the JSON results to classify the failure. The `raw_chars` and `code_chars` fields tell you which of three failure modes occurred:

### Support Files

- `scripts/ollama-coding-benchmark.py` – The benchmark script used in this skill.

### Example Output

**2026-07-17 v1 run** (temp 0.3, 180s timeout; Ornith-9B Q8_0 vs Qwen3.5-9B-mlx vs Gemma4-agent:12b):

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/ollama-model-benchmark/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[ollama-model-management]]
