---
type: concept
title: Dify Mcp Investigation
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - uncategorized
---

# dify-mcp-investigation

Investigation of Dify MCP installation options and requirements

## Usage

# Dify MCP Installation Investigation

## Current State (2026-08-02)

| Check | Status |
|-------|--------|
| Dify SaaS account | ❓ Unknown |
| Dify self-hosted | ❓ Unknown |
| Dify MCP plugin installed | ❓ Unknown |
| MCP plugin in Marketplace | ✅ Available |
| Hermes MCP configuration | ❌ Not configured |

## Installation Options

### Option 1: Dify SaaS MCP Server (Recommended)

**Requires:** Dify SaaS account + API key

**Steps:**

1. **Install MCP Server Plugin**
   - Log in to Dify SaaS workspace
   - Navigate to **Marketplace**
   - Search for `mcp-server` (by hlarry)
   - Install the plugin

2. **Create/App Selection**
   - Select an existing Chat or Workflow app
   - Or create a new app (e.g., "Research Assistant")

3. **Configure MCP Endpoint**
   - In MCP plugin settings:
     - Endpoint Name: `deep_research` (or custom)
     - App: Select your app
     - App Type: Chat or Workflow
     - Input Schema: Define parameters (JSON format)

4. **Get Endpoint URL**
   - Plugin generates unique URL: `https://******.ai-plugin.io/sse`
   - Copy this URL

5. **Configure Hermes**
   ```bash
   hermes config set tools.mcp.dify-server.url https://******.ai-plugin.io/sse
   hermes config set tools.mcp.dify-server.headers.Authorization "Bearer YOUR_DIFY_API_KEY"
   ```

**Pros:**
- No local installation
- Managed by Dify
- Easy setup
- HTTPS endpoint ready

**Cons:**
- Requires Dify SaaS account
- Data processed on Dify servers
- Potential costs

### Option 2: Dify Self-Hosted + MCP Plugin

**Requires:** Self-hosted Dify instance

**Steps:**

1. **Deploy Dify** (if not already running)
   ```bash
   git clone https://github.com/langgenius/dify.git
   cd dify/docker
   docker-compose up -d
   ```

2. **Access Marketplace**
   - Navigate to `http://localhost` or your domain
   - Login to admin panel
   - Go to **Marketplace**
   - Install `mcp-server` plugin

3. **Configure Endpoint** (same as Option 1)

4. **Configure Hermes**
   ```bash
   hermes config set tools.mcp.dify-server.url http://localhost/sse
   hermes config set tools.mcp.dify-server.headers.Authorization "Bearer YOUR_API_KEY"
   ```

**Pros:**
- Data stays local
- Full control
- No external dependencies

**Cons:**
- Requires Docker
- More setup complexity
- Maintenance required

### Option 3: Dify MCP Client (Call External MCP)

**Requires:** Dify v1.6.0 or later

**Purpose:** Dify acts as MCP client, calls external MCP servers

**Not applicable** for this use case (we want Dify as MCP server for Hermes)

## Prerequisites Checklist

- [ ] Dify SaaS account OR self-hosted Dify instance
- [ ] Dify API key (from workspace settings)
- [ ] MCP Server plugin installed
- [ ] App created and configured
- [ ] Endpoint URL generated

## Alternative: Direct Dify API

If MCP setup is problematic, use direct API calls:

```python
import requests

DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"
DIFY_API_KEY = "your-api-key"

def query_dify(query: str) -> dict:
    headers = {
        "Authorizati

...(truncated)