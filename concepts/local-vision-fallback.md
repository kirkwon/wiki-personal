---
date: 2026-07-19
type: concept
title: Local Vision Fallback
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Vision
- OCR
- Ollama
- Debugging
- Charts
- software-development
sources:
- hermes://skill/local-vision-fallback
description: See images when the active model lacks native vision.
---

# Local Vision Fallback

> See images when the active model lacks native vision.

## Overview

- **When to Use** — - `vision_analyze` failed with `code: 1210` or `content.type is invalid` - You need to verify a generated chart, diagram, or screenshot rendered correctly - You generated graphics with `image_generate` or matplotlib and must confirm them before delivery - The active model is text-only (e.g. glm-5, deepseek, gemma text variants) but the task requires visual QA - You want to read text/numbers OUT of an image (OCR) rather than judge its aesthetics - You're setting up a new Hermes instance and need to wire vision from scratch
- **Prerequisites** — **Step 0 — Fix the config (primary fix, see Procedure):** - A multimodal model available in Ollama (e.g. `glm-ocr:latest`, `llava:7b`, `minicpm-v:8b`) - `hermes config` CLI access
- **How to Run** — **Step 0 — Fix `auxiliary.vision.model` (primary fix):**

## Further detail

### Pitfalls

- **The config fix IS the fix — don't skip to OCR/VLM.** The most common cause of `code: 1210` is `auxiliary.vision.model` pointed at a text-only model (e.g. `qwen3.5:9b-mlx`). Swapping to any multimodal Ollama model (`glm-ocr:latest`, `llava:7b`) via `hermes config set auxiliary.vision.model <model>` resolves it permanently. Always try the config fix before falling back to OCR/VLM workarounds. - **OCR path got moved.** The script lives at `software-development/vision/scripts/screen_ocr.py` (under the category dir), NOT `~/.hermes/skills/vision/scripts/`. If you get `[Errno 2] No such file or

### Verification

Confirm both paths work on a known image:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/local-vision-fallback/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
