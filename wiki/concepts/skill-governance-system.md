---
type: note
title: Skill Governance System — Meta-Masters, Scoring & Archive
author: Kirk Won
date: 2026-07-01
status: draft
tags: [skill-governance, meta-skills, scoring, archival, consolidation]
created: 2026-07-01
source: brain/ (retired 2026-09-13)
---
# Skill Governance System

A curation system that evolves your skill library by evaluation, not extermination. Skills are scored, consolidated, and archived — never deleted.

## The Philosophy

- **All skills are valuable**, but not equally valuable *right now*
- Deleting loses knowledge; archiving preserves it with a timestamp
- Meta-masters coordinate sub-skills and can absorb their content
- Consolidation is the default; deletion is never the answer

## Architecture

### 1. Category Design (5 meta-masters)

| Meta-Master | Sub-Skills Include | Phase |
|---|---|---|
| **knowledge-master** | research/*, arxiv, blogwatcher, analyze-paper, extract-wisdom, youtube-video-ingestion, permanent-questions, gbrain-* | discover + assimilate |
| **finance-master** | portfolio-dashboard, options-market-analysis, causal-modeling, mean-variance-analyzer, optionality-valuer, game-theoretic-finance-analysis, equity-research/* | analyze + model |
| **productivity-master** | gmail, inbox-triage, inbox, session-logging, ocr-and-documents, nano-pdf, unify-document-formats, conversation-logging, apple ecosystem | operate |
| **creativity-master** | mermaid-diagrams, excalidraw, cli-anything-*, architecture-diagram, design-md, improve-writing, creative-ideation, multi-perspective-essay | generate |
| **learning-master** | spaced-repetition, knowledge-metabolism, defrag, notebooklm-*, memory-tier-system, concept-cross-linking (assimilate phase) | retain |

Note: Knowledge and Learning are two phases of the same pipeline — "discover" and "assimilate" living under one `knowledge-master`. This avoids the Research/Learning overlap by sequencing: `knowledge-master discover:arxiv "topic" → digest → knowledge-master assimilate:cross-link "concepts"`.

### 2. Meta-Master Pattern (every category)

Each meta-master has a `SKILL.md` with:

```yaml
---
name: knowledge-master
description: Discover and assimilate knowledge — research, sources, synthesis
type: meta-skill
sub_skills:
  - name: arxiv
    path: research/arxiv
    tags: [paper-discovery, academic]
    last_used: 2026-06-30
    score: 8
    consolidated_from: []
  - name: youtube-video-ingestion
    path: research/youtube-video-ingestion
    tags: [video, ingest]
    last_used: 2026-06-15
    score: 4
    consolidated_from: []
  - name: old-paper-digest
    path: null  # archived
    tags: [paper, archive]
    last_used: 2025-11-01
    score: 1
    consolidated_from: []
    archived_at: 2026-07-01
    content_absorbed_into: research/analyze-paper
---
```

And a dispatch block:

```markdown
## Dispatch

Use this meta-skill when the user asks for anything knowledge-related.

### discover phase
- "find papers on X" → `research/arxiv` or `research/blogwatcher`
- "research X company" → `research/domain-intel` or `research/web-researcher`
- "analyze this paper" → `research/analyze-paper`

### assimilate phase
- "connect concepts X and Y" → `knowledge-metabolism` or `knowledge/cross-link`
- "review last 30 days" → `research/last30days`
- "save to gbrain" → `research/gbrain-content-ops`
- "create notebookLM" → `research/gbrain-to-notebooklm`

### If archived skill is referenced
If the user mentions `old-paper-digest` (archived): "That content is now part of `analyze-paper`. Let me use that instead."
```

### 3. Scoring System

Skills scored quarterly on 3 axes (each 0-10):

| Axis | Weight | Metric |
|---|---|---|
| **Recency** | 40% | Days since last use (10 = used this week, 0 = not used in 12+ months) |
| **Frequency** | 35% | Uses in last 3 months (10 = 20+, 0 = 0) |
| **Quality** | 25% | Subjective — did it deliver? Did it work reliably? |

**Thresholds:**
- **8-10**: Core skill — actively maintained
- **4-7**: Utility skill — used occasionally, kept
- **1-3**: Dormant skill — candidate for consolidation
- **0**: Cold skill — archive immediately

### 4. Consolidation & Archive Workflow

```
score ≤ 3
    ↓
Review content — can it fold into a sibling or the master?
    ├── Yes → Absorb content into target skill (frontmatter `consolidated_from: [old-skill]`)
    │         Move old skill to .archive/{old-skill}/
    │         Add to master's `sub_skills: [{...archived_at, content_absorbed_into}]`
    └── No  → Move directly to .archive/{old-skill}/
              Update master's sub_skills list
```

**Archive path**: `~/.hermes/skills/.archive/{skill-name}/SKILL.md`
**Metadata added to archived skill**: `archived_at: 2026-07-01, last_used: 2026-01-15, archived_by: score=2`

### 5. Cron: Quarterly Score + Archive Sweep

A cron job that runs every 3 months:
1. Read each meta-master's `sub_skills` list
2. Check `last_used` dates (recency)
3. Check git log or invocation logs (frequency)
4. Recommend consolidation candidates
5. Optionally auto-archive scores ≤ 1

## Implementation Order

1. **Create 5 meta-master skills** — frontmatter + dispatch blocks first
2. **Populate sub_skills lists** — inventory each category thoroughly
3. **Scoring script** — `skill-score.py` that computes scores from hermes logs
4. **Archive workflow** — documented in `read-the-damn-docs` as "never delete, archive"
5. **Quarterly cron** — auto-sweep with review gate

## Benefits

- **No more deletions** — archive is discoverable, rescuable
- **Meta-master coordinates** — one entry point per domain, dispatch logic centralized
- **Consolidation preserves** — old content lives inside the successor skill
- **Score-based pruning** — objective, not arbitrary
- **Archived skills can be revived** — `last_used` and `archived_at` tell you when it went cold
