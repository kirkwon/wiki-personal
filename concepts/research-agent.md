---
date: 2026-07-19
type: concept
title: Research Agent
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Research
- Multi-Agent
- Arxiv
- Knowledge
- Synthesis
- research
sources:
- hermes://skill/research-agent
description: '4-agent crew for structured research: planner → researcher → extractor
  → synthesizer. Searches arXiv, web, and GBrain knowledge base.'
---

# Research Agent

> 4-agent crew for structured research: planner → researcher → extractor → synthesizer. Searches arXiv, web, and GBrain knowledge base.

## Overview

- **Output** — Results saved to: `~/brain/research/research-<slug>-<date>.md`
- **Key Findings** — - ...
- **Implications** — - ...

## Further detail

### Related Topics

- PPO vs GRPO comparison - RLHF for LLMs - Reward modeling

### STORM Enhancement: Multi-Perspective Research

**STORM** (Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking) is a Stanford framework that upgrades the Planner phase. Instead of a single decomposition, STORM generates **multiple expert personas** who each interrogate the topic from different angles, surfacing question categories a single-perspective planner would miss.

### Pitfalls

- arXiv requires network access; rate limited to ~1 req/3 seconds - GBrain search requires GBrain instance running - Web search needs web_search tool availability - No findings = "Further research needed" (not an error) - **STORM adds cost** — N personas × M questions each = N×M search calls. Use `--quick` or limit personas to 3-4 for cost-sensitive runs. - **Always verify deliverables exist** before claiming research gaps. Check the filesystem and prior session outputs before telling the user something was "never delivered."

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/research-agent/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
