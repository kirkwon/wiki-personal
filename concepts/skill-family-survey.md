---
date: 2026-07-19
type: concept
title: Skill Family Survey
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Skills
- Survey
- Comparison
- Synthesis
- knowledge-management
sources:
- hermes://skill/skill-family-survey
description: Compare sibling skills by batch-loading their docs.
---

# Skill Family Survey

> Compare sibling skills by batch-loading their docs.

## Overview

- **When to Use** — - "Tell me about the various masters" / "what X-master skills do you have" - "Compare these skills" / "how are knowledge-master and learning-master different" - "What skills do you have for Y?" spanning 3+ siblings - Any survey/overview/explain-the-landscape question over a skill family - "Which skill should I use for X?" when multiple candidates exist
- **Prerequisites** — - `skills` toolset enabled — to call `skill_view` - The target skill family installed (e.g., the 7 `*-master` meta-skills)
- **How to Run** — 1. Enumerate the FULL family — never miss a sibling. Scan the skill index in the system prompt or the category directory before loading. 2. Batch-load ALL siblings via `skill_view` in ONE tool block (parallel calls), not serially across turns. 3. Extract a uniform shape from each: architecture type, sub-skill count, key differentiator, phase/contract discipline. 4. Synthesize five layers (below). End with an honest critique and a concrete offer to act on it.

## Further detail

### Quick Reference

- Load command: `skill_view(name='X')` — repeat for each sibling in one tool block - Uniform shape: `{name, domain, architecture_type, sub_skill_count, differentiator}` - Five synthesis layers: table → shared DNA → flow/DAG → outliers → critique - Skill index source: the `available_skills` block in the system prompt - Category directory: `~/.hermes/skills/<category>/`

### Procedure

1. **Enumerate the family.** Identify every sibling before touching a tool. If the user names some ("knowledge master, learning master, coding master"), infer the family (`*-master`) and include siblings they did not name (creativity, finance, decision). Missing a sibling is the #1 survey defect. 2. **Batch-load.** Emit all `skill_view` calls in a SINGLE tool block so they execute in parallel. Never load one skill, respond, then load the next — that burns round-trips and reads stale partial state. 3. **Extract uniform shape** from each loaded skill. Same fields for every sibling so they line u

### Pitfalls

- **Missing siblings.** A survey of 5 when 7 exist is defective. Enumerate from the index first; the user naming a few does not bound the family. - **Serial loading.** Loading one skill per turn wastes round-trips and risks reading partial state. Batch in one tool block always. - **Paraphrase over structure.** Re-pasting each skill's prose is noise. The value is the uniform-shape extraction and the five synthesis layers — structural, not narrative. - **No critique.** A survey that only praises is useless. The honest critique (overlap, bloat, dead test logs) is where leverage lives — the user v

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/skill-family-survey/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
