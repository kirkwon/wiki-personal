---
date: 2026-07-19
type: concept
title: Project_scaffolder
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/project_scaffolder
description: Initializes a zero-padded, OKF-compliant, agent-optimized workspace with
  an integrated auto-research pipeline and decision-tracking subsystem.
---

# Project_scaffolder

> Initializes a zero-padded, OKF-compliant, agent-optimized workspace with an integrated auto-research pipeline and decision-tracking subsystem.

## Overview

- **When to Use** — - Starting a new project, research track, or experiment that belongs in `~/clawd/` - User says "create a new clawd project" or "new project for X" with request for structured scaffolding - You need a project with integrated auto-research pipeline and decision-tracking from day one - When starting projects that require systematic research workflows (incoming → refined) and decision logging
- **Execution Steps** — Follow these in order. **Do not skip steps.**
- **OKF Compliance Notes** — - **index.md** at project root → OKF reserved name, optional frontmatter with `okf_version` - **Every .md file** that is a "concept document" must have YAML frontmatter with `type` field - **AGENTS.md** → `type: playbook` - **Decision records** → `type: decision-record` - **ACTIVITY.md** → `type: log` (used instead of `log.md` per existing clawd convention) - **Archive/** files should get `status: archived` in their frontmatter

## Further detail

### Templates Embedded in Skill

The skill contains embedded templates for all files created. When executing, these templates are instantiated with the provided parameters.

### Integration Notes

- **Research Pipeline**: The `02.Research/incoming/` → `02.Research/refined/` structure supports your autonomous research workflow where raw intelligence is pulled in, then refined into atomic concepts. - **Decision Tracking**: The `decisions/` subsystem includes both a status board (INDEX.md) and append-only log (decision-log.md) for tracking architectural decisions and tradeoffs. - **Agent Optimization**: The AGENTS.md serves as a linear run book with phase gating, designed to be followed step-by-step during project execution. - **Zero-Padding**: Uses NNN format (001, 002, etc.) to ensure pr

### Pitfalls to Avoid

- **Don't renumber existing folders**: Breaks inbound references (cron, config, gbrain) - **Don't create folders past N=999**: Consider grouping if approaching limit - **Git init inside git-tracked parent**: Each project gets its own independent .git repo (don't add as submodule unless explicitly asked) - **Maintain OKF compliance**: Ensure all .md concept documents have proper frontmatter with type field - **Update parent workspace**: Always update ~/clawd/INDEX.md and ~/clawd/ACTIVITY.md after creation

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/project_scaffolder/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
