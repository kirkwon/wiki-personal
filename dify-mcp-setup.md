---
type: concept
title: Dify Mcp Setup
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - uncategorized
---

# dify-mcp-setup

Configure Dify MCP integration with Hermes

## Usage

# Dify MCP Configuration

Configure Dify MCP server integration with Hermes Agent for tool calling.

## When to Use

- Setting up Dify as an MCP server for Hermes
- Exposing Dify apps as callable tools
- Integrating Dify's AI capabilities into Hermes workflows

## Prerequisites

1. **Dify Instance**: Self-hosted or SaaS Dify deployment
2. **MCP Plugin**: Dify MCP plugin installed in Dify workspace
3. **Dify API Key**: API key from Dify workspace settings

## Configuration

### Step 1: Enable MCP Plugin in Dify

1. Log in to your Dify workspace
2. Navigate to **Marketplace**
3. Install **MCP Server** plugin
4. Enable MCP Server for your app
5. Copy the SSE endpoint (e.g., `https://your-dify.com/api/mcp/sse`)

### Step 2: Configure Hermes MCP

Add to `~/.hermes/config.yaml`:

```yaml
tools:
  mcp:
    - name: dify-server
      url: https://your-dify.com/api/mcp/sse
      headers:
        Authorization: "Bearer YOUR_DIFY_API_KEY"
```

### Step 3: Reload Hermes

```bash
hermes config reload
```

Or restart Hermes service.

## Usage

### List Available MCP Tools

```bash
hermes mcp list
```

Look for `dify-server` in the output.

### Query Dify App

In a Hermes session:

```
Use the dify MCP tool to query my knowledge base about [topic]
```

Hermes will call the Dify app and return results.

## Troubleshooting

### "MCP server not found"

**Cause:** MCP server not configured in config.yaml

**Fix:**
```bash
hermes config set tools.mcp.dify-server.url https://your-dify.com/api/mcp/sse
hermes config set tools.mcp.dify-server.headers.Authorization "Bearer YOUR_API_KEY"
```

### "Connection refused"

**Cause:** Dify instance not running or wrong URL

**Fix:**
- Verify Dify is running: `docker ps | grep dify`
- Test SSE endpoint: `curl https://your-dify.com/api/mcp/sse`

### "401 Unauthorized"

**Cause:** Invalid or missing API key

**Fix:**
- Regenerate API key in Dify workspace settings
- Update Authorization header with new key

## Alternative: Dify Self-Hosted Integration

If MCP setup is problematic, use the self-hosted integration skill:

```bash
hermes config set skills.add dify-self-hosted-integration
```

This provides direct API calls to Dify without MCP overhead.

## Notes

- MCP servers run as separate processes
- Tool discovery happens on Hermes start
- Changes to config.yaml require Hermes restart
- SSE endpoints provide real-time streaming responses

## Related Skills

- `dify-self-hosted-integration` — Direct API integration
- `dify-test` — Test configuration

## Next Steps

1. Obtain Dify API key
2. Enable MCP plugin in Dify
3. Copy SSE endpoint
4. Configure in `~/.hermes/config.yaml`
5. Restart Hermes
6. Test with query