---
type: note
title: Gateway Debugging
source: hermes-memory
recency: '2026-07-15T00:00:00.000Z'
frequency: low
offloaded: '2026-08-03T00:00:00.000Z'
importance: medium
truthfulness: verified
ingested_via: put_page
ingested_at: '2026-08-03T22:28:12.638Z'
source_kind: put_page
created: 2026-08-03
---
# Gateway Crash Debugging

- Error: "Sorry, I encountered an unexpected error" = Python crash in gateway/run.py
- Logs: ~/.hermes/logs/errors.log + gateway.error.log
- Source: ~/.hermes/hermes-agent/gateway/run.py (patchable)
- Restart: user runs `hermes gateway restart` from separate Terminal (can't restart from session)
