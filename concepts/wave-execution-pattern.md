---
date: 2026-07-19
type: concept
title: Wave Execution Pattern
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/wave-execution-pattern
description: Implement Wave Execution pattern for dependency-aware parallel processing
  in Hermes workflows
---

# Wave Execution Pattern

> Implement Wave Execution pattern for dependency-aware parallel processing in Hermes workflows

## Overview

- **Overview** — Wave Execution organizes tasks into waves based on dependencies: - **Wave**: A group of tasks that can run in parallel (no dependencies between them) - **Dependencies**: Tasks in later waves depend on completion of earlier waves - **Execution**: All tasks in a wave run concurrently; next wave waits for current wave to complete
- **Wave Execution Algorithm** — 1. **Dependency Analysis**: Analyze tasks to determine dependencies 2. **Wave Formation**: Group tasks into waves where: - No task in a wave depends on another task in the same wave - All dependencies of a task are in earlier waves 3. **Sequential Wave Processing**: - Execute all tasks in Wave 1 in parallel - Wait for Wave 1 completion - Execute all tasks in Wave 2 in parallel - Continue until all waves complete
- **Benefits** — 1. **Performance**: Maximizes parallelism while respecting dependencies 2. **Safety**: Prevents race conditions by ensuring dependencies are met 3. **Clarity**: Makes dependency structure explicit 4. **Monitoring**: Enables wave-by-wave progress tracking 5. **Fault Isolation**: Failures contained within wave

## Further detail

### Integration Points

1. **With delegate_task-protocol**: Use wave execution as an optimization strategy 2. **With structured-execution**: Combine wave execution with phased approaches 3. **With cron-orchestrator**: Schedule wave-based maintenance jobs 4. **With knowledge-metabolism**: Apply wave learning to improve future wave planning

### References

- Maestro-Flow Wave Execution: https://github.com/catlog22/maestro-flow - Dependency-aware parallel processing patterns - DAG-based task scheduling algorithms

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/wave-execution-pattern/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
