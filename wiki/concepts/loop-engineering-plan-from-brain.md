---
type: note
title: Implementation Plan
created: 2026-08-10
source: brain/ (retired 2026-09-13)
---
# Implementation Plan

**Project:** loop-engineering-2026-06-12
**Author:** Hermes Agent (deepseek-v4-flash)
**Created:** 2026-06-12

---

## 🎯 Top Deliverables

| Deliverable | Impact | Effort | Priority |
|-------------|--------|--------|----------|
| **Phase 1: Critic Separation** | High | Small | P0 — Foundation |
| **Phase 2: Triage Inbox** | High | Medium | P0 — Visibility |
| **Phase 3: Skill Auto-Patch** | Medium | Medium | P1 — Feedback |
| **Phase 4: /goal Primitive** | High | Large | P1 — Automation |

---

## 📋 Phase 1: Critic Separation

### Goal
Transform the Self-Harness cycle so that validation (critic) runs in a completely separate sub-agent from code-writing (doer). The doer proposes changes; the critic validates them independently.

### Deliverables

1. **Critic-only sub-agent template**
   - Create `~/.hermes/scripts/critic-agent.sh` — a script that receives a validation target (file path + expected SHA256 + test command), runs validation, and returns structured output (PASS/FAIL with evidence)
   - The critic NEVER writes files — only reads and validates
   
2. **Doer sub-agent updated**
   - Modify the Self-Harness workflow so the doer sub-agent is called with `delegate_task(role='leaf')` and the critic with a separate `delegate_task` call
   - The main loop receives results from both and decides next step

3. **Verification**
   - Test: Run a Self-Harness cycle where doer writes code, critic validates separately
   - Expected: Critic returns PASS/FAIL without having modified any files

### Implementation Notes

- Key pattern: `delegate_task(goal="write X")` → get result → `delegate_task(goal="validate X against Y")` → compare
- The critic's context must include the expected SHA256 hash so it can verify without trusting the doer's output
- Store the "expected" hash before the doer runs, compare after

### Files to Create/Modify

- Create: `~/.hermes/scripts/loop-engine/critic.sh`
- Create: `~/.hermes/scripts/loop-engine/run_critic_loop.py`
- Create: `~/loop-state/` directory structure

---

## 📋 Phase 2: Triage Inbox

### Goal
Every failed validation writes a structured markdown note to `~/loop-state/triage/`. A cron job sweeps these weekly and surfaces patterns.

### Deliverables

1. **Triage note writer**
   - Create `~/.hermes/scripts/loop-engine/triage-write.py` — writes markdown notes with frontmatter (date, script, failure type, evidence, next-step suggestion)

2. **Triage directory**
   - `~/loop-state/triage/YYYY-MM-DD-slug.md` per failure
   - `~/loop-state/triage/INDEX.md` — summary of open items

3. **Weekly sweep cron**
   - Cron job runs every Monday: reads all open triage notes, groups by script, surfaces patterns

### Implementation Notes

- Triage notes follow a strict template so the sweep cron can parse them
- Each note auto-suggests a next action (e.g., "retry with different parameters", "update skill", "escalate to human")

### Files

- Create: `~/.hermes/scripts/loop-engine/triage-write.py`
- Create: `~/loop-state/triage/INDEX.md`
- Create: `~/.hermes/scripts/loop-engine/triage-sweep.sh`
- Cron: weekly sweep job

---

## 📋 Phase 3: Skill Auto-Patch

### Goal
After a Self-Harness cycle completes, check whether the findings should update an existing skill or create a new one. If yes, auto-propose the change via `skill_manage(action='patch')`.

### Deliverables

1. **Post-validation skill updater**
   - After a successful validation, compare the "before" and "after" states
   - If the change represents a new approach/workflow, propose a skill patch
   
2. **Change detection**
   - Track what changed: new flags, new functions, new patterns
   - Map to existing skills by keyword match
   - If no match, propose new skill creation

3. **Auto-patch execution**
   - Generate the `skill_manage(action='patch')` call with old_string/new_string
   - Write to a review file first — don't auto-apply without human review

### Implementation Notes

- This is intentionally conservative: auto-detect, auto-propose, but DON'T auto-apply
- The review file goes to `~/loop-state/reviews/YYYY-MM-DD-patch-review.md`

### Files

- Create: `~/.hermes/scripts/loop-engine/skill-patch-detect.py`
- Create: `~/loop-state/reviews/`

---

## 📋 Phase 4: /goal Primitive

### Goal
Create a run-until-done wrapper: `python3 goal.py "condition" --command "delegate_task(goal='...')"` that keeps iterating until the condition is met or max iterations is hit.

### Deliverables

1. **goal.py**
   - Accepts: `--condition` (Python expression that returns bool), `--command` (shell command or delegate_task spec), `--max-iterations` (default 10)
   - After each iteration: re-evaluate condition
   - On success: Telegram notification + log to `~/loop-state/goals/`
   - On failure: triage note

2. **Condition checking**
   - The condition is a script or Python expression
   - E.g., `--condition "sha256sum file == expected_hash"`
   - E.g., `--condition "pytest tests/ -x --tb=short && echo PASS"`

3. **Integration**
   - `/goal` becomes a Hermes skill invocation
   - Works with `delegate_task` sub-agents
   - Logs iteration count, wall time, final status

### Implementation Notes

- This is the most ambitious phase — it wraps the entire loop infrastructure
- The condition must be checkable WITHOUT running the command (so we know when to stop BEFORE starting)
- Safety: max iterations, timeout per iteration, total timeout

### Files

- Create: `~/.hermes/scripts/loop-engine/goal.py`
- Create: `~/loop-state/goals/`
- Modify: `last30days` skill to include `/goal` as a related primitive

---

## 📊 Progress Tracking

| Phase | Tasks | Complete | Blocked |
|-------|-------|----------|---------|
| Phase 1 | 3 | 0 | 0 |
| Phase 2 | 3 | 0 | 0 |
| Phase 3 | 3 | 0 | 0 |
| Phase 4 | 3 | 0 | 0 |

---

## 📝 Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06-12 | Block auto-apply on Phase 3 | Safety: skills affect all future agent sessions, must be human-reviewed |
| 2026-06-12 | Critic runs AFTER doer, not in parallel | The critic needs the doer's output to validate — sequential is correct |
| 2026-06-12 | All state under ~/loop-state/ | Clean separation from ~/.hermes/ (agent config) and ~/10-projects/ (project docs) |

---

## 🔗 References

- [Addy Osmani - Loop Engineering](https://addyosmani.com/blog/loop-engineering/)
- [Self-Harness skill](~/.hermes/skills/software-development/self-harness/)
- [methodology-loop.md](~/wiki-personal/wiki/concepts/methodology-loop.md)
- [delegate_task documentation](~/.hermes/hermes-agent/docs/)

---

**Last Updated:** 2026-06-12
