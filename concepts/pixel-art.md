---
date: 2026-07-19
type: concept
title: Pixel Art
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- creative
- pixel-art
- arcade
- snes
- nes
- gameboy
- retro
- image
- video
sources:
- hermes://skill/pixel-art
description: Pixel art w/ era palettes (NES, Game Boy, PICO-8).
---

# Pixel Art

> Pixel art w/ era palettes (NES, Game Boy, PICO-8).

## Overview

- **When to Use** — - User wants retro pixel art from a source image - User asks for NES / Game Boy / PICO-8 / C64 / arcade / SNES styling - User wants a short looping animation (rain scene, night sky, snow, etc.) - Posters, album covers, social posts, sprites, characters, avatars
- **Workflow** — Before generating, confirm the style with the user. Different presets produce very different outputs and regenerating is costly.
- **Preset Catalog** — | Preset | Era | Palette | Block | Best for | |--------|-----|---------|-------|----------| | `arcade` | 80s arcade | adaptive 16 | 8px | Bold posters, hero art | | `snes` | 16-bit | adaptive 32 | 4px | Characters, detailed scenes | | `nes` | 8-bit | NES (54) | 8px | True NES look | | `gameboy` | DMG handheld | 4 green shades | 8px | Monochrome Game Boy | | `gameboy_pocket` | Pocket handheld | 4 grey shades | 8px | Mono GB Pocket | | `pico8` | PICO-8 | 16 fixed | 6px | Fantasy-console look | | `c64` | Commodore 64 | 16 fixed | 8px | 8-bit home computer | | `apple2` | Apple II hi-res | 6 fixed

## Further detail

### Scene Catalog (for video)

| Scene | Effects | |-------|---------| | `night` | Twinkling stars + fireflies + drifting leaves | | `dusk` | Fireflies + sparkles | | `tavern` | Dust motes + warm sparkles | | `indoor` | Dust motes | | `urban` | Rain + neon pulse | | `nature` | Leaves + fireflies | | `magic` | Sparkles + fireflies | | `storm` | Rain + lightning | | `underwater` | Bubbles + light sparkles | | `fire` | Embers + sparkles | | `snow` | Snowflakes + sparkles | | `desert` | Heat shimmer + dust |

### Pipeline Rationale

**Pixel conversion:** 1. Boost contrast/color/sharpness (stronger for smaller palettes) 2. Posterize to simplify tonal regions before quantization 3. Downscale by `block` with `Image.NEAREST` (hard pixels, no interpolation) 4. Quantize with Floyd-Steinberg dithering — against either an adaptive N-color palette OR a named hardware palette 5. Upscale back with `Image.NEAREST`

### Dependencies

- Python 3.9+ - Pillow (`pip install Pillow`) - ffmpeg on PATH (only needed for video — Hermes installs package this)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/pixel-art/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
