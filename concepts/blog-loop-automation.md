---
type: concept
title: Blog Loop Automation
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Blog Loop Automation

> Generate blog posts from completed work using a critic/doer feedback loop.

## Overview

- **When to Use** — - You want a hands‑off way to turn daily work into publishable content. - You have a growing set of completed tasks, project logs, or experiment notes that deserve sharing. - You want to improve the quality and consistency of generated posts via automated critique and revision. - You are comfortable setting up cron jobs and delegating tasks to subagents.
- **Prerequisites** — - Hermes Agent with cron, delegate_task, terminal, read_file, write_file, and memory tools available. - Access to your workspace’s `ACTIVITY.md`, daily `memory/YYYY-MM-DD.md` files, and any project `INDEX.md` or notes. - A place to store generated blog posts (e.g., the `10.Blog` folder in your workspace or a connected GitHub repo). - Optional: access to a publishing platform (e.g., a CMS or static site generator) if you want automatic posting.
- **How to Run** — The canonical way to run the blog loop is via a cron job that invokes the loop’s goal‑primitive script. Example:

## Further detail

### Quick Reference

- `hermes cronjob list` – view scheduled loops - `hermes cronjob run <job_id>` – trigger a loop run immediately - `hermes delegate_task --goal "<goal>"` – run a one‑off delegation - `./scripts/blog-loop-goal.sh` – execute the loop manually - `./scripts/critic.sh` – validate a draft blog post - `./scripts/triage-write.py` – log failures for later review - `./scripts/skill-patch-detect.py` – detect skill improvements from successful runs

### Procedure

**1. Ensure the blog folder exists**

### Pitfalls

- **Critic too strict**: The default critic looks for a title, length >150 words, and no placeholders. Adjust thresholds in `critic.sh` if your drafting style differs. - **Draft quality depends on model**: The `draft-blog.sh` uses `hermes -z` (one-shot mode) to generate markdown from notes. If output is weak, consider refining the prompt in `draft-blog.sh` or providing more structured notes. - **File path assumptions**: Scripts assume the workspace is at `/Users/kirkwon/clawd`. Update `--workdir` and paths if your workspace lives elsewhere. - **Cron overlaps**: Ensure the schedule interval is

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/blog-loop-automation/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[blog-vintage-futuristic]]

[[blog-writing]]
