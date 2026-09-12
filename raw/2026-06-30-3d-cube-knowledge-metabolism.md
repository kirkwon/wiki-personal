---
type: source
source: telegram-conversation
date: 2026-06-30
tags:
  - 3d-cube
  - knowledge-metabolism
  - self-improving-loops
  - agentic-memory
created: 2026-06-30
updated: 2026-06-30
---

# 3D Cube: Knowledge Metabolism Pattern

Synthesized from the conversation about Femke Plantinga's tweet, Codez's tweet, and the Slite guide on self-maintaining knowledge bases.

## The Three Dimensions

| Dimension | Axis | What It Controls |
|---|---|---|
| Stage | Ingest → Detect Drift → Propose Fix → Human Approve → Ship + Re-Verify | Phase of the loop |
| Domain | Internal (wiki/gbrain) ↔ External (news/search/code) | Source of truth |
| Cadence | 5m ⋯ hourly ⋯ daily ⋯ weekly ⋯ monthly ⋯ quarterly | Freshness tolerance |

Any box in that 3D cube maps to a concrete tool or cron job. The leverage is spotting gaps as empty cells.

## Source Tweets

### Femke Plantinga
https://x.com/femke_plantinga/status/2071909327808483360

"The traditional corporate wiki is officially dead. Teams are shifting to agentic (self-updating) knowledge bases."

The Self-Improving Knowledge Loop:
1. Auto-Ingest — Pulling fresh updates from Slack, Jira, and GitHub
2. Detect Drift — Finding exactly where documentation and reality split
3. Propose Fix — AI drafts the change, but never auto-publishes
4. Human Approves — The team retains absolute control over the source of truth
5. Ship + Re-Verify — The cycle resets automatically on a scheduled cadence

Links to: https://slite.com/learn/self-maintaining-knowledge-base-guide

### Codez
https://x.com/0xcodez/status/2071996078568701978

"Ex-Google engineer explains how to build memory for self-improving AI agents in 12 minutes."

Memory types:
- Procedural (how to act / skills)
- Semantic (durable facts / profile)
- Episodic (dated events / chat history)

Formula: Memory + loops + harness + evals = self-improving agent system

## Slite Guide Summary

"A self-maintaining knowledge base uses an AI agent to write, update, restructure, and archive docs, closing the gap between what's documented and what's actually true."

Key insight: "One stale doc no longer mis-trains one human. It mis-trains every downstream bot, and unlike a human, the bot won't know to ask in Slack."

Distinctions: self-healing ≠ self-learning ≠ self-maintaining. Self-maintaining does operational upkeep with human approval at the write step.

## Mapping to Existing Setup

### Internal (wiki/gbrain) Pipeline
| Stage | Tools |
|---|---|
| Auto-Ingest | ingest-paper, ingest-repo, gbrain sync, LLm-wiki delta sync (every 180m) |
| Detect Drift | comprehension-debt-report.py, stale-page-watchdog.sh (65 stale pages), memory-demotion.py (14-day check) |
| Propose Fix | GBrain dream cycle, cron-based maintenance (nightly dreams, weekly defrag) |
| Human Approves | Telegram-delivered reports (SPCX, market-close, cron watchdog) |
| Ship + Re-Verify | Cron cascade: 180m → daily → weekly → monthly → quarterly |

### External (news/search) Pipeline
| Stage | Tools |
|---|---|
| Auto-Ingest | last30days skill (HN, GitHub, Reddit, RSS), cron-scheduled fetch |
| Detect Drift | Last-run timestamps, deduplication, new-vs-seen tracking |
| Propose Fix | Curated brief output, Telegram delivery |
| Human Approves | User reading/skipping delivered briefs |
| Ship + Re-Verify | Every-N-hour cron cadence |

### Memory Architecture
| Memory Type | Implementation |
|---|---|
| Procedural (skills) | Skills in ~/.hermes/skills/, queue-router dispatch rules |
| Semantic (facts) | Wiki-personal + GBrain (5000+ pages), AGENTS.md, MEMORY.md |
| Episodic (events) | Daily notes in memory/, session history DB, cron logs |

## Gaps Identified
1. Drift detection from live sources (Slack, Jira) — weak
2. Explicit human-approval gate before auto-publishing changes — missing
3. External domain + drift detection — broken (FireCrawl credits dead, no replacement bound yet)
4. Evals/metrics — comprehension-debt-report tracks gaps but no improvement/decay metrics

## Connected Concepts
- knowledge-metabolism-loop
- agentic-memory-types
- self-maintaining-knowledge-base
- last30days
- GraphMind (AST-level code knowledge graph)
