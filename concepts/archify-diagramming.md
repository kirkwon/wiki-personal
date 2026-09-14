---
type: concept
title: Archify Diagramming
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Archify Diagramming
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- creative
- diagram
- architecture
- workflow
- sequence
- data-flow
- lifecycle
- documentation
sources:
- hermes://skill/archify-diagramming
description: Generate beautiful architecture, workflow, sequence, data-flow, and lifecycle
  diagrams from plain English descriptions. Produces self-contained HTML files with
  dark/light toggle, copy-to-clipboard PNG, and up-to-4x multi-format export. From
  tt-a1i/archify. Bridges creativity-master (diagrams) and software-development-master
  (architecture docs).
---

# Archify Diagramming

> Generate beautiful architecture, workflow, sequence, data-flow, and lifecycle diagrams from plain English descriptions. Produces self-contained HTML files with dark/light toggle, copy-to-clipboard PNG, and up-to-4x multi-format export. From tt-a1i/archify. Bridges creativity-master (diagrams) and software-development-master (architecture docs).

## Overview

- **Diagram Types** — | Type | Good For | How to Ask | |------|----------|------------| | **Architecture** | System components, cloud resources, databases, caches, services, boundaries, security groups | "Diagram this system architecture" | | **Workflow** | Request lifecycles, approval flows, tool calls, CI/CD, runbooks, incident response | "Show the deployment workflow" | | **Sequence** | API call chains, request lifecycles, cache fallback, auth checks, async traces | "Trace the API call flow" | | **Data Flow** | Data pipelines, ETL/ELT, analytics events, PII isolation, warehouse sync, lineage | "Map the data pipe
- **How to Use** — Archify generates a **self-contained HTML file** — open in any browser, interact immediately:
- **When to Use** — | Trigger | Output | |---|---| | "Diagram the architecture" | Architecture diagram (components, connections, boundaries) | | "Show the request flow" | Workflow diagram (swimlanes, participants, steps) | | "Trace the API calls" | Sequence diagram (who calls whom, in what order) | | "Map the data pipeline" | Data flow diagram (sources → processing → storage → consumers) | | "Show lifecycle states" | State machine diagram (states, transitions, events) |

## Further detail

### Integration

This skill bridges creativity-master and software-development-master:

### Comparison

| Tool | Input | Output | Best For | |------|-------|--------|----------| | **archify** | Natural language | Self-contained HTML | Architecture docs, shareable diagrams | | **mermaid-diagrams** | Mermaid DSL | PNG/SVG/PDF | Inline docs, technical flowcharts | | **architecture-diagram** | Description | Dark-themed SVG | Cloud architecture presentations | | **cli-anything-drawio** | Commands | Draw.io XML | Interactive editing, templates | | **excalidraw** | Description | JSON | Hand-drawn wireframes, brainstorming |

### Notes

- Archify outputs are **zero-dependency HTML files** — share by sending the file - Works with any natural language description — no diagram syntax to learn - Particularly good for: system architecture documentation, onboarding docs, PR descriptions, runbooks - For PRs: attach the HTML file — reviewers can open it in their browser without any tools

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/archify-diagramming/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
