---
date: 2026-07-19
type: concept
title: Gbrain Health Dashboard
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gbrain
- health
- dashboard
- monitoring
- cron
- knowledge
sources:
- hermes://skill/gbrain-health-dashboard
description: 'GBrain weekly health monitoring pipeline: rich doctor JSON parsing,
  rolling history tracking, and auto-generated HTML dashboard with charts/trends.'
---

# Gbrain Health Dashboard

> GBrain weekly health monitoring pipeline: rich doctor JSON parsing, rolling history tracking, and auto-generated HTML dashboard with charts/trends.

## Overview

- **Components** — | Component | Path | Purpose | |-----------|------|---------| | Health check script | `~/.hermes/scripts/gbrain-health-check.sh` | Runs `gbrain doctor --json` + `gbrain stats`, parses rich JSON | | History file | `~/.hermes/data/gbrain-health-history.json` | Rolling 52-week JSON array | | Dashboard generator | `~/.hermes/scripts/generate-gbrain-dashboard.py` | Produces `gbrain-dashboard.html` with embedded data | | Dashboard HTML | `~/.hermes/data/gbrain-dashboard.html` | Self-contained, open in browser |
- **Cron Job** — **Job:** `gbrain-weekly-health` (id: `3d85b5b4bf38`) **Schedule:** Monday 6:00 AM **Script:** `gbrain-health-check.sh && python3 ~/.hermes/scripts/generate-gbrain-dashboard.py` **Mode:** no_agent (zero tokens)
- **What the Script Captures** — From `gbrain doctor --json`: - **category_scores**: brain, skill, ops, meta (each /100) - **brain_score** check message: overall score + embed/links/timeline/orphans/dead-links subscores - **top_issues**: up to 10 prioritized with fix suggestions - **issue_counts**: fail/warn counts - **counts**: pages, chunks, embedded, links, orphans (from `gbrain stats` + `gbrain orphans`)

## Further detail

### Key Fix (v0.41+ Compatibility)

`gbrain doctor --json` exits **code 1** when brain is "unhealthy" (which is normal — there are always some warnings). The old script used bash `||` fallback which **swallowed the real output** and replaced it with `{"health_score":"?"}`.

### Dashboard Features

- Dark theme (GitHub-dark inspired) - Brain score gauge + trend line over time - Category scores (bar chart + color-coded pills) - Brain breakdown radar (embed/links/timeline/orphans/dead-links) - Pages & links dual-axis trend - Top issues list with fix suggestions - Trend indicators (week-over-week changes) - Responsive layout

### Data History

- Entries are appended on each run (max 52 to keep 1 year) - Pre-upgrade entries (May 4-25, 2026): backfilled with limited data from old v0.31.x cron outputs - Post-upgrade gap (Jun 1-22): script was broken by v0.41.0 upgrade — page/link counts available, brain scores lost - Current (Jun 23+): full data including category scores + brain score breakdown

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/gbrain-health-dashboard/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
