---
date: 2026-08-02
type: concept
title: Dify Self Hosted Integration
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- Dify
- Ollama
- Self-Hosted
- Plugins
- RAG
- Local-LLM
- mlops
sources:
- hermes://skill/dify-self-hosted-integration
description: Manage self-hosted Dify with local LLMs via plugins.
---

# Dify Self Hosted Integration

> Manage self-hosted Dify with local LLMs via plugins.

## Overview

- **When to Use** — - Setting up self-hosted Dify with local models (Ollama, LM Studio, etc.) - Installing model providers as plugins (required for Dify v1.0+) - Configuring embedding providers for knowledge bases - Debugging Web UI login vs Console API authentication - Clean reset procedures for Dify Docker deployments
- **Prerequisites** — - Docker Desktop (macOS/Windows) or Linux with Docker Compose - Ollama installed and running on host (`ollama serve`) - Embedding model pulled: `ollama pull nomic-embed-text` - Dify admin credentials - **Port 3000 free** — Dify's nginx proxy uses host port 8080; stop any service on 3000 (Grafana, Open WebUI, etc.)
- **Quick Reference** — | Task | Command | |------|---------| | Clean reset | `cd /tmp/dify/docker && docker compose down -v && docker compose up -d` | | Verify API health | `curl -s http://localhost:5001/health` | | Login via Console API | `curl -X POST http://localhost:8080/console/api/login -d '{"email":"...","password":"<base64>","language":"en-US"}'` | | List model providers | `curl -H "X-CSRF-Token: $TOKEN" http://localhost:8080/console/api/workspaces/current/model-providers` | | Install plugin (marketplace) | `curl -X POST .../plugin/install/marketplace -d '{"plugin_unique_identifiers":["langgenius/ollama"]}'`

## Further detail

### Service API Document Upload (create-by-file)

**Endpoint**: `POST /v1/datasets/{dataset_id}/document/create-by-file`

### Web UI vs Console API Authentication

| Aspect | Web UI (port 3000) | Console API (port 8080) | |--------|-------------------|------------------------| | Password | **Raw** (frontend base64-encodes) | **Base64-encoded** in JSON | | Endpoint | Form submits via SPA router | `POST /console/api/login` | | CSRF | Auto via cookies | Manual `X-CSRF-Token` header | | Session | Cookie-based | Cookie + CSRF token |

### Clean Reset Procedure

Wait for all services: - `docker ps` — all 15 containers running - `curl -s http://localhost:5001/health` — returns `{"status":"healthy"}` - `curl -s http://localhost:3000` — returns HTML login page

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/dify-self-hosted-integration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
