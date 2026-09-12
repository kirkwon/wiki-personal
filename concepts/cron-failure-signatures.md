------

# Cron Failure Signatures

Classify a cron failure by its **signature** (a machine-readable token the wrapper emits)
before deciding to retry, alert, or skip. Exit code alone is not enough: the same non-zero
exit can mean "transient, will self-heal" or "broken, needs a human".

## Why

Retry logic that ignores the failure *reason* wastes its budget on conditions it cannot fix.
Real case (2026-09-07, `agent-logs-gbrain-sync`): the wrapper retried 3x90s (~4.5 min) into a
gbrain PGLite **auto-repair cooldown of 10 minutes** — a window it could never outlast — and was
SIGTERM'd at ~182s. Result: a false "newly failing" alert plus an open incident, while the next
scheduled tick self-healed.

## Pattern

Emit a signature as the wrapper's final stdout line, then classify:

| Signature | Class | Action |
|-----------|-------|--------|
| TRANSIENT_PGLITE_REPAIR_COOLDOWN | transient | log SKIPPED, exit 0, defer to next tick |
| SCRIPT_NOT_FOUND | actionable | exit 1, alert |
| TIMEOUT_UPSTREAM | transient | defer / retry with backoff |

- **transient** — do not create a backlog card; the next run self-heals.
- **actionable** — create a card, alert, assign.

Match on both the token and the descriptive phrase so pre-fix incidents classify too
(`auto-repair stays off for 10 minutes` maps to `TRANSIENT_PGLITE_REPAIR_COOLDOWN`).

## Design rule

**The retry window must exceed the expected transient duration, or the retry is theatre.**
If the condition needs 10 minutes to clear and your backoff totals 4.5, prefer *defer to the
next scheduled tick* over in-run retries.

## Related

- [[silent-cron-failures]]
- [[cron-job-triage-repair]]
- [[cron-audit]]
- [[structured-run-traces-for-rca]]

[[self-heal-cron-job]]
