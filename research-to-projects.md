---
type: concept
title: Research To Projects
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - research
---

# research-to-projects

Papers to GraphWork projects with nodes and metrics.

## Usage

# Research Papers → GraphWork Projects

> *Research stays "nice ideas" until it has a GRAPH.md with nodes, exit criteria, and ground truth anchors.*

## When to Use

- You have read research papers and want to extract actionable system improvement ideas
- You need to translate paper methodology into project scaffolding (GRAPH.md with nodes, loops, metrics)
- You want to prioritize improvements by impact and effort

## Quick Start

```bash
# 1. Analyze papers (5 min per paper)
# Extract: Problem, Methodology, Current Systems, Impact, Implementation

# 2. Triage ideas (2 min)
# HIGH: Measurable impact + reasonable effort (2-6 weeks)
# MEDIUM: Strategic benefit + moderate effort (3-5 weeks)
# LOW: Skip (incremental or unclear ROI)

# 3. Scaffold projects (10 min per project)
python3 ~/clawd/32.GraphEngineeredWork/scripts/graph_scaffold.py \
  "Project Name" \
  --just-cause "Why this matters" \
  --description "Brief summary" \
  --graph-type hybrid

# 4. Customize GRAPH.md with:
# - Nodes (5-9 sequential tasks with exit criteria)
# - Success metrics (baseline → target)
# - Loops (daily/weekly rhythms)
# - Anchors (ground truth verification)
```

## Workflow

### Step 1: Paper Analysis Framework (10 min)

For each paper, extract:

| Dimension | Questions | Output |
|-----------|-----------|--------|
| **Problem** | What does the paper solve? Current state vs target? | Gap identification |
| **Methodology** | Core approach? 2-3 key techniques? | Actionable techniques |
| **Current Systems** | Which systems could benefit? | Target system list |
| **Expected Impact** | Metrics improve? By how much? | Quantified benefits |
| **Implementation** | Concrete in your stack? Code/pipeline/integration? | Implementation sketch |

**Example (Frontis-MA1):**
```
Problem: Recursive self-improvement requires AI that builds AI
Methodology: 4 atomic operators (Draft → Improve → Debug → Crossover)
Current Systems: Self-harness (V1), Dojo eval, Hermes skills
Expected Impact: 50% → 70% success rate (+20% improvement)
Implementation: SelfHarnessV2 class with operator methods, search loop, Dojo integration
```

### Step 2: Extract 5W+ Framework (5 min)

For each actionable idea, document:

| Component | What to Specify |
|-----------|-----------------|
| **WHO** | Target system |
| **WHAT** | Change/integration |
| **WHEN** | Timing/dependencies |
| **WHERE** | Component/module |
| **WHY** | Benefit/metrics |
| **HOW** | Implementation approach |

**Example (Beacon):**
```
WHO: Hermes tool selection system
WHAT: Adaptive tool policy with necessity-aware rewards
WHEN: After collecting 10K tool invocations
WHERE: tool_usage_tracker.py, necessity_policy.py, adaptive_router.py
WHY: Reduce tool calls by 30-50%, lower token costs 20-30%
HOW: Collect data → calculate effect → train policy → implement router
```

### Step 3: Priority Triaging (2 min)

Classify ideas by impact and effort:

| Priority | Criteria | Signal |
|----------|----------|--------|
| **HIGH** | Measurable im

...(truncated)