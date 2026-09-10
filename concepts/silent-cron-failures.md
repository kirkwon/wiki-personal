---
date: 2026-09-09
type: concept
title: Silent Cron Failures
created: 2026-09-09
updated: 2026-09-09
tags:
  - devops
  - cron
  - rca
sources:
  - hermes://session/2026-09-09
---

# Silent Cron Failures

A cron job can **exit 0 and still be broken**. When a script renders a plausible-looking
output from bad data, the exit-code gate passes, the job reports `ok`, and the watchdog stays
silent — the failure is invisible.

## Case

`market-close-summary` (2026-09-07/09): the data provider returned NaN for every ticker, so
the script printed a table of `$nan` / `nan%` for all 8 positions and still exited 0. The job
showed `last_status: ok` while delivering garbage. Secondary issue: the run was a `catch_up`
fired at 18:03 instead of 13:05 (machine asleep, lateness ~17,864s), so the summary was ~5h stale.

## Rule

**Validate output, not just exit code.** When a script's whole purpose is to transform fetched
data, add a sanity check: if no valid data is returned, write a clear error to stderr and exit
non-zero so the failure surfaces.

- Reject non-finite values (NaN/inf) at the fetch boundary; surface them as "no data" rather than formatting them.
- Fail hard when *all* inputs fail; warn (but continue) on partial failure.
- Never let a derived metric (best/worst, counts) be computed over non-finite values.

## Related

- [[cron-failure-signatures]]
- [[cron-audit]]
- [[cron-job-triage-repair]]
- [[structured-run-traces-for-rca]]
