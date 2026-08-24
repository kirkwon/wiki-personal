---
date: 2026-06-30

type: concept
title: "Self-Maintaining Knowledge Base"
source: "Slite guide + @femke_plantinga tweet + @0xcodez tweet"
tags:
  - knowledge-management
  - agentic-loops
  - documentation
  - ai-infrastructure
created: 2026-07-26
updated: 2026-07-26
---

# Self-Maintaining Knowledge Base

## Source Threads

1. **Femke Plantinga** — [tweet](https://x.com/femke_plantinga/status/2071909327808483360): "The traditional corporate wiki is officially dead" — teams shifting to agentic, self-updating knowledge bases.
2. **Codez** — [tweet](https://x.com/0xcodez/status/2071996078568701978): "Ex-Google engineer explains how to build memory for self-improving AI agents" — breaks memory into procedural + semantic + episodic.
3. **Slite** — [guide](https://slite.com/learn/self-maintaining-knowledge-base-guide): "The self-maintaining knowledge base: what it is and why every team needs one."

## The Problem

> "One stale doc no longer mis-trains one human. It mis-trains every downstream bot, and unlike a human, the bot won't know to ask in Slack."
> — Slite guide

Stale docs used to slow humans down. Now they mis-train every AI agent that reads them. A human can tell when a doc looks off and ask in Slack. An agent can't, and will hallucinate confidently on top of an outdated SOP.

## The Self-Improving Knowledge Loop (Femke Plantinga)

| Stage | Description |
|---|---|
| **Auto-Ingest** | Pulling fresh updates from Slack, Jira, GitHub, etc. |
| **Detect Drift** | Finding exactly where documentation and reality split. |
| **Propose Fix** | AI drafts the change, but never auto-publishes. |
| **Human Approves** | Team retains absolute control over source of truth. |
| **Ship + Re-Verify** | Cycle resets automatically on a scheduled cadence. |

## The Memory Architecture (Codez tweet)

> Memory + loops + harness + evals = self-improving agent system

| Memory Type | Description | Maps To |
|---|---|---|
| **Procedural** | How to act / skills | Skills, dispatch rules |
| **Semantic** | Durable facts / profile | Wiki, concepts, MEMORY.md |
| **Episodic** | Dated events / chat history | Daily notes, session history, cron logs |

## Slite's Definition

> "A self-maintaining knowledge base uses an AI agent to write, update, restructure, and archive docs, closing the gap between what's documented and what's actually true."

The loop:
- Slite agent auto-ingests from connected sources
- Detects drift between docs and reality
- Proposes a fix (AI drafts the change)
- Human approves
- KB stays accurate over time

### Key Distinctions

Slite distinguishes **self-maintaining** from adjacent ideas:
- **Self-healing**: patches drift automatically after detection
- **Self-learning**: adapts to usage patterns
- **Self-maintaining**: does the operational upkeep work, with human approval at the write step

The critical constraint: every change needs human review, because errors don't stay local.

## The 3-Dimensional Knowledge Metabolism Pattern

Synthesizing the two tweet threads + Slite guide into a general framework:

| Dimension | Axis Values |
|---|---|
| **Loop Stage** | Ingest → Detect Drift → Propose Fix → Human Approve → Ship + Re-Verify |
| **Domain** | Internal (wiki/gbrain/docs) ↔ External (news/search/code) |
| **Cadence** | Minutes/hours → Daily → Weekly → Monthly → Quarterly |

Any box in this 3D cube maps to a concrete tool or pipeline. The leverage is spotting gaps as empty cells.

## Relevance to Hermes Setup

The existing pipeline already implements this loop across multiple domains:

| Loop Stage | Internal (wiki/gbrain) | External (news/search) |
|---|---|---|
| Auto-Ingest | ingest-paper, ingest-repo, gbrain sync | last30days (HN, GitHub, Reddit, RSS) |
| Detect Drift | comprehension-debt-report, stale-page watchdog | Last-run timestamps, dedup |
| Propose Fix | GBrain dream cycle, cron maintenance | Curated brief output |
| Human Approves | Telegram-delivered reports for review | User reading/skipping briefs |
| Ship + Re-Verify | Cron cascade (180m → daily → weekly → qtr) | Every-N-hour cron cadence |

Gap: drift detection from live sources (Slack, Jira) and explicit human-approval gate before auto-publishing changes.
