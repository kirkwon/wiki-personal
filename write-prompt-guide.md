---
type: concept
title: Write Prompt Guide
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - prompt-engineering
---

# write-prompt-guide

>-

## Usage

# Write a Prompt for Claude

## Purpose

A self-contained, opinionated checklist for writing high-quality prompts for Claude's latest models (Opus 4.8 / 4.7 / 4.6, Sonnet 4.6, Haiku 4.5). It distills Anthropic's canonical prompt-engineering guidance — the [overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) and [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) pages — into a single reference you can pull in whenever you draft or refine a prompt. Read-only knowledge artifact: it tells *you* (or an agent acting on your behalf) how to construct a prompt; it does not call any API. The LaTeX/math-formatting guidance from the source is intentionally excluded.

## When to Use

- You're drafting a new system prompt or user prompt and want it right the first time.
- An existing prompt is underperforming and you need a structured way to diagnose and fix it.
- You're migrating prompts to a newer Claude model and behavior has shifted (verbosity, tool triggering, thinking, prefill).
- You're building an agentic harness (coding agent, research agent, long-horizon task runner) and need prompt patterns for autonomy, state tracking, and safety.
- You want to refresh this guide from source — the canonical pages are fetchable as clean Markdown (see Workflow step 0 and Gotchas).

## Workflow

**Optimal retrieval path (how this guide stays current).** The canonical docs serve clean Markdown at the same URL with a `.md` suffix — no browser, login, or scraping needed. `recommended_method: fetch`. To refresh:

```
GET https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview.md
GET https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices.md
```

Both return `text/markdown; 200`. Prefer this over rendering the HTML page. Everything below is the distilled product of those two pages.

### 0. Prerequisites — before you prompt-engineer

1. **Define success criteria** for your use case (what does a good output look like, measurably).
2. **Build a way to test** against those criteria (even a handful of eval cases).
3. **Have a first-draft prompt** to improve. (No draft? Use the prompt generator in the Claude Console.)
4. **Confirm prompting is the right lever.** Latency and cost are often better solved by model choice or the `effort` parameter than by prompt wording.

### 1. Core principles (apply to every prompt)

- **Be clear and direct.** Treat Claude as a brilliant new employee with zero context on your norms. State exactly what you want, including output format and constraints. If you want "above and beyond" effort, ask for it explicitly — don't rely on inference. **Golden rule:** show your prompt to a colleague with minimal context; if they'd be confused, so will Claude.
- **Use sequential steps** (numbered lists / bullets) when order or completeness matters.
- **Add context and

...(truncated)