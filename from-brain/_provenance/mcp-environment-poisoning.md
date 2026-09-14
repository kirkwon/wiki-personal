---
type: note
title: Mcp Environment Poisoning
source: hermes-memory
recency: '2026-08-03T00:00:00.000Z'
frequency: medium
offloaded: '2026-08-03T00:00:00.000Z'
importance: high
truthfulness: verified
ingested_via: put_page
ingested_at: '2026-08-03T22:28:14.129Z'
source_kind: put_page
created: 2026-08-03
---
# MCP PYTHONPATH Poisoning

- Hermes venv (Py3.11) leaks into uvx/local-venv MCP subprocesses (Py3.10/3.12)
- pydantic_core ABI mismatch
- Fix: `unset PYTHONPATH` in wrappers, or mcp-wrappers/ with `env -u PYTHONPATH`
- MCP SDK 2.0.0 removed decorators — pin `mcp<2`
- Skill: troubleshooting/mcp-server-troubleshooting
