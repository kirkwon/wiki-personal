---
type: concept
title: Dify Mcp Installation Guide
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - uncategorized
---

# dify-mcp-installation-guide

Step-by-step guide for installing Dify MCP plugin and obtaining API key

## Usage

# Dify MCP Plugin Installation & API Key Guide

## Prerequisites

- ✅ Dify Docker instance running (detected at http://localhost:8080)
- ✅ Dify version: 1.16.1
- ✅ Docker Compose: `/tmp/dify/docker/`
- ✅ Nginx proxy running (port 8080)

## Step 1: Access Dify Web UI

Open in browser:
```
http://localhost:8080
```

## Step 2: Login to Workspace

1. Click **Sign In**
2. Enter credentials (email/password)
3. Access your workspace

## Step 3: Navigate to Marketplace

1. In the sidebar (left side), click **Marketplace** (plug icon)
2. Search bar appears

## Step 4: Install MCP Server Plugin

1. In search bar, type: `mcp-server`
2. Find plugin by **hlarry**
3. Click **Install** button

**Plugin Details:**
- Name: `mcp-server`
- Publisher: `hlarry`
- Type: Extension Plugin
- Purpose: Exposes Dify apps as MCP endpoints

## Step 5: Verify Plugin Installation

After installation:
1. Click **Plugins** (in sidebar)
2. Look for `mcp-server` in the list
3. Status should be **Enabled** (green checkmark)

## Step 6: Create or Select a Dify App

You need a Chat or Workflow app to expose as MCP.

**Option A: Use Existing App**
1. Click **Studio** (in sidebar)
2. Select your existing app
3. Note the app ID (from URL: `/apps/{app-id}`)

**Option B: Create New App**
1. Click **Create App** (top right)
2. Choose **Chat** or **Workflow**
3. Name: `Research Assistant` (or your preference)
4. Configure the app:
   - Add knowledge base (if needed)
   - Set model provider (OpenAI, Anthropic, etc.)
   - Write system prompt

## Step 7: Configure MCP Endpoint

1. Go to **Plugins** → click `mcp-server`
2. Click **Add Endpoint** (or similar button)
3. Fill in the form:

| Field | Value | Description |
|-------|-------|-------------|
| **Endpoint Name** | `deep_research` | Name for your MCP tool |
| **App** | Select your app | Chat or Workflow app |
| **App Type** | Chat / Workflow | Match your app type |
| **Input Schema** | JSON (see below) | Define parameters |

**Sample Input Schema** (for a research app):
```json
{
  "name": "deep_research",
  "description": "Conduct in-depth research based on user query using multiple search rounds",
  "inputSchema": {
    "title": "deep_researchArguments",
    "type": "object",
    "properties": {
      "query": {
        "title": "User Query",
        "description": "The user's main question or topic for research",
        "type": "string"
      },
      "depth": {
        "title": "Search Depth",
        "description": "Number of search rounds to perform (1-10)",
        "type": "number",
        "default": 3
      }
    },
    "required": ["query"]
  }
}
```

4. Click **Save**

## Step 8: Get MCP Endpoint URL

After saving, the plugin generates a unique endpoint URL:

**Format:**
```
http://localhost:8080/mcp/sse
```

or

```
http://localhost:8080/plugins/mcp-server/endpoint/{endpoint-name}/sse
```

**Copy this URL** — you'll need it for Hermes configuration.

## Step 9: Get Dify API Key

There are TWO types of API keys in Dify:

### T

...(truncated)