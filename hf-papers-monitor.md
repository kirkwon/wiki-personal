---
type: concept
title: Hf Papers Monitor
created: 2026-09-01
updated: 2026-09-01
tags:
  - Skill
  - research
---

# hf-papers-monitor

>

## Usage

# HF Papers Monitor — Daily Trending Paper Discovery

Scans Hugging Face's trending papers API, scores relevance against your 7 permanent research questions (Q01-Q07), and delivers a Telegram-ready brief.

## Why This Exists

- **arXiv scanner** (existing): keyword search across arXiv — broad but noisy
- **HF Papers Monitor** (this): curated trending papers with community upvotes — signal-rich, narrower scope
- Together: broad coverage + community-filtered quality

## Quick Commands

```bash
# Today's trending papers (text brief)
python3 ~/.hermes/scripts/hf-papers-monitor.py

# Include non-matching papers too
python3 ~/.hermes/scripts/hf-papers-monitor.py --all

# Last 7 days
python3 ~/.hermes/scripts/hf-papers-monitor.py --days 7

# JSON output (for pipeline integration)
python3 ~/.hermes/scripts/hf-papers-monitor.py --json

# Fetch a specific paper's markdown (for ingestion)
python3 ~/.hermes/scripts/hf-papers-monitor.py --fetch-md 2501.10120
```

## How It Works

```
HF API (huggingface.co/api/daily_papers)
    │
    ▼  50 trending papers (JSON: title, abstract, upvotes, arxiv_id)
┌──────────────────────────────────┐
│  Keyword Scorer                  │
│  • Q01-Q07 keyword match         │
│  • General interest keywords     │
│  • Deduplication (seen.json)     │
└──────────────────────────────────┘
    │
    ▼  Scored + ranked papers
┌──────────────────────────────────┐
│  Brief Formatter                 │
│  🎯 Q-file matches (top 10)      │
│  💡 Interesting (top 5)           │
│  📋 Other trending (top 5)       │
└──────────────────────────────────┘
    │
    ▼  Telegram-ready text
```

## Q-File Mapping

The monitor maps papers to your permanent research questions:

| Q-ID | Topic | Sample Keywords |
|------|-------|-----------------|
| Q01 | AI/ML × Finance bridge | finance, trading, portfolio, quant, option |
| Q02 | Agent self-improvement | self-play, constitutional ai, auto-curriculum |
| Q03 | Accelerating learning | transfer, meta-learning, RLHF, DPO, GRPO |
| Q04 | Symbolic/energy-based | energy-based, bayesian, probabilistic, variational |
| Q05 | AI + Finance predictive | forecasting, time series, regime, factor model |
| Q06 | Agent recursive improvement | SWE agent, tool use, MCP, autonomous agent |
| Q07 | Post-60/40 portfolio | allocation, rebalancing, hedging, real estate |

## The .md Trick (Zero-Cost Paper Ingestion)

Hugging Face serves markdown versions of every paper page. Just append `.md`:

```bash
# Get clean markdown of any paper
curl -sL "https://huggingface.co/papers/2501.10120.md"
```

This is cheaper than agent-browser + markitdown for HF papers specifically. Use the full pipeline only for non-HF sources.

## Ingestion Pipeline

```bash
# 1. Discover relevant papers
python3 ~/.hermes/scripts/hf-papers-monitor.py --json > /tmp/hf_today.json

# 2. Fetch markdown of a high-relevance paper
python3 ~/.hermes/scripts/hf-papers-monitor.py --fetch-md 2607.26115 > /tmp/paper.md

# 3. Ingest into gbrain
gbrain add /tmp/paper

...(truncated)