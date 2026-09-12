---
type: concept
title: Single_Layer_Lora_Heartbeat
created: 2026-09-11
updated: 2026-09-11
tags:
  - Skill
  - heartbeat
---

# single_layer_lora_heartbeat

Health-check that validates the current single-layer LoRA adapter on GSM8K and logs accuracy. Alerts if accuracy drops below threshold.

## Usage

# Single Layer LoRA Heartbeat

Periodic health-check that:
1. Loads the current adapter (or baseline model if no adapter exists yet)
2. Runs GSM8K evaluation on 60 problems (seed varies per run)
3. Logs accuracy to `audit/heartbeat_log.md`
4. Alerts if accuracy drops below 25% — an **integrity floor**, deliberately below the
   measured un-adapted baseline of **31.5%** (n=200, 2026-08-25 recalibration).
   It detects real regression/corruption only; it is NOT a performance target.
   The adapter's true rate (~29%) is statistically equal to baseline — see
   decisions/decision-log.md D-P5-07.

## Trigger
- Cron: every 4 hours
- Manual: `bash ~/.hermes/skills/single_layer_lora_heartbeat/scripts/check_heartbeat.sh`

## Dependencies
- P5 project venv: `~/clawd/01.P5-singlelayer-rl/.venv`
- P5 eval script: `~/clawd/01.P5-singlelayer-rl/03.Scripts/01_baseline_eval.py`