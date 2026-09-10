---
date: 2026-07-19
type: concept
title: Deterministic First Cron
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Cron
- Automation
- Shell-First
- No-Agent
- Architecture
- devops
sources:
- hermes://skill/deterministic-first-cron
description: Deterministic cron layer first, LLM summarization second.
---

# Deterministic First Cron

> Deterministic cron layer first, LLM summarization second.

## Overview

- **When to Use** — - Building any new recurring cron job that fetches data and reports it - A cron job keeps failing on auth, `execute_code` blocks, or provider errors - You need a job that works even when the LLM provider is down - Rewiring an LLM-agent cron that does mostly mechanical data fetching - Adding monitoring/watchdog jobs (they must never depend on an LLM to detect failure)
- **Prerequisites** — - `gws` CLI installed (`/opt/homebrew/bin/gws` on macOS) — for Google Workspace data - `jq` — for JSON parsing in shell - `curl` — for HTTP APIs (weather, financial data) - Bash 4+ (macOS default is fine for `set -euo pipefail`) - The `terminal` tool for running scripts via `cronjob`
- **How to Run** — 1. Write a bash script to `~/.hermes/scripts/<job-name>.sh`. 2. Make it executable: invoke `chmod +x` through the `terminal` tool. 3. Create a cron job with `no_agent=true` and `script="<job-name>.sh"` via the `cronjob` tool (action=`create`). 4. The script's stdout is delivered to the configured channel (e.g., Telegram). Empty stdout = silent.

## Further detail

### Pitfalls

- **Wrapper auth override**: The most insidious bug. A Python wrapper sets `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` to a stale token file, shadowing the keyring. Symptom: `gws auth status` says valid, but API calls through the wrapper fail. Fix: call `gws` directly without the env var. Full debugging trail in `references/gws-auth-quirks.md`. - **Auth status lies — pair with a live smoke test**: `gws auth status` can report `token_valid: true` while actual API calls fail (token cache corruption, machine migration). Always pair any auth-status check with a real API call (e.g., `gws gmail users me

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/deterministic-first-cron/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
