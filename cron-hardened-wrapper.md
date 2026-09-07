---
type: concept
title: Cron Hardened Wrapper
created: 2026-09-06
updated: 2026-09-06
tags:
  - Skill
  - devops
---

# cron-hardened-wrapper

Generic hardened wrapper for Hermes cron jobs.

## Usage

# Cron Hardened Wrapper

A generic, reusable wrapper script for Hermes cron jobs that addresses common failure patterns:
- Missing PATH in cron environment
- Timeout issues (both overall and per-script)
- Log bloat from uncontrolled output
- Unclear success/failure criteria
- Missing environment isolation (PYTHONPATH poisoning)

## When to Use

Use this wrapper when:
- A cron job repeatedly fails due to PATH issues
- A cron job needs timeout protection
- A cron job produces excessive output that needs rotation
- You want standardized logging across multiple cron jobs
- A job treats certain exit codes (like 1 for threshold breaches) as success
- A cron job script only sets up environment but doesn't execute actual work (common pitfall)

## Features

1. **Timeout Protection** - Configurable overall timeout with graceful handling
2. **Environment Isolation** - Explicit PATH export and optional PYTHONPATH unset
3. **Timestamped Logging** - Each run logs to a unique file with job name and timestamp
4. **Automatic Log Rotation** - Cleans logs older than configurable days
5. **Flexible Exit Code Handling** - Define success codes and codes to ignore (treat as success)
6. **Clear Status Indicators** - Visible start/completion markers in logs
7. **Non-blocking Remediation Support** - Optional secondary script that won't fail the main job

## Location

`~/.hermes/scripts/cron-hardened-wrapper.sh`

## Usage

Set these environment variables before calling the wrapper:

```bash
JOB_NAME="descriptive-job-name"  # Used for log directory and messages
SCRIPT_TO_RUN="/full/path/to/actual/script.py"  # The script to execute (USE ABSOLUTE PATH)
TIMEOUT_SECS=300  # Overall timeout in seconds (default 300/5min)
LOG_KEEP_DAYS=7  # Days to keep logs (default 7)
SUCCESS_EXIT_CODES="0"  # Comma-separated list of success codes (default "0")
IGNORE_EXIT_CODES="1"  # Comma-separated list of codes to treat as success (e.g., "1" for threshold breaches)
```

Then in your cron job's `script` field:

```bash
~/.hermes/scripts/cron-hardened-wrapper.sh
```

## Example: Knowledge-Eval Cron Job

The knowledge-eval cron job (`38e94c97bf84`) uses a specialized wrapper that incorporates these patterns:

```bash
# ~/.hermes/scripts/knowledge-eval-cron-wrapper.sh
#!/bin/bash
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
# ... (job-specific configuration)
```

## Benefits

- **Eliminates repetitive boilerplate** - No need to reimplement timeout/logging logic in each wrapper
- **Ensures consistency** - All wrapped jobs follow the same patterns for timeouts, logging, and environment
- **Reduces maintenance** - Fix the wrapper once, benefit all jobs that use it
- **Standardized verification** - Log rotation and timeout handling work predictably
- **Clear diagnostics** - Timestamped logs make it easy to trace specific runs

## Customization Points

While the wrapper provides sensible defaults, you can customize:

1. **Timeout values** - Adjust TIMEOUT_SECS per job based on expected run

...(truncated)