---
date: 2026-07-19
type: concept
title: Prism Scan
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Prism
- Analysis
- Code-Analysis
- Code-Review
- Architecture
- Quality
- uncategorized
sources:
- hermes://skill/prism-scan
description: Structural analysis through dynamically generated cognitive lenses. Generates
  the optimal analytical lens for the specific code/artifact, then executes it. Finds
  conservation laws, structural invariants, and concrete bugs that vanilla analysis
  misses. Use on any code file, system design, or text artifact.
---

# Prism Scan

> Structural analysis through dynamically generated cognitive lenses. Generates the optimal analytical lens for the specific code/artifact, then executes it. Finds conservation laws, structural invariants, and concrete bugs that vanilla analysis misses. Use on any code file, system design, or text artifact.

## Overview

- **When to Use** — Use on a single code file, system design, spec, or any text artifact when the user wants depth rather than a checklist — "what's structurally wrong with this", "what trade-off can't I escape here", "review this properly". Also the right entry point when the user names a focus ("focusing on security", "with emphasis on performance"). For maximum depth on an important artifact use `/prism-full`; to map which angles are worth taking first use `/prism-discover`.
- **STEP 0: Check for prior constraint knowledge (growth)** — Look for a `.prism-history.md` file in the current project directory. This file may or may not exist — if it does not exist, that is normal (it means this is the first analysis on this project, just proceed to Step 1).
- **STEP 1: Cook the lens** — You are a lens generator. Read the artifact the user provided. Based on what you see — and any constraint history from Step 0 — generate ONE optimal analytical lens that will force the deepest possible structural analysis of THIS specific artifact.

## Further detail

### STEP 2: Execute the lens

Now execute your generated lens against the artifact. Follow every instruction in the lens. Output the complete analysis. Do not summarize, do not ask permission, do not skip steps.

### Reliability Note

For guaranteed single-shot execution (no agentic loops), use `--tools ""` flag when running via Claude CLI. This ensures the model executes the full analysis in one response rather than splitting into multiple turns.

### Proven Prisms (reference material)

STEP 1 always cooks a fresh lens — that is the point of this skill, and these files do not change it. They ship alongside the skill as pre-validated alternatives for the two cases where a fixed lens is wanted: the user asks for a specific prism by name, or asks for a scored/reproducible lens instead of a generated one. Load one on demand with `skill_view("prism-scan", "<path>")`.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/prism-scan/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
