---
date: 2026-07-19
type: concept
title: Defrag
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- obsidian
- maintenance
- knowledge-graph
- weekly
- cron-job
- knowledge
sources:
- hermes://skill/defrag
description: 'Weekly Obsidian vault maintenance: fix broken links, consolidate duplicates,
  update stale frontmatter, generate health report. Keeps your knowledge graph healthy.'
---

# Defrag

> Weekly Obsidian vault maintenance: fix broken links, consolidate duplicates, update stale frontmatter, generate health report. Keeps your knowledge graph healthy.

## Overview

- **When to Use This Skill** — Use this skill when: - Running as a scheduled task (cron job, weekly, Monday 9 AM) - Vault feels cluttered or slow to search - You suspect broken links or duplicate notes - After a period of heavy note creation - Maintaining the Agent-Logs-GBrain corpus (specialized use case)
- **How to Run** — This skill is designed to be run via its associated script or through cron jobs. Direct invocation with `hermes skill run` is not supported for this skill.
- **Safety Policy** — - Never delete content - Rollback before any changes - Confirm for: duplicate merges, large splits, bulk >50 files - Dry-run mode available

## Further detail

### GBrain Multi-Source Considerations

When running defrag on GBrain vaults with multiple sources, health metrics vary by source:

### Getting Health Data (GBrain, Vault, etc.)

**When `gbrain health` hangs via terminal:** do NOT retry via terminal or delegate_task — these time out. Instead, read the cron job's most recent output file directly.

### Success Metrics (GBrain vault, as of 2026-08-30)

Current state: - Pages: 7,749 (vault-wide, all sources) - Orphan pages: 5,749 (Trend: ↓159 week-over-week; 74% of vault — normal for large vaults with intentional unlinked content; skill baseline says 1,000+ is expected) - Health score: varies by source; see `gbrain doctor --fast --json` for live numbers

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/defrag/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
