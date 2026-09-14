---
type: source
title: "Loop Engineering: The 14-Step Roadmap from Prompter to Loop Designer"
description: "A comprehensive framework for building autonomous agent loops — replacing manual prompting with systems that find work, execute, verify, and decide next moves."
author: "@0xCodez"
source_url: "https://x.com/0xcodez/status/2064374643729773029"
published: 2026-06-09
tags: [loop-engineering, agents, automation, mcp, skills, worktrees, sub-agents, anthropic]
confidence: verified
created: 2026-06-25
source: brain/ (retired 2026-09-13)
---
# Loop Engineering: The 14-Step Roadmap from Prompter to Loop Designer

> Leverage point moved — from typing prompts to designing systems that prompt.

**Author:** @0xCodez
**Posted:** 2026-06-09
**Source:** [X Post](https://x.com/0xcodez/status/2064374643729773029)

Loop engineering means building a small system that finds work, hands it to the agent, checks the result, records what happened, and decides the next move — on its own. You design that system once; it prompts the agent from then on.

**Key stat:** Anthropic engineers now merge 8× more code per day than in 2024 (Anthropic calls this "almost certainly an overstatement" of true productivity gain — but the mechanism is real).

---

## Core Thesis

The leverage point has moved from **typing prompts** to **designing systems that prompt**. Most developers still prompt their coding agents by hand: type, wait, read the diff, type again. 9 out of 10 builders have never written a single loop that prompts the agent for them — no automation, no state file, no verifier, no schedule.

---

## Part 1 — The Why & The Test

### Step 1: Loop Engineering Defined

> Addy Osmani breaks loops into six parts: find the work → hand it to the agent → check the result → record → decide next move → repeat.

The core pattern is the **evaluator-optimizer** from Anthropic's Dec 2024 engineering post — one agent generates, another verifies.

### Step 2: The 4-Condition Test (mandatory before building)

> Miss one condition and the loop costs more than it returns.

1. **Task repeats weekly or more** — one-time jobs stay manual
2. **Automated verification exists** — test suite, type checker, linter, or build that rejects bad output
3. **Token budget can absorb waste** — loops re-read context, retry, explore; scales with budget
4. **Agent has senior engineer's tools** — logs, reproduction environment, ability to run code it writes

### Step 3: Who Wins vs Who Loses

**Winners:**
- Teams with repetitive, machine-checkable work and token budget
- Codebases with strong test suites
- Async-first teams already using multi-agent patterns
- The gap between winners and losers will widen

**Skip for now:**
- Solo builders on consumer plans ($20 plan)
- Codebases with no automated verification
- Teams where review capacity (not typing speed) is the bottleneck
- One-off tasks or exploratory work

### Step 4: The 30-Second Loop Check (per task)

1. Happens at least weekly? (else setup never amortizes)
2. Automated gate exists? (test/type/build/linter)
3. Agent can run the code it changes?
4. Hard stop defined? (token/iteration/time limit)
5. Human reviews before merge/deploy/dependency changes?

**Good first loops:** CI failure triage, dependency bump PRs, lint-and-fix passes, flaky test reproduction, issue-to-PR drafts on well-tested code.

**Bad first loops:** Architecture rewrites, auth/payments code, production deploys, vague product work, judgment-call tasks (naming, UX, prioritization).

---

## Part 2 — The 5 Building Blocks

### Step 5: Automations — The Heartbeat

Fire on schedule, event, or trigger.

- **Codex:** Automations tab (project + prompt + cadence)
- **Claude Code:** Three primitives — `/loop` (session-scoped cadence), Desktop scheduled tasks (system-level), Routines (cloud runs)
- **Key distinction:** `/loop` re-runs on a cadence; `/goal` keeps going until an objective condition is *actually true* — checked by a separate small model (maker-vs-checker split for stop conditions)

### Step 6: Worktrees — Parallel Without Chaos

> Two agents writing the same file is the same headache as two engineers committing to the same lines.

- **Codex:** Built-in worktree support for parallel threads
- **Claude Code:** `--worktree` flag, `isolation: worktree` setting for subagents with auto-cleanup
- **Limitation:** Your review bandwidth decides how many parallel agents you can actually run — not the tool

### Step 7: Skills — Write Once, Read Every Run

A folder with `SKILL.md` containing instructions, metadata, optional scripts/references. Without skills, every run re-derives project context from zero. With skills, intent compounds.

### Step 8: Connectors — Touch Real Tools via MCP

Built on the Model Context Protocol. Difference between "here is the fix" and a loop that opens the PR, links the ticket, and pings the channel once CI is green.

**Fastest-paying connectors in order:**
1. GitHub (repos, branches, PRs, issues, webhooks)
2. Linear/Jira (update tickets, link PRs, auto-close)
3. Slack (post triage results, ping humans, summarize overnight runs)
4. Sentry/error tracker (investigate live alerts, draft fixes)

### Step 9: Sub-Agents — Maker vs Checker

> The model that wrote the code is way too nice grading its own homework.

- **Pattern:** Evaluator-optimizer — one generates, another critiques
- **Codex:** Define agents as TOML files in `.codex/agents/`
- **Claude Code:** Similar subagents in `.claude/agents/` + agent teams
- **Usual split:** one explores, one implements, one verifies against spec
- **Trade-off:** burns more tokens — spend where a second opinion is worth paying for

---

## Part 3 — Build It Right or Don't Build It

### Step 10: The State File — The Spine of Every Working Loop

> The agent forgets. The file does not. ^[inferred]

Persistent state records what's done and what's next. Two patterns:
- **`STATE.md`** in repo — version-controlled, simple, solo/small team
- **External system** (Linear board, task queue) — team-wide visibility, production loops

Pair with a standing spec (e.g. `VISION.md`) that the agent re-reads each run so it knows where it's going.

### Step 11: The Minimum Viable Loop (MVL)

Four parts, no more:
1. **Automation** (the trigger — schedule/event)
2. **State file** (remembers what was done)
3. **Verifier** (checks the output)
4. **Connector** (reports back)

Build these four and stop. Any more is premature.

### Step 12: Hard Stops — Protect Against Runaway Loops

- **Token budget** — cut at N tokens
- **Iteration cap** — stop after N cycles
- **Time limit** — kill after N minutes
- **Change percentage** — flag if diff touches >X% of files
- **Dependency guard** — pin versions, require human review for upgrades
- **Repo-aware** — detect scope creep by change footprint
- Recommendation: 3-tier — warn at 60%, soft stop at 80%, hard stop at 100%

### Step 13: Observability

> Engineers who instrument their loops find problems faster and ship more.

- **Dashboards** — count runs, pass/fail, tokens burned, agents spawned
- **Logs** — every run produces a timestamped file with input, output, decisions
- **Audit trail** — who changed what, when, by which agent
- Recommendation: publish per-loop stats to a channel so humans can watch the loop work

### Step 14: Comprehension Debt & Cognitive Surrender

Two risks that compound silently:

> **Comprehension debt** — the faster the loop ships code you didn't write, the larger the distance between what the repository contains and what you understand. The day you have to debug a system no one on the team has read. ^[inferred]

> **Cognitive surrender** — the pull to stop forming an opinion and accept whatever the loop returns. The easiest review is the rubber stamp. ^[inferred]

**Mitigations:**
- Review requirements, not output (spec first, diff second)
- Have a "no silent changes" policy — every merge should be seen
- Run comprehension audits — can you explain the system's architecture without reading it?
- Sampling reviews — pick N random PRs per week and read them deeply
- Time-bounded review slots — limit review time per PR to force focused reading

---

## Connections to existing infrastructure

This paper maps directly to ongoing work in the wiki-tools project and Hermes agent system:

- **Goal-based loops** — the `goal-loop` skill and `goal-loop.sh` wrapper implement the `/goal` pattern from Step 5
- **Skills** — the 333 Hermes skills (Step 7) already exist; the paper reinforces the pattern
- **Connectors/MCP** — MCP servers for GitHub, Linear, Slack (Step 8) are already configured
- **Sub-agents** — Symphony multi-agent orchestration (Step 9) already implements the maker-checker split
- **State files** — `STATE.md`, `MEMORY.md`, daily `memory/` files (Step 10) are already in place
- **Hard stops** — token budgets (Step 12) are already configured in model tiering
- **Comprehension debt** — the wiki-tools project (ontology explorer, cross-ref) directly addresses this risk (Step 14)

**High-leverage gaps identified:**
1. ^[inferred] The 4-condition test (Step 2) should be applied to all 42 existing cron jobs to prune non-earning loops
2. ^[inferred] Comprehension debt audits (Step 14) could be automated via the wiki-tools cross-ref command
3. ^[inferred] Goal-based loops (à la `/goal`) are missing — now built via the `goal-loop` skill
