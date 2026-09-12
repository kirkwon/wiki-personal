---
date: 2026-07-19
type: concept
title: Maestro Integration Workflow
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Workflow
- Maestro
- Integration
- Optimization
- Process
- workflow
sources:
- hermes://skill/maestro-integration-workflow
description: Guide Maestro workflow integration through assessment and optimization
  phases.
---

# Maestro Integration Workflow

> Guide Maestro workflow integration through assessment and optimization phases.

## Overview

- **When to Use** — - Integrating Maestro workflow tools into Hermes agent workflows - Assessing and improving AI agent workflow quality using Maestro's diagnostic framework - Implementing dependency-aware parallel execution patterns for delegate_task optimization - Following a phased workflow enhancement process: Assess → Refine → Fortify → Evaluate → Optimize
- **Prerequisites** — - Node.js v20.0.0 or higher installed - npm package manager available - maestro-workflow-mcp npm package installed globally (`npm install -g maestro-workflow-mcp`) - maestro-bridge skill available in Hermes - Basic understanding of Maestro workflow concepts (slop test, wave execution, fortify/refine/streamline/evaluate/accelerate/guard)
- **How to Run** — Follow the Procedure section using Hermes tools like `skill_manage`, `delegate_task`, and `write_file`. Execute each step sequentially using the referenced tools to complete the Maestro integration workflow.

## Further detail

### Quick Reference

- skill_manage create decision/workflow-slop-assessment - skill_manage create software-development/wave-execution-pattern - delegate_task goal: "Run Maestro /diagnose command" skills=["mcp/maestro-bridge"] - delegate_task goal: "Run Maestro /refine command" skills=["mcp/maestro-bridge"] - delegate_task goal: "Run Maestro /fortify command" skills=["mcp/maestro-bridge"] - delegate_task goal: "Run Maestro /evaluate command" skills=["mcp/maestro-bridge"] - delegate_task goal: "Run Maestro /streamline command" skills=["mcp/maestro-bridge"] - delegate_task goal: "Assess workflow slop" skills=["decis

### Procedure

1. Create Maestro workflow slop assessment skill:

### Pitfalls

- Forgetting to install maestro-workflow-mcp globally causes MCP bridge to return empty responses for all Maestro commands - Proceeding to remediation steps before assessment delegations complete (wait for /diagnose and slop assessment results) - Overlooking the requirement to check for .maestro/context.md and .maestro.md files in agent workflows when implementing context gathering - Assuming Maestro commands work identically in Hermes without proper context setup through the MCP bridge - Neglecting to verify skill creation (using skill_view) before attempting to use custom Maestro-integration

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/workflow/maestro-integration-workflow/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[project-integration-workflow]]
