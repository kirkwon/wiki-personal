---
type: concept
title: Blog Loop Automation
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - uncategorized
---

# blog-loop-automation

Generate blog posts from completed work using a critic/doer feedback loop.

## Usage

# Blog Loop Automation

Automatically turn completed tasks, project notes, and lessons learned into blog posts using a closed-loop critic/doer system. The workflow separates execution (doer) from validation (critic), captures failures for triage, evolves skills from successful runs, and monitors outcomes for continuous improvement.

## When to Use

- You want a hands‑off way to turn daily work into publishable content.
- You have a growing set of completed tasks, project logs, or experiment notes that deserve sharing.
- You want to improve the quality and consistency of generated posts via automated critique and revision.
- You are comfortable setting up cron jobs and delegating tasks to subagents.

## Prerequisites

- Hermes Agent with cron, delegate_task, terminal, read_file, write_file, and memory tools available.
- Access to your workspace’s `ACTIVITY.md`, daily `memory/YYYY-MM-DD.md` files, and any project `INDEX.md` or notes.
- A place to store generated blog posts (e.g., the `10.Blog` folder in your workspace or a connected GitHub repo).
- Optional: access to a publishing platform (e.g., a CMS or static site generator) if you want automatic posting.

## How to Run

The canonical way to run the blog loop is via a cron job that invokes the loop’s goal‑primitive script. Example:

```bash
hermes cronjob create \
  --schedule "0 9 * * *" \
  --name "blog-loop" \
  --prompt "Run the blog generation loop: ./scripts/blog-loop-goal.sh" \
  --workdir "/Users/kirkwon/clawd" \
  --notify_on_complete true
```

The script `scripts/blog-loop-goal.sh` (see **Procedure**) implements the goal primitive with success conditions, iteration limits, and calls the internal loop steps.

You can also run the loop manually for testing:

```bash
./scripts/blog-loop-goal.sh
```

## Quick Reference

- `hermes cronjob list` – view scheduled loops
- `hermes cronjob run <job_id>` – trigger a loop run immediately
- `hermes delegate_task --goal "<goal>"` – run a one‑off delegation
- `./scripts/blog-loop-goal.sh` – execute the loop manually
- `./scripts/critic.sh` – validate a draft blog post
- `./scripts/triage-write.py` – log failures for later review
- `./scripts/skill-patch-detect.py` – detect skill improvements from successful runs

## Procedure

**1. Ensure the blog folder exists**

In your workspace root (`/Users/kirkwon/clawd` by default), verify or create the blog folder:

```bash
mkdir -p "10.Blog"
```

The skill’s scripts will write finished posts here.

**2. Install the critic script (Layer 2 – Critic/Doer separation)**

Create `scripts/critic.sh` (relative to the skill directory; if you are using the installed skill, this file already exists):

```bash
#!/usr/bin/env bash
# critic.sh – validate a blog draft
# Input: $1 = path to draft markdown file
# Output: JSON feedback to stdout, exit code 0 = pass, non‑zero = fail

DRAFT="$1"
if [[ ! -f "$DRAFT" ]]; then
  echo '{"pass":false,"reason":"Draft file not found"}'
  exit 1
fi

# Basic checks: has title, reasonabl

...(truncated)