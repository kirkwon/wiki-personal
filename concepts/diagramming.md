---
date: 2026-07-19
type: concept
title: Diagramming
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/diagramming
description: Create architecture diagrams, system designs, and visual documentation
  using Draw.io, Mermaid, Excalidraw, and hand-coded SVG. Prefer cli-anything-drawio
  for canonical architecture diagrams. Use Mermaid for inline flowcharts in markdown
  docs. Use Excalidraw for hand-drawn style wireframes. Trigger on phrases like "architecture
  diagram", "draw this", "visualize", "flowchart", "system design", "mermaid", "drawio",
  "excalidraw".
---

# Diagramming

> Create architecture diagrams, system designs, and visual documentation using Draw.io, Mermaid, Excalidraw, and hand-coded SVG. Prefer cli-anything-drawio for canonical architecture diagrams. Use Mermaid for inline flowcharts in markdown docs. Use Excalidraw for hand-drawn style wireframes. Trigger on phrases like "architecture diagram", "draw this", "visualize", "flowchart", "system design", "mermaid", "drawio", "excalidraw".

## Overview

- **Tool Selection** — | Format | Tool | Best For | |--------|------|----------| | Draw.io | `cli-anything-drawio` | Canonical architecture diagrams, 15+ shape types, 5 export formats | | Mermaid | Inline in markdown | Simple flowcharts, sequence diagrams, state machines in docs | | Excalidraw | `excalidraw` skill | Hand-drawn style wireframes, sketches, whiteboard-style | | SVG | Hand-coded or generated | Complex custom visuals, dark-themed architecture diagrams |
- **Semantic Color Palette** — | Layer | Fill | Stroke | |-------|------|--------| | Identity/Layer 0 | `#1a1a2e` | `#e94560` | | Strategy/Layer 1 | `#0a3d2e` | `#34d399` | | Execution/Layer 2 | `#16213e` | `#0ea5e9` | | Review/Layer 3 | `#3d0a2e` | `#f43f5e` | | Belief/Layer 4 | `#2e1a3d` | `#a78bfa` | | Communication/Layer 5 | `#3d2e0a` | `#f59e0b` | | Knowledge/Layer 6 | `#201a3d` | `#6366f1` |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/diagramming/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
