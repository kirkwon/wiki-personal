---
type: concept
title: Loop Engineering
created: 2026-06-15
updated: 2026-06-15
tags: [meta, agent-systems, methodology]
sources: [hermes-sessions]
---

# Loop Engineering

Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, another validates. This separation enables the agent to improve itself without circular reasoning: the critic's judgment is independent of the doer's output, providing an objective signal the system can learn from.

The concept originates from the observation that an agent cannot reliably judge its own work in the same reasoning step that produced it. By splitting action from evaluation across separate invocations, the system gains a ground-truth anchor that makes iterative learning tractable.

## Core Primitives

### Critic/Doer Separation

The fundamental architectural insight. The **doer** modifies state (writes files, runs commands, produces artifacts). The **critic** validates state against expected outcomes (checks hashes, runs tests, inspects results). They communicate through files — never through shared memory or passing judgment within the same process.

| Role | Responsibility | Tool |
|------|---------------|------|
| Doer | Produce or modify an artifact | `run_critic_loop.py` (phase 1) |
| Critic | Validate artifact against objective criteria | `critic.sh`, `goal.py` (condition check) |

### `/goal` Primitive — Run-Until-Done

The `/goal` primitive (implemented in `goal.py`) is a loop-with-condition: execute a command repeatedly until a condition becomes true, then stop. Parameters:

- `--condition`: Shell command that exits 0 when the goal is met
- `--command`: Shell command to run each iteration (the doer)
- `--max-iterations`: Safety limit (default 10)
- `--iteration-timeout`: Per-attempt time limit (default 300s)
- `--total-timeout`: Wall-clock limit (default 3600s)

The loop checks the condition first (fast-fail if already satisfied), then iterates: doer → condition check → repeat. Iteration logs are written to `~/loop-state/goals/` as structured JSON files.

This is distinct from a simple retry loop — the condition is evaluated independently of the doer's exit code, enabling the critic to detect success even when the doer's process returns non-zero.

### Meta-Loop

The meta-loop is a loop *about* the improvement process itself. It observes:

- Iteration counts per cycle (rising counts → restructure the harness)
- Gap signatures across sessions (personal catalog of recurring weakness patterns)
- Validation threshold effectiveness (false-positive/false-negative rates)
- Harness lifecycle (should a harness be retired, merged, or split?)

This is what transforms one-off fixes into a self-modifying system. See [[#Self-Harness Paradigm]] for the full three-layered architecture.

## Components

All scripts live under `~/.hermes/scripts/loop-engine/`. The Hermes codebase mirrors them at `github/hermes-code/loop-engine/`.

### `critic.sh`

A pure validation script — never modifies files. Validates three conditions in order:

1. **File exists** — the target artifact is present
2. **SHA256 matches** — the artifact's hash equals an expected value
3. **Optional test command passes** — runs a user-supplied validation command

Outputs structured JSON (`{"status":"PASS"|"FAIL","checks":{...},"evidence":"...","actual-sha256":"..."}`). Exits 0 on PASS, 1 on FAIL.

The critic skips downstream checks when prior ones fail (e.g., no tests run if SHA256 mismatches). This ensures the evidence chain is meaningful.

### `goal.py`

Implements the `/goal` primitive. Written in Python 3.8+, zero stdlib dependencies beyond `subprocess`, `json`, `argparse`, `time`. Key behaviors:

- Checks condition **before** the first iteration (fast-path for already-satisfied goals)
- Per-iteration and total-wall-clock timeouts prevent infinite hangs
- Logs every iteration as a separate JSON file plus a final summary
- Status outcomes: `already-satisfied`, `achieved`, `max-iterations`

### `skill-patch-detect.py`

Compares "before" and "after" versions of a script, extracts structured changes (functions, imports, CLI flags, docstrings, comments), and maps them to existing Hermes skills by keyword overlap. Writes a review proposal to `~/loop-state/reviews/`.

Uses a weighted scoring system (function definitions score 3×, imports 2×, identifiers 1×) to rank skill relevance. The output drives the skill-update workflow in the meta-loop.

### `triage-sweep.sh`

A weekly triage sweep that reads all triage notes from `~/loop-state/triage/`, groups failures by script name, and outputs a plain-text summary. For each script it reports:

- Failure count
- Most common failure type
- Oldest open item (with `[STALE]` marker for notes >14 days old)

Written entirely in bash (no Python dependency). Designed for Telegram delivery.

### `triage-write.py`

Writes structured markdown triage notes with YAML frontmatter. Validated failure types: `sha256-mismatch`, `test-failure`, `timeout`, `error`. Automatically regenerates `~/loop-state/triage/INDEX.md` on each write.

### `run_critic_loop.py`

Orchestrates a complete doer→critic cycle:

1. Capture SHA256 hash **before** doer runs
2. Execute doer command
3. Capture hash after doer
4. Execute critic (test command, expected to call `critic.sh`)
5. Compare doer exit vs critic exit
6. Emit structured JSON

Status outcomes: `pass`, `doer_fail`, `critic_fail`, `both_fail`, `mismatch`.

## Runtime State

The loop engineering system uses `~/loop-state/` for all transient and persistent state:

| Directory | Purpose |
|-----------|---------|
| `~/loop-state/goals/` | Iteration logs and summaries from `goal.py` |
| `~/loop-state/reviews/` | Patch review proposals from `skill-patch-detect.py` |
| `~/loop-state/triage/` | Triage notes and auto-generated INDEX.md |

## Key Insight

**Separating the critic from the doer enables faster learning** because:

1. **Independent signal** — the critic's judgment is not contaminated by the doer's reasoning context. The same agent, acting as critic in a separate invocation, can catch errors the doer-phase self would miss.

2. **Objective ground truth** — SHA256 hashes and exit codes are deterministic. The agent doesn't negotiate with itself about whether a change is correct; the hash either matches or it doesn't.

3. **Parallel improvement** — the critic logic can be improved independently of the doer logic, and vice versa. A better critic (more thorough tests, tighter tolerances) immediately improves the whole loop without touching how work gets done.

4. **Forgiving failures** — when the critic catches a failure, the doer can retry with the failure evidence in context. Without the critic, the doer would either silently produce a bad artifact or waste resources on post-hoc self-inspection.

This maps to the [[self-harness-paradigm]]'s inner loop: Weakness Mine → Harness Propose → Proposal Validate. The critic is the Proposal Validate gate, and the meta-loop turns iteration data into improvement of the improvement process itself.

## Related Concepts

- [[self-harness-paradigm]] — The three-layer improvement methodology that loop engineering powers
- [[methodology-loop]] — The full three-layered system (inner: self-harness, middle: validation gate, outer: meta-loop)
- [[memory-tiering]] — Data lifecycle concept for harness state management across hot/warm/cold tiers
