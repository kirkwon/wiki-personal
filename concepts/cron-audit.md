---
date: 2026-07-19
type: concept
title: Cron Audit
created: 2026-07-19
updated: 2026-09-09
tags:
  - devops
  - cron
  - loop-engineering
sources:
  - hermes://skill/cron-audit
---

# Cron Audit

Methodology for deciding whether a cron job justifies its ongoing cost, derived from the
Loop Engineering paper (@0xCodez, 2026-06-09). Run periodically on any cron farm.

## The 4-Condition Test

A loop earns its cost **only if all four hold**:

1. **Task repeats** — weekly or more often (monthly jobs never amortize setup cost).
2. **Verification automated** — a gate rejects bad output (test, linter, build; for `no_agent` scripts the exit code counts).
3. **Token budget absorbs waste** — retries/exploration fit the budget. `no_agent` scripts cost near-zero; LLM jobs burn tokens every run.
4. **Senior-engineer tools** — logs, repro environment, ability to run its own output.

> Miss one condition and the loop costs more than it returns.

## Verdicts

- Keep — all 4 met
- Review — 1-2 questionable (repairable?)
- Pause — superseded by another job
- Prune — 0-1 met, no repair path
- Fix to Goal — meets 1/3/4 but has a natural stopping point; convert to a goal-loop

## Related

- [[cron-failure-signatures]] — classify failures before deciding to keep a job
- [[silent-cron-failures]] — a job can pass the exit-code gate while emitting garbage
- [[self-heal-cron-job]] — repair loop for jobs worth keeping
