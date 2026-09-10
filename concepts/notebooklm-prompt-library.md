---
date: 2026-07-19
type: concept
title: Notebooklm Prompt Library
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/notebooklm-prompt-library
description: Curated NotebookLM prompts for research analysis, critical evaluation,
  and styled output generation.
---

# Notebooklm Prompt Library

> Curated NotebookLM prompts for research analysis, critical evaluation, and styled output generation.

## Overview

- **When to Use** — Load this skill when you need to: - **Analyze reports/sources** with critical depth (not just summarize) - **Style NotebookLM output** (slides, video, infographics) with professional design - **Synthesize multiple sources** into actionable intelligence - **Reality-check tools/frameworks** before adoption (eval-first) - **Research a new domain** from multiple documents
- **Integration with Domain Notebook Syncs** — The shared runner script is wired into 5 domain notebook sync scripts via a **post-sync hook**. After sources load, each script auto-runs a domain-appropriate prompt and saves the output.
- **Validation** — See `references/test-validation-loop-engineering.md` for validated test results — prompts #4 (Multi-Pass) and #5 (Disillusionment Filter) tested on the Loop Engineering notebook, both PASS. Also includes E2E integration test (decision-science sync → auto-disillusionment analysis, 4993 chars).

## Further detail

### Sources

- **serenakeyitan/awesome-notebookLM-prompts** (⭐4.1k) — visual slide prompts - **danielrosehill/NotebookLM-Custom-Prompts** (⭐101) — skeptical report analysis - **GMartin-Data/notebooklm-prompts** (⭐151) — 60-prompt library with empirical testing - **0xeb/TheBigPromptLibrary** — leaked NotebookLM system prompt (reference only)

### Related Skills

- `notebooklm-cli` — full CLI command reference for `nlm` - `notebooklm-research-pipeline` — end-to-end research pipeline

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/notebooklm-prompt-library/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
