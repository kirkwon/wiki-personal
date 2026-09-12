---
type: project
title: GBrain Knowledge Ecosystem
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P1
ingested_via: put_page
ingested_at: '2026-09-12T13:15:49.628Z'
source_kind: put_page
---

# GBrain Knowledge Ecosystem

## Summary
Self-maintaining personal knowledge graph: ~19,800 pages, 8 ingestion pipelines, cron-driven sync across GBrain + NotebookLM + Obsidian wiki.

## Why
Compound knowledge system that captures, connects, and surfaces insights across research, sessions, and media — without manual curation.

## Progress

- [x] Core GBrain repo (`~/gbrain/`, 146K+ pages, Postgres, text-embedding-3-large)
- [x] Brain vault (`~/brain/`, git repo, symlinks to wiki-personal)
- [x] LLM knowledge base (`~/llm-wiki/`)
- [x] 8 ingestion pipelines (YouTube, sessions, email, papers, etc.)
- [x] NotebookLM integration (42 notebooks, 5 domain notebooks auto-updated)
- [x] Daily dream cycle + weekly health checks + backup verification
- [x] GBrain live sync + update check + daily backup
- [ ] GAP 1: Wiki sync consistency (path/flat link mismatches)
- [ ] GAP 4: Frontmatter normalization across sources
- [ ] GAP 5: Timeline investigation (partially addressed)
- [ ] GAP 7: 658 simple stubs + 3,034 internal stale links remain from defrag

## Next Steps
1. Fix remaining 658 broken link stubs from vault defrag
2. Normalize frontmatter across ingestion sources
3. Wire Apple Notes ingestion (new pipeline)
4. Monthly GBrain review (first run Jul 1)

## Blockers / Needs Input
- 3,034 internal stale links — need batch stub generation or redirect strategy
- Firecrawl credits exhausted — affects web ingestion pipeline

## Key Files / Resources
- `~/gbrain/` — core repo
- `~/brain/` — brain vault
- `~/wiki-personal/` — personal Obsidian wiki
- `~/llm-wiki/` — LLM knowledge base
- `~/brain/knowledge-ingestion-processing-architecture.md` — canonical architecture doc (441 lines)

## Automation / Cron
- `fa590abde977` — GBrain Live Sync (daily 3am)
- `3052a259f7e7` — GBrain Daily Update Check (daily 9am)
- `a5c62be1b347` — GBrain Daily Backup (daily 3am)
- `3d85b5b4bf38` — GBrain Weekly Health Check + Dashboard (Mon 6am)
- `c9054275b156` — LLM-wiki → GBrain delta sync (every 3h)
- `0e080c0f1b3f` — GBrain Nightly Dream (daily 2am)
- `d7de66e67f27` — Weekly maintenance: wiki-personal (Mon 2am)
- `f640c3684f87` — Weekly maintenance: wiki (Tue 2am)
- `e5cfaee6ac8b` — Monthly review (1st of month 4am)
- `e024e1b39470` — Quarterly cleanup (1st of quarter 5am)
- `015f05583a89` — Backup integrity verify (daily 3:05am)
- `35e2b00fe269` — Weekly vault defrag (Mon 9am)
- `e8d96cd0db89` — Weekly questions scan (weekly)
- `2a4765d0d53e` — Token usage log (daily 2am)
- `a97b4f7c29db` — Update AI/ML Notebook (daily 6am)
- `5f0018c30a38` — Update Decision Science Notebook (daily 7am)
- `c3303354e3ec` — Update Financial Strategy Notebook (Mon 7am) ⚠️ ERROR
- `a29a9d6f234c` — Update Cooking Science Notebook (Wed 7am)
- `dfc174665ec4` — Update Jazz Theory Notebook (Wed 7am)

## Notes
- Financial Strategy Notebook cron has error status — needs investigation
- This is the highest-cron-density project (19 jobs)
