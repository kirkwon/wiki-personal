---
type: note
title: Research Pipeline Architecture
source: hermes-memory
recency: '2026-08-03T00:00:00.000Z'
frequency: daily
offloaded: '2026-08-03T00:00:00.000Z'
importance: high
truthfulness: verified
ingested_via: put_page
ingested_at: '2026-08-03T22:28:11.852Z'
source_kind: put_page
created: 2026-08-03
---
# Research Pipeline Architecture

## arXiv Scanner
- Schedule: Mon 9AM

## HF Papers Pipeline (daily)
- Schedule: 9:30AM, job 62926a7402db
- Loop: score Q01-Q07 → fetch .md → gbrain → Q-file evidence → NLM
- Scripts: hf-papers-pipeline.py, hf-papers-daily.sh
- API: huggingface.co/api/daily_papers?date=

## Q→NLM Mapping
- Q01-Q04 → aiml-analysis
- Q05 → financial-strategy
- Q06 → loop-eng
- Q07 → wealth-synthesis

## NLM→GBrain Export
- Job: bdc0a7bb8025, daily 10AM, no_agent=True
