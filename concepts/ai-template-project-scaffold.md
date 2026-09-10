---
date: 2026-08-02
type: concept
title: Ai Template Project Scaffold
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/ai-template-project-scaffold
description: Scaffold projects with GraphWork + AI template overlay.
---

# Ai Template Project Scaffold

> Scaffold projects with GraphWork + AI template overlay.

## Overview

- **When to Use** — Use when you want to start a new AI‑focused project (LLM agents, retrieval pipelines, prompt engineering, etc.) and benefit from both: - GraphWork enforced protocols (decision logging, activity logging, task checklists, independent verification) - The AI template’s concern‑based folder layout (agents, pipelines, retrieval, llm, guardrails, etc.)
- **Steps** — 1. Ensure the AI template repository is present at `~/clawd/ai-template`. If missing, clone it:
- **References** — - `references/ai-template-structure.md` – detailed mapping of AI template folders to GraphWork concern folders. - `templates/graph_scaffold_ai_template.patch` – the patch applied to `graph_scaffold.py` to add the `--template ai` functionality.

## Further detail

### Pitfalls

- The AI template must be cloned under `~/clawd/ai-template`; otherwise the scaffolder will fail to find the source files. - If you modify the AI template locally, remember to re‑run the scaffolder for new projects to capture those changes. - The `--template ai` flag is optional; omitting it yields a plain GraphWork project (no AI overlay).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/project-management/ai-template-project-scaffold/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
