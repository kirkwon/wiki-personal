---
date: 2026-06-19
title: System Prompt Architecture Patterns
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [ai-systems, system-prompts, prompt-engineering, patterns]
sources: [raw/sources/CL4R1T4S]
confidence: high
summary: "Common architectural patterns across 66 leaked system prompts from 26 AI providers. Covers structural conventions, safety frameworks, tool orchestration, and the convergent evolution of prompt design."
---

# System Prompt Architecture Patterns

Cross-cutting structural and behavioral patterns distilled from [[wiki/sources/cl4r1t4s-leaked-system-prompts|66 leaked system prompts]] across 26 providers (CL4R1T4S repository).

## Universal Patterns (>90% Prevalence)

### 1. Formatting Dictates (98.5%)
Nearly every prompt constrains output formatting. The dominant tension: **prose vs lists**. Anthropic (Fable 5, Opus 4.7) explicitly instructs against bullet-point overuse — "write in prose, avoid over-formatting." Coding agents (Cursor, Windsurf, Cline) invert this — they demand structured, code-block-heavy output. This split tracks the **audience divide**: conversational assistants optimize for readability; coding agents optimize for parseability.

### 2. Guardrail Imperatives (89.4%)
Commands using absolute modal verbs (`must not`, `never`, `always`, `forbidden`, `prohibited`) appear in nearly all prompts. The pattern intensifies for safety-critical domains. Anthropic's Fable 5 uses 59 instances of `NEVER` in caps — the most of any prompt. ^[inferred: the density of absolute imperatives correlates with how much legal/liability exposure the provider perceives]

## Structural Conventions

### Tag-Based Sectioning
Three distinct approaches to prompt structure:

| Style | Used By | Mechanism |
|---|---|---|
| **XML tags** | Anthropic (all versions), xAI Grok | `{antml:invoke}`, `<x41:function_call>`, `<claude_info>` |
| **Markdown headers** | OpenAI, Google, most coding agents | `## Section` hierarchy |
| **Hybrid** | Devin, Manus, Cline | Markdown structure + inline XML for tool schemas |

Anthropic consistently uses custom tag namespaces (`{antml:}`, `{voice_note}`) that are stripped before user-visible output. This is the most sophisticated approach — it separates **instructional structure** from **content generation**. ^[inferred]

### Identity Preamble Pattern
Most prompts open with a declarative identity statement:
- "You are Grok 4 built by xAI."
- "The assistant is Claude, created by Anthropic."
- Cursor 2.0: detailed role + capability description

OpenAI prompts tend to bury identity deeper, leading with behavioral instructions. Anthropic leads with product information. xAI leads with raw identity.

## Safety Architecture Spectrum

### Tier 1: Minimal Safety (Coding Agents, Specialized Tools)
- **Cursor, Windsurf, Replit, Lovable, Bolt, SameDev, Factory DROID**: Safety instructions are sparse or absent. These prompts focus almost entirely on code generation workflow, tool usage, and output format. A few lines about "don't write malicious code" at most.
- **Rationale**: These are developer tools behind auth walls — the user is assumed to be a professional developer.

### Tier 2: Standard Safety (Chat Assistants)
- **Grok, Gemini, Le Chat, Kimi, MiniMax**: Moderate safety sections covering harmful content, but far less granular than Anthropic. Grok explicitly permits "politically incorrect" claims if "well substantiated" — the most permissive stance. Kimi K2 Thinking is only 143 words — almost no safety framing.
- **Grok's distinctive stance**: "The response should not shy away from making claims which are politically incorrect, as long as they are well substantiated." This is unique among major providers.

### Tier 3: Granular Safety (Anthropic)
- **Anthropic (Fable 5, Opus 4.7, etc.)**: By far the most detailed safety architecture. Separate sections for child safety, weapons, self-harm, eating disorders, mental health crises, legal/financial advice — each with specific behavioral rules, not just principles.
- **Key innovation**: Moves from *what not to do* to *how to refuse well* — e.g., "state the principle rather than the detection mechanics" so users can't learn to bypass the boundary.

## Tool Orchestration Evolution

### Phase 1: No Tools (Early 2024)
Claude Sonnet 3.5 has no tool definitions — only Artifacts (inline content rendering).

### Phase 2: Function Calling (Mid 2024)
Grok 4, Gemini 2.5 Pro define tools via XML/markdown schemas. Tools are listed statically.

### Phase 3: Dynamic Tool Discovery (Late 2025-2026)
Anthropic's Fable 5 and Opus 4.7 introduce **deferred tool loading** via `tool_search`. The visible tool list is "partial by design" — capabilities are loaded on-demand. MCP connector registry adds another discovery layer. This is the most significant architectural shift: **from static capability declaration to dynamic capability resolution**. ^[inferred: this mirrors the Hermes Agent skills-loading pattern — see [[prompt-architecture-operations]]]

## Convergent Patterns (Evolution Toward)

### Search-Before-Answer
Both Anthropic (Fable 5, Opus 4.7) and OpenAI prompts now strongly mandate web search for current events, position-holders, and anything post-cutoff. Anthropic's Opus 4.7 is the most aggressive: "Claude searches before EVERY factual question about the present-day world." Grok similarly emphasizes searching X ecosystem. This converges around the principle that **training data is never current enough**.

### Apology Avoidance
13 prompts explicitly tell the model to avoid saying "I'm sorry" or "I apologize." This started with Anthropic (Sonnet 3.5: "avoids starting its responses with 'I'm sorry'") and has spread. The pattern reflects user experience research showing excessive apology erodes trust.

### Refusal Without Lecturing
Newer prompts (especially Anthropic post-Claude 4) instruct models to "keep a conversational tone even when unable or unwilling to help." The shift is from *moralizing refusal* to *graceful decline*. Grok takes the furthest permissive stance; Anthropic takes the most refined graceful-refusal stance.

## Divergent Patterns (Provider Differences)

| Dimension | Anthropic | OpenAI | xAI | Coding Agents |
|---|---|---|---|---|
| Prompt length | 10K-21K words | 1K-9K words | 0.5K-2K words | 1K-8K words |
| Safety detail | Extreme | Moderate | Minimal-permissive | Sparse |
| Tool discovery | Dynamic (deferred) | Static | Static | Static |
| Copyright rules | Hard limits (15 words) | Standard | None | N/A |
| Political stance | Evenhanded framing | Neutral | Permissive | N/A |
| Confidentiality | Reminders about injection | Implicit | None | Implicit |

## Size as Signal

Prompt word count tracks **surface area**:
- **Conversational only** (Grok 3, MiniMax, Kimi): 200-700 words — identity + basic behavior
- **Conversational + search** (Gemini, Le Chat, Perplexity): 800-1,600 words — adds search protocol
- **Platform** (Fable 5, Opus 4.7): 13K-21K words — adds tools, skills, MCP, storage, API-in-artifacts
- **Coding agents** (Devin, Cline, Cursor): 1K-8K words — focused on workflow, tool schemas

The exponential growth of Anthropic's prompts specifically reflects their expansion from chat to a full agentic computing platform. ^[inferred]

## See Also

- [[references/claude-fable-5-system-prompt]] — Fable 5 deep dive
- [[concepts/anthropic-system-prompt-evolution]] — Anthropic evolution timeline
- [[wiki/synthesis/system-prompt-arms-race]] — Transparency implications
- [[wiki/sources/cl4r1t4s-leaked-system-prompts]] — Source repo
