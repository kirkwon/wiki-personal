---
date: 2026-07-19
type: concept
title: Subagent Driven Development
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- delegation
- subagent
- implementation
- workflow
- parallel
- software-development
sources:
- hermes://skill/subagent-driven-development
description: Execute plans via delegate_task subagents (2-stage review).
---

# Subagent Driven Development

> Execute plans via delegate_task subagents (2-stage review).

## Overview

- **Overview** — Execute implementation plans by dispatching fresh subagents per task with systematic two-stage review.
- **When to Use** — Use this skill when: - You have an implementation plan (from writing-plans skill or user requirements) - Tasks are mostly independent - Quality and spec compliance are important - You want automated review between tasks
- **Task Granularity** — **Each task = 2-5 minutes of focused work.**

## Further detail

### Red Flags — Never Do These

- Start implementation without a plan - Skip reviews (spec compliance OR code quality) - Proceed with unfixed critical/important issues - Dispatch multiple implementation subagents for tasks that touch the same files - Make subagent read the plan file (provide full text in context instead) - Skip scene-setting context (subagent needs to understand where the task fits) - Ignore subagent questions (answer before letting them proceed) - Accept "close enough" on spec compliance - Skip review loops (reviewer found issues → implementer fixes → review again) - Let implementer self-review replace actu

### Efficiency Notes

**Why fresh subagent per task:** - Prevents context pollution from accumulated state - Each subagent gets clean, focused context - No confusion from prior tasks' code or reasoning

### Remember

**Quality is not an accident. It's the result of systematic process.**

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/subagent-driven-development/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
