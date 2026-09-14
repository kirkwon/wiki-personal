---
type: concept
title: Awesome Autoresearch Workflow Automation
ingested_via: put_page
ingested_at: '2026-07-26T15:01:04.582Z'
source_kind: put_page
created: 2026-07-26
---
# Workflow Automation

Use this category for examples where autoresearch is embedded in an operational workflow that reduces manual research and hands results to downstream actions.

## Submission format

```md
- [Name](URL) - Industry: one-sentence description of the autoresearch use case.
```

## Entries

- [PM document optimizer](https://github.com/lifang-mban/pm-document-optimizer) - Product workflow automation: applies a Karpathy-style git ratchet to markdown artifacts like PRDs and strategy docs, scoring each draft with programmatic checks and committing only higher-scoring revisions.
- [Trip Optimizer Pro](https://github.com/michaelpersonal/trip-optimizer) - Travel planning workflow automation: applies the autoresearch pattern to itinerary generation by researching destinations, scoring multi-day plans, and keeping only itinerary mutations that improve a weighted travel-quality score.
- [Autoresearch for Software Development](https://github.com/smallnest/autoresearch) - Software delivery automation: adapts autoresearch to GitHub Issues by rotating agents through implement → review → fix loops, then auto-merging only issues that clear a score gate plus build, lint, and test checks.
- [autobrowse](https://skills.sh/browserbase/skills/autobrowse) - Browser workflow automation: applies an autoresearch loop to browser tasks by iterating on `strategy.md`, replaying tasks with Browserbase, and graduating only reliable workflows into reusable Claude Code skills.
