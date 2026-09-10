---
date: 2026-07-19
type: concept
title: Agent Self Introspection
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Self-Knowledge
- Hermes
- Introspection
- Grounding
- knowledge-management
sources:
- hermes://skill/agent-self-introspection
description: Explain your own systems from skills and live state.
---

# Agent Self Introspection

> Explain your own systems from skills and live state.

## Overview

- **When to Use** — - "Tell me about your memory system" / "how do you remember things" - "What tools do you have?" / "what providers can you use?" - "How does X work in Hermes?" (memory, skills, cron, gateway, profiles) - "What do you know about me?" (profile/memory contents) - Any question where the answer lives in Hermes internals, not the outside world
- **Prerequisites** — - `skills` toolset enabled — to call `skill_view` - The `hermes-agent` skill installed (default)
- **How to Run** — 1. Load the authoritative skill with `skill_view(name='hermes-agent')`. 2. Read the live state already in your system prompt — the **MEMORY** block and **USER PROFILE** block — for actual current contents, budgets, and capacity. 3. Cross-reference: architecture + exact keys/paths from the skill doc; actual stored facts + budget from live state. 4. Synthesize a structured answer. Be honest about gaps, capacities (e.g. "99% full"), and where one tier ends and the next begins.

## Further detail

### Quick Reference

- Authoritative skill: `hermes-agent` (load via `skill_view`) - Live state in context: `MEMORY` block (~3.5KB), `USER PROFILE` block (~2KB) - Memory tool: `memory` (target `memory` or `user`) - Session history: `session_search` - Skills directory: `~/.hermes/skills/` - CLI: `hermes memory status`, `hermes config`

### Procedure

1. Recognize the question is introspective — it concerns your own internals, not the external world. 2. Invoke `skill_view(name='hermes-agent')` to fetch ground-truth architecture BEFORE answering. 3. Scan the injected `MEMORY` and `USER PROFILE` blocks for actual current contents relevant to the question. 4. Structure the answer by layer or mechanism, citing verbatim facts (config keys, paths, budget numbers) from BOTH sources. 5. Flag any drift between parametric knowledge and the skill doc — trust the skill doc. 6. Offer to show on-disk files or tune the system rather than over-explaining u

### Pitfalls

- **Parametric drift**: remembered knowledge of Hermes internals may be outdated; the skill doc is authoritative. If they conflict, trust the skill. - **Conflating tiers**: do not blur the `memory` tool (hot facts, 3.5KB) with session transcripts (`session_search`) with GBrain (deep store) with skills (procedural). Each has a distinct role and budget. - **Skipping the skill load for informational questions**: the system prompt already mandates loading `hermes-agent` for config/troubleshoot tasks; this skill extends that mandate to informational and introspective questions, which is the easy ca

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/agent-self-introspection/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
