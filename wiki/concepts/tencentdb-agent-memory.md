---
type: concept
title: TencentDB Agent Memory - Local Agent Memory System
source: Twitter thread @thesupermanmx status 2082513702587445595
ingested_via: put_page
ingested_at: '2026-07-30T06:18:42.314Z'
source_kind: put_page
tags:
  - agent-memory
  - local-ai
  - memory-system
  - open-source
  - tencent
created: 2026-07-30
provenance: brain/ (retired 2026-09-13)
---
# TencentDB Agent Memory

A fully local, open-source memory system for AI agents that provides human-like long-term recall without cloud dependencies or API costs.

## Key Claims from Announcement
- **61.38% fewer tokens per session** - Dramatic reduction in token usage
- **76% persona accuracy** (up from 48%) - Significantly improved consistency in agent personality/behavior
- **51.52% higher task success rate** - Substantial improvement in task completion effectiveness
- **Works with any agent** - Agnostic to underlying LLM or agent framework
- **100% Open Source** - MIT or similar license implied

## Core Architecture: Four Memory Types
1. **Chat Memory** - Conversation history and contextual awareness
2. **Skill** - Reusable agent capabilities and procedures  
3. **LLM-Wiki** - Structured knowledge base (similar to our gbrain concept)
4. **Code-Graph** - Structural understanding of codebases

## Relevance to Our System
This represents a convergent evolution with our gbrain + Hermes skill system approach, validating the architectural choices.
