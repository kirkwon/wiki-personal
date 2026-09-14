---
type: concept
title: Cli Anything Drawio
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Cli Anything Drawio
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- drawio
- diagrams
- architecture
- svg
- cli
- agent-native
- creative
sources:
- hermes://skill/cli-anything-drawio
description: Agent-native Draw.io CLI — create, edit, and export architecture diagrams
  from the command line. 7 command groups (project, page, shape, connect, export,
  session, repl), 15 shape types, 4 edge styles, 5 export formats (SVG, PNG, PDF,
  VSDX, XML). All commands support --json output.
---

# Cli Anything Drawio

> Agent-native Draw.io CLI — create, edit, and export architecture diagrams from the command line. 7 command groups (project, page, shape, connect, export, session, repl), 15 shape types, 4 edge styles, 5 export formats (SVG, PNG, PDF, VSDX, XML). All commands support --json output.

## Overview

- **When to Use** — - Creating architecture diagrams (replaces hand-coded SVG) - Editing existing .drawio files from CLI - Exporting diagrams to SVG, PNG, PDF - Adding shapes, connectors, labels to existing diagrams
- **Installation** — Installed under Hermes venv at `~/.hermes/hermes-agent/venv/bin/cli-anything-drawio`.
- **Quick Reference** — **Global options:** `--json`, `--project FILE`, `--dry-run`

## Further detail

### Line Breaks in Labels (CRITICAL PITFALL)

The CLI accepts `<br>` in label strings but **XML-escapes them** to `&lt;br&gt;`, which draw.io renders as literal text. After building a diagram, post-process the XML:

### Scripted Diagram Generation Pattern

For complex diagrams with 15+ shapes, write a Python build script rather than issuing one-off CLI commands. Pattern:

### Related Skills

- `architecture-diagram` — SVG fallback for diagrams that need the dark-grid aesthetic - `mermaid-diagrams` — Simpler flowcharts in markdown - `cli-anything-mermaid` — Mermaid live editor CLI

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/cli-anything-drawio/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
