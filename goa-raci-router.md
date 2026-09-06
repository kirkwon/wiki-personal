---
type: concept
title: Goa Raci Router
created: 2026-09-05
updated: 2026-09-05
tags:
  - Skill
  - uncategorized
---

# goa-raci-router

"Use when a task could involve multiple master skills (knowledge, decision, finance, coding, etc.) and you need to decide which to delegate to. Performs Graph-of-Agents RACI routing — reads domain cards, assigns R/C/I roles, builds directed message-passing edges. Fallback to keyword matching."

## Usage

# GoA RACI Router

## When to Use
- A complex task spans multiple domains (e.g., "evaluate and rebalance portfolio" = finance + decision)
- You're about to fan out to delegate_task and need to decide which masters to involve
- The task is ambiguous and could route to 3+ different master skills

## When NOT to Use
- Linear tasks with one obvious master (e.g., "fix this bug" → coding only)
- Simple tasks you can handle directly
- Tasks with <2 potential masters involved

## How It Works

### Phase 1: Read Domain Cards
```
Read: ~/clawd/01.Graph-of-agentsracirouter/01.Core/domain-cards.yaml
```
This file declares each master's domains, activation triggers, and consultation edges.

### Phase 2: Assign RACI Roles (YOU are the LLM sampler)

Given the task and domain cards, assign:

- **R (Responsible)**: 1-3 masters who will actively DO the work
- **C (Consulted)**: 0-2 masters who ENHANCE R-nodes via message passing
- **I (Informed)**: All remaining masters — not involved

Rules (from GoA paper, ICLR 2026):
- Total R + C should be 2-4 masters (3 active agents is optimal)
- Pick R nodes by strongest domain match
- Pick C nodes that complement R nodes
- NEVER assign more than 3 R nodes
- If only 1 master is relevant, R=[that master], C=[], I=[rest]

### Phase 3: Build Directed Edges

For message passing between selected nodes:
- **expert_to_generalist**: R nodes ordered by relevance (most → least)
- **consult**: C nodes → R nodes they complement

### Phase 4: Execute

1. Delegate to R-nodes via `delegate_task` (parallel if independent)
2. For each C→R edge: pass R-node's initial output to C-node for enhancement
3. **Critique each R-node output via RDEIUR** (see Phase 5)
4. Pool R-node responses (weighted by relevance order, exclude escalated)

### Phase 5: RDEIUR Critic Gate (MANDATORY when OmniRoute is online)

After each R-node's `delegate_task` returns, run the critic BEFORE pooling:

```bash
# Check if OmniRoute is online (returns 200 = online)
curl -s -o /dev/null -w "%{http_code}" http://localhost:20128/v1/models

# If online, critique each R-node's output:
python3 ~/clawd/108.RdeiurCycle/03.Scripts/rdeiur_critic.py \
  --content "<R-node response text>" \
  --criteria "<exit criteria from the task>" \
  --json
```

**Verdict handling:**
- `accept` → Use the response as-is
- `retry` → Use the response but flag defects to the user
- `escalate` → **Discard the response**. Re-delegate to a different master or do it yourself

**If OmniRoute is offline**: skip the critic (graceful degradation — pool normally).

## CLI Fallback

If you need programmatic routing (e.g., in a script):
```bash
python3 ~/clawd/01.Graph-of-agentsracirouter/03.Scripts/goa_router.py \
  --task "Backtest covered call strategy" --json
```

Uses keyword matching as fallback when no LLM API is available.

## Example

**Task**: "Should I rebalance my portfolio? Evaluate the risk tradeoff"

**Domain card match**: finance-master (portfolio, rebalance) + decision-master (evaluate, risk

...(truncated)