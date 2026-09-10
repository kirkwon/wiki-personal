---
date: 2026-07-19
type: concept
title: Token Optimization
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- token-optimization
- cost-savings
- compression
- caching
- headroom
- context-optimization
- mlops
sources:
- hermes://skill/token-optimization
description: Reduce token usage for AI agent conversations. Covers Headroom proxy/MCP
  integration, content deduplication, compression strategies, and provider-level caching.
  Applicable when agent costs are high or context windows are filling too fast.
---

# Token Optimization

> Reduce token usage for AI agent conversations. Covers Headroom proxy/MCP integration, content deduplication, compression strategies, and provider-level caching. Applicable when agent costs are high or context windows are filling too fast.

## Overview

- **Headroom Integration (Primary Tool)** — > **Note:** The operational `headroom` skill contains the actual MCP tool usage, proxy management, and troubleshooting steps. This section covers the strategy and architecture; the `headroom` skill covers the daily operations.
- **When to Use Each Mode** — | Situation | Mode | Why | |-----------|------|-----| | Tool outputs dominate your context | Proxy (Mode B) | Transparent compression of all tool returns | | You want to test before committing | MCP (Mode A) | Explicit calls, easy to verify savings | | Both tool outputs AND conversation are large | Both (Mode C) | Proxy handles tool output, MCP handles explicit retrieval | | Cost is your primary concern | Both + KV caching | Stack all three for maximum reduction |
- **Related Skills** — - `headroom` — Operational: MCP tool usage, proxy management, launchd service, troubleshooting - `self-harness` — Agent improvement loop (complementary: improve the agent AND compress its traffic) - `hermes-cli-latency` — Latency optimization for Hermes CLI calls

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/token-optimization/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
