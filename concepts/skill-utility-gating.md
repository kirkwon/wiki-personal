---
date: 2026-08-23
type: concept
title: Skill Utility Gating
created: 2026-08-23
updated: 2026-08-23
tags: [methodology, skills, evaluation]
sources: [papers/break-it-down-skill-transfer, papers/skillgate-inpolicy-skill-selection, papers/tmi-task-model-induction]
---

# Skill Utility Gating

The principle that **skills must clear an expected-utility bar before entering (or remaining in) an agent's retrieval path** — self-generated or mined skills are not benign by default; unreliably-transferring skills actively harm the agent that retrieves them.

## Evidence (Aug 2026 cluster)

| Source | Finding |
|--------|---------|
| [[papers/break-it-down-skill-transfer]] | Task-level induced skills drop performance **below no-memory baseline**; subtask-level + text format transfer best. Pre-execution utility score (specificity × abstractness) predicts transfer success without running tasks. |
| [[papers/skillgate-inpolicy-skill-selection]] | Outcome RL cannot train skill selection (selector credit starvation — correct choices punished by downstream execution failure). Disjoint credit channels fix it: 9B policy 40.8% → 53.2%. |
| [[papers/tmi-task-model-induction]] | Mined skills (from computer-use traces) help +30% — but only after task disentanglement; naive mining without attribution hygiene contaminates failure statistics. |
| [[papers/phantom-gains-self-improvement-null]] | Self-training artifacts can corrupt baseline-solved problems; every self-improvement delta needs a frozen-control null. |
| FinSkillBench ([2608.18099](https://arxiv.org/abs/2608.18099)) | Curated skill packages: +16.2pp (0.366→0.528); **self-generated skills: +0.5pp — no reliable benefit**. Cross-harness replication incl. Hermes Agent (8 models, 5,280 episodes). |

The convergent theme across four independent groups: **self-generated/mined skill artifacts require measured utility before reuse, and selection decisions need de-confounded credit.**

## Operational Form

1. **Library gate (inference-time):** score candidate skills by specificity × abstractness against the task description before loading; discard sub-utility-bar skills. Costs no execution.
2. **Selection gate (training-time, P3):** when training on skill-conditioned traces, split credit channels so skill-naming tokens don't inherit execution outcome noise (SkillGate pattern).
3. **Audit gate (evaluation):** any claimed skill benefit passes the [[papers/phantom-gains-self-improvement-null|frozen-control null]] test before it's believed.

## Relations

- [[concepts/scaffold-optimization]] — gating is the quality-control stage of the skill-as-learnable-scaffold pipeline
- [[concepts/co-failure-ceiling]] — low-utility skills are a source of skill–agent co-failure; utility is a prior for β attribution
- [[concepts/skill-governance]] — the existing governance concept this extends with a quantitative gate
- [[concepts/skill-vetting]] — operational vetting pipeline this gates

[[skill-vetting]]
