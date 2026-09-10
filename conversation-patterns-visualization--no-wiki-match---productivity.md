---
date: 2026-07-13
type: concept
title: Conversation Patterns Visualization
created: 2026-07-13
updated: '2026-09-09'
tags:
- skill
- Skill
sources:
- hermes://skill/conversation-patterns-visualization
description: Generate HTML dashboards visualizing conversation logging patterns, tag
  frequencies, mental model usage, and anti-patterns over time. Integrates with weekly_review.py
  for automated post-review visualization.
---

# Conversation Patterns Visualization

> Generate HTML dashboards visualizing conversation logging patterns, tag frequencies, mental model usage, and anti-patterns over time. Integrates with weekly_review.py for automated post-review visualization.

## Overview

- **Overview** — Generates interactive HTML dashboards from compressed conversation logs, surfacing patterns invisible in individual conversations.
- **Tools** — - `python3` scripts at `~/.hermes/scripts/conversation_patterns_visualizer.py` - `~/.hermes/scripts/weekly_review.py` (with `--dashboard` flag) - Chart.js for visualizations (CDN-loaded)
- **Dashboard Contents** — | Section | Description | |---------|-------------| | Stats Overview | Total conversations, decisions, anti-patterns, unique tags | | Tag Frequency | Horizontal bar chart of most-used tags | | Mental Model Usage | Doughnut chart of cognitive frameworks applied | | Anti-Patterns Detected | Ranked list with occurrence counts | | Activity Timeline | Line chart of decisions & anti-patterns over time | | Conversation Timeline | Individual cards with date, stats, tags |

## Further detail

### Data Requirements

Dashboard parses compressed logs from `~/.hermes/conversation-logs/compressed/`.

### Decisions Made

- Decision 1 - Decision 2

### Mental Models

1. **Inversion** - description

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/conversation-patterns-visualization/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
