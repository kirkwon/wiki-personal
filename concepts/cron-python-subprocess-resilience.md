---
date: 2026-08-02
type: concept
title: Cron Python Subprocess Resilience
created: 2026-08-02
updated: 2026-09-09
tags:
  - devops
  - cron
  - python
sources:
  - hermes://skill/cron-python-subprocess-resilience
---

# Cron Python Subprocess Resilience

Cron Python scripts that call `subprocess.run(..., timeout=N)` raise `TimeoutExpired` when
the timeout fires. Uncaught, this kills the script with a raw traceback — the job reports
failure even when the timeout was expected behaviour in a degraded environment.

## Rule

Always wrap a timeout-bearing `subprocess.run` in an explicit `except subprocess.TimeoutExpired`
handler that converts the timeout into a **controlled, classified outcome** (retry, defer, or a
clear failure message) instead of a traceback.

```python
try:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
except subprocess.TimeoutExpired:
    print("TIMEOUT_UPSTREAM - deferred", file=sys.stderr)
    sys.exit(0)   # transient: defer; use non-zero for a genuine failure
```

## Related

- [[cron-failure-signatures]] — timeouts are one signature class
- [[self-heal-cron-job]]
