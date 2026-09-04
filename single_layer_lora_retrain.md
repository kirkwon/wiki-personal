---
type: concept
title: Single_Layer_Lora_Retrain
created: 2026-09-03
updated: 2026-09-03
tags:
  - Skill
  - cron
---

# single_layer_lora_retrain

Weekly retraining job for the single-layer LoRA adapter. Runs GRPO training on arm B (single layer 18) and copies the fresh adapter to the canonical location.

## Usage

# Single Layer LoRA Retrain

Weekly cron job that retrains the single-layer LoRA adapter (arm B: layer 18 only, rank 64)
using GRPO on GSM8K, then atomically swaps the fresh adapter into the canonical location.

## Trigger
- Cron: weekly (Sunday 03:00)
- Manual: `bash ~/.hermes/skills/single_layer_lora_retrain/scripts/run_retrain.sh`

## What it does
1. Activates the P5 venv (torch 2.13, transformers 5.14, peft 0.20)
2. Runs `03_grpo_train.py --model Qwen/Qwen2.5-0.5B-Instruct --arm B --steps 200`
3. Adapter saves to the canonical `03.Scripts/adapter_arm_B/` (path fixed 2026-08-17)
4. Runs a quick 20-sample sanity eval (same 0.5B base) and logs the accuracy

## Cron wiring (2026-08-17)
- Job `weekly_lora_retrain` (547ffc18c9ae) is a **no_agent script job** → `~/.hermes/scripts/lora-weekly-retrain.sh` (shim) → this script. Never run it as an agent job: the 2026-08-16 agent run tried to patch the training script mid-run, failed, and self-reported ok.
- TIMEOUT_SECS=3900: 200 steps × ~16s/step ≈ 55 min + eval. The hardened-wrapper default (300s) would kill it at step ~15.

## Pitfalls (proven 2026-08-17)
- **Model consistency is load-bearing**: train/eval/heartbeat must ALL use the same base model. Training defaulted to 3B while the heartbeat evals 0.5B → shape mismatch (2048 vs 896 dim), adapter unloadable. Chain is now standardized on 0.5B.
- **3B is cron-infeasible**: ~6 min/step → 200 steps ≈ 20h. 0.5B ≈ 16s/step ≈ 55 min.
- **Adapter save path**: `03_grpo_train.py` must save to `Path(__file__).parent/adapter_arm_{arm}`. The old `output_dir.parent/"03.Scripts"/...` resolution put it under `audit/` when invoked from the cron wrapper.
- **GRPO gradients**: log-probs must come from a grad-enabled teacher-forced forward over the full sequence — `model.generate()`'s `output_scores` are detached. The `.detach().requires_grad_(True)` escape masks the error and trains nothing (see `grpo-lora-gradient-fix` — its "fix" was an error mask; the real fix landed 2026-08-16 in the training script).

## Dependencies
- P5 project venv: `~/clawd/01.P5-singlelayer-rl/.venv`
- P5 scripts: `~/clawd/01.P5-singlelayer-rl/03.Scripts/`
- Model cached: `~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/`