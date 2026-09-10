---
date: 2026-08-02
type: concept
title: Bias Hazard Scanner
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/bias-hazard-scanner
description: 'Turns the cognitive biases library (217+ bias notes) into an action-oriented

  decision tool. Scans any plan, decision, GRAPH.md, goal, or postmortem for

  cognitive bias hazards. Produces bias-mapped risk analysis with via-negativa

  constraints and inversion-thinking prompts. Works as a prefilter for premortem

  and decision-master, or as a standalone debiasing lens.'
---

# Bias Hazard Scanner

> Turns the cognitive biases library (217+ bias notes) into an action-oriented
decision tool. Scans any plan, decision, GRAPH.md, goal, or postmortem for
cognitive bias hazards. Produces bias-mapped risk analysis with via-negativa
constraints and inversion-thinking prompts. Works as a prefilter for premortem
and decision-master, or as a standalone debiasing lens.

## Overview

- **When to Use** — | Context | Trigger | Output | |---------|---------|--------| | **Premortem prefilter** | "bias scan this plan before premortem" | Top hazards → feeds premortem agents specific bias lenses | | **Decision debiasing** | "bias check this decision" | Active biases + constraints to add | | **Goal setting** | "what biases affect this goal" | Via-negativa: what NOT to do | | **Postmortem** | "what biases caused this failure" | Retrospective bias mapping | | **GRAPH.md audit** | "scan GRAPH.md for cognitive hazards" | Structural bias risks in the plan itself |
- **The Bias Library** — Each note has: definition, manifestations, anti-patterns, detection questions, mitigation strategies, related biases, and cross-links.
- **Target** — [What was scanned: project name, file, decision]

## Further detail

### Structural Hazards

[Biases identified from the plan's structure, not just content]

### Via Negata Constraints (Compiled)

A consolidated list of "what NOT to do" — add these as constraints to the plan: 1. Do NOT [constraint from bias 1] 2. Do NOT [constraint from bias 2] ...

### Inversion Analysis

"If we wanted this to fail via cognitive bias, what would we do?" 1. [Inverted action revealing the bias] 2. [Inverted action] ...

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/decision/bias-hazard-scanner/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
