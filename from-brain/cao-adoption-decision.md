---
type: note
title: Cao Adoption Decision
related:
  - symphony
  - queue
  - autoresearch-curation
  - autoresearch-pattern
ingested_via: put_page
ingested_at: '2026-06-30T07:09:04.713Z'
source_kind: put_page
tags:
  - architecture
  - cao
  - migration
  - orchestration
  - queue
created: 2026-06-30
---
# Architecture Decision: Adopt CAO, Keep Queue Layer

**Date:** 2026-06-29
**Status:** Decided
**Decision:** Adopt AWS CLI Agent Orchestrator (CAO) v2.2.0 as the multi-agent execution layer, while retaining our Hermes queue as the task planning layer and the autoresearch-curation skill for periodic sweeps.

---

## Context

We have three systems that overlap:

| System | What It Does | Why We Built It |
|--------|-------------|----------------|
| **Symphony** | Multi-agent orchestration (6 agents, 15 assignees, Hermes bridges) | Coordinate coding agents |
| **Hermes Queue** | SQLite-backed task queue (enqueue → claim → lease → complete) | Persistent task tracking with HITL workflow |
| **Kanban board-server** | Web dashboard for queue state (:8799) | Visual task management |

CAO (v2.2.0, AWS Labs) offers a more mature version of Symphony's orchestration layer with:
- 11+ agent providers (including Hermes, Claude Code, Codex, Gemini, OpenCode, Antigravity)
- MCP-native orchestration primitives (handoff, assign, send_message)
- tmux session isolation (real PTY, human-attachable)
- Built-in Web UI (React dashboard + agent view + event stream)
- REST API (FastAPI on :9889)
- Cross-provider mixing (Hermes + Claude + Codex in one session)
- Event-driven architecture with pub/sub event bus
- Plugin system (Discord, webhooks)
- Apache 2.0 license
- 300+ test files

## Decision

### Keep
1. **Hermes Queue** (`~/.hermes/queue/`) — Task planning layer. Enqueue, claim, complete, skip. The queue is the source of truth for what work exists and its status.
2. **Queue Router** (`queue-router.py`) — Auto-dispatches queue tasks to the appropriate agent. Will route to CAO agent profiles.
3. **Autoresearch-curation skill** — Periodic evidence sweeps for awesome-autoresearch. Independent of orchestration.

### Replace with CAO
1. **Symphony** — CAO provides better cross-provider orchestration, tmux isolation, and MCP-native communication.
2. **Kanban board-server** — CAO's built-in Web UI provides dashboard, agent view, and event stream.

### Integration Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        User / Hermes                          │
│                         (main session)                        │
└────────────────────────┬─────────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
    ┌─────▼──────┐              ┌──────▼──────┐
    │ Queue       │              │ CAO MCP     │
    │ (task plan) │              │ Server      │
    │ enqueue→    │              │ orchestrator│
    │ claim→done  │              │             │
    └─────┬──────┘              └──────┬───────┘
          │                            │
          └──────────┬─────────────────┘
                     │
          ┌──────────▼──────────┐
          │  Queue Router        │
          │  maps task tags →    │
          │  CAO agent profiles  │
          └──────────┬──────────┘
                     │
            ┌────────▼────────┐
            │  CAO Session     │
            │  (tmux-managed)  │
            ├─────────────────┤
            │  handoff: Claude │
            │  assign: OpenCode│
            │  assign: Goose   │
            │  send: Hermes    │
            └─────────────────┘
```

## CAO Agent Profiles (our agents mapped)

| Agent | CAO Provider | Profile | Hermes Integration |
|-------|-------------|---------|-------------------|
| Claude Code | claude_code | `claude_developer` | MCP tools via cao-mcp |
| OpenCode | opencode_cli | `opencode_developer` | MCP tools via cao-mcp |
| Goose | goose | `goose_worker` | Custom provider? |
| Mimo | mimo | `mimo_worker` | Custom provider? |
| Antigravity | antigravity_cli | `agy_researcher` | Native CAO support |

*Note: Goose and Mimo may need custom CAO providers if not in tree.*

## Timeline

1. Install CAO and verify it runs
2. Configure cao-mcp-server in Hermes profile
3. Create agent profiles for our agents
4. Test: CAO launch with each agent
5. Test: Queue → Router → CAO integration
6. Migrate Symphony workflows → CAO profiles
7. Sunset kanban board-server → CAO Web UI
8. Document for future sessions

## Risks

| Risk | Mitigation |
|------|-----------|
| Goose/Mimo not in CAO provider tree | Use Hermes wrapper (Hermes runs them, CAO orchestrates Hermes) |
| tmux 3.3+ required | Already installed on macOS 26.1 |
| Python 3.10+ needed | uv-managed Python 3.11 works |
| CAO is Beta (v2.2.0) | Well-tested, AWS-backed, active development |
| Network boundary for queue integration | Queue and CAO both local; integration via shell/MCP |

## References
- https://github.com/awslabs/cli-agent-orchestrator
- `~/.hermes/queue/` — our queue implementation
- `wiki/sources/awesome-autoresearch.md` — curated list
- `~/.hermes/skills/research/autoresearch-curation/` — curation skill
