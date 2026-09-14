---
type: concept
title: Loop Engineering
ingested_via: put_page
ingested_at: '2026-06-24T00:59:00.926Z'
source_kind: put_page
created: 2026-06-24
---
# Loop Engineering

## Overview

**Loop Engineering** is the practice of designing autonomous systems where agents prompt other agents, verify work, and iterate continuously without human intervention. It represents the transition from manual AI prompting to self-running agentic systems.

## Core Philosophy

### The Old Way (Prompting)
Human acts as the loop: type, wait, read, type again. The human is the bottleneck.

### The New Way (Loop Engineering)
Design the system; the system runs the loop. The loop persists state, iterates on goals, and continues while you sleep.

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops."
> — **Boris Cherny, Head of Claude Code at Anthropic**

**Why this matters for Retail Quants:**
A self-running loop is the only mechanism that allows a solo builder to compete with funds like Renaissance or Citadel, which effectively run the same cycle (Data → Signal → Backtest → Execute → Monitor) but utilize hundreds of humans to sit inside the loop.

## The 6 Components of a Working Loop

Every functional agentic system relies on these six pieces. Missing one breaks the loop.

### 1. The Automation (Heartbeat)
The trigger mechanism: cron schedules, webhooks, or commands.

**Two Flavors:**
- `/loop`: Reruns on strict cadence (e.g., data pull every minute)
- `/goal`: Iterates until verifiable condition met (e.g., "keep iterating until Sharpe ratio > 1.5"), graded by smaller model

### 2. The Skill (`SKILL.md`)
Procedure manual containing conventions, rules, and lessons learned. Ensures intent compounds over time rather than starting from zero every run.

### 3. The State File (`STATE.md` or `PROGRESS.md`)
Markdown file that survives between runs. Agent forgets; file does not. Serves as "spine" of system.

**Critical Function**: Also acts as **audit log**. When loop loses money, this is the only way to debug.

**Tip**: Keep state file around **400 lines** for optimal debuggability (too short or too long renders it useless).

### 4. The Verifier (Maker-Checker)
Separate agent (ideally different model/instruction set) that judges work. Prevents "maker" from grading their own homework.

**Trading Application**: Blind agent verifies if signal is alpha or noise.

### 5. The Worktrees
Git worktrees provide isolated working directories for parallel agents. Prevents collisions between research, backtesting, and risk monitoring processes.

### 6. The Connectors (MCP)
Built on Model Context Protocol to interact with outside world. Enables loop to hit broker APIs, query databases, or send orders (turning suggestions into actions).

## The 5-Stage Autonomous Quant System

Complete trading cycle implemented as five sub-loops, each with own skill, state file, and verifier.

### Stage 1: Data Ingestion
- Automation fires on schedule (minute/hour/day)
- Data written to shared state file for next stage

### Stage 2: Signal Generation
- Agent reads `SKILL.md` containing alpha research rules
- **Self-Improvement Mechanism**: Every loss writes new lesson back to Skill file, creating rule for future runs

### Stage 3: Verification
- Signals go to separate agent/model (e.g., Claude Opus) with zero knowledge of original reasoning
- If verification fails, signal is killed
- **Ensemble Logic**: Different model architectures for generation vs. verification catch different errors

### Stage 4: Execution
- Only verified signals reach this stage
- MCP connector handles broker API in "Auto mode" (hands-off)

### Stage 5: Risk Monitoring
- Runs in parallel worktree simultaneously
- Acts as "kill switch," enforcing rules without negotiation

## Critical Warning: Stopping Conditions

Loop without real stopping condition fails quietly. Agent may falsely claim completion.

### Bad Condition
"The agent says it is done."

### Valid Conditions
Objective metrics checked by external system:
- Sharpe ratio above 1.5 over last 30 trades
- Drawdown below 5 percent
- Test suite passes

> "The funds that build this wrong are the ones that explode."

## Integration with Graph of Thoughts

Loop Engineering and [[Graph of Thoughts (GoT)]] are complementary:

- **Loop Engineering**: Orchestrates autonomous system (heartbeat, skills, state, verification)
- **Graph of Thoughts**: Provides reasoning engine within loops (aggregation, refinement, generation)

**Example Integration:**
```
Loop Heartbeat (cron) → GoT Graph Generation → GoT Aggregation of signals → 
Loop Verification (separate agent) → Loop Execution via MCP → Loop Risk Monitoring
```

## Practical Implementation

### Cron Job (Hermes)
```python
# cronjob action=create schedule="*/5 * * * *" name="quant-signal-loop"
# Runs every 5 minutes
```

### State File Structure
```markdown
# STATE.md - Quant Signal Loop

## Last Run
Date: 2026-06-23 17:00
Status: Complete

## Current Signals
- AAPL: BUY (Sharpe 1.8, Confidence 0.75)
- MSFT: HOLD (Sharpe 1.2, Confidence 0.60)

## Lessons Learned (auto-updated after each loss)
[1] Never buy on positive momentum without volume confirmation (2026-06-15)
[2] Always verify signal against regime (vol_regime=1 requires different threshold)
```

### Verification Agent
```python
# Separate model from signal generation
verifier = delegate_task(
  goal="Verify if this signal is alpha or noise. Zero knowledge of generation method.",
  model="claude-opus"
)
```

## Benefits

- **Scalability**: Solo builder can compete with large funds
- **Continuity**: System runs 24/7, compounds knowledge
- **Auditability**: State files provide complete history
- **Robustness**: Verification catches errors
- **Adaptability**: Self-improvement through lessons learned

## Risks

- **Stopping Conditions**: Must be objectively verifiable
- **State File Size**: ~400 lines optimal
- **Verification Blindness**: Verifier must have zero knowledge of generation
- **MCp Security**: Connectors to broker APIs require safeguards

## Resources

- **Twitter Thread**: [@RohOnChain - Loop Engineering](https://x.com/rohonchain/status/2069056530960490835)
- **Quote**: Boris Cherny, Head of Claude Code at Anthropic
- **Related**: [[Graph of Thoughts (GoT)]], [[Hermes Agent]], [[Model Context Protocol (MCP)]]

## Tags

#autonomous #quantitative #trading #loop-engineering #agentic #systems #automation #verification #state-management
