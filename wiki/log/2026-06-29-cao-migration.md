---
date: 2026-06-30

type: log
tags: [cao, orchestration, migration, process]
related: [cao-adoption-2026-06-29]
---

# Migration: Adopt CAO, Keep Queue + Autoresearch

**Date:** 2026-06-29
**Duration:** ~45 min
**Decision:** `wiki/decisions/cao-adoption-2026-06-29.md`

---

## What was done

### 1. Decision document
Created `wiki/decisions/cao-adoption-2026-06-29.md` — architecture decision to adopt CAO as execution layer while retaining Hermes Queue (task planner) and autoresearch-curation skill.

### 2. CAO installation
```bash
uv tool install git+https://github.com/awslabs/cli-agent-orchestrator.git@main --upgrade
```
Installed v2.2.0 with 4 executables:
- `cao` — CLI for session management
- `cao-mcp-server` — MCP server for agent orchestration
- `cao-ops-mcp-server` — Operations MCP server
- `cao-server` — REST API + Web UI server (FastAPI on :9889)

### 3. Prerequisites installed
- `tmux 3.7` via Homebrew (CAO requires 3.3+)
- CAO database initialized (`cao init`)
- Built-in agents installed: `developer`, `code_supervisor`

### 4. Hermes config updated
Added `cao-mcp-server` to `~/.hermes/config.yaml` MCP servers:
```yaml
  cao-mcp-server:
    enabled: true
    command: cao-mcp-server
    env:
      CAO_TERMINAL_ID: ${CAO_TERMINAL_ID}
```

### 5. Agent profiles created (4)
Installed via `cao install /path/to/profile.md`:

| Profile | Provider | Role | Purpose |
|---------|----------|------|---------|
| `hermes_supervisor` | hermes | supervisor | Coordinates workers via CAO MCP tools |
| `claude_developer` | claude_code | developer | Complex refactoring, backend, architecture |
| `opencode_worker` | opencode_cli | worker | Frontend, review, general implementation |
| `agy_researcher` | antigravity_cli | worker | Prototyping, research, data analysis |

### 6. Testing results

| Test | Provider | Result | Notes |
|------|----------|--------|-------|
| `cao launch` with Hermes | hermes | ✅ | Full cycle: prompt → reason → exec → output → idle |
| `cao launch` with Claude Code | claude_code | ⚠️ | Session created but timed out at 30s (needs longer init) |
| Queue functionality | — | ✅ | `queue list` shows 5 completed tasks, independent of CAO |

### 7. Verification: Hermes in CAO tmux session
The running Hermes session inside CAO's tmux correctly:
- Received the launch prompt
- Reasoned about the task autonomously
- Executed `echo "CAO test: hello from orchestrated agent"`
- Produced output: "CAO test: hello from orchestrated agent"
- Returned to idle state

## Integration Architecture (Final)

```
┌──────────────────────────────────────┐
│       User ↔ Hermes (main session)    │
│         (cao-mcp-server enabled)       │
└────────────┬─────────────────────────┘
             │
    ┌────────┴────────┐
    │ Queue (planner) │    CAO MCP Server
    │ enqueue→claim→  │    handoff/assign/
    │ complete/skip   │    send_message
    └────────┬────────┘    └────────────┘
             │                  │
    ┌────────┴──────────────────┘
    │    Queue Router
    │    maps tags → CAO profiles
    └────────┬──────────────────┐
             │                  │
    ┌────────┴────────┐  ┌─────┴──────────┐
    │ CAO Session      │  │ CAO Server     │
    │ (tmux-managed)   │  │ (REST :9889)   │
    │ hermes_supervisor │  │ Web UI        │
    │ → handoff: claude  │  │ Dashboard     │
    │ → assign: opencode│  └────────────────┘
    │ → assign: agy     │
    └──────────────────┘
```

## What was preserved
- **Hermes Queue** (`~/.hermes/queue/`) — fully operational
- **Queue Router** (`queue-router.py`) — no changes needed
- **Autoresearch-curation skill** — independent of orchestration
- **Existing MCP servers** (brave-search, github, etc.) — untouched

## What changes next
1. **Longer timeout for Claude Code** — the 30s CAO timeout needs adjustment
2. **Queue → CAO bridge** — route queue tasks through CAO profiles
3. **Sunset kanban board-server** when CAO Web UI proves sufficient
4. **Tune Hermes supervisor** profile with more detailed worker instructions
