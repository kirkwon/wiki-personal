---
date: 2026-06-30

type: source
title: "BuilderIO Skills — Repo Analysis"
source: "github.com/BuilderIO/skills"
tags:
  - skills
  - builderio
  - agent-skills
  - coding-agents
created: 2026-07-26
updated: 2026-07-26
---

# BuilderIO Skills — Analysis

Source: [github.com/BuilderIO/skills](https://github.com/BuilderIO/skills) by Steve8708

## Skill Evaluation

| # | Skill | What It Does | Fit | Verdict |
|---|-------|-------------|-----|---------|
| 1 | **agent-watchdog** | Audit another agent's work from session/PR/transcript | Already use GPT for review; watchdog is for code agents | 🟡 Maybe — if you start delegating to Claude Code / OpenCode |
| 2 | **efficient-fable** | Use expensive Fable model only for judgment; cheaper agents do scans/edits | Your dispatch skill already routes by task type | 🟡 Overlap with dispatch skill |
| 3 | **efficient-frontier** | Model-agnostic version of efficient-fable | Same as above | 🟡 Overlap with dispatch skill |
| 4 | **plan-arbiter** | Compare competing agent plans, choose one | Your premortem skill does this for decisions | 🟡 Overlap with premortem skill |
| 5 | **plow-ahead** | Work through ambiguity, make assumptions, keep going | Anti-pattern for your eval-first philosophy | ❌ Don't adopt — you want traceability |
| 6 | **quick-recap** | Red/yellow/green status footer on every response | Lightweight, easy to add to AGENTS.md | ✅ **Add it** — low effort, high signal |
| 7 | **read-the-damn-docs** | Docs-first: web search before guessing APIs | Strong philosophy alignment | ✅ **Add it** — prevents hallucinated APIs |
| 8 | **stay-within-limits** | Budget loop for long-running agent work | Relevant for parallel dispatch + cron | 🟡 Maybe — if you hit token limits |
| 9 | **visual-plan** | MDX visual review surfaces for implementation plans | Requires agent-native viewer; separate tool | ❌ Too heavy for current workflow |
| 10 | **visual-recap** | MDX visual recap for diffs/PRs | Same as above | ❌ Too heavy for current workflow |

## Recommendations

### ✅ Add These

**`quick-recap`** — A 3-line AGENTS.md addition that adds a 🟢/🟡/🔴 status footer to every response. Zero-cost signal for status. Just adds a convention.

**`read-the-damn-docs`** — A docs-first discipline that forces agents to web-search before guessing API behavior. Currently, I sometimes guess package versions or API signatures. This skill adds mandatory docs checks for external APIs, libraries, frameworks, and CLIs. It aligns with your eval-first, traceability philosophy.

### 🟡 Consider If

**`agent-watchdog`** — If you start dispatching real coding work to Claude Code/OpenCode via the dispatch skill, this would audit their output and catch gaps. Not useful yet since you're not delegating to code agents.

**`stay-within-limits`** — If you start running parallel subagents at scale, this prevents burning through rate limits mid-task. Not a problem yet.

### ❌ Skip

**`plow-ahead`** — Makes assumptions and runs with them. Anti-pattern for your eval-first, knowledge-metabolism approach. You want traceable decisions, not autonomous guessing.

**`visual-plan` / `visual-recap`** — Require the Agent-Native MDX viewer. Cool tech but adds a full web dependency for what you currently do in markdown.

**`efficient-fable` / `efficient-frontier` / `plan-arbiter`** — Overlap significantly with your existing dispatch + premortem + knowledge-metabolism skills. The routing logic is already baked into dispatch.

### Install Note

BuilderIO skills install via:
```sh
npx @agent-native/skills@latest add --skill <name>
```

This copies a SKILL.md into your workspace. The source repo is MIT licensed.
