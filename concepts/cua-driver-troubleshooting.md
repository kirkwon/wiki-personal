---
date: 2026-08-02
type: concept
title: Cua Driver Troubleshooting
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- cua-driver
- troubleshooting
- computer-use
- session-error
- software-development
sources:
- hermes://skill/cua-driver-troubleshooting
description: Fix cua-driver session errors in Hermes computer_use.
---

# Cua Driver Troubleshooting

> Fix cua-driver session errors in Hermes computer_use.

## Overview

- **Symptom** — The `computer_use` tool returns an error like:
- **Cause** — The cua-driver session ended unexpectedly (e.g., daemon restart, crash, or explicit end_session). The Hermes tool's error detection did not recognize this as a recoverable session closure, so the error was returned to the user instead of triggering an automatic retry.
- **Fix** — The Hermes `computer_use` tool already includes logic to recover from closed sessions. Update the `_is_closed_session_error` method in `~/.hermes/hermes-agent/tools/computer_use/cua_backend.py` to also treat error messages indicating an ended session as recoverable:

## Further detail

### Verification

To verify the fix, you can simulate a session end (e.g., by restarting the cua-driver daemon) and observe that subsequent `computer_use` calls succeed after a brief retry.

### Related

- `computer_use` skill - hermes computer-use doctor

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/cua-driver-troubleshooting/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
