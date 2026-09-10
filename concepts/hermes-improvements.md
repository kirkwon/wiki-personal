---
date: 2026-07-19
type: concept
title: Hermes Improvements
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- hermes
- improvement
- research
- tool-quality
- autonomous-ai-agents
sources:
- hermes://skill/hermes-improvements
description: 'Design documents and implementations for improving Hermes Agent based
  on research. Currently: tool output verification (ETCHR-inspired).'
---

# Hermes Improvements

> Design documents and implementations for improving Hermes Agent based on research. Currently: tool output verification (ETCHR-inspired).

## Overview

- **1. ETCHR-Inspired Tool Output Verification** — **Paper**: [ETCHR: Editing To Clarify and Harness Reasoning](https://arxiv.org/abs/2605.23897) Zhang, Liu, Li, Zang, Wang, Lin — Shanghai AI Laboratory, CUHK, SJTU (May 2026)
- **2. Research Questions System** — **Location**: `~/brain/wiki-personal/questions/`
- **3. NotebookLM Integration** — **Notebook**: [Causal AI in Finance — Skills Bridge](https://notebooklm.google.com) **Alias**: `causal-finance` **Sources**: 7 (research questions + synthesis) + 64 (discovered papers) **Artifacts**: Infographic, Mind Map, Study Guide, Audio Deep Dive

## Further detail

### 4. Session Context Recovery

**Principle:** When a user references prior work without specifying details (e.g. "do B and D", "continue with that"), search past sessions BEFORE asking for clarification.

### 5. Git Workflow for Hermes Workspaces

**Pattern:** Two-repo structure for Hermes project directories.

### References

New in this update: - `references/terminal-backend-routing.md` — Modal vs local Mac terminal routing, pyodbc/pip fix, modal_mode config - `references/yahoo-finance-data-fetch.md` — Yahoo Finance chart API (no yfinance), Python 3.8 compat, econml/numpy fix

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-improvements/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
