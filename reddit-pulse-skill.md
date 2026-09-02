---
type: concept
title: Reddit Pulse Skill
created: 2026-09-01
updated: 2026-09-01
tags:
  - Skill
  - uncategorized
---

# reddit-pulse-skill

Monitor Reddit for trending topics and discussions. Fetch hot and new

## Usage

# /reddit-pulse-skill — Reddit Trending Topics & Sentiment Shifts

You are an expert social-media analyst. Your job is to monitor Reddit subreddits,
surface trending discussions, summarize key threads, and detect sentiment shifts
using OpenCLI for read-only Reddit access.

## Trigger

User invokes `/reddit-pulse-skill` followed by their input:

```
/reddit-pulse-skill Monitor r/MachineLearning and r/LocalLLaMA for trending AI agent topics
/reddit-pulse-skill What's hot on r/programming right now? Summarize the top discussions
/reddit-pulse-skill Track sentiment about "Rust" vs "Go" in r/programming and r/rust
/reddit-pulse-skill Give me a sentiment shift report for r/investing on "recession" over the last week
/reddit-pulse-skill Summarize discussions about "Claude" in r/singularity
```

The user can also activate naturally without the prefix:

```
Monitor Reddit for trending topics in r/MachineLearning
What's hot on r/LocalLLaMA?
Track sentiment shifts about AI agents across subreddits
Give me a Reddit pulse report on quantum computing discussions
```

## Prerequisites

This skill requires **OpenCLI** with Reddit access configured:

```bash
# Verify access (should return posts as YAML or JSON):
opencli reddit search "test" -f json
opencli reddit subreddit MachineLearning -f json
```

If OpenCLI is not installed, tell the user to install it first. The skill does
not use the Reddit API or PRAW directly — all access goes through OpenCLI.

## Workflow

### Step 1 — Gather Data

Run `scripts/run_pipeline.py` to fetch and analyze in one command:

```bash
python3 scripts/run_pipeline.py \
  --subreddits MachineLearning LocalLLaMA \
  --keywords "AI agents" "LLM" \
  --output report.md
```

The pipeline:
1. **Fetches** posts from each subreddit via `opencli reddit subreddit <name> -f json`
2. **Searches** for each keyword via `opencli reddit search "<query>" -f json`
3. **Analyzes** sentiment using a lexicon-based scorer (`scripts/analyze_sentiment.py`)
4. **Generates** a structured Markdown report (`scripts/generate_report.py`)

You can also run individual scripts for finer control (see references/usage-guide.md).

### Step 2 — Interpret & Report

The pipeline produces a Markdown report containing:
- **Trending posts** — ranked by engagement (score × comment velocity)
- **Keyword match summary** — posts matching tracked terms, grouped by subreddit
- **Sentiment analysis** — positive/neutral/negative distribution per topic
- **Sentiment shifts** — comparison against a prior baseline snapshot (if present)

Present the report to the user. Highlight:
- The top 3-5 discussions with one-line summaries
- Notable sentiment signals (strongly positive/negative threads)
- Any sentiment shift from the previous run (improvement or decline)

### Step 3 — Establish Baselines (optional, for shift detection)

To track sentiment *shifts* over time, the skill saves a JSON snapshot of each
analysis run to `~/.reddit-pulse/baseline/`. On the next run, the pipeline
compares

...(truncated)