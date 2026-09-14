---
type: concept
title: GitHub Skill Discovery Loop (8-Agent Continuous Learning)
sources:
  - 'https://x.com/rvaniaaaa/status/2082562583131726050'
  - 'https://x.com/rvaniaaaa/status/2075975822461084061'
ingested: '2026-07-29T00:00:00.000Z'
ingested_via: put_page
ingested_at: '2026-07-30T03:06:02.375Z'
source_kind: put_page
tags:
  - agent-architecture
  - automation
  - continuous-learning
  - github-monitoring
  - skill-discovery
created: 2026-07-30
source: brain/ (retired 2026-09-13)
---
# GitHub Skill Discovery Loop — 8-Agent Continuous Learning

## Core Concept
An 8-agent autonomous pipeline that monitors GitHub trending, extracts reusable workflows, converts them into Agent Skills, and publishes them via PR for human review. The library compounds: more skills → richer context → better discoveries → stronger skills.

## Architecture — 8 Agents in a Loop

1. **Scout** — Monitors GitHub Trending + targeted searches. Query patterns: agent framework, langgraph, mcp, multi-agent. Filters: stars:>100, language:Python, archived=false, sort:updated-desc. Output: list of discovered repos.
2. **Filter** — Deterministic rules (no LLM) to remove irrelevant repos. KEEP/REJECT with reason. Cost-saving design: filter before any model touches it.
3. **Reader** — Reads repo in order: README → docs/ → examples/ → package.json → requirements.txt → source code (only if needed). Output: structured context about the project.
4. **Workflow Extractor** — Extracts reusable workflow: skill_name, goal, inputs, steps, outputs. Or REJECT if not general-purpose.
5. **Skill Score** — Objective validation: README exists, examples exist, ≥3 workflow steps, general purpose, confidence >0.85. PASS/REJECT.
6. **Skill Generator** — Converts validated workflow into SKILL.md package (description, inputs, examples, commands, tests).
7. **Reviewer** — LLM judge: "Would an experienced engineer install this Skill without editing it?" YES/NO with reasoning.
8. **Publisher** — Creates branch, commits skill package, opens PR for human review.

## Compounding Loop
More Skills → Richer Content for Analysis → Higher Quality Discoveries → Stronger Skills Added → repeat.

## Key Design Decisions
- Deterministic filtering BEFORE LLM (cost savings)
- Human-in-the-loop only at final PR review
- Confidence threshold 0.85
- Skills must be general-purpose and reusable (not domain-locked)
- Reader reads docs FIRST, code only if needed (efficiency)

## Connection to Our Stack
- **agent-skill-creator (v6.0)**: Covers agents 6-7 (generator + reviewer) — we already have the factory
- **GraphWork**: Can orchestrate the full pipeline as a DAG with embedded loops
- **Missing agents we'd need to build**:
  - Scout (GitHub trending monitor — cron-driven)
  - Filter (deterministic rule engine)
  - Reader (repo ingestion pipeline)
  - Extractor (workflow pattern miner)
  - Publisher (GitHub PR automation)
- **Build path**: GraphWork project with cron-driven Scout, delegate_task fan-out for parallel processing
