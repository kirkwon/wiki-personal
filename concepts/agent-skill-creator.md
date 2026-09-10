---
date: 2026-08-02
type: concept
title: Agent Skill Creator
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/agent-skill-creator
description: Create cross-platform agent skills from workflow descriptions. Activates
  when users ask to create an agent, automate a repetitive workflow, create a custom
  skill, or need advanced agent creation. Triggers on phrases like create agent for,
  automate workflow, create skill for, every day I have to, daily I need to, turn
  process into agent, need to automate, create a cross-platform skill, validate this
  skill, export this skill, migrate this skill. Supports single skills, multi-agent
  suites, transcript processing, template-based creation, interactive configuration,
  cross-platform export, and spec validation.
---

# Agent Skill Creator

> Create cross-platform agent skills from workflow descriptions. Activates when users ask to create an agent, automate a repetitive workflow, create a custom skill, or need advanced agent creation. Triggers on phrases like create agent for, automate workflow, create skill for, every day I have to, daily I need to, turn process into agent, need to automate, create a cross-platform skill, validate this skill, export this skill, migrate this skill. Supports single skills, multi-agent suites, transcript processing, template-based creation, interactive configuration, cross-platform export, and spec validation.

## Overview

- **Trigger** — User invokes `/agent-skill-creator` followed by their input:
- **How the Factory Works** — Raw material goes in. A validated, security-scanned, self-contained skill comes out.
- **Trigger** — User invokes `/skill-name` followed by their input:

## Further detail

### Architecture Decision

| Factor | Simple Skill | Complex Suite | |--------|-------------|---------------| | Workflows | 1-2 | 3+ distinct | | Code size | <1000 lines | >2000 lines | | Maintenance | Single developer | Team | | Structure | Single SKILL.md | Multiple component SKILL.md files | | marketplace.json | Shipped by default (`.claude-plugin/`, Step 6.5) | Shipped by default (official fields only) |

### Cross-Platform Support

Generated skills work across 17 tools in 3 tiers. Every generated skill outputs both **SKILL.md** (skill definition, ~15 tools) and **AGENTS.md** (instruction file, ~15 tools) to maximize reach.

### Validation and Security

After generating a skill, run:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/agent-skill-creator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
