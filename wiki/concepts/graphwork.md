---
type: concept
title: GraphWork
created: '2026-07-21T00:00:00.000Z'
updated: '2026-07-21T00:00:00.000Z'
ingested_via: put_page
ingested_at: '2026-07-21T23:52:07.128Z'
source_kind: put_page
tags:
  - dag
  - declarative
  - loop-engineering
  - toolchain
  - work-models
source: brain/ (retired 2026-09-13)
---

# GraphWork

GraphWork is the declarative toolchain that implements [[graph-engineering]]. It provides a markdown-native format (GRAPH.md) for modeling work as directed graphs with embedded loops, plus a parser, validator, scaffold generator, and Mermaid visualizer.

## Philosophy

Born from the insight that projects are DAGs (they end) and habits are loops (they don't), and that the two have been treated separately when they should be unified. GraphWork makes the finite/infinite distinction explicit in a single declarative file.

**One-line model:** *Run finite DAGs to deliver, run infinite loops to grow, spend a Gittins-indexed slice exploring.*

## Components

### graph_scaffold.py (Unified Scaffolder)
Creates new projects with full GraphWork structure:
- `GRAPH.md` — DAG topology with embedded loops
- `AGENTS.md` — Linear run book with enforced protocols
- `INDEX.md` — OKF-compliant navigation map
- `ACTIVITY.md` — Append-only activity log
- `decisions/` — Decision status board + append-only log
- `loops.md` + `review.md` — Outer loop declarations + double-loop review log
- `01.Core/`, `02.Research/incoming+refined/`, `03.Scripts/`, `logs/`, `audit/`, `tests/`, `memory/`, `Archive/`

Usage:
```bash
python3 ~/clawd/32.GraphEngineeredWork/scripts/graph_scaffold.py "Project Name" \
  --just-cause "Why this exists" \
  --description "Brief summary" \
  --graph-type hybrid    # finite | infinite | hybrid
```

### graph_parser.py (Parser + Validator)
- Cycle detection in `depends_on` edges (DAG must be acyclic)
- 8 validation rules: dangling refs, missing exit_criteria, missing ground_truth, unresolved decisions
- Critical path computation (longest dependency chain)
- Mermaid diagram generation (shape-by-type, status colors)
- JSON output for programmatic use

### Enforced Protocols
Every GraphWork project has mandatory protocols:
- **Decision logging**: Context → Options → Decision → Rationale → Tradeoffs
- **Activity logging**: One line per meaningful work session
- **Task completion checklist**: Exit criteria met, ground truth verified, decision logged, activity updated
- **Independent verification**: Milestone completion requires verification from a separate code path

## Option A vs Option B

- **Option A** (current): Declarative only. Validates structure, computes critical path, renders diagrams. Doesn't execute tasks.
- **Option B** (planned): Executable engine. Reads graph, tracks state, executes nodes in dependency order, runs loops on cadence, verifies anchors against ground truth automatically.

## Projects Built with GraphWork

7 projects scaffolded as of Jul 2026:
- 30.Research-Pipeline — Deep research harness (16-step pipeline)
- 34.PortfolioRebalance — Portfolio rebalancing system
- 35.GbrainKnowledgeMaintenance — GBrain maintenance automation
- 36.ClawdWorkspaceReorg — Workspace reorganization
- 37.ArchitectureSafe — LikeC4 architecture validation
- 38.ArchitectureWorkspace — Architecture-as-code workspace
- 39.ArchitectureAutogen — AST-based .c4 generation

## Related

- [[graph-engineering]] — The conceptual framework GraphWork implements
- [[loop-engineering]] — Predecessor paradigm (individual loop design)
- [[wave-execution-pattern]] — DAG math for parallel execution
- [[structured-execution]] — GO/HOLD/SKIP decision gates

## Source Files
- Spec: `~/clawd/32.GraphEngineeredWork/GRAPH_SPEC.md`
- Scripts: `~/clawd/32.GraphEngineeredWork/scripts/`
- Skill: `graph-engineered-work`
