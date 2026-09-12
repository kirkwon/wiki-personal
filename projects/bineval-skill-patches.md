---
type: project
title: BINEVAL Binary Evaluation Patches (6 Skills)
status: completed
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P2
ingested_via: put_page
ingested_at: '2026-09-11T13:00:38.472Z'
source_kind: put_page
---

# BINEVAL Binary Evaluation Patches

## Summary
Applied BINEVAL (binary question decomposition) methodology to 6 evaluation/critique skills. Created shared reference file. Each skill now decomposes its evaluation into yes/no questions that produce structured, discriminative assessments.

## Progress
- [x] Shared BINEVAL method reference created (reusable across skills)
- [x] `meta-critic` — BINEVAL reward decomposition patched
- [x] `critical-review` — binary question templates per dimension patched
- [x] `grill-me` — binary grilling mode patched
- [x] `impl-validator` — binary check decomposition patched
- [x] `autoresearch` — BINEVAL eval layer patched
- [x] `judgment-equation` — binary trust questions patched

## Key Files
- `~/.hermes/skills/software-development/meta-critic/SKILL.md`
- `~/.hermes/skills/software-development/critical-review/SKILL.md`
- `~/.hermes/skills/software-development/grill-me/SKILL.md`
- `~/.hermes/skills/software-development/impl-validator/SKILL.md`
- `~/.hermes/skills/research/autoresearch/SKILL.md`
- `~/.hermes/skills/strategy/judgment-equation/SKILL.md`

## Notes
- Source paper: BINEVAL — Interpretable LLM Evaluation via Binary Decomposition
- Shared reference file location: in skill directory (binary-decomposition method spec)
- Patched in prior session (Jun 27), verified via search_files
