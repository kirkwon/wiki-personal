---
type: concept
title: >-
  Enhancing Adaptive Mixed-Criticality Scheduling with Deep Reinforcement
  Learning
created: '2024-11-01T00:00:00.000Z'
sources: []
updated: '2024-11-01T00:00:00.000Z'
---

# Enhancing Adaptive Mixed-Criticality Scheduling with Deep Reinforcement Learning

**arXiv:** 2411.00572 | **Published:** 2024-11-01
**Authors:** Bruno Mendes, Pedro F. Souto, Pedro C. Diniz
**Affiliations:** DEI/FEUP, CISTER Research Centre
**Categories:** cs.OS, cs.LG
**PDF:** https://arxiv.org/pdf/2411.00572

## Summary

**First application of Deep Reinforcement Learning (DRL) to Adaptive Mixed-Criticality (AMC) scheduling** in hard real-time systems. The paper uses a Deep Q-Network (DQN) to dynamically adjust task budgets, preventing deadline misses.

## Problem

- **Adaptive Mixed-Criticality (AMC)** is a fixed-priority preemptive scheduling algorithm used in mixed-criticality real-time systems
- Key limitation: AMC may **drop jobs from low-priority tasks** when tasks overrun their allocated time budgets
- This degrades system performance in dynamic environments (e.g., automotive systems)

## Proposed Solution

A **Deep Q-Network (DRL)** approach that:
1. Is **trained offline** on historical workload data
2. At **runtime**, dynamically adjusts low-criticality task budgets
3. Prevents budget overruns while ensuring no job misses its deadline

## Results

- **Reduces budget overruns by up to 50%** even when task budgets are sampled from execution time distributions
- Evaluated via simulation of realistic automotive workloads
- Maintains timing guarantees while improving adaptability

## Key Innovation

> "To the best of our knowledge, this is the first use of DRL in AMC reported in the literature."

## Relevance to Cron Orchestration

This paper's approach maps directly to **priority-aware cron scheduling**:
- High-priority jobs (health checks, backups) get guaranteed resources
- Low-priority jobs (reports, non-critical syncs) get adaptive budgets
- A DRL agent learns to adjust resource allocation dynamically
- Prevents low-priority jobs from starving or causing deadline misses
