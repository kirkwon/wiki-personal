---
date: 2026-07-19
type: concept
title: Jupyter Live Kernel
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- jupyter
- notebook
- repl
- data-science
- exploration
- iterative
sources:
- hermes://skill/jupyter-live-kernel
description: Iterative Python via live Jupyter kernel (hamelnb).
---

# Jupyter Live Kernel

> Iterative Python via live Jupyter kernel (hamelnb).

## Overview

- **When to Use This vs Other Tools** — | Tool | Use When | |------|----------| | **This skill** | Iterative exploration, state across steps, data science, ML, "let me try this and check" | | `execute_code` | One-shot scripts needing hermes tool access (web_search, file ops). Stateless. | | `terminal` | Shell commands, builds, installs, git, process management |
- **Prerequisites** — 1. **uv** must be installed (check: `which uv`) 2. **JupyterLab** must be installed: `uv tool install jupyterlab` 3. A Jupyter server must be running (see Setup below)
- **Setup** — The hamelnb script location:

## Further detail

### Core Workflow

All commands return structured JSON. Always use `--compact` to save tokens.

### Practical Tips from Experience

1. **First execution after server start may timeout** — the kernel needs a moment to initialize. If you get a timeout, just retry.

### Timeout Defaults

The script has a 30-second default timeout per execution. For long-running operations, pass `--timeout 120`. Use generous timeouts (60+) for initial setup or heavy computation.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/data-science/jupyter-live-kernel/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
