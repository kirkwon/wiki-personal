---
date: 2026-07-19
type: concept
title: Extract Wisdom
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- research
sources:
- hermes://skill/extract-wisdom
description: Extract profound, actionable insights from text (books, articles, transcripts)
  with structured output for knowledge bases like Obsidian and GBrain.
---

# Extract Wisdom

> Extract profound, actionable insights from text (books, articles, transcripts) with structured output for knowledge bases like Obsidian and GBrain.

## Overview

- **Steps** — 1. Ingest full input text (use `read_file` or `youtube-content` skill for videos) 2. Identify core themes and recurring concepts 3. Extract 3-5 actionable insights per theme, with direct quotes/source context 4. For multi-lens texts (e.g., multiple philosophers), extract insights PER lens first, then add 1-2 cross-cutting insights that synthesize multiple lenses 5. Format output with YAML frontmatter (title, source, date) + Markdown body 6. Link to existing GBrain entities or Obsidian notes if applicable 7. Verify no hallucinated insights against source text
- **Output Format for Multi-Lens Texts** — When extracting wisdom from texts with multiple perspectives: - Section 1: Per-lens insights (attributed to each philosopher/framework) - Section 2: Cross-cutting insights (synthesizing tensions/complementarities) - Each insight: 1-2 sentences, self-contained, actionable - Target 5-7 total insights for a standard essay
- **Pitfalls** — - Avoid over-interpreting edge cases as core insights - Preserve source context — never strip attribution - Keep insights concise (1-2 sentences each)

## Further detail

### Verification

- Cross-check extracted insights against original text - Ensure at least one link to existing knowledge base (if available)

### Usage

To extract wisdom from a text file using the Hermes agent:

### Cost Considerations

This skill invokes a local LLM (typically phi3 via Ollama) to analyze and extract insights. Expect approximately 0.5-1 second of processing time per file on modest hardware. For large batches (hundreds of files), consider: - Running extraction only on ongoing sources (e.g., daily notes) rather than historical imports - Sampling a subset of historical data for enrichment - Queuing extraction as a separate lower-priority job

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/extract-wisdom/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
