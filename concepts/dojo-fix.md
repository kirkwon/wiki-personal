---
date: 2026-07-19
type: concept
title: Dojo Fix
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/dojo-fix
description: Reads Dojo analysis output and applies skill patches/fixes using skill_manage.
  Auto-fix phase of the monitor → analyze → fix pipeline.
---

# Dojo Fix

> Reads Dojo analysis output and applies skill patches/fixes using skill_manage. Auto-fix phase of the monitor → analyze → fix pipeline.

## Overview

- **Prerequisites** — 1. `dojo-eval.py` has been run recently (it reads `~/.hermes/state.db`) 2. `dojo-analyze.py` has been run recently (it reads the monitor output and generates fix recommendations) 3. Analysis output is at `~/.hermes/dojo-eval/latest_analysis.json` 4. Fix plan is at `~/.hermes/dojo-eval/fix_plan.json` (if `--fix-plan` was used)
- **Fix Templates** — Use these templates for new skill creation:
- **Workflow** — 1. <step 1> 2. <step 2>

## Further detail

### Error Handling

- If <error X>: <fix Y> - If <error Z>: <fix W>

### Prerequisites

- <dependency>

### Usage

Use `web_extract` to fetch content from <target>.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/dojo-fix/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
