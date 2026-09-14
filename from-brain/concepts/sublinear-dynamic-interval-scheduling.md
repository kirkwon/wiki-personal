---
type: concept
title: Sublinear Dynamic Interval Scheduling (on one or multiple machines)
created: '2022-03-27T00:00:00.000Z'
sources: []
updated: '2022-03-27T00:00:00.000Z'
---

# Sublinear Dynamic Interval Scheduling (on one or multiple machines)

**arXiv:** 2203.14310 | **Published:** 2022-03-27 (revised 2022-10-03)
**Authors:** Paweł Gawrychowski, Karol Pokorski
**Categories:** cs.DS
**PDF:** https://arxiv.org/pdf/2203.14310

## Summary

This paper revisits the classical **Interval Scheduling** problem in a **dynamic setting**. The goal is to maintain a set of intervals under insertions and deletions, reporting the maximum size subset of pairwise disjoint intervals after each update — all in **sublinear time**.

## Key Contributions

### Single Machine
- **Amortized update time:** Õ(n^(1/3))
- First exact sublinear-time solution for dynamic interval scheduling

### Multiple Machines (m ≥ 2)
- **Amortized update time:** Õ(n^(1-1/m))
- Extends single-machine techniques to multiple machines

### Lower Bound (Weighted Case)
- Shows an **almost linear lower bound** for weighted dynamic interval scheduling
- Conditional on the hardness of Minimum Weight k-Clique
- Implies that for weighted cases, approximation is necessary

## Problem Context

**Dynamic Interval Scheduling:** Given a set of intervals, maintain them under insertions and deletions. After each update, report the size (or total weight) of the maximum subset of pairwise disjoint intervals.

Prior work had only approximation algorithms; this paper provides the first **exact** sublinear-time dynamic structure.

## Technical Highlights

- Avoids recomputing the answer from scratch after each update
- Multi-machine extension leverages single-machine techniques
- Lower bound shows inherent complexity barriers for exact weighted cases

## Relevance to Cron Orchestration

Interval scheduling is the **mathematical foundation** of cron scheduling:
- Each job occupies a time interval (start time + duration)
- The scheduler must select non-overlapping intervals to maximize throughput
- Dynamic interval scheduling handles **job insertions/deletions** (new cron jobs, cancelled jobs)
- The sublinear update time means the scheduler can adapt quickly without full recomputation
- Multi-machine extension maps to **distributed cron systems** (multiple workers)
