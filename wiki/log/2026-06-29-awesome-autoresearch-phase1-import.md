---
type: log
tags: [autoresearch, import, phase1, process]
---

# Phase 1 Complete: awesome-autoresearch Import

**Date:** 2026-06-29
**Repo:** https://github.com/yibie/awesome-autoresearch
**Commit:** latest main (cloned fresh)
**Elapsed:** ~30 min

## What was created

### Wiki source
- `sources/awesome-autoresearch.md` — full repo overview with structure, inclusion criteria, build pipeline, key patterns

### Wiki concepts
- `concepts/autoresearch-pattern.md` — core loop (propose→implement→run→evaluate→decide→repeat), 9 documented variants, key properties that distinguish it from generic agents
- `concepts/karpathy-autoresearch-loop.md` — three-file architecture (prepare.py/train.py/eval.py), why it works (bounded experiments, empirical gate, emergent serendipity, git discipline)

### GBrain pages (19 total)
All imported with tag `autoresearch`:

| Slug | Type | Size |
|------|------|------|
| awesome-autoresearch-competitive-intelligence | concept | 1 chunk |
| awesome-autoresearch-content-research | concept | 1 chunk |
| awesome-autoresearch-customer-discovery | concept | 1 chunk |
| awesome-autoresearch-evaluation-red-teaming | concept | 2 chunks |
| awesome-autoresearch-finance-trading | concept | 3 chunks |
| awesome-autoresearch-infra-skills-forks | concept | 10 chunks |
| awesome-autoresearch-knowledge-base-rag-preparation | concept | 1 chunk |
| awesome-autoresearch-lead-generation | concept | 1 chunk |
| awesome-autoresearch-market-research | concept | 1 chunk |
| awesome-autoresearch-personal-knowledge-humanities | concept | 1 chunk |
| awesome-autoresearch-related-practices-discussions | concept | 14 chunks |
| awesome-autoresearch-scientific-research | concept | 6 chunks |
| awesome-autoresearch-software-systems-optimization | concept | 5 chunks |
| awesome-autoresearch-trend-monitoring | concept | 1 chunk |
| awesome-autoresearch-workflow-automation | concept | 1 chunk |
| awesome-autoresearch-curation-skill | concept | 4 chunks |
| awesome-autoresearch-source | source | 1 chunk |
| autoresearch-pattern | concept | 1 chunk |
| karpathy-autoresearch-loop | concept | 1 chunk |

### Cron job
- **Name:** awesome-autoresearch-weekly-sync
- **Schedule:** Sunday 8:00 AM
- **Script:** `~/.hermes/scripts/sync-awesome-autoresearch.sh`
- **Mode:** no_agent — pulls latest from upstream, re-imports only if changed
- **First run:** 2026-07-05

### Hermes skill
- **Name:** autoresearch-curation
- **Category:** research
- **Purpose:** periodic evidence sweeps, promotion workflow, entry addition

## What was learned
1. **GBrain import works well** with raw markdown — the `put` command accepts content via stdin and auto-chunks pages larger than the threshold
2. **The related-practices-discussions page** (50KB, 146 entries) triggered gbrain's content-sanity warning — future imports of very large pages should consider splitting
3. The repo's curation skill is well-structured and integrates cleanly with Hermes — no adaption needed beyond importing the SKILL.md verbatim
4. The repo uses `--tag autoresearch` as its primary tagging convention — consistent tagging makes GBrain search easy

## Metrics
- 684 total entries across 14 category files + 5 open (seeding) categories
- 19 GBrain pages created
- 1 cron job deployed
- 1 Hermes skill registered
- ~50 GBrain chunks consumed across all pages
