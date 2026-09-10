---
type: project
title: Blog & Content Pipeline
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P2
ingested_via: put_page
ingested_at: '2026-09-10T13:00:19.801Z'
source_kind: put_page
---

# Blog & Content Pipeline

## Summary
Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.

## Why
Convert accumulated knowledge architecture, research, and "I built this" experiences into publishable thought leadership. Kirk puts final spin; agent produces raw material and structure.

## Progress

- [x] Blog directory created (`~/brain/blog/`)
- [x] README index with 14 candidates, series clusters, conventions
- [x] Draft 1: Self-Organizing Agent Architecture (status: draft, 11.9K chars)
- [x] Draft 2: Spam Invoice Escalation (status: raw-material, 7.5K chars)
- [x] Full inventory scan: 14 candidates verified on disk (3 agents cross-validated)
- [x] Series clusters defined: Autonomous Systems, Quant/Finance, AI Research
- [ ] Promote Tier 1 candidates to active drafting
- [ ] Publish Draft 1 (self-organizing agents)

## Next Steps
1. Pick 1-2 Tier 1 candidates to promote to draft status
2. Move `blog-self-organizing-agent-architecture.md` from root into `blog/`
3. Ship Draft 1

## Blockers / Needs Input
- Which candidates to prioritize? Top ready-to-ship: LLM Novelty series, Loop Engineering, Anthropic Margin Cascade, SpaceX SOTP

## Key Files / Resources
- `~/brain/blog/README.md` — full backlog index
- `~/brain/blog/blog-spam-invoice-escalation.md` — draft
- `~/brain/blog-self-organizing-agent-architecture.md` — draft (root, needs move)

### Tier 1 sources (ready to ship)
- `~/brain/knowledge-ingestion-processing-architecture.md` (441 lines)
- `~/brain/llm-novelty-literature-review.md` (175 lines)
- `~/brain/anthropic-gross-margin-cascade-model.md` (105 lines)
- `~/brain/spacex-spcx-deep-dive-scenarios.md` (177 lines)
- `~/brain/mega-ipo-index-impact-2026.md` (187 lines)

## Automation / Cron
- None currently. Could add a weekly "stale draft" reminder.

## Notes
- Blog format follows frontmatter: type=blog-draft, status=raw-material→draft→published, author=Kirk Won
- English only (user does not understand Chinese)
