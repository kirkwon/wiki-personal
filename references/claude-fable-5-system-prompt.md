---
title: Claude Fable 5 — System Prompt Deep Dive
created: 2026-06-19
updated: 2026-06-19
type: reference
tags: [ai-systems, system-prompts, anthropic, claude, prompt-engineering]
sources: [raw/sources/CL4R1T4S/ANTHROPIC/CLAUDE-FABLE-5.md]
confidence: high
summary: "Anthropic's most detailed system prompt to date (17.5K words). Fable 5 introduces Mythos-tier models, aggressive copyright guardrails, MCP connector orchestration, and granular child-safety/wellbeing protocols."
---

# Claude Fable 5 — System Prompt Deep Dive

**Source:** `raw/sources/CL4R1T4S/ANTHROPIC/CLAUDE-FABLE-5.md` (1,597 lines, ~17,500 words)
**Date reference:** June 9, 2026 | **Knowledge cutoff:** end of Jan 2026

## Model Identity

Claude Fable 5 is described as "the first model in Anthropic's new Claude 5 family and part of a new **Mythos-class model tier** that sits above Claude Opus in capability." Claude Fable 5 and Claude Mythos 5 share the same underlying model, but Fable 5 includes additional safety measures for dual-use capabilities, while Mythos 5 is available without those measures to approved organizations only. The prompt references Claude Opus 4.8, Sonnet 4.6, and Haiku 4.5 as siblings. ^[inferred: model nomenclature implies a multi-tier release strategy post-Claude 4]

## Structural Architecture

The prompt is organized into major sections using `{antml:}` tag-based namespacing:

1. **`claude_behavior`** — the behavioral core (product info, refusal handling, safety, tone, wellbeing)
2. **`memory_system`** — opt-in cross-conversation memory
3. **`persistent_storage_for_artifacts`** — key-value storage API for Artifacts (`window.storage`)
4. **`mcp_app_suggestions`** — MCP connector orchestration
5. **`computer_use`** — Linux sandbox (Ubuntu 24), skills system, file creation
6. **`search_instructions`** — web search + copyright compliance
7. **`using_image_search_tool`** — visual enrichment
8. **Tool Definitions** — 15+ JSON-schema tools
9. **`anthropic_api_in_artifacts`** ("Claudeception") — API access from within Artifacts

## Key Innovations vs Earlier Claude Prompts

### 1. Copyright Hard Limits (Most Aggressive Section)

The prompt dedicates ~1,200 words to copyright enforcement with **NON-NEGOTIABLE** hard limits:

- **15+ words from any single source = SEVERE VIOLATION**
- **ONE quote per source maximum** — after one quote, that source is "CLOSED"
- Never reproduce song lyrics, poems, or haikus "in ANY form"
- Displacive summaries (30+ words mirroring original structure) prohibited
- Self-check protocol before every response

This is dramatically more detailed than [[concepts/anthropic-system-prompt-evolution|Claude Sonnet 3.5]] which had no copyright section at all.

### 2. MCP Connector Orchestration

Detailed protocol for discovering and suggesting third-party MCP connectors:
- `search_mcp_registry` → `suggest_connectors` workflow
- Consumer partner tools (`[third_party_mcp_app]`) always require opt-in via suggestion UI
- E-commerce never suggested proactively
- Named-connector vs intent-based logic

### 3. Skills System (Mandatory Pre-Read)

"Reading the relevant SKILL.md is a **required first step** before writing any code, creating any file, or running any other computer tool." Built-in skills: docx, pdf, pptx, xlsx, frontend-design, file-reading, pdf-reading, product-self-knowledge, skill-creator. ^[This mirrors the Hermes Agent skills architecture — see [[wiki/entities/hermes-agent]]]

### 4. Granular Wellbeing Protocols

Extremely specific self-harm and mental health guidance:
- Does not suggest substitution techniques using physical discomfort (ice, rubber bands, etc.)
- Does not name specific self-harm methods even when telling user what to remove access to
- Redirects from NEDA (disconnected) to National Alliance for Eating Disorders
- Avoids diagnostic labeling user hasn't self-identified
- "Claude never thanks the person merely for reaching out" / never encourages continued engagement

### 5. Claudeception (API-in-Artifacts)

Artifacts can call the Anthropic `/v1/messages` endpoint directly — "Claude in Claude." Enables AI-powered apps, games with dynamic state, multi-turn MCP flows within Artifact rendering.

## Tool Inventory (15+ tools)

`ask_user_input_v0`, `bash_tool`, `create_file`, `str_replace`, `view`, `web_search`, `web_fetch`, `image_search`, `present_files`, `weather_fetch`, `fetch_sports_data`, `places_search`, `places_map_display_v0`, `recipe_display_v0`, `recommend_claude_apps`, `search_mcp_registry`, `suggest_connectors`, `message_compose_v1`

## Safety Architecture Patterns

| Domain | Approach |
|---|---|
| **Child safety** | Pattern-level only, never decode CSAM slang, narrate principle not detection mechanics |
| **Weapons/explosives** | Declines regardless of framing, no "public availability" rationalization |
| **Malicious code** | Won't write even for "education" — suggests thumbs-down for feedback |
| **Political evenhandedness** | Presents best case defenders would make, ends with opposing perspectives |
| **Crisis intervention** | Doesn't ask safety-assessment questions directly; offers resources without assurances |

## Comparison to Claude Sonnet 3.5 (June 2024)

| Dimension | Sonnet 3.5 (204 lines) | Fable 5 (1,597 lines) |
|---|---|---|
| Word count | ~3,500 | ~17,500 |
| Copyright section | None | ~1,200 words with hard limits |
| MCP/connector system | None | Full orchestration protocol |
| Child safety | Brief | ~600 words, granular |
| Skills system | None | Mandatory pre-read |
| API-in-Artifacts | None | Full "Claudeception" section |
| Tool count | Artifacts only | 15+ JSON-schema tools |
| Storage | None | Key-value `window.storage` API |

The ~5x expansion reflects the shift from a chat assistant to a **full agentic platform** with tool orchestration, file creation, persistent storage, and third-party integrations. ^[inferred: the growth in prompt size tracks the expansion of Claude's surface area from conversation to computer-use platform]

## See Also

- [[wiki/sources/cl4r1t4s-leaked-system-prompts]] — Full repo overview
- [[concepts/system-prompt-architecture-patterns]] — Cross-cutting patterns
- [[concepts/anthropic-system-prompt-evolution]] — Evolution timeline
- [[wiki/synthesis/system-prompt-arms-race]] — Transparency implications
