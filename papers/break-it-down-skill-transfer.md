---
date: 2026-08-23
type: entity
title: "Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents"
created: 2026-08-23
updated: 2026-08-23
tags: [model, agents, skills, methodology]
sources: [https://arxiv.org/abs/2608.20274]
---

# Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents

**Authors:** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
**Submitted:** 20 Aug 2026 (v1)
**arXiv:** [2608.20274](https://arxiv.org/abs/2608.20274) · 34 pp., 28 figs.

## Core Findings

Controlled study of how skill-induction design shapes cross-task transfer, along two axes:

1. **Granularity:** **task-level skills mostly reduce performance below the no-memory baseline**; **subtask-level skills raise it above** on average.
2. **Format:** **text skills transfer better than code skills.**

Neither specificity (how closely a skill matches real tasks) nor abstractness (how evenly relevance spreads) alone predicts success — but their **combined effect does**, proposed as a **skill utility score**. The score correlates consistently with task success under transfer; subtask-level and text skills score higher. Crucially, computing it needs **only the skills and task descriptions — no task execution**.

## Why It Matters for β (Co-Failure Rate)

Documents skill–agent co-failure directly: a retrieved skill can degrade the agent that retrieved it (task-level skills fall below no-memory baseline). The pre-execution utility score is a diagnostic computable before any run — a candidate gate for the skill library and a prior for skill-level β attribution (low-utility skills predictably harm).

## Caveats

- Effect sizes and domains not stated in abstract; single-group study.
- Utility score validated on their induction pipeline — revalidation needed on our skill corpus before adoption as a gate ^[inferred]

## Connections

- [[concepts/skill-utility-gating]] — this paper is the primary evidence for that concept
- [[papers/skillgate-inpolicy-skill-selection]] — SkillGate trains selection; this gates the library itself
- [[concepts/scaffold-optimization]] — skill granularity and format are scaffold design parameters
