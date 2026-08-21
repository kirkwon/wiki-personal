---
date: 2026-06-29

type: concept
tags: [autoresearch, research-loop, experiment-automation, ml-research, methodology]
related: [awesome-autoresearch, karpathy-autoresearch-loop, experiment-loop, iterative-research]
---

# Autoresearch Pattern

A general-purpose autonomous research methodology where an AI agent proposes hypotheses, implements them as code changes, runs experiments against a fixed evaluator, and keeps or discards each change based on empirical results.

## Core loop
1. **Propose** — agent reads the current state and suggests a single change
2. **Implement** — agent edits one file (usually `train.py` or equivalent)
3. **Run** — fixed-budget experiment (time, tokens, or compute limit)
4. **Evaluate** — metric against a held-out evaluator (validation loss, accuracy, throughput)
5. **Decide** — keep (commit) or discard (revert) based on improvement
6. **Repeat** — loop back to step 1

## Key properties
- **Single-file mutation** — only one mutable file (`train.py`, `optimize.py`); all other files are locked (chmod 444)
- **Fixed evaluator** — the evaluation script is frozen and trusted
- **Short budget** — experiments are cheap (2-15 minutes) to enable rapid iteration
- **Git ratchet** — commits only improvements; discards are git reverts
- **Results ledger** — `results.tsv` or JSONL logs every experiment

## Variants across domains
| Variant | Source | Difference |
|---------|--------|------------|
| Karpathy original | karpathy/autoresearch | GPT-2 nano, val_bpb metric |
| Paired-seed | autoresearch-speedrun | Two seed runs per change, only accept if both improve |
| Scout-promote | openroad-autoresearch | Cheap scout runs → full eval only for strong candidates |
| Multi-agent | AutoScientists | Decentralized team, shared hypothesis pool |
| Phased strategist | AutoMedal | Strategist → Researcher → Experimenter roles |
| Paper-augmented | Paper Lantern | MCP server with 2M papers to inform proposals |
| 100-round scaffold opt | MiniMax M2.7 | Optimizes the scaffold itself, kept 30% eval improvement |
| Self-healing | AutoResearchClaw | Autonomous recovery from failed experiments |
| Evidence-gated | Vesuvius AutoResearch | MetricContract enforcement before promotion |

## What makes it different from generic agents
- **Empirical, not declarative** — the agent proves its change works by running real code and measuring a metric, not by reasoning about why it should work
- **Bounded risk** — each experiment is cheap and revertible; you can't lose more than one experiment cycle
- **Emergent discovery** — the keep/discard mechanism lets the agent find non-obvious improvements a human wouldn't propose

## Source
- Originally published by Andrej Karpathy (Feb 2026): https://github.com/karpathy/autoresearch
- Curated list: https://github.com/yibie/awesome-autoresearch
