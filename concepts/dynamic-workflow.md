---
type: concept
title: Dynamic Workflow
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Dynamic Workflow
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- orchestration
- fan-out
- subagents
- delegation
- verification
- migration
- audit
- research
- autonomous-ai-agents
sources:
- hermes://skill/dynamic-workflow
description: Orchestrate large fan-out work as a plan-in-code "workflow" so the agent's
  context holds only the final verified answer, not the exhaust of hundreds of intermediate
  steps. Use for codebase-wide sweeps, large migrations, multi-angle research, and
  any task too big for one context window where the split strategy is known enough
  to script. Includes the adversarial-convergence verification recipe (independent
  attempts + refuters, keep only surviving claims).
---

# Dynamic Workflow

> Orchestrate large fan-out work as a plan-in-code "workflow" so the agent's context holds only the final verified answer, not the exhaust of hundreds of intermediate steps. Use for codebase-wide sweeps, large migrations, multi-angle research, and any task too big for one context window where the split strategy is known enough to script. Includes the adversarial-convergence verification recipe (independent attempts + refuters, keep only surviving claims).

## Overview

- **The two orchestration-script layers (pick the right one — they are NOT interchangeable)** — Hermes has no JS runtime. The "orchestration script" is one of two layers, and the split is enforced by a real capability boundary, not a style preference:
- **The synchronous trap (READ THIS — it is the #1 way a "workflow" disappoints)** — `delegate_task` runs **synchronously inside the parent turn**. If the user sends a new message, hits /stop, or /new, every in-flight child is **cancelled and its work discarded** (status `interrupted`). It does NOT run in the background, and it does NOT survive the turn. There is no cache-resume of a half-finished fan-out.
- **Workflow recipe (foreground)** — 1. **Decompose into independent units.** What is the unit — a file? an endpoint? a source? a record? Each unit must be answerable WITHOUT the others' output (else it's serial, not fan-out — see when_not_to_use). 2. **Deterministic pre-pass (Layer A).** In one `execute_code` script, gather the manifest: list the files, extract the candidate sites, fetch the raw sources, compute anything regex/parse can compute. Write a manifest to a **unique per-run** directory — `/tmp/wf_<name>_<uuid>/manifest.jsonl` (one unit per line), never a bare `/tmp/wf_<name>/` that a prior interrupted run could have le

## Further detail

### The novel mechanic worth building: adversarial convergence

This is the part Hermes did NOT already have and the real reason to bother. Claude Code's quality claim ("independent agents try to refute each other's findings; only surviving claims surface; iterate until they converge") maps cleanly onto `delegate_task` batch mode:

### Cost discipline (this is the thing that bites)

A workflow can consume dramatically more tokens than a normal turn — that is inherent, not a bug. Two real multipliers:

### Pitfalls

- **Writing `delegate_task` inside an `execute_code` script.** It's not in `SANDBOX_ALLOWED_TOOLS`; the import/stub won't exist. Layer A is deterministic tools only. Fan out LLM judgment from the parent turn, not from inside a script. - **Promising background/resumable from `delegate_task`.** It's synchronous and turn-scoped. Durable = kanban swarm. - **Trusting `summary` fields for content.** Route structured output to files (Pattern 2 in delegate-task-output-patterns). - **Non-atomic claims in the verify recipe.** Unfalsifiable claims survive refutation by default and pollute the output. For

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/dynamic-workflow/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
