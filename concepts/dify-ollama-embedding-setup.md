---
type: concept
title: Dify Ollama Embedding Setup
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Dify Ollama Embedding Setup

> Set up Dify to use Ollama embeddings via OpenAI API.

## Overview

- **When to Use** — - User wants private, zero-cost embeddings for Dify knowledge bases - User has Ollama installed locally with embedding models (e.g., `nomic-embed-text`) - User runs Dify via Docker Compose and needs containers to reach host Ollama - User prefers local inference over cloud APIs (OpenAI, OpenRouter, etc.)
- **Prerequisites** — - **Ollama** installed and running on host (`ollama serve`) - **Embedding model pulled**: `ollama pull nomic-embed-text` (or `bge-large-en-v1.5`) - **Docker Desktop** (macOS/Windows) or Linux with host network access - **Dify** running via Docker Compose (containers must resolve `host.docker.internal`) - **Dify admin credentials** for web UI login
- **How to Run** — 1. Verify Ollama is reachable from containers:

## Further detail

### Quick Reference

| Check | Command | |-------|---------| | Ollama models list | `ollama list` | | Test `/api/embed` | `curl -X POST http://host.docker.internal:11434/api/embed -d '{"model":"nomic-embed-text","input":["test"]}'` | | Test `/v1/embeddings` | `curl -X POST http://host.docker.internal:11434/v1/embeddings -d '{"model":"nomic-embed-text","input":["test"]}'` | | Dify login (API) | `curl -X POST http://localhost:8080/console/api/login -d '{"email":"...","password":"<base64>","language":"en-US"}'` |

### Pitfalls

- **Dify web login expects base64-encoded password**: The login form sends `base64(password)`. Raw password fails with "Invalid encrypted data". Use `echo -n "password" | base64` to encode. - **`host.docker.internal` only works with Docker Desktop**. On Linux, use `--network host` or host IP. - **First embedding request is slower** (~40-70ms load duration) as model loads into memory. Subsequent requests ~20-30ms. - **Model name must match exactly**: `nomic-embed-text` (no `:latest` tag in Dify provider config). - **CSRF token required for Console API**: Web session uses cookies + `X-CSRF-Token

### Verification

Run this single check to confirm end-to-end wiring:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/dify-ollama-embedding-setup/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[ollama-model-management]]

[[mlx-local-models]]
