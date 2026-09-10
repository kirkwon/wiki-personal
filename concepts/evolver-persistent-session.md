---
date: 2026-07-19
type: concept
title: Evolver Persistent Session
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- evolver
- session
- latency
- testing
- performance
- auto-renew
- autonomous-ai-agents
sources:
- hermes://skill/evolver-persistent-session
description: Manage a persistent Hermes agent session with auto-renewal for low-latency
  evolver/testing workloads. Reduces initialization overhead and periodically refreshes
  to avoid context bloat.
---

# Evolver Persistent Session

> Manage a persistent Hermes agent session with auto-renewal for low-latency evolver/testing workloads. Reduces initialization overhead and periodically refreshes to avoid context bloat.

## Overview

- **Why Auto-Renew?** — Long-running sessions accumulate conversation history, which can slow down calls and increase memory usage. Auto-renewal gives you: - **Fast calls** after initial session warmup - **Fresh context** every N calls to prevent degradation - **Automatic cleanup** of old sessions
- **Installation** — This adds `evolver_session_id` and `evolver_query` functions to your shell.
- **Auto-Renew Logic** — 1. **Call increment**: Each `evolver_query` increments a counter 2. **Threshold check**: When counter ≥ `EVOLVER_RENEW_AFTER`: - Archive current session ID - Create new session - Reset counter 3. **State persistence**: Call count and session ID stored in `.evolver_state/`

## Further detail

### Performance Comparison

| Method | First Call | Subsequent Calls | Memory Use | |--------|------------|------------------|------------| | Fresh `chat -q` each time | 10-30s | 10-30s (variable) | Low | | Persistent session (no renew) | 10-30s | 2-5s | Grows over time | | **Persistent + auto-renew** | 10-30s | 2-5s | Bounded |

### Verification

Expected: First call ~10-15s, subsequent calls ~2-5s.

### FAQ

**Q: Why not just use `--ignore-rules` on every fresh call?** A: Faster, but you lose agent identity (SOUL.md/USER.md). Persistent sessions give you both speed and context.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/evolver-persistent-session/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
