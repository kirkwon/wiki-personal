---
date: 2026-07-19
type: concept
title: Baoyu Article Illustrator
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- article-illustration
- creative
- image-generation
sources:
- hermes://skill/baoyu-article-illustrator
description: 'Article illustrations: type × style × palette consistency.'
---

# Baoyu Article Illustrator

> Article illustrations: type × style × palette consistency.

## Overview

- **When to Use** — Trigger this skill when the user asks to illustrate an article, add images to an article, generate illustrations for content, or uses phrases like "为文章配图", "illustrate article", or "add images". The user provides an article (file path or pasted content) and optionally specifies type, style, palette, or density.
- **Three Dimensions** — | Dimension | Controls | Examples | |-----------|----------|----------| | **Type** | Information structure | infographic, scene, flowchart, comparison, framework, timeline | | **Style** | Rendering approach | notion, warm, minimal, blueprint, watercolor, elegant | | **Palette** | Color scheme (optional) | macaron, warm, neon — overrides style's default colors |
- **Types** — | Type | Best For | |------|----------| | `infographic` | Data, metrics, technical | | `scene` | Narratives, emotional | | `flowchart` | Processes, workflows | | `comparison` | Side-by-side, options | | `framework` | Models, architecture | | `timeline` | History, evolution |

## Further detail

### Styles

See [references/styles.md](references/styles.md) for Core Styles, the full gallery, and Type × Style compatibility.

### Output Structure

**Default output directory**:

### Core Principles

- **Visualize concepts, not metaphors** — if the article uses a metaphor (e.g., "电锯切西瓜"), illustrate the underlying concept, not the literal image. - **Labels use article data** — actual numbers, terms, and quotes from the article, not generic placeholders. - **Prompt files are reproducibility records** — every illustration must have a saved prompt file under `prompts/` before any image is generated. - **Strip secrets** — scan source content for API keys, tokens, or credentials before writing anything to disk.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
