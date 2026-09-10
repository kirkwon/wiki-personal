---
date: 2026-07-19
type: concept
title: Decision Logger
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- core
sources:
- hermes://skill/decision-logger
description: Log decisions to a JSONL file for audit and reflection.
---

# Decision Logger

> Log decisions to a JSONL file for audit and reflection.

## Overview

- **When to Use** — - You need to record important decisions made during agent workflows - You want to maintain a decision history for session continuity - You want to review past decisions to improve future workflows - You need to integrate decision logging with Hermes' memory system
- **Prerequisites** — - None
- **How to Run** — Invoke through the `skill_manage` tool to access the skill's scripts, then use the `terminal` tool to run the decision logging script.

## Further detail

### Quick Reference

- `scripts/log_decision.py`: Log a decision to .maestro/decisions.jsonl - `scripts/get_recent_decisions.py`: Retrieve recent decisions from the log

### Procedure

1. **Ensure the decision log directory exists** - If working in a project with Maestro context, ensure `.maestro/` directory exists - If not, the script will create it

### Pitfalls

- **File permissions**: Ensure the script has write access to the .maestro directory - **Log rotation**: The log file will grow indefinitely; consider implementing rotation for long-running projects - **JSONL format**: Each line is a valid JSON object; do not corrupt the file with non-JSON lines

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/core/decision-logger/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
