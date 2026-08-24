---
created: 2026-06-12
updated: 2026-06-12
---
# Loop Engineering Implementation Plan

**Start Date:** 2026-06-12
**Status:** 🟢 Active
**Phase:** Phase 1 - Critic Separation

---

## 🎯 Project Overview

Apply Addy Osmani's Loop Engineering thesis to tighten Kirk's agentic loops, critic loop, and learning loop. Build the concrete infrastructure that separates critics from doers, surfaces failures into a triage inbox, auto-updates skills from loop output, and adds a `/goal` run-until-done primitive.

---

## 📋 Philosophy

This project encodes loop engineering values into system behavior:

| Value | System Implementation |
|-------|---------------------|
| **Separation of concerns** | Critic and doer are never the same sub-agent |
| **Auditable failures** | Every validation failure writes a structured triage note |
| **Closed-loop learning** | Loop output feeds back into skill updates automatically |
| **Run-until-done** | `/goal` primitive replaces manual iteration |
| **Six-piece architecture** | Every loop has: Automations, Worktrees, Skills, Plugins, Sub-agents, Memory |

---

## 📂 Systems Touched

| System | Role | Integration Point |
|--------|------|------------------|
| **Self-Harness** (methodology-loop.md) | Core improvement loop | Critic separation, triage, auto-patch |
| **delegate_task** | Sub-agent execution | Worktree isolation, critic/doer split |
| **~/.hermes/skills/** | Skill repository | Auto-patch phase 3 |
| **~/.hermes/scripts/** | Cron jobs | `/goal` primitive integration |
| **~/loop-state/** | New triage + state directory | Phases 2, 4 |
| **Telegram** | Notification | Triage alerts, goal completion |

---

## 🤔 Why This Project

Osmani's loop engineering thesis maps precisely onto the three loops Kirk already runs:
- **Agentic loop** (Self-Harness: Weakness Mine → Harness Propose → Proposal Validate) — the doer loop
- **Critic loop** (Validation Layer: tests, hashes, metrics) — the verifier
- **Learning loop** (Meta-Loop: meta-weakness mine → meta-propose → meta-validate) — the improver

The gap: all three currently run as the same agent context. Separating them is the single highest-leverage change — it's small in code, transformative in architecture.

---

## 📅 Timeline & Phases

### **Phase 1: Critic Separation** (2026-06-12)
High-leverage, small code change. Split the Self-Harness cycle so the critic/validator runs as a completely separate sub-agent.

### **Phase 2: Triage Inbox** (2026-06-12)
Medium scope. Create `~/loop-state/triage/` directory + validation-failure writing script + cron-driven sweep.

### **Phase 3: Skill Auto-Patch** (2026-06-12)
Medium scope. Add post-validation step that checks if findings should update a skill. Creates `skill_manage(action='patch')` calls automatically.

### **Phase 4: /goal Primitive** (2026-06-12)
Larger scope. Wraps delegate_task in a `while-until-satisfied` loop with condition checking, iteration limits, and Telegram notification on completion.

---

## 📊 Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Critic/doer separation | Same agent | Different sub-agents |
| Failure visibility | Telegram only | Triage inbox + Telegram |
| Skill update latency | Manual | Auto-proposed |
| Loop iteration | Manual re-run | `/goal` run-until-done |

---

## 🔗 Resources

- **Inspiration:** [Addy Osmani - Loop Engineering](https://addyosmani.com/blog/loop-engineering/)
- **Related:** [methodology-loop.md](https://github.com/kirkwon/wiki-personal/blob/main/wiki/concepts/methodology-loop.md)
- **Skills:** Self-Harness, delegate_task, writing-plans, subagent-driven-development
- **Repo:** [hermes-code](https://github.com/kirkwon/hermes-code) on GitHub

---

## 📝 Notes

All four phases build on each other. Phase 1 (critic separation) is the foundation — without it, the other phases have no independent verifier to write triage notes about.

---

**Last Updated:** 2026-06-12
