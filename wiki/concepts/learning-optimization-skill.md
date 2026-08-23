---
date: 2026-07-02
type: concept
title: Learning Optimization System (skill candidate)
description: "Executable skill for optimizing learning through spaced repetition scheduling, retrieval practice prompts, dual-process calibration, focus state management, and feedback loop design."
created: 2026-07-02
updated: 2026-07-02
tags:
- skill-candidate
- knowledge
- learning
phase: P3
io_contract:
  input: "{learning_goal, current_knowledge_level, time_available_per_week, preferred_medium, focus_pattern, topics[]}"
  output: "{spaced_repetition_schedule, retrieval_prompts[], focus_blocks[], feedback_loops[], dual_process_calibration, memory_tier_recommendations[]}"
depends_on:
- spaced-repetition (wiki)
- retrieval-practice (wiki)
- active-revision-techniques (wiki)
- deliberate-practice (wiki)
- feynman-technique (wiki)
- dual-process-theory (wiki)
- deep-focus (wiki)
- habit-loop (wiki)
- memory-tier-system (skill)
priority: high
rationale: "Learning optimization is an active user concern. 25KB+ of wiki content across 10+ evidence-based learning methods with no executable skill tying them together. Learning-master has the retention pipeline but no active learning scheduler."
---
# Learning Optimization System

**Phase:** P3 (Execute)
**Master:** learning-master
**Priority:** High

## Input Schema
```json
{
  "learning_goal": "Master causal inference for financial markets",
  "current_knowledge_level": "intermediate",
  "time_available_per_week_hours": 5,
  "preferred_medium": ["papers", "code", "notes"],
  "focus_pattern": "deep_focus_morning",
  "topics": [
    {"name": "ATE estimation", "priority": "high", "current_level": "basic"},
    {"name": "CausalForestDML", "priority": "high", "current_level": "none"},
    {"name": "Instrumental variables", "priority": "medium", "current_level": "basic"}
  ]
}
```

## Output Schema
```json
{
  "spaced_repetition_schedule": [
    {"topic": "ATE computation", "next_review": "2026-07-03", "interval": "1d", "tier": "HOT"},
    {"topic": "Confounders vs colliders", "next_review": "2026-07-05", "interval": "3d", "tier": "WARM"},
    {"topic": "CausalForestDML hyperparams", "next_review": "2026-07-09", "interval": "7d", "tier": "WARM"}
  ],
  "retrieval_prompts": [
    "Explain the difference between ATE and CATE in your own words",
    "Why does confounder adjustment flip the sign of the P6 ATE estimate?",
    "Code: implement OLS ATE estimation from scratch"
  ],
  "focus_blocks": [
    {"day": "Monday", "time": "07:00-08:30", "type": "deep_focus", "task": "Read Hernan & Robins Ch12"},
    {"day": "Wednesday", "time": "07:00-08:00", "type": "retrieval_practice", "task": "Review yesterday's ATE experiment"},
    {"day": "Friday", "time": "07:00-08:30", "type": "deliberate_practice", "task": "Implement CausalForestDML on real data"}
  ],
  "feedback_loops": [
    {"metric": "CI_width_reduction", "target": ">=15%", "check_frequency": "weekly"},
    {"metric": "ATE_correct_sign", "target": "matches domain knowledge", "check_frequency": "per_experiment"}
  ],
  "dual_process_calibration": {
    "system1_heuristics": "Past experiment outcome = future result",
    "system2_correction": "Check CATE by regime — effect may be conditional",
    "calibration_method": "Prediction log: before each experiment, record expected ATE sign + magnitude"
  },
  "memory_tier_recommendations": [
    {"concept": "ATE formula", "recommended_tier": "HOT", "reason": "Used daily in experiments"},
    {"concept": "CATE breakdown patterns", "recommended_tier": "WARM", "reason": "Weekly reference"},
    {"concept": "Self-harness methodology", "recommended_tier": "COOL", "reason": "Monthly review"}
  ]
}
```

## Sources
- [[spaced-repetition]] (4.5KB) — Scheduling algorithm
- [[retrieval-practice]] (2.2KB) — Testing effect
- [[active-revision-techniques]] (2.3KB) — Study methods
- [[deliberate-practice]] (4.0KB) — Skill improvement framework
- [[feynman-technique]] (1.9KB) — Explanation as verification
- [[dual-process-theory]] (3.2KB) — System 1/2 calibration
- [[deep-focus]] (3.2KB) — Focus state management
- [[habit-loop]] (5.9KB) — Habit formation loop
- [[calibration-training]] (1.3KB) — Prediction calibration
- [[feedback-loop-design]] (2.9KB) — Learning feedback
- [[memory-tier-system]] (skill) — Tier promotion logic
- [[knowledge-metabolism]] (skill) — Concept digestion

## DAG Position
`inputs → LearningOptimizer → memory-tier-system (tier assignment) → knowledge-metabolism (digest) → gbrain-content-ops (store schedule)`
