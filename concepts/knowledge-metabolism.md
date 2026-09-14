---
type: concept
title: Knowledge Metabolism
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Knowledge Metabolism
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/knowledge-metabolism
description: '3D Cube Knowledge Metabolism — models the knowledge base as a 3-dimensional

  cube (Loop Stage × Domain × Cadence) where each cell maps to a concrete tool

  or cron job. Finds gaps (empty cells), suggests pipelines, runs health checks,

  and links to the eval system. Covers all 3 memory types (procedural, semantic,

  episodic). Also includes cron consolidation and execution-health patterns.'
---

# Knowledge Metabolism

> 3D Cube Knowledge Metabolism — models the knowledge base as a 3-dimensional
cube (Loop Stage × Domain × Cadence) where each cell maps to a concrete tool
or cron job. Finds gaps (empty cells), suggests pipelines, runs health checks,
and links to the eval system. Covers all 3 memory types (procedural, semantic,
episodic). Also includes cron consolidation and execution-health patterns.

## Overview

- **Overview** — The Knowledge Metabolism pattern models your knowledge infrastructure as a **3-dimensional cube** where every cell maps to a concrete tool, script, or cron job. The leverage is **spotting gaps as empty cells**.
- **Suggested Workflow (Quickstart)** — Combine the 4 commands in sequence for a complete metabolism cycle:
- **Gap-Finding Mode Detail** — Run `check-gaps` to trigger this logic:

## Further detail

### Anti-Patterns

- **Empty cube cells you ignore.** Every empty cell is a potential failure mode. The 3D cube model is only useful if you regularly audit it. - **Running pipelines without drift detection.** Ingest without drift detection means you're accumulating stale data faster than fresh data. - **Auto-publishing without human approval.** "One stale doc mis-trains every downstream bot, and unlike a human, the bot won't know to ask in Slack." - **Confusing self-maintaining with self-healing.** Self-maintaining does operational upkeep with human approval. Self-healing patches automatically. These are distinc

### Source Documents

- `~/wiki-personal/raw/2026-06-30-3d-cube-knowledge-metabolism.md` — Raw ingestion - `~/wiki-personal/concepts/self-maintaining-knowledge-base.md` — Synthesized concept - `references/source-materials.md` (in this skill) — Condensed reference for all source materials - `references/concept-synthesis-workflow.md` (in this skill) — Concept dedup + tiering workflow from gbrain skillpack - [Femke Plantinga tweet](https://x.com/femke_plantinga/status/2071909327808483360) — Self-improving knowledge loop - [Codez tweet](https://x.com/0xcodez/status/2071996078568701978) — Agent memory types - [Slite gui

### Related Skills

- `premortem` — For stress-testing knowledge pipeline changes - `last30days` — External domain ingest pipeline - `wiki-lint` — Wiki quality audit - `knowledge-health` — The eval system (`knowledge-eval.py`) that powers the `link-eval` command - `memory-tier-system` — Memory tier management (hot/warm/cool/cold), referenced by `memory-demotion.py` - `wiki-raw-ingest` — Contains the `ingest-paper` and `ingest-repo` CLI tools for the Internal ingest pipeline - `wiki-ingest` — Full-distillation ingest pipeline for multi-document content - `gbrain-health-dashboard` — GBrain health monitoring dashboa

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-metabolism/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
