---
date: 2026-07-19
type: concept
title: Tts Setup
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- tts
- text-to-speech
- audio
- edge-tts
- kokoro
- hermes
- media
sources:
- hermes://skill/tts-setup
description: Text-to-Speech setup, providers, and troubleshooting for Hermes Agent
  environments
---

# Tts Setup

> Text-to-Speech setup, providers, and troubleshooting for Hermes Agent environments

## Overview

- **Hermes Agent Config** — TTS configured in `~/.hermes/config.yaml` under `tts:` section:
- **Known Pitfalls** — - **mlx-kokoro not installed**: Config says `mlx-kokoro` but package missing. Use edge-tts or kokoro-tts CLI instead. - **Python path issues**: Packages installed in venv but not in default Python. Use `python3` from venv or set PYTHONPATH. - **Voice not found**: `kokoro-tts` voices are different from Edge voices. Use `kokoro-tts --help-voices` to see available options. - **Model files not found**: kokoro-tts CLI can't find model files unless you specify --model and --voices paths explicitly. Default paths don't match where you put the models. - **Hermes has no voice command**: There is no `he
- **MARPTalk TTS** — MARPtalk uses kokoro-tts via Node.js wrapper: - Path: `~/.zeroclaw/workspace/projects/MARPtalk/marptalk/` - Script: `src/generate-audio-kokoro.js` - Model files present: `kokoro-v1.0.onnx` (310MB), `voices-v1.0.bin` (25MB) - CLI installed: `/Users/kirkwon/.local/bin/kokoro-tts`

## Further detail

### Size Comparison

- **kokoro-tts model files**: ~335MB total (310MB + 25MB) - **mlx-audio package**: similar model size, but requires MLX-converted model (different format) - **mlx-kokoro (via MLX on Apple Silicon)**: should be faster than Python-based kokoro-tts, but not installed due to dependency issues (numpy version mismatch)

### mlx-audio Install Issues

Requires compatible numpy version. Check https://github.com/Blaizzy/mlx-audio for latest requirements.

### On-device Speed

Per kokoro documentation: "3-5x real-time speed on a CPU and at least 50x on a GPU". Kokoro-82M processes texts in under 0.3 seconds across tested lengths.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/tts-setup/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
