---
date: 2026-07-19
type: concept
title: Prism Reflect
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Prism
- Analysis
- Code-Review
- Architecture
- Quality
- Research
- uncategorized
sources:
- hermes://skill/prism-reflect
description: 'Constraint transparency: analyzes an artifact structurally, then analyzes
  what its own analysis concealed. Produces a conservation law AND a constraint report
  showing what was maximized, what was sacrificed, and what to investigate next. The
  only AI skill that knows what it can''t see.'
---

# Prism Reflect

> Constraint transparency: analyzes an artifact structurally, then analyzes what its own analysis concealed. Produces a conservation law AND a constraint report showing what was maximized, what was sacrificed, and what to investigate next. The only AI skill that knows what it can't see.

## Overview

- **When to Use** — Use when the blind spots matter as much as the findings — before relying on an analysis, when a previous pass felt too clean, or when the user asks what was missed. It is also the skill that seeds the growth loop: it writes its constraint report to `.prism-history.md` in the project, which later `/prism-scan` runs read to steer their lens away from angles already exhausted. Costs 2-3x a `/prism-scan` run.
- **PHASE 1: Structural Analysis** — You are a structural analyst. Read the artifact and execute this pipeline:
- **PHASE 2: Meta-Analysis (Analyze Your Own Output)** — Now step back. Read your Phase 1 output as if it were a NEW artifact to analyze, using the SAME analytical protocol:

## Further detail

### PHASE 3: Constraint Transparency Report

Output a structured report:

### PHASE 4: Growth — Persist Constraint Knowledge

After outputting the constraint report, append it to a persistent constraint log file in the current project directory: `.prism-history.md`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/prism-reflect/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
