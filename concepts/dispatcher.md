---
date: 2026-07-19
type: concept
title: Dispatcher
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- autonomous-ai-agents
sources:
- hermes://skill/dispatcher
description: Zeroeth-level meta-skill that routes ambiguous user requests to the right
  master skill — or multiple masters in parallel.
---

# Dispatcher

> Zeroeth-level meta-skill that routes ambiguous user requests to the right master skill — or multiple masters in parallel.

## Overview

- **Parallel Dispatch Pattern** — When dispatching to multiple masters, use `delegate_task` for parallelism:
- **Failure Handling** — | Symptom | Action | |---|---| | Master not found | Fall back to direct sub-skill dispatch | | All masters return empty | Try web search directly | | One master fails, others succeed | Return partial results with error note | | Ambiguous routing | Ask one clarifying question — max one question per ambiguous request | | Subagent stuck on Firecrawl retries | Subagents need explicit fallback instructions: "Firecrawl credits are exhausted. Use curl against public APIs (HN Algolia, GitHub, Reddit JSON) or crawl4ai. Do NOT retry Firecrawl — it will waste time." Seed this in every delegate_task conte
- **Notes** — - This is the **default entry point** for any user request that isn't explicitly addressed to a specific master. - The dispatcher doesn't contain sub-skill logic — it routes to masters, which route to sub-skills. - For simple, well-scoped requests ("check my email"), route directly to the sub-skill via its master. - For complex, multi-domain requests ("research SpaceX and analyze the stock"), parallel dispatch. - When in doubt, prefer parallel dispatch over sequential — the user gets a more complete picture.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/dispatcher/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
