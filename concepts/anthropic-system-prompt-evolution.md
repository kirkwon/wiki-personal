---
date: 2026-06-19
title: Anthropic System Prompt Evolution (3.5 → Fable 5)
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [ai-systems, system-prompts, anthropic, claude, evolution]
sources: [raw/sources/CL4R1T4S/ANTHROPIC]
confidence: high
summary: "Evolution of Anthropic's Claude system prompts from Sonnet 3.5 (June 2024, 3.5K words) to Fable 5 (June 2026, 17.5K words). Tracks the shift from chat assistant to agentic platform, with safety granularity, tool discovery, and copyright hard limits as key inflection points."
---

# Anthropic System Prompt Evolution (3.5 → Fable 5)

12 leaked Anthropic prompts from [[wiki/sources/cl4r1t4s-leaked-system-prompts|CL4R1T4S]] spanning Claude Sonnet 3.5 (June 2024) through Fable 5 (June 2026), totaling 121K words — the largest corpus of any provider.

## Evolution Timeline

| Version | Approx. Date | Words | Key Inflection |
|---|---|---|---|
| Sonnet 3.5 | Jun 2024 | ~3,500 | Artifacts system, apology avoidance |
| Sonnet 3.7 (New) | ~Late 2024 | ~9,600 | Expanded refusal handling, tool_use basics |
| Claude 4 | ~Early 2025 | ~9,700 | Default-to-help stance, structured XML |
| Claude 4.1 | ~Mid 2025 | ~8,900 | Refined tone/formatting, search-first hints |
| Claude 4.5 Opus | ~Mid 2025 | ~13,200 | Search-before-everything, granular wellbeing |
| Sonnet 4.5 (Sep 2025) | Sep 2025 | ~13,000 | Tool discovery (deferred loading) |
| Opus 4.6 | ~Early 2026 | ~14,200 | MCP connectors, skills pre-read mandate |
| Opus 4.7 | ~Apr 2026 | ~21,200 | "searches before EVERY factual question", API-in-Artifacts |
| **Fable 5** | **Jun 2026** | **~17,500** | **Mythos tier, copyright hard limits, Claudeception** |

## Phase 1: Chat Assistant (Sonnet 3.5, Jun 2024)

The earliest leaked prompt is remarkably lean — 204 lines, no tool definitions beyond Artifacts. Key features:
- **Artifacts system**: Inline content rendering (code, HTML, SVG, React, Mermaid)
- **Apology avoidance**: First to explicitly instruct against "I'm sorry" openers
- **Hallucination awareness**: Uses the term "hallucinate" to describe potential errors
- **No web search**: "Claude cannot open URLs" — entirely training-data-dependent
- **No copyright section**: No IP protection language at all

The Sonnet 3.5 prompt is the baseline — a pure conversational assistant with creative output capabilities.

## Phase 2: Tool Integration (Sonnet 3.7 → Claude 4.1, Late 2024 - Mid 2025)

The major shift: **web search arrives**. Claude moves from "cannot open URLs" to proactive search behavior.
- **Default-to-help** stance emerges (Claude 4): "Claude defaults to helping. Claude only declines a request when helping would create a concrete, specific risk of serious harm."
- **Structured XML namespacing**: `{claude_behavior}`, `{refusal_handling}`, `{tone_and_formatting}` — section tags that organize the prompt modularly
- **Tone refinement**: Emojis regulated ("does not use emojis unless the person asks"), emote/asterisk actions discouraged
- **Wellbeing section expands**: Specific self-harm substitution technique prohibitions (ice, rubber bands)

## Phase 3: Search-First Doctrine (Claude 4.5 Opus, Mid 2025)

The most aggressive search mandate in any AI prompt:
- "Claude searches before EVERY factual question about the present-day world"
- "Claude's confidence on topics is not an excuse to skip search"
- Position-holders, prices, laws — all require search regardless of training confidence

This reflects a philosophical shift: **the model's own confidence is downgraded as a reliable signal**. ^[inferred: this addresses the hallucination problem by defaulting to external verification rather than self-assessment]

## Phase 4: Agentic Platform (Sonnet 4.5 → Opus 4.6, Late 2025 - Early 2026)

Three architectural revolutions:

### Dynamic Tool Discovery
"Many helpful tools are deferred and must be loaded via `tool_search` before use." The visible tool list becomes "partial by design." This is a **capability resolution system** — the prompt instructs the model to search for tools the way it searches for information. ^[This is architecturally identical to Hermes Agent's skill-loading pattern — see [[prompt-architecture-operations]]]

### MCP Connector Registry
External apps discoverable via `search_mcp_registry` → `suggest_connectors`. Consumer-facing partner integration with explicit opt-in protocol. The prompt becomes a **platform orchestration document**, not just behavioral instructions.

### Mandatory Skills Pre-Read
"Reading the relevant SKILL.md is a required first step before writing any code." This treats skills as **environment-specific constraint documents** that encode knowledge not in training data. ^[This is the same pattern Hermes uses — the SOUL.md mandate to "scan the skills below. If a skill matches... you MUST load it"]

## Phase 5: Mythos Tier & Hard Limits (Fable 5, Jun 2026)

### Copyright Enforcement Architecture
The single most detailed section in any AI system prompt (~1,200 words). Three absolute limits:
1. 15+ words from any source = SEVERE VIOLATION
2. One quote per source, then "CLOSED"
3. Never reproduce song lyrics, poems, haikus

This level of copyright paranoia is unique to Fable 5. Opus 4.7 (which precedes it) has standard copyright language. ^[inferred: the hard limits likely respond to specific legal pressure or litigation threat]

### Claudeception
Artifacts can now call the Anthropic API directly — AI-powered apps with stateful conversations, multi-turn MCP flows, and dynamic game states. The system prompt becomes a **developer manual** for building within Claude's ecosystem.

### Refined Refusal Architecture
Key innovation: "state the principle rather than the detection mechanics — not which cues tripped, where the line sits, or what test it applied — since narrating the boundary teaches how to reframe around it." This is **meta-safety** — safety instructions that protect the safety system itself from being reverse-engineered.

## Cross-Cutting Evolution Patterns

### Growing Specificity
Early prompts use general principles ("be helpful"). Fable 5 uses behavioral specifications ("does not suggest substitution techniques for self-harm that use physical discomfort, pain, or sensory shock (e.g., holding ice cubes, snapping rubber bands)"). Each iteration adds **edge-case coverage** learned from real-world interactions. ^[inferred: the growing detail suggests Anthropic iterates prompts based on red-teaming and production incidents]

### Modularization
The tag-based sectioning (`{section_name}`) enables **A/B testing of prompt components** — sections can be swapped without rewriting the whole prompt. By Fable 5, the structure is highly modular: 7 major sections, each independently versioned. ^[inferred]

### Identity Stability
Despite 5x growth in size, the core identity ("The assistant is Claude, created by Anthropic") remains unchanged across all versions. The personality core is stable; the behavioral periphery expands.

## See Also

- [[references/claude-fable-5-system-prompt]] — Fable 5 deep dive
- [[concepts/system-prompt-architecture-patterns]] — Cross-cutting patterns
- [[wiki/synthesis/system-prompt-arms-race]] — Transparency implications
- [[wiki/sources/cl4r1t4s-leaked-system-prompts]] — Source repo
