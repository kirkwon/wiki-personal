---
date: 2026-08-02
type: concept
title: Decision Workflow Slop Assessment
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/decision-workflow-slop-assessment
description: Assess workflow quality using Maestro's Workflow Slop Test to detect
  anti-patterns in AI agent workflows
---

# Decision Workflow Slop Assessment

> Assess workflow quality using Maestro's Workflow Slop Test to detect anti-patterns in AI agent workflows

## Overview

- **Overview** — This skill provides a structured assessment based on Maestro's Workflow Slop Test to identify anti-patterns in AI agent workflows. It can be used as part of Hermes' decision-making process to evaluate workflow quality before execution.
- **The Workflow Slop Checklist** — Based on Maestro's agent-workflow skill, a workflow exhibits "slop" if any of these conditions are true:
- **Integration with Hermes Decision Framework** — This assessment can be integrated into Hermes' decision process:

## Further detail

### Integration Points

1. **With decision-logger skill**: Add slop assessment to decision entries 2. **With agent-workflow skill**: Use as pre-check before applying Maestro commands 3. **In delegation workflows**: Assess delegate_task goals for slop before spawning subagents 4. **In cron jobs**: Periodically assess active workflows for slop accumulation

### References

- Maestro agent-workflow skill: https://github.com/sharpdeveye/maestro/blob/main/source/skills/agent-workflow/SKILL.md - Workflow Slop Test section: https://github.com/sharpdeveye/maestro/blob/main/source/skills/agent-workflow/SKILL.md#the-workflow-slop-test

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/decision/workflow-slop-assessment/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
