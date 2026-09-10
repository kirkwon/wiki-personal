---
date: 2026-07-19
type: concept
title: Baoyu Comic
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- comic
- knowledge-comic
- creative
- image-generation
sources:
- hermes://skill/baoyu-comic
description: 'Knowledge comics (知识漫画): educational, biography, tutorial.'
---

# Baoyu Comic

> Knowledge comics (知识漫画): educational, biography, tutorial.

## Overview

- **When to Use** — Trigger this skill when the user asks to create a knowledge/educational comic, biography comic, tutorial comic, or uses terms like "知识漫画", "教育漫画", or "Logicomix-style". The user provides content (text, file path, URL, or topic) and optionally specifies art style, tone, layout, aspect ratio, or language.
- **Reference Images** — Hermes' `image_generate` tool is **prompt-only** — it accepts a text prompt and an aspect ratio, and returns an image URL. It does **NOT** accept reference images. When the user supplies a reference image, use it to **extract traits in text** that get embedded in every page prompt:
- **File Structure** — Output directory: `comic/{topic-slug}/` - Slug: 2-4 words kebab-case from topic (e.g., `alan-turing-bio`) - Conflict: append timestamp (e.g., `turing-story-20260118-143052`)

## Further detail

### Language Handling

**Detection Priority**: 1. User-specified language (explicit option) 2. User's conversation language 3. Source content language

### References

**Core Templates**: - [analysis-framework.md](references/analysis-framework.md) - Deep content analysis - [character-template.md](references/character-template.md) - Character definition format - [storyboard-template.md](references/storyboard-template.md) - Storyboard structure - [ohmsha-guide.md](references/ohmsha-guide.md) - Ohmsha manga specifics

### Page Modification

| Action | Steps | |--------|-------| | **Edit** | **Update prompt file FIRST** → regenerate image → download new PNG | | **Add** | Create prompt at position → generate with character descriptions embedded → renumber subsequent → update storyboard | | **Delete** | Remove files → renumber subsequent → update storyboard |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/baoyu-comic/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
