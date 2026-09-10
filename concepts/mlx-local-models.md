---
date: 2026-07-19
type: concept
title: Mlx Local Models
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mlx
- apple-silicon
- local-inference
- macOS
- quantization
- gemma4
- mlops
sources:
- hermes://skill/mlx-local-models
description: Run MLX-optimized models on macOS (Apple Silicon) — setup, usage, and
  troubleshooting
---

# Mlx Local Models

> Run MLX-optimized models on macOS (Apple Silicon) — setup, usage, and troubleshooting

## Overview

- **When This Skill Activates** — Use this skill when: - User asks to run a model locally via MLX (Apple's ML framework) - User wants to compare MLX-quantized models vs GGUF/Ollama versions - Setting up inference with `mlx-community/` models from HuggingFace - Dealing with OptiQ-quantized models specifically (sensitivity-aware mixed precision) - Debugging model loading, tokenizer, or thinking-channel issues
- **Pitfalls** — 1. **Stacked `mix.py` from multiple venv creations** — If you create a venv, fail, then recreate with a different Python binary, old `lib/python3.x/site-packages` dirs may persist. Always `rm -rf ~/mlx-env` before recreating.
- **Related Skills** — - **llama-cpp** — For GGUF models via llama.cpp (different ecosystem, also runs on Mac) - **gguf-quantization** — For the GGUF quantization workflow

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/mlx-local-models/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
