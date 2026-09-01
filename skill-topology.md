---
type: concept
title: Skill Topology
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - meta-learning
---

# skill-topology

Analyze skill-library structure via semantic similarity — find duplicates, subsets/supersets, parallel siblings, and sequential pipeline candidates across ~/.hermes/skills. Use when reducing skill footprint, merging overlapping skills, organizing masters/categories, or before creating new skills that might duplicate existing ones.

## Usage

# Skill Topology

Meta-skill for mapping the skill library's semantic structure and reducing its
footprint. Treats the library as a graph of configurations:

- **duplicates** (cos ≥ 0.90) — near-identical purpose → merge into one
- **subset/superset** (token containment + sim ≥ 0.70) — fold narrow into broad
- **siblings** (0.70–0.90) — run PARALLEL: same phase, adjacent domains → keep both, group under one master category
- **pipeline candidates** (0.55–0.70) — possible SEQUENCE: A's output feeds B → flag for LLM review, never auto-decide

## How to Run

```bash
# Full analysis (~15s, local Ollama embeddings, $0)
python3 ~/clawd/01.Skillutilityscoring/03.Scripts/skill_topology.py
```

**Outputs** (`01.Skillutilityscoring/02.Research/refined/`):
- `skill-topology.json` — relations, clusters, footprint-reduction estimate
- `skill-topology.md` — mermaid diagram of top clusters

## Interpretation Rules

1. **Merge only duplicates with ≥0.93 sim AND human eyeball of both descriptions** — v2 evaluators vs v1 are legitimate keeps if behavior differs
2. **Subset folds require reading both SKILL.md bodies** — token containment is a heuristic, body content wins over metadata
3. **Sibling groups inform master-category organization** — this replaces manual master classification with semantic grouping
4. **Pipeline pairs are hypotheses only** — sequence detection needs LLM review of trigger semantics (does B say "after A" / "once X exists"?)
5. **Usage/discoverability stays OUT of merge decisions** — usage ≠ utility (D002); a heavily-used duplicate is still a duplicate

## Known Limits (validated 2026-08-24)

- Naive graph clustering at cos ≥ 0.62 degenerates into 2 mega-hairballs — use pairwise relations, not components
- nomic baseline similarity inflates pair counts (19k "pipeline?" candidates = noise floor); raise to ≥0.60 for review batches
- Deterministic pass finds high-confidence merges only; the real consolidation work is LLM/human review of flagged pairs in utility order

## Integration

- Feeds P3 dataset curation (merged skills = cleaner training data)
- Master categories should follow sibling-group boundaries, not manual labels
- Re-run after any bulk skill addition/removal; diff relation sets between runs