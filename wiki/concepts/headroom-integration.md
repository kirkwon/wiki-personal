---
type: concept
title: Headroom — Context Compression for Hermes
created: 2026-06-12
updated: 2026-06-12
tags: [concept, tooling, hermes, compression, headroom]
---

# Headroom — Context Compression for Hermes

**Installed:** 2026-06-12 via `uv`
**Version:** 0.25.0
**Location:** `~/.local/bin/headroom`
**GitHub:** https://github.com/chopratejas/headroom

---

## What It Does

Headroom sits between Hermes and the LLM provider. It **compresses tool outputs, file reads, search results, and conversation history** before they reach the model — then forwards the compressed request to the provider.

**Savings:** 60-95% token reduction on tool outputs (verified: 17.8% on search results, more on verbose content). Originals are cached and retrievable via MCP.

---

## Architecture

```
 Hermes Agent
    │  (API calls via http://127.0.0.1:8787)
    ▼
┌──────────────────────────────┐
│  Headroom Proxy (port 8787)  │  ← launchd auto-start
│  ── Compresses tool outputs  │
│  ── Caches originals (CCR)   │
│  ── Forwards to provider     │
└──────────────────────────────┘
    │
    ▼
 DeepSeek / OpenRouter / etc.

MCP Server (stdio)  →  headroom_compress, headroom_retrieve, headroom_stats
```

---

## Two Ways Compression Works

### 1. Proxy Mode (Automatic — ALL traffic)
Every API call from Hermes is compressed before it reaches the provider. No code changes needed.

**Activated by:** Setting `base_url: http://127.0.0.1:8787` in Hermes config (already done).

### 2. MCP Tools (Explicit — on demand)
The agent can call compression tools directly when it knows content is bloated.

| Tool | What it does |
|---|---|
| `headroom_compress` | Compress content, returns compressed text + hash |
| `headroom_retrieve` | Get original content by hash (CCR) |
| `headroom_stats` | Session compression statistics |

MCP tools are available as `mcp_headroom_headroom_compress` etc. in Hermes.

---

## Managing the Proxy

### Status Check
```bash
headroom-switch.sh status
# or:
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/stats       # Compression stats
curl http://127.0.0.1:8787/stats-history  # Historical savings
```

### Switch Provider
```bash
headroom-switch.sh deepseek     # Route through DeepSeek
headroom-switch.sh openrouter   # Route through OpenRouter (300+ models)
```

### Manual Start/Stop
```bash
launchctl load   ~/Library/LaunchAgents/ai.headroom.proxy.plist
launchctl unload ~/Library/LaunchAgents/ai.headroom.proxy.plist
```

### View Logs
```bash
tail -f ~/.hermes/logs/headroom-proxy.log
tail -f ~/.hermes/logs/headroom-proxy.error.log
```

---

## Savings Profile

The proxy currently uses the `agent-90` profile (90% savings target):

```bash
headroom agent-savings --profile agent-90
```

Key settings:
- `HEADROOM_COMPRESS_USER_MESSAGES=1` — also compress what the user sends
- `HEADROOM_COMPRESS_SYSTEM_MESSAGES=1` — also compress system prompts
- `HEADROOM_MIN_TOKENS_TO_CRUSH=500` — only compress blocks >500 tokens
- `HEADROOM_ACCURACY_GUARD=strict` — don't compress if accuracy might suffer

To see real savings after Hermes restart:
```bash
headroom perf --hours 24
```

---

## MCP Server

The Headroom MCP server runs on demand (stdio, spawned when Hermes connects).

### Test MCP Connection
```bash
hermes mcp test headroom
```

### MCP Config (in ~/.hermes/config.yaml)
```yaml
mcp_servers:
  headroom:
    command: headroom
    args:
      - mcp
      - serve
    enabled: true
    timeout: 120
    connect_timeout: 60
```

---

## Provider Compatibility

| Provider | Proxy Flag | Notes |
|---|---|---|
| **DeepSeek** (current) | `--openai-api-url https://api.deepseek.com` | Uses OpenAI-compatible `/v1/chat/completions` |
| **OpenRouter** | `--backend openrouter` | Routes to 300+ models through OpenRouter |
| **Anthropic Claude** | `--backend anthropic` (default) | Uses `/v1/messages` format |
| **OpenAI GPT** | `--backend openai` | Uses `/v1/chat/completions` |

To switch providers permanently, edit the launchd plist at `~/Library/LaunchAgents/ai.headroom.proxy.plist` or use the switch script.

---

## How to Verify It's Working After Restart

1. Restart Hermes (config `base_url` routes through proxy)
2. Send a few messages
3. Check savings:
   ```bash
   curl http://127.0.0.1:8787/stats | python3 -m json.tool | grep -E "saved|percent|avg_compression"
   ```
4. Check MCP tools:
   ```bash
   hermes mcp test headroom
   ```
5. Run perf report:
   ```bash
   headroom perf --hours 1
   ```

---

## Files Created

| File | Purpose |
|---|---|
| `~/.local/bin/headroom` | Headroom binary (installed via uv) |
| `~/.local/bin/headroom-switch.sh` | Provider switch script |
| `~/Library/LaunchAgents/ai.headroom.proxy.plist` | Proxy launchd service |
| `~/Library/LaunchAgents/ai.headroom.mcp.plist` | MCP launchd service |
| `~/.hermes/config.yaml` | Hermes config (base_url + MCP server) |
| `~/.hermes/logs/headroom-proxy.log` | Proxy logs |
| `~/.hermes/logs/headroom-mcp.log` | MCP logs |
| `~/.headroom/` | Headroom state directory |
| `~/10-projects/loop-engineering-2026-06-12/` | Project docs |

---

## Troubleshooting

### Proxy won't start
```bash
launchctl list | grep headroom   # Check if running
headroom proxy --port 8787       # Run in foreground to see errors
```

### Compression isn't happening
- Content must be >500 tokens (`HEADROOM_MIN_TOKENS_TO_CRUSH`)
- MCP tool is conservative; real savings come from proxy mode
- Check `HEADROOM_MODE=token` is set

### MCP connection fails
```bash
headroom mcp serve --debug   # Run in foreground
# Then from another terminal: hermes mcp test headroom
```

### Provider errors
```bash
# Check which upstream the proxy is using
curl http://127.0.0.1:8787/health | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['config']['backend'])"
```

---

**Related:** [[last30days]] skill for multi-source search, [[loop-engineering]] for agent architecture.
