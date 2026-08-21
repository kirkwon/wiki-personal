---
type: concept
title: Decision Master
created: 2026-07-15
updated: 2026-07-15
tags: [domain-master, decision-making, systems-thinking, architecture]
---

# Decision Master

## Summary

Decision Master is a **domain-specialized cognitive layer** within the Hermes agent architecture responsible for structured decision-making, decision provenance tracking, and decision hygiene enforcement.

## Purpose

Decision Master operates as a semi-autonomous subsystem that:
- Applies structured decision frameworks (pre-mortem, black swan analysis)
- Maintains decision logs with clear provenance
- Enforces decision audit trails
- Provides veto authority on high-risk tool calls

## Responsibilities

| Responsibility | Mechanism | Integration Point |
|:--------------|:----------|:----------------|
| Pre-mortem Analysis | `[[premortem-skill]]` integration | → Analysis |
| Decision Tracking | Structured log: {id, context, options, choice, rationale, outcome} | → Learning |
| Risk Assessment | Leverage-seeking + downside bounding | → Interaction |
| Outcome Validation | Retrospective verification | → Learning |

## Decision Framework

### The Pre-mortem Process
1. **State the decision** clearly with context
2. **Identify assumptions** underlying the decision
3. **Generate failure scenarios** ("One thing that could break this")
4. **Quantify confidence** with explicit uncertainty
5. **Log decision** with outcome tracking field

### Stopping Conditions
- Objective metrics verified externally (not "agent says done")
- Sharpe ratio > 1.5 over rolling 30-trade window
- Decision accuracy tracking validated retroactively

## Health Signals

- **open_decisions**: Number of tracked open decisions
- **pending_premortems**: Decisions requiring analysis
- **accuracy_rate**: Percentage of decisions validated post-hoc
- **decision_latency**: Time from decision to outcome

## Related Pages

- [[hermes-agent-stack]] — Core architecture context
- [[premortem-skill]] — Decision analysis tool
- [[black-swan-protocol]] — Assumption-challenging principle from SOUL.md
- [[documentation-master]] — Sibling domain master
- [[knowledge-master]] — Knowledge integration layer