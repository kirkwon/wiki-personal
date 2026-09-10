---
date: 2026-07-19
type: concept
title: Cron Job Triage Repair
created: 2026-07-19
updated: 2026-09-09
tags:
  - devops
  - cron
sources:
  - hermes://skill/cron-job-triage-repair
---

# Cron Job Triage Repair

Diagnose and fix cron job failures from logs and config.

## Triage order

1. **Read the failure** — `cron_incidents` in `~/.hermes/cron/executions.db` (state,
   failure_type, error_sig, output_file) plus the run output in `~/.hermes/cron/output/<job_id>/`.
2. **Classify** — transient (self-healing) vs actionable (needs a fix). See [[cron-failure-signatures]].
3. **Environment diff** — cron runs with a minimal PATH and no shell profile; the number-one
   cause of cron failures is environment mismatch (PATH, env vars, working directory).
4. **Check dependencies** — every binary the script calls must resolve in cron's PATH.
5. **Fix, verify, generalize** — reproduce under a clean environment
   (`env -i HOME=$HOME PATH=/usr/bin:/bin`), then audit sibling scripts for the same pattern.

## Related

- [[cron-audit]]
- [[cron-failure-signatures]]
- [[silent-cron-failures]]
