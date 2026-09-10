---
date: 2026-07-19
type: concept
title: Prism Full
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Prism
- Analysis
- Code-Analysis
- Code-Review
- Quality
- Refactoring
- uncategorized
sources:
- hermes://skill/prism-full
description: 'Full Prism: multi-pass structural analysis with mandatory adversarial
  self-correction. Designs custom analytical passes, executes them with chaining,
  then attacks its own findings before synthesizing. Use for maximum depth on important
  code or artifacts.'
---

# Prism Full

> Full Prism: multi-pass structural analysis with mandatory adversarial self-correction. Designs custom analytical passes, executes them with chaining, then attacks its own findings before synthesizing. Use for maximum depth on important code or artifacts.

## Overview

- **When to Use** — Use when the artifact matters enough to pay for depth — a core module, a design about to be committed to, a document whose conclusions will be acted on. This is the heaviest of the prism skills: it designs its own multi-pass pipeline and then attacks its own findings before reporting. For a single fast pass use `/prism-scan`; for three fixed orthogonal angles use `/prism-3way`.
- **PHASE 1: Design the pipeline** — You are a pipeline architect. Read the artifact the user provided. Design analytical passes specifically for THIS artifact.
- **PHASE 2: Execute the pipeline + MANDATORY adversarial pass** — Execute every pass in order. For each: 1. State which pass you are executing 2. Execute the full instructions against the artifact (and for passes 2+, against all previous analysis) 3. Output the complete analysis

## Further detail

### PHASE 3: Synthesis

Produce the final reconciled output:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/prism-full/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
