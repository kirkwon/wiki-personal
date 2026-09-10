---
date: 2026-07-19
type: concept
title: Mermaid Diagrams
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mermaid
- diagrams
- mmdc
- puppeteer
- visualization
- charts
- creative
sources:
- hermes://skill/mermaid-diagrams
description: Generate Mermaid diagrams and render them to PNG/SVG/PDF using mmdc (Mermaid
  CLI). Covers installation, Puppeteer configuration, and rendering workflows.
---

# Mermaid Diagrams

> Generate Mermaid diagrams and render them to PNG/SVG/PDF using mmdc (Mermaid CLI). Covers installation, Puppeteer configuration, and rendering workflows.

## Overview

- **When to use this skill** — - User asks to create a flowchart, sequence diagram, class diagram, state diagram, ER diagram, gantt chart, or any Mermaid-supported diagram type - User wants to render a `.mmd` file to an image - User asks to install or configure mmdc / Mermaid CLI
- **Installation** — **Do NOT use `pip install mmdc`** — the Python package has broken dependencies. Use npm:
- **Themes** — - `default` — light background - `dark` — dark background - `forest` — green-tinted - `neutral` — grayscale

## Further detail

### Common Diagram Types

| Type | Syntax | Best For | |------|--------|----------| | Flowchart | `graph TD` / `graph LR` | Process flows, decision trees | | Sequence Diagram | `sequenceDiagram` | API calls, message passing | | Class Diagram | `classDiagram` | OOP structure | | State Diagram | `stateDiagram-v2` | State machines | | ER Diagram | `erDiagram` | Database schemas | | Gantt Chart | `gantt` | Project timelines | | Pie Chart | `pie` | Data proportions | | Mindmap | `mindmap` | Hierarchical ideas |

### Quick Test

Expected output: `Generating single mermaid chart` with no errors.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/mermaid-diagrams/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
