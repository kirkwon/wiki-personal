---
date: 2026-07-19
type: concept
title: Python Debugpy
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- debugging
- python
- pdb
- debugpy
- breakpoints
- dap
- post-mortem
- software-development
sources:
- hermes://skill/python-debugpy
description: 'Debug Python: pdb REPL + debugpy remote (DAP).'
---

# Python Debugpy

> Debug Python: pdb REPL + debugpy remote (DAP).

## Overview

- **Overview** — Three tools, picked by situation:
- **When to Use** — - A test fails and the traceback doesn't reveal why a value is wrong - You need to step through a function and watch a collection mutate - A long-running process (hermes gateway, tui_gateway) misbehaves and you can't restart it - Post-mortem: an exception fired in prod-ish code and you want to inspect locals at the crash site - A subprocess / child (Python `_SlashWorker`, PTY bridge worker) is the actual bug site
- **pdb Quick Reference** — Inside any pdb prompt (`(Pdb)`):

## Further detail

### Recipe 1: Local breakpoint

Easiest. Edit the file:

### Recipe 3: Debug a pytest test

The hermes test runner and pytest both support this:

### Recipe 4: Post-mortem on any exception

Or wrap a whole script:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/python-debugpy/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
