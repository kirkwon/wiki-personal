---
date: 2026-07-19
type: concept
title: Ollama Model Management
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/ollama-model-management
description: Manage local LLM models via Ollama and wire them into Hermes providers
  — pull/remove/list models, configure provider lists and fallback providers, test
  model capabilities, and set up smart model routing.
---

# Ollama Model Management

> Manage local LLM models via Ollama and wire them into Hermes providers — pull/remove/list models, configure provider lists and fallback providers, test model capabilities, and set up smart model routing.

## Overview

- **Lookup Model Info Online** — When Firecrawl credits are exhausted, use curl to scrape ollama.com:
- **Custom Modelfiles & Model Tags** — Custom Ollama model tags (e.g. `gemma4-agent:12b`) created via Modelfile are **metadata-only** — they don't duplicate model weights. See `references/custom-modelfiles.md` for the full workflow: inspecting model settings with `ollama show --modelfile`, creating custom tags with increased `num_ctx`, and the replacement workflow when upgrading models.
- **Mixture-of-Agents (MoA) Preset Cost Optimization** — Hermes MoA (Mixture of Agents) council runs reference models + an aggregator per call. Default presets can route everything through expensive OpenRouter models (claude-sonnet-4, claude-opus-4.8, gpt-5, gpt-5.5-pro). When credit budgets are tight, reconfigure presets to use cheap direct providers or free local models.

## Further detail

### Pitfalls

- **Missing `num_ctx` = Ollama's low default (version-dependent)**: If a model's Modelfile does not set `num_ctx` explicitly (`ollama show --modelfile <model> | grep num_ctx` returns nothing), Ollama silently runs it at a tiny default regardless of the model's advertised context length. The default is **2,048 in Ollama < 0.5** and **4,096 in Ollama ≥ 0.5** (current). Either way it's catastrophic for agentic/tool-use workloads — a model advertised as 128K context silently truncates at 4K. Diagnose with `curl http://127.0.0.1:11434/v1/chat/completions` on a long prompt and watch for HTTP 400 "ex

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/ollama-model-management/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
