---
date: 2026-08-02
type: concept
title: Agent Self Knowledge
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- Skills
- Self-Awareness
- Capabilities
- Agent-Behavior
- software-development
sources:
- hermes://skill/agent-self-knowledge
description: Check own skills before claiming capabilities or limitations.
---

# Agent Self Knowledge

> Check own skills before claiming capabilities or limitations.

## Overview

- **When to Use** — - User asks "can you do X?" or "do you have a skill for Y?" - User asks "look through your skills" or "what can you generate?" - User mentions a tool/skill name and asks if you have it - About to claim a capability limitation - User says "you should know this" or expresses frustration about forgotten capabilities
- **How to Run** — 1. Run `skills_list(category)` for the relevant category — or `skills_list()` with no category to see all 2. If a matching skill exists, run `skill_view(name)` to confirm it covers the capability 3. THEN answer the user with what you actually found
- **Procedure** — 1. **Trigger detection**: Any question about capabilities, tools, or "can you..." 2. **Category scan**: `skills_list(category)` for the domain (mlops, research, productivity, etc.) 3. **Deep check**: If a skill name looks relevant, `skill_view(name)` to read its full content 4. **Answer with evidence**: "Yes, I have `notebooklm-cli` which supports [specific commands]" — not "I think I might have something"

## Further detail

### Pitfalls

- **Fabricating capability gaps is worse than admitting ignorance.** Saying "I don't have NotebookLM skills" when 4 exist destroys trust. The fix is mechanical: check `skills_list` first. - **`skill_manage` patches are blocked on most skills.** Skills with `created_by=None` (which includes most manually-authored and even some agent-created skills) are off-limits to autonomous patching. Route fixes via memory or create new umbrella skills. - **Memory captures user preferences; skills capture task procedures.** "User prefers concise output" → memory. "Always run skills_list before answering capa

### Verification

After answering a capability question, verify your answer by checking:

### Session Provenance

Created 2026-07-20. Session had agent claim 3 times it lacked NotebookLM capabilities despite having 4 NLM skills. User: "this model is quite forgettable and doesn't like following instructions." Also: "Look through your skills" (asked 3 times). Also: "What does my soul say?" — agent gave philosophical rambling instead of reading SOUL.md. The root cause was skipping the check-then-answer pattern.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/agent-self-knowledge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
