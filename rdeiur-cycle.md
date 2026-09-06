---
type: concept
title: Rdeiur Cycle
created: 2026-09-05
updated: 2026-09-05
tags:
  - Skill
  - agents
---

# rdeiur-cycle

RDEIUR (Run→Discuss→Execute→Invalidate→Update→Resume) cycle — separated plan/execute/critique loop with OmniRoute dual-model critic, targeted replanning, and canary-calibrated verification.

## Usage

# RDEIUR Cycle — Separated Plan/Execute/Critique Loop

A named, stateful cycle where the executor (you) runs a task and a **different model** (via OmniRoute) independently critiques the output before it's committed to the knowledge graph. Closes the "Invalidate" gap identified in the 11-diagram audit.

## When to Use

- **Code tasks** (functions, scripts, configs) — critic catches bugs the executor misses
- **Analysis tasks** (research summaries, decision docs) — critic finds logical gaps
- **Any task where a silent defect compounds** — critic is the safety net

## When NOT to Use

- Trivial tasks (rename a file, fix a typo)
- Tasks you can verify deterministically (run a test, check an exit code)
- Time-critical tasks where 25-30s of critic latency is unacceptable

## The Six Phases

### R — Run
Accept the task. Initialize state. Load relevant context. On a retry re-entry, load the prior verdict's **retry_context** (defects + affected subtasks) instead of starting fresh.

```
State: { task, context, started_at, status: "running" }
```

### D — Discuss (Plan/Decompose)
Decompose the task into subtasks. Write the execution plan. Identify dependencies. Pass the plan to the critic so defects carry `subtask_index` — this is what makes **targeted replanning** possible.

```
State: { ..., plan: [{subtask, approach, exit_criteria}], status: "planning" }
```

### E — Execute
Run each subtask per the plan. Produce the output. On retry, fix **only the affected subtasks** from the retry_context.

```
State: { ..., output: <artifact>, status: "executing" }
```

### I — Invalidate (Critique)
**The core innovation.** Route the output to a different model via OmniRoute for independent verification. The critic has zero context about how the output was produced — it only sees the artifact and the exit criteria.

```
State: { ..., verdict: {decision, defects, severity, confidence}, status: "critiqued" }
```

**Verdict values:**
- `accept` — output meets exit criteria, no critical defects
- `retry` — defects found, executor should fix and resubmit
- `escalate` — fundamental problem, needs human review

**Severity-weighted decisions:** the final decision is computed from defect severities, not taken verbatim from the model. Any critical/high defect forces retry; low nits alone never do (Goodhart's Law mitigation).

**Plan-aware defects:** each defect may include `subtask_index` — which plan subtask it belongs to. The retry then targets only those subtasks.

### U — Update
Write verified results to gbrain + project state. Record lessons.

```
State: { ..., updated_graph: true, status: "updated" }
```

### R — Resume
Pick up next task or iterate on flagged gaps.

```
State: { ..., status: "resumed" | "completed" | "escalated" }
```

## Configuration

### Default Critic Model
`oc/deepseek-v4-flash-free` — free, catches 2.5× more defects than executor (benchmark-validated)

### High-Stakes Critic
`aug/claude-sonnet-4.6` — free via OmniRoute, stronger reasoning

### Fall

...(truncated)