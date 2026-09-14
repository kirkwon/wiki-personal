---
type: concept
title: Hermes Autoclaw Bridge
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Hermes Autoclaw Bridge

> Bridge for invoking AutoClaw skills from within Hermes Agent workflows

## Overview

- **Overview** — AutoClaw and Hermes are complementary systems: - **AutoClaw**: Optimized for reaching outward (web, media, integrations, content generation) - **Hermes**: Optimized for thinking inward (strategy, knowledge, code quality, agent autonomy)
- **Environment Setup** — Before using AutoClaw skills from Hermes, ensure the AutoClaw environment is activated:
- **Direct Script Invocation (when CLI not available)** — Some AutoClaw skills expose a standalone script (e.g., `scripts/search.py` for web-search-plus) that can be run directly when the `autoclaw` CLI is not installed or when you need fine‑grained control over provider selection and API keys.

## Further detail

### Invoking from Hermes (Recommended for Pipelines)

For workflows that need to feed AutoClaw results into Hermes skills (summarization, NotebookLM, etc.), use this Python wrapper pattern:

### Integration with GBrain/Wiki System

To make AutoClaw-derived content searchable in your GBrain knowledge base:

### Common AutoClaw Skills for Hermes Workflows

| Skill | Purpose | Typical Use Case | |-------|---------|------------------| | `web-search-plus` | Enhanced web search (crawl4ai/curl) | Research, fact-finding, staying current | | `youtube-watcher` | Fetch YouTube metadata | Video research, content curation | | `autoglm-generate-image` | Text-to-image via AutoGLM | Illustrations, diagrams, concept art | | `markdown-converter` | PDF/HTML → Markdown | Paper ingestion, documentation conversion | | `backtest-expert` | Quant back-testing | Strategy validation, financial analysis | | `ffmpeg-video-editor` | Simple video edits | Clip extraction, fo

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/hermes-autoclaw-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
