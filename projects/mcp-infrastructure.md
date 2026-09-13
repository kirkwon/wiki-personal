---
type: project
title: MCP Server Infrastructure & Automation
status: active
created: '2026-06-28T00:00:00.000Z'
updated: '2026-06-28T00:00:00.000Z'
priority: P1
ingested_via: put_page
ingested_at: '2026-09-13T13:00:55.404Z'
source_kind: put_page
---

# MCP Server Infrastructure & Automation

## Summary
13 MCP servers configured across Hermes, providing tools for search, code, finance, data, and automation. n8n deployed as visual automation layer. Docker infrastructure running.

## Progress

### MCP Servers (13 total)
- [x] Brave Search MCP — web search (key active)
- [x] Notion MCP — workspace docs (key active)
- [x] Sequential Thinking MCP — structured reasoning
- [x] Filesystem MCP — file access
- [x] SQLite MCP — local database
- [x] GitHub MCP — repo/PR management (key active)
- [x] Git MCP — version control
- [x] Headroom MCP — context compression (:8787)
- [x] OpenBB MCP — financial data (v3.4.2 @ :8001)
- [x] Financial Datasets MCP — stock quotes (secondary)
- [x] FRED MCP — economic data
- [x] SEC EDGAR MCP — SEC filings (edgar-mcp v1.0.2, no key needed)
- [x] Alpha Vantage MCP — stock data (@gviper/alphavantage-mcp, 66 tools)

### Docker & n8n
- [x] n8n deployed — v2.27.4 on :5678, data at `~/.docker-data/n8n`
- [x] Docker v29.4.1 running
- [x] n8n task broker on :5679
- [ ] n8n workflows not yet built
- [ ] n8n Python task runner warning (no Python 3 in container — JS nodes work)

### Stock Quote System
- [x] 3 providers tested: OpenBB/yfinance (PRIMARY), Financial Datasets (secondary), Alpha Vantage (backup)
- [x] All 3 return consistent prices (AAPL $283.78 verified)
- [x] `stock-provider-health.py` written (151 lines)
- [ ] Health monitor not wired to cron
- [ ] `stock-provider-health.py` not yet tested

## Next Steps
1. Wire `stock-provider-health.py` to cron (hourly check)
2. Build first n8n automation workflow
3. Add missing API keys (xAI, GitHub PAT, Anthropic, FMP)

## Key Files
- `~/.hermes/config.yaml` — MCP server configurations
- `~/.hermes/.env` — API keys (ALPHA_VANTAGE_API_KEY)
- `~/.hermes/scripts/stock-provider-health.py` — provider health monitor
- `~/.local/bin/edgar-mcp-launcher` — SEC EDGAR wrapper
- `~/.local/bin/python3` → python3.11 symlink (fixes npx MCP servers)

## Blockers
- xAI key missing → x_search tool inactive
- GitHub PAT missing → GitHub MCP limited
- Anthropic key missing → no Claude direct access
- FMP key missing → densest finance data source unavailable
