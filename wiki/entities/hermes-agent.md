---
type: entity
title: Hermes Agent
description: "Hermes Agent (by Nous Research) is an advanced AI agent framework designed for autonomous, multi-session task execution."
created: 2026-06-15
updated: 2026-06-15
tags: [ai, tool, agent, automation]
sources: [hermes-sessions]
---

# Hermes Agent

**Hermes Agent** (by Nous Research) is an advanced AI agent framework designed for autonomous, multi-session task execution. It serves as the primary AI assistant in Kirk's workflow — a "Bayesian Rogue" that operates across Telegram, TUI, and CLI interfaces, managing everything from one-shot coding tasks to persistent cron-driven maintenance pipelines.

## Architecture Overview

Hermes runs as a local agent on macOS, connecting to a model provider via a Headroom proxy on `:8787`. The default model is `deepseek-v4-flash` (provider: DeepSeek). It supports fallback providers (Ollama, OpenRouter) and a wide range of auxiliary services (vision, web extraction, TTS, STT, compression).

Key configuration lives at:
- **Global config:** `~/.hermes/config.yaml`
- **Profile configs:** `~/.hermes/profiles/<name>/config.yaml`
- **Sessions:** `~/.hermes/sessions/sessions.json`
- **Cron jobs:** `~/.hermes/cron/jobs.json`

## Profiles

Hermes supports **runtime profiles** — configuration bundles that change the agent's behavior, toolset, and resource limits. Each profile lives under `~/.hermes/profiles/<name>/` with its own `config.yaml`, optional skills/ and memories/ directories.

### Active Profiles

| Profile | Model | Toolsets | Delegation | Purpose |
|---|---|---|---|---|
| **backend_developer** | deepseek-v4-flash | terminal, file, web, delegation | orchestrator, 3 children | Main coding agent |
| **systemarchitect** | deepseek-v4-flash | terminal, file, web, delegation, browser | orchestrator, 2 children | Architecture & design |
| **businessanalyst** | deepseek-v4-flash | web, file, search | no orchestrator | Research & analysis |
| **technicalwriter** | deepseek-v4-flash | file, web, search (no terminal) | 1 child | Documentation |
| **projectmanager** | deepseek-v4-flash | web, file, delegation, cronjob (no terminal) | orchestrator | Coordination |
| **qualityassuranceengineer** | deepseek-v4-flash | terminal, file, web, delegation | orchestrator, 3 children, reasoning:high | Testing & validation |
| **web_content_retriever** | deepseek-v4-flash | web, file, search (no terminal) | no orchestrator | Web scraping |
| **wittgenstein** | openrouter/owl-alpha | hermes-cli, web | orchestrator | Philosophical mode |

Profiles can override: model, provider, context length, toolset access, delegation depth, memory limits, terminal backend, and personality presets.

## Identity & Persona

The agent's active identity is stored in `~/.hermes/memories/MEMORY.md`:

> **User: Kirk Won. Bayesian Rogue.**
> Work: Explore → Sieve → Exploit, concrete plans, SHA256 verify, Telegram docs, no hand-holding. Likes methodological frameworks.

This memory is loaded on every session start via the memory() tool (Tier 1 / hot memory). The system prompt defaults to a Kantian personality ("Act only according to that maxim...") with 22+ alternate personalities available (laozi, chef, detective, strategist, socrates, etc.).

## Coding CLI Delegation Pattern

Hermes uses a **subagent delegation** system for complex multi-step tasks:

1. **Orchestrator mode** (`orchestrator_enabled: true`) — the parent agent spawns child subagents to work in parallel
2. **Default toolsets** passed to children: terminal, file, web
3. **Concurrency limit**: typically 2–3 children per parent
4. **Max spawn depth**: 1 (children cannot spawn grandchildren)
5. **Child timeout**: 600s (10 minutes) per child

The delegation toolset (`toolsets: [delegation]`) enables `delegate_task()` which spawns independent agents with their own context windows. This is the primary pattern for:
- Parallel coding tasks (refactor + test + document simultaneously)
- Research across multiple sources
- Breaking large tasks into independent work units

## Skills System

Skills are reusable, versioned instruction bundles that teach the agent how to perform specific workflows. They live under `~/.hermes/skills/<domain>/<skill-name>/`.

### Installed Skills

- **knowledge-management/gbrain-operations** — GBrain maintenance, cron templates
- **productivity/portfolio-analyzer** — Financial portfolio analysis with templates
- **autoresearch/experiments/rag-retrieval-opt** — RAG optimization experiments
- **mlops/inference/obliteratus** — ML model ablation experiments

Skills use YAML template files (e.g., `templates/cron-weekly-maintenance.yaml`) and can be invoked via cron job configurations. Each skill can define: system prompts, tool requirements, template variables, and output contracts.

## Memory Layers (Tiered Architecture)

Kirk's Hermes uses a **4-tier memory system** to manage context efficiently:

### Tier 1 — Hot Memory (memory() tool)
- In-session tool call for immediate facts
- Character limit: 2,200 chars
- `flush_min_turns: 6` — automatically flushed to warm tier after 6 turns of inactivity
- Stored in `~/.hermes/memories/MEMORY.md`

### Tier 2 — Warm Memory (MEMORY.md)
- `~/.hermes/MEMORY.md` — loaded on every session start (via AGENTS.md reference)
- Contains recent work (last ~2 weeks) and cross-session facts
- Content older than 2 weeks archived to GBrain
- Also per-profile: `~/.hermes/profiles/<name>/memories/MEMORY.md`

### Tier 3 — Cool Memory (File Logs)
- **Curator logs:** `~/.hermes/logs/curator/*/REPORT.md` — weekly curation reports
- **Cron output:** `~/.hermes/cron/output/<job-id>/*.md` — job execution logs
- **Conversation review logs:** `~/.hermes/conversation-logs/reviews/` — weekly review files
- **DECISIONS.md:** `~/.hermes/conversation-logs/DECISIONS.md` — persistent decision ledger

### Tier 4 — Cold Memory (GBrain)
- **GBrain:** a vector/knowledge-base database at `~/.hermes/gbrain/`
- ~19K pages, version 0.41.14.0
- Accessed via `gbrain-*` shell scripts (sync, update-check, health-check, backup, dream-cycle)
- Long-term archival for historical session data and stale warm memory entries

## Cron Infrastructure

Hermes has a built-in **cron daemon** that schedules and executes recurring jobs. Jobs are defined in `~/.hermes/cron/jobs.json`.

### Active Cron Jobs

| Job | Schedule | Type | Last Status |
|---|---|---|---|
| Weekly Conversation Review | Sun 21:00 | Agent prompt | OK (11 runs) |
| GBrain Live Sync | Daily 03:00 | Shell script (no agent) | OK (745 runs) |
| GBrain Daily Update Check | Daily 09:00 | Shell script (no agent) | OK (43 runs) |
| GBrain Weekly Health Check | Mon 06:00 | Shell script (PAUSED) | OK (6 runs) |
| weekly-vault-defrag | Mon 09:00 | Agent prompt (defrag skill) | Error (7 runs) |
| GBrain Daily Backup | Daily 03:00 | Shell script (no agent) | Error (39 runs) |
| gbrain-nightly-dream | Daily 02:00 | Shell script (no agent) | Error (44 runs) |
| gbrain-weekly-health | Mon 06:00 | Shell script (no agent) | OK (10 runs) |
| LLm-wiki → GBrain delta sync | Every 180m | Shell script (no agent) | OK (385 runs) |
| Update AI/ML Notebook | Daily 06:00 | Shell script (no agent) | OK (41 runs) |
| Token Optimization Daily Report | Daily 06:00 | Shell script (no agent) | OK (37 runs) |
| kanban-gemini-dispatch | Every 5m | Shell script (PAUSED) | OK (197 runs) |

Jobs can be:
- **Agent-based** — spawn a full Hermes agent session with a prompt
- **Script-based** (`no_agent: true`) — execute a shell script directly
- **Skill-based** — load a skill and run its workflow

Output goes to `~/.hermes/cron/output/<job-id>/<timestamp>.md`. Results can be delivered to Telegram or stored locally.

## Platforms

Hermes operates across multiple interfaces:
- **Telegram** — primary messaging platform (streaming enabled)
- **CLI/TUI** — terminal-based interaction (Interface: CLI, TUI skin: slate)
- **Discord** — secondary platform (streaming disabled)
- **Voice** — microphone input with local STT (Whisper base) and Kokoro TTS output
- **Desktop app** — Electron/React-based native client

## Web Extraction (Provider Architecture)

Hermes uses a **pluggable web provider system** with per-capability routing (search vs. extract can use different backends). See [[concepts/web-extraction-provider-architecture]].

| Backend | Type | Search | Extract | Cost | Status |
|---|---|---|---|---|---|
| Firecrawl | Cloud | ✅ | ✅ | Credits | Active (search) |
| [[entities/crawl4ai]] | Local | ❌ | ✅ | **Free** | **Active (extract)** |
| [[entities/scrapegraphai]] | Local | ❌ | ✅ | **Free** (Ollama) | Available |
| DDGS | Local | ✅ | ❌ | Free | Available |
| Tavily/Exa/Brave | Cloud | ✅ | ✅ | Credits | Available |

Config: `web.backend: firecrawl` (search) + `web.extract_backend: crawl4ai` (extract). Switch extract backend without code changes via `hermes config set web.extract_backend <name>`.

**Architectural change (2026-06-21):** Added Crawl4AI + ScrapeGraphAI as extract-only backends. This eliminates the Firecrawl credit dependency for content extraction — all `web_extract` calls now run locally, free. See [[concepts/web-extraction-provider-architecture]].

## Related

- [[entities/hermes-skill]] — Skill system definition
- [[entities/gbrain]] — Cold storage knowledge base
- [[entities/headroom]] — Session compression proxy
- [[concepts/web-extraction-provider-architecture]] — Web extraction plugin system
- [[entities/crawl4ai]] — Free local extraction backend
- [[entities/scrapegraphai]] — LLM-powered extraction backend
