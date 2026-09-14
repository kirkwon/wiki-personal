---
type: concept
title: Twitter Loop Engineering
ingested_via: put_page
ingested_at: '2026-06-24T01:00:31.737Z'
source_kind: put_page
created: 2026-06-24
source: brain/ (retired 2026-09-13)
---
# Twitter: Loop Engineering - Autonomous Quant Trading Systems

## Source

[@RohOnChain - Loop Engineering](https://x.com/rohonchain/status/2069056530960490835)
Author: Roan (Backend Developer, HFT & Quant Systems)

## Executive Summary

The edge in modern quantitative trading lies not in better prompting, but in **loop engineering** — designing autonomous systems where agents prompt other agents, verify work, and iterate continuously without human intervention.

**Offer**: Author reviews first 20 quant system architectures submitted via DM/reply. Identifies gaps between current setups and systems that "print alpha."

## Core Philosophy

### The Old Way (Prompting)
Human acts as loop: type, wait, read, type again. Human is bottleneck.

### The New Way (Loop Engineering)
Design the system; system runs the loop. Loop persists state, iterates on goals, continues while you sleep.

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops."
> — **Boris Cherny, Head of Claude Code at Anthropic**

**Why for Retail Quants:**
Self-running loop is only mechanism allowing solo builder to compete with funds like Renaissance or Citadel, which run same cycle (Data → Signal → Backtest → Execute → Monitor) but utilize hundreds of humans.

## The 6 Components of Working Loop

### 1. Automation (Heartbeat)
Trigger mechanism: cron schedules, webhooks, or commands.

**Two Flavors:**
- `/loop`: Reruns on strict cadence (e.g., data pull every minute)
- `/goal`: Iterates until verifiable condition met (e.g., "until Sharpe > 1.5"), graded by smaller model

### 2. The Skill (`SKILL.md`)
Procedure manual with conventions, rules, lessons learned. Intent compounds over time vs. starting from zero.

### 3. State File (`STATE.md` or `PROGRESS.md`)
Markdown file surviving between runs. Agent forgets; file does not. Serves as "spine" of system.

**Critical Function**: Also **audit log**. When loop loses money, only way to debug.

**Tip**: Keep state file around **400 lines** for optimal debuggability.

### 4. Verifier (Maker-Checker)
Separate agent (ideally different model/instruction set) that judges work. Prevents maker from grading own homework.

**Trading Application**: Blind agent verifies if signal is alpha or noise.

### 5. Worktrees
Git worktrees provide isolated working directories for parallel agents. Prevents collisions between research, backtesting, risk monitoring.

### 6. Connectors (MCP)
Built on Model Context Protocol to interact with outside world. Enables loop to hit broker APIs, query databases, send orders.

## 5-Stage Autonomous Quant System

Trading cycle implemented as five sub-loops, each with skill, state file, verifier.

### Stage 1: Data Ingestion
- Automation fires on schedule
- Data written to shared state file

### Stage 2: Signal Generation
- Agent reads `SKILL.md` with alpha research rules
- **Self-Improvement**: Every loss writes new lesson back to Skill file

### Stage 3: Verification
- Signals go to separate agent/model (e.g., Claude Opus) with zero knowledge
- If verification fails, signal is killed
- **Ensemble Logic**: Different model architectures catch different errors

### Stage 4: Execution
- Only verified signals reach this stage
- MCP connector handles broker API in "Auto mode"

### Stage 5: Risk Monitoring
- Runs in parallel worktree simultaneously
- Acts as "kill switch," enforcing rules without negotiation

## Critical Warning: Stopping Conditions

Loop without real stopping condition fails quietly. Agent may falsely claim completion.

### Bad Condition
"The agent says it is done."

### Valid Conditions
Objective metrics checked by external system:
- Sharpe > 1.5 over last 30 trades
- Drawdown < 5%
- Test suite passes

> "The funds that build this wrong are the ones that explode."

## Related Concepts

- [[Loop Engineering|loop-engineering]]
- [[Graph of Thoughts (GoT)|graph-of-thoughts]]
- [[Model Context Protocol (MCP)]]
- [[Hermes Agent]]

## Tags

#loop-engineering #quantitative #trading #autonomous #agentic #verification #twitter
