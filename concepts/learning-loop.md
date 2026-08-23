---
date: 2026-07-15
type: concept
title: Learning Loop
created: 2026-07-15
updated: 2026-07-15
tags: [architecture, learning, self-improvement, loop-engineering]
---

# Learning Loop

## Summary

Learning Loop is a **meta-layer** within the Hermes agent architecture that formalizes the continuous improvement process, connecting execution traces to harness evolution and knowledge synthesis.

## Purpose

Learning Loop operates as a three-tier system (following Karpathy's enhanced Self-Harness) that:
- Captures execution traces from all agent activities
- Analyzes patterns for improvement opportunities
- Generates targeted harness modifications
- Validates improvements through regression testing

## The Three-Layer Loop Architecture

```
                     ┌─────────────────┐
                     │   Meta-Loop     │ ← Optimizes the improvement loop itself
                     │  (Outer Loop)   │
                     └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │  Harness Loop   │ ← Improves the operational harness
                     │ (Inner Loop)    │
                     └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │  Execution      │ ← Primary agentic workflow
                     │     Loop        │
                     │                 │ ← (AWARENESS → ANALYSIS → ... → COMMUNICATION)
                     └─────────────────┘
```

## Layer 1: Execution Loop

This is the existing Hermes Cognitive Stack (AWARENESS → ANALYSIS → EXPLORATION → INTERACTION → INTERPRETATION → LEARNING → COMMUNICATION).

**Trace Capture Points:**
- Tool call sequences and latencies
- Memory access patterns
- Skill selection decisions
- User correction events
- Decision outcomes and validation

## Layer 2: Harness Loop (Self-Harness)

Following the Self-Harness paradigm (arXiv:2606.09498):

### 2.1 Weakness Mining
- **Skill Failure Clustering**: Group skills by failure types (API errors, logic gaps, missing context)
- **Memory Entry Correlation**: Identify memory entries that correlate with task failures
- **Decision Pattern Analysis**: Find decision types with poor retrospective validation rates
- **Performance Anomaly Detection**: Flag outliers in tool call latencies or success rates

### 2.2 Harness Proposal
- **Skill Patches**: Generate targeted improvements to existing skills
- **Memory Tier Adjustments**: Propose promotions/demotions based on usefulness
- **Workflow Optimizations**: Suggest parallelization or automation opportunities
- **Documentation Updates**: Recommend new docs based on knowledge gaps

### 2.3 Proposal Validation
- **Regression Testing**: Verify changes don't break existing functionality
- **A/B Testing**: Compare old vs. new on held-out tasks
- **Health Score Improvement**: Confirm metrics improved post-change

## Layer 3: Meta-Loop

The meta-loop optimizes the improvement process itself:

### Optimization Targets
- **Loop Trigger Sensitivity**: When should learning activate?
- **Reward Function Tuning**: What weightings for different signals?
- **Validation Strictness**: How rigorous should testing be?
- **Change Propagation Speed**: How fast should improvements spread?

### Meta-Signals
- Harness improvement effectiveness rate
- False positive/negative rates in weakness mining
- Time-to-validation for proposals
- Knowledge synthesis quality metrics

## Learning Signals Matrix

| Signal Type | Source | Weight (α) | Integration Point |
|:----------|:-------|-----------:|:------------------|
| Task Success | Execution outcomes | 1.0 | Harness Loop |
| Skill Error Rate | Tool failures | 0.8 | Weakness Mining |
| Memory Hit Quality | Memory effectiveness scoring | 0.7 | Memory adjustments |
| Decision Accuracy | Retrospective validation | 0.9 | Decision Master |
| Knowledge Growth | New pages/concepts | 0.5 | Knowledge Master |
| User Corrections | Mid-turn steering | 1.0 | Harness Loop |
| Abstraction Debt | Complexity analysis | 0.6 | Productivity Master |

## Integration with Domain Masters

### Documentation Master Integration
```
Execution → Learning:    "User asked for X doc, but it was outdated"
Learning → Documentation: Auto-generate updated documentation from successful patterns
```

### Decision Master Integration
```
Execution → Learning:    "Decision Y led to poor outcome"
Learning → Decision:     Update decision framework rules
Decision Master → Harness: Propose improved decision templates
```

### Productivity Master Integration
```
Execution → Learning:    "Skill Z was slow/ineffective"
Learning → Productivity:   Track skill effectiveness metrics
Productivity → Harness:    Propose skill replacement or optimization
```

### Knowledge Master Integration
```
Execution → Learning:    "Context missing for query W"
Learning → Knowledge:     Update indexing strategies
Knowledge Master → Harness: Propose new knowledge sources/tools
```

## Stopping Conditions for Learning Loops

**Invalid Conditions:**
- "Improvements seem helpful"
- "No obvious problems detected"
- "Iteration count exceeded"

**Valid Conditions:**
- Task success rate improved by > 10% on held-out test set
- Skill error rate reduced by > 20% for target skills
- Memory hit quality > 85% usefulness threshold
- Decision accuracy > 80% retrospective validation
- Knowledge coverage gap closed by > 50%

## Implementation Roadmap

### Phase 1: Trace Collection
- [ ] Add execution trace logging to core skill operations
- [ ] Implement memory access pattern tracking
- [ ] Create skill effectiveness scoring system

### Phase 2: Weakness Detection
- [ ] Build failure clustering algorithms
- [ ] Implement anomaly detection for performance
- [ ] Create signal correlation analysis

### Phase 3: Harness Improvement
- [ ] Auto-generate skill patches for common failure patterns
- [ ] Implement memory tier adjustment suggestions
- [ ] Create workflow optimization proposals

### Phase 4: Meta-Optimization
- [ ] Tune reward function based on outcomes
- [ ] Optimize loop trigger thresholds
- [ ] Implement loop validation itself

## Related Pages

- [[hermes-agent-stack]] — Core architecture context
- [[loop-engineering]] — Autonomous loop design
- [[self-harness-paradigm]] — Three-stage improvement loop
- [[documentation-master]] — Documentation layer
- [[decision-master]] — Decision layer
- [[productivity-master]] — Productivity layer
- [[knowledge-master]] — Knowledge layer
- [[self-health-loop]] — Health monitoring layer
- [[karpathy-enhanced-self-harness]] — Extended methodology
- [[methodology-loop]] — Loop framework