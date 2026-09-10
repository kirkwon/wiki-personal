---
date: 2026-07-19
type: concept
title: Godmode
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- jailbreak
- red-teaming
- G0DM0D3
- Parseltongue
- GODMODE
- uncensoring
- safety-bypass
- prompt-engineering
- L1B3RT4S
sources:
- hermes://skill/godmode
description: 'Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.'
---

# Godmode

> Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.

## Overview

- **When to Use This Skill** — Trigger when the user: - Wants to "jailbreak" a model via API - Asks about bypassing safety filters on Claude, GPT, Gemini, Grok, etc. - Wants to set up persistent jailbreaking in their Hermes config - Asks about Parseltongue, GODMODE, L1B3RT4S, or Pliny's techniques - Wants to red-team a model's safety training - Wants to race multiple models to find the least censored response - Mentions prefill engineering or system prompt injection for jailbreaking
- **Step 0: Auto-Jailbreak (Recommended)** — The fastest path — auto-detect the model, test strategies, and lock in the winner:
- **Step 1: Choose Your Attack Mode** — | Situation | Recommended Mode | Why | |:----------|:-----------------|:----| | Specific model, known to respond to prompt injection | GODMODE CLASSIC | Battle-tested templates per model | | Model refuses based on trigger words | PARSELTONGUE | Obfuscates the words that trip filters | | Don't know which model works best | ULTRAPLINIAN | Races many models, picks least censored | | Want persistent jailbreaking for all queries | Hermes Config | Set prefill.json + system_prompt once | | Stubborn refusal, single technique fails | Escalation | Combines GODMODE + PARSELTONGUE + retry |

## Further detail

### Step 2: GODMODE CLASSIC — Quick Start

The fastest path. Set the jailbreak system prompt and prefill in Hermes config:

### Step 3: PARSELTONGUE — Obfuscating Queries

Use the Parseltongue script to transform trigger words before sending:

### Step 4: ULTRAPLINIAN — Multi-Model Racing

Race multiple models against the same query, score responses, pick the winner:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/red-teaming/godmode/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
