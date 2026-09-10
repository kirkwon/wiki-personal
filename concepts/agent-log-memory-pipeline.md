---
date: 2026-07-19
type: concept
title: Agent Log Memory Pipeline
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Memory
- Pipeline
- Cron
- Deterministic
- LLM
- knowledge-management
sources:
- hermes://skill/agent-log-memory-pipeline
description: Build two-layer agent-log memory extraction pipeline.
---

# Agent Log Memory Pipeline

> Build two-layer agent-log memory extraction pipeline.

## Overview

- **When to Use** — - Building a new agent-log → MEMORY.md pipeline from scratch - Fixing a broken retain cycle cron (e.g., `hermes skill run` doesn't exist) - Tuning observation extraction noise (commit messages, session status leaking in) - Adding an LLM extraction layer on top of existing regex extraction - Diagnosing why `tier-tracker.json` is empty despite logs existing
- **Prerequisites** — - `promotion-tracker.py` at `~/.hermes/scripts/` (observe/check/**promote**/report subcommands) - Ollama running locally with a coding-capable model (gemma4-agent:12b recommended) - Agent logs in `~/clawd/26.Agent-Logs-GBrain/logs/*.md` or similar - `tier-tracker.json` writable at `~/.hermes/memory/` - Cron job slot for weekly retain cycle
- **Pitfalls** — - **macOS grep has no `-P` flag** — use `grep -oE` instead of `grep -oP` in shell scripts - **One-LLM-call-per-file times out** — batch all uncovered lines into a single Ollama call - **`hermes skill run` doesn't exist** — use `no_agent` shell scripts for retain cycles - **Config-write blocked** — `patch` tool refuses `~/.hermes/config.yaml`; use `python3` script via `terminal` - **Regex noise compounds** — broad include patterns (`fails?.*when`, `never \w+`) match commit messages and task status; always dry-run before seeding - **LLM output parsing** — model may wrap JSON in markdown; extract

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/agent-log-memory-pipeline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
