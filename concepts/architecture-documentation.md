---
date: 2026-07-19
type: concept
title: Architecture Documentation
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- architecture
- documentation
- knowledge-archaeology
- system-mapping
- notebooklm
- mermaid-diagrams
- knowledge
sources:
- hermes://skill/architecture-documentation
description: Systematic cross-workspace knowledge archaeology for comprehensive system
  architecture documentation with Mermaid diagrams and NotebookLM-ready output.
---

# Architecture Documentation

> Systematic cross-workspace knowledge archaeology for comprehensive system architecture documentation with Mermaid diagrams and NotebookLM-ready output.

## Overview

- **When to Use** — - User asks "document my [system/stack/architecture]" referencing multiple components - Need to produce a NotebookLM-ready markdown document from scattered sources - System spans multiple workspaces (~/clawd/, ~/.zeroclaw/, ~/Downloads/, ~/10-projects/, etc.) - User wants architecture diagrams (Mermaid) generated from textual system understanding - Documenting the agent system itself (dogfood documentation) - User says "document this" for a single system — **evaluate depth**: heavy archaeology (this skill) vs lightweight manifest (productivity-master workflow E)
- **Mode Selection: Lightweight Manifest vs Heavy Archaeology** — When asked to "document this system," choose the right depth:
- **1. Section** — Narrative explanation.

## Further detail

### References

See `references/2026-06-13-hermes-architecture-session.md` for the full session notes on the original cross-workspace archaeology (24K words, 11 diagrams). See `references/2026-07-03-skill-ecosystem-manifest-session.md` for a lightweight manifest session (text + 4 PNGs, 8 tool calls, single-system scope).

### Example Output

The architecture guide produced by this pattern lives at `~/clawd/hermes-architecture-guide.md` (24K words, 11 Mermaid diagrams, 9 sections covering Hermes ingestion, agentic harness, and memory systems).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/architecture-documentation/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
