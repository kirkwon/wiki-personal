---
type: concept
title: Parallel Search Orchestration
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Parallel Search Orchestration
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- parallel
- concurrency
- search
- threadpool
- python
- pattern
- software-development
sources:
- hermes://skill/parallel-search-orchestration
description: Use when implementing concurrent multi-source search in a CLI tool. Uses
  ThreadPoolExecutor for parallel dispatch, cache-first strategy, and graceful error
  handling per source. Pattern for combining speed of parallel execution with cache-aside
  reliability.
---

# Parallel Search Orchestration

> Use when implementing concurrent multi-source search in a CLI tool. Uses ThreadPoolExecutor for parallel dispatch, cache-first strategy, and graceful error handling per source. Pattern for combining speed of parallel execution with cache-aside reliability.

## Overview

- **When to Use** — - Querying multiple data sources simultaneously (databases, APIs, filesystems) - Reducing total latency from O(sum) to O(max) across sources - Implementing cache-aside with fresh-fetch fallback - Building meta-search or unified-search tools
- **Adapter Signature Convention** — Each searcher function must follow:
- **Testing** — Expected: Sequential ~2.0s, Parallel ~0.5s.

## Further detail

### Pitfalls

1. **Cache check inside the thread** — every cached result still gets scheduled, defeating the optimization. Check cache BEFORE submitting. 2. **No global timeout** — a hung searcher blocks the entire search. Use `concurrent.futures.wait()` with `timeout` or individual per-searcher timeouts. 3. **Results order non-deterministic** — use `as_completed` and process results as they arrive. For deterministic ordering, collect all futures and sort afterward. 4. **Shared state between searchers** — ThreadPoolExecutor shares memory. Each searcher should be stateless (input → output only). 5. **Not han

### Success Metrics

| Metric | Target | How to Measure | |--------|--------|----------------| | Parallel vs sequential speedup | ~Nx for N sources | `time` command on search | | Cache hit overhead | <50ms | Measure cached query time | | Error isolation | 0 cross-contamination | Kill one source, verify others complete |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/parallel-search-orchestration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
