---
type: concept
title: Graph Engineering
created: '2026-07-21T00:00:00.000Z'
related:
  - ai-agents
  - autoresearch
  - graphwork
updated: '2026-07-29T07:02:00.000Z'
ingested_via: put_page
ingested_at: '2026-07-29T07:02:18.626Z'
source_kind: put_page
tags:
  - agent-architecture
  - dag
  - finite-games
  - graph-engineering
  - graph-theory
  - loop-engineering
  - multi-agent
  - systems-thinking
  - work-models
source: brain/ (retired 2026-09-13)
---

# Graph Engineering

The progression from agent loops to agent graphs. The thesis: **a loop externalizes revision, a chain externalizes task order, a network externalizes role specialization, a graph externalizes shared state and relationships.**

## Progression (Ng/Anthropic synthesis)

```
Loop → Chain → Network → Graph
```

Each stage externalizes one dimension of cognition. Each is justified by a specific failure in the prior stage, not by architectural preference.

## Our System (GraphWork)
- **graph_runner.py**: topological DAG executor with action callables, decision routing, anchor gates, fan-out, persistence
- **autoresearch.graph.md**: propose→research→eval→ratchet→commit/revert (tested live with real web_search)
- **Ground truth anchors**: gates that cant be faked
- **gbrain**: persistent knowledge layer (cross-session, cross-agent shared memory)

## Sources
- **@mikenevermiss tweet** (Jul 2026): Anthropic playbook, simple-graph-agents repo
- **@KanikaBK article** (Jul 2026): Andrew Ng 12-page synthesis, loop→chain→network→graph
- **Ng DeepLearning.AI course** (Jul 2026): Agentic Knowledge Graphs with Neo4j + Google ADK
- **Anthropic** (Dec 2024 + 2026): Building Effective Agents, 5 workflow patterns

## The 3 Graph Roles
1. Shared memory (replaces transcript bottleneck)
2. Grounding layer (evaluator checks against typed edges with provenance)
3. Persistent world model (survives context flushes)

## Decision Rule (our heuristic)
> Add the next pattern when the current one fails measurably. A loop with a state file is already partway to a graph. A graph nobody queries is an overengineered loop.
