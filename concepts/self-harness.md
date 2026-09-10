---
date: 2026-07-19
type: concept
title: Self Harness
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/self-harness
---

# Self Harness

## Overview

- **When to Use** — - **After agent tasks complete**: Collect trajectories from tool-use sessions - **Improving agent behavior**: Use preference models to rank trajectories - **Crash recovery**: Recover trajectories and memory from interrupted sessions - **Debugging**: Inspect exact tool calls and results
- **Testing** — All 6 tests cover: 1. Trajectory serialization (exact format) 2. Trajectory deserialization (round-trip) 3. Memory operations (JSON persistence) 4. Crash recovery (incomplete JSON handling) 5. Memory corruption recovery 6. Trajectory append mode
- **Next Iteration** — The current implementation (first iteration) provides: - Basic trajectory collection - Memory persistence - Crash recovery

## Further detail

### Related Files

- `~/.hermes/scripts/self_harness_first_iteration/main.py` - Core implementation - `~/.hermes/scripts/self_harness_first_iteration/tests/test_file_level.py` - Test suite

### Exit Codes

- `main.py`: 0 (success) - `pytest`: 0 (all tests pass), 1 (tests failed)

### Limitations

- No preference model yet (first iteration only) - No automatic trajectory ranking - Manual trigger required for collection - No integration with agent sessions (manual import only)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/self-harness/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
