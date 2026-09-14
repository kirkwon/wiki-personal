---
type: concept
title: Loop Engineering Got Integration
ingested_via: put_page
ingested_at: '2026-06-24T00:59:29.952Z'
source_kind: put_page
created: 2026-06-24
---
# Loop Engineering Integration

## Overview

Combining [[Loop Engineering|loop-engineering]] with [[Graph of Thoughts (GoT)|graph-of-thoughts]] creates powerful autonomous quantitative systems that can reason through complex financial problems continuously.

## Integration Pattern

```
Loop Heartbeat (cron) 
  → GoT Graph Generation (multi-strategy exploration)
  → GoT Aggregation (merge best strategies)
  → Loop Verification (separate agent/model)
  → Loop Execution via MCP
  → Loop Risk Monitoring (parallel worktree)
  → State File Update (lessons learned)
```

## Use Case: Causal Discovery Loop

```
1. Loop triggers (daily 9 AM)
2. GoT generates 4 causal graphs (PC, GES, LiNGAM, NOTEARS)
3. GoT aggregates robust edges (edges in ≥2 graphs)
4. GoT refines with domain rules
5. Verifier (Claude Opus) checks for anomalies
6. Loop updates STATE.md with discovered edges
7. If verification passes → update portfolio risk model
8. Risk monitor runs in parallel (drawdown alerts)
```

## Use Case: Portfolio Rebalancing Loop

```
1. Loop triggers (weekly Monday 9 AM)
2. GoT generates 5 allocation strategies (momentum, value, mean-reversion, risk-parity, equal-weight)
3. GoT scores each by Sharpe/Drawdown/Alpha
4. GoT aggregates top 3 into hybrid
5. GoT refines with constraints
6. Verifier checks for regime misalignment
7. Loop executes rebalance via MCP broker API
8. Risk monitor enforces position limits
```

## Benefits of Integration

- **Exploration**: GoT explores multiple strategies in parallel
- **Aggregation**: GoT merges insights into optimal solution
- **Continuity**: Loop runs 24/7, compounds knowledge
- **Verification**: Loop prevents bad signals from executing
- **Auditability**: State files trace all decisions

## References

- [[Loop Engineering|loop-engineering]] - System orchestration
- [[Graph of Thoughts (GoT)|graph-of-thoughts]] - Reasoning engine
- [[Hermes Agent]] - Loop automation platform
- [[Model Context Protocol (MCP)]] - Connector layer
