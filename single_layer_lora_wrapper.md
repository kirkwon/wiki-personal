---
type: concept
title: Single_Layer_Lora_Wrapper
created: 2026-09-03
updated: 2026-09-03
tags:
  - Skill
  - tool
---

# single_layer_lora_wrapper

Wraps the single-layer LoRA adapter training and application logic as a Hermes tool.

## Usage

# The skill provides a tool named `skill_to_lora_single` that can be used in config.yaml
# to convert a raw skill directory into a LoRA (or merged model) using the single-layer
# adapter trained in the P5 experiment.
tools:
  - name: skill_to_lora_single
    description: Apply the single-layer LoRA adapter (optionally merged) to a skill directory.
    type: tool
    # The actual implementation is the script at:
    #   /Users/kirkwon/clawd/01.Singlelayerloraintegration/03.Scripts/skill_to_lora_single.py
    # We'll reference it via the `script` field (relative to skill directory).
    script: 03.Scripts/skill_to_lora_single.py
    # The tool expects two positional arguments: skill_dir and an optional flag --merge.
    # We'll define the signature here for documentation.
    args:
      - name: skill_dir
        description: Path to the raw skill directory (containing SKILL.md).
        type: string
        required: true
      - name: merge
        description: If present, merge the adapter into a full HF model.
        type: boolean
        default: false
# No hooks needed for this simple tool.