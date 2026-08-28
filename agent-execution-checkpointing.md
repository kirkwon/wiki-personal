---
type: concept
title: Agent Execution Checkpointing
created: 2026-08-27
updated: 2026-08-27
tags:
  - Skill
  - uncategorized
---

# agent-execution-checkpointing

Use when agent tasks may span context or turn limits.

## Usage

# Agent Execution Checkpointing

## When to Use

- A task is too large to complete in one context window or session
- The agent may hit turn limits, context caps, or session hard-stops mid-execution
- You need a clean resumption point that a fresh invocation can pick up from
- The task has natural milestones where checkpointing makes sense

**Not for:** one-shot tasks, tasks small enough to fit in a single invocation, or tasks where you have a more specific persistence mechanism already in place.

## Core Principle

**The plan document is the checkpoint.** A self-contained planning document that tracks progress, decisions, and next steps serves as the resumption artifact. A fresh agent invocation reads the plan, sees what's done and what's next, and continues — no external state wrangling required.

This is the ExecPlan methodology: a single markdown file with living sections that the executing agent updates as it goes. The plan is self-contained — a novice (or fresh agent) can read it top-to-bottom and produce a working result.

## Methodology

### The ExecPlan Pattern

An ExecPlan is a single markdown file (optionally wrapped in a fenced code block) that contains:

1. **Purpose / Big Picture** — what someone gains after this change, how to see it working
2. **Progress** — timestamped checkbox list; every stopping point documented; may split "done" vs "remaining" for partially completed steps
3. **Surprises & Discoveries** — unexpected behaviors, bugs, optimizations found during execution (with evidence)
4. **Decision Log** — every decision made, with rationale and date/author
5. **Outcomes & Retrospective** — filled at major milestones or completion
6. **Context and Orientation** — current state as if the reader knows nothing; key files by full path; definitions of non-obvious terms
7. **Plan of Work** — prose sequence of edits and additions
8. **Concrete Steps** — exact commands to run, working directory, expected output; updated as work proceeds
9. **Validation and Acceptance** — how to verify; acceptance phrased as observable behavior
10. **Idempotence and Recovery** — safe retry paths, rollback for risky steps
11. **Artifacts and Notes** — terminal output, diffs, logs that prove success
12. **Interfaces and Dependencies** — libraries, modules, services to use; types/signatures that must exist

### Golden Rules

- **Self-contained:** the plan contains all knowledge needed. No external docs, no "as defined previously," no inference from prior context.
- **Living document:** update Progress, Decision Log, and Surprises as you go. Every revision must remain self-contained.
- **Observable acceptance:** phrase validation as behavior a human can verify ("navigating to /health returns HTTP 200 with body OK"), not internal attributes ("added a HealthCheck struct").
- **No "next steps" prompting:** the agent proceeds to the next milestone autonomously. Don't ask the user for direction between milestones.
- **Novice-guiding:** a complete novice (or fr

...(truncated)