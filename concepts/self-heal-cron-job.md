---
type: concept
title: Self-Heal Cron Job
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Self-Heal Cron Job

Workflow for turning an existing cron job into a self-healing one: instrument the target
script with structured JSON logs, run an outer-loop monitor that detects repeated failures,
diagnose the root cause, apply a fix (retry/backoff, config patch), validate, and record the
lesson. It does **not** modify the scheduler — it works on the script and environment the job
references.

## Loop shape

- **Inner loop** — the target script writes JSON-line events to `~/.hermes/logs/<script>.jsonl`
  at each major step (step name, status, error, context).
- **Outer loop** — monitor script (`~/.hermes/scripts/outer_loop_<script>.py`) detects repeated
  failures, diagnoses, patches, and validates.
- **Backups** — `~/.hermes/loop_backups/<script>/` before any patch.
- **Lesson capture** — write the fix + rationale to a knowledge page.

## Procedure

1. Identify the failing job (`hermes cron list`; inspect `~/.hermes/cron/output/<job_id>/`).
2. Instrument the script with structured JSON logging.
3. Deploy the outer-loop monitor on a schedule.
4. Fix, validate in a clean environment, record the lesson.

## Related

- [[cron-audit]] — decide whether the job is worth healing at all
- [[cron-python-subprocess-resilience]] — a common failure this loop fixes
- [[cron-job-triage-repair]]

[[cron-failure-signatures]]
