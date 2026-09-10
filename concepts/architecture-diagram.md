---
date: 2026-07-19
type: concept
title: Architecture Diagram
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- architecture
- diagrams
- SVG
- HTML
- visualization
- infrastructure
- cloud
- creative
sources:
- hermes://skill/architecture-diagram
description: Dark-themed SVG architecture/cloud/infra diagrams as HTML.
---

# Architecture Diagram

> Dark-themed SVG architecture/cloud/infra diagrams as HTML.

## Overview

- **Scope** — **Best suited for:** - Software system architecture (frontend / backend / database layers) - Cloud infrastructure (VPC, regions, subnets, managed services) - Microservice / service-mesh topology - Database + API map, deployment diagrams - Anything with a tech-infra subject that fits a dark, grid-backed aesthetic
- **Workflow** — 1. User describes their system architecture (components, connections, technologies) 2. Generate the HTML file following the design system below 3. Save with `write_file` to a `.html` file (e.g. `~/architecture-diagram.html`) 4. User opens in any browser — works offline, no dependencies
- **Document Structure** — The generated HTML file follows a four-part layout: 1. **Header:** Title with a pulsing dot indicator and subtitle 2. **Main SVG:** The diagram contained within a rounded border card 3. **Summary Cards:** A grid of three cards below the diagram for high-level details 4. **Footer:** Minimal metadata

## Further detail

### Output Requirements

- **Single File:** One self-contained `.html` file - **No External Dependencies:** All CSS and SVG must be inline (except Google Fonts) - **No JavaScript:** Use pure CSS for any animations (like pulsing dots) - **Compatibility:** Must render correctly in any modern web browser

### Template Reference

Load the full HTML template for the exact structure, CSS, and SVG component examples:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/architecture-diagram/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
