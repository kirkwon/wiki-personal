---
date: 2026-07-19
type: concept
title: Creativity Master
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/creativity-master
description: Meta-skill for generating — diagrams, writing, media, ideation. Turn
  ideas into visual and written artifacts.
---

# Creativity Master

> Meta-skill for generating — diagrams, writing, media, ideation. Turn ideas into visual and written artifacts.

## Overview

- **A/B Testing Overlap Pairs** — | Skill A | Skill B | Overlap | Test Prompt | |---|---|---|---| | `mermaid-diagrams` | `cli-anything-mermaid` | Both create Mermaid diagrams | "Draw a system architecture" | | `excalidraw` | `architecture-diagram` | Both produce visual diagrams | "Design a cloud architecture" | | `gif-search` | `gifs` | Both find GIFs | "Find a reaction GIF" | | `improve-writing` | `multi-perspective-essay` | Both work with writing | "Improve this draft" |
- **Notes** — - Mermaid is the most versatile diagram format — renders to PNG, SVG, PDF via mmdc. Prefer it for most diagram needs. - `cli-anything-mermaid` and `cli-anything-drawio` are browser-based CLIs. Useful when you need to see and edit the diagram interactively. - `architecture-diagram` produces HTML-based dark-themed SVGs. Best for presentation-ready infrastructure diagrams. - Media skills (spotify, gif-search, tts-setup) are lightweight utilities. They don't feed into the knowledge pipeline. - Creativity outputs often become knowledge inputs — the bridge from creativity-master to knowledge-master

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creativity-master/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
