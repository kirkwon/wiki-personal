---
type: concept
title: Web Api Reverse Engineer
created: 2026-09-03
updated: 2026-09-03
tags:
  - Skill
  - devops
---

# web-api-reverse-engineer

>

## Usage

# web-api-reverse-engineer

Derive a Python API client from a website's own network traffic. Instead of reverse-engineering request formats by guessing, **record what the browser actually sends**, then replay it with httpx. Deterministic-first: the HAR file is ground truth.

Load the **agent-browser** skill for core command syntax (open, snapshot, click, eval).

## When to use

- A web app loads the data you want via XHR/fetch, and there's no public API.
- You need to automate data fetching that currently requires clicking around a UI.
- You want a reusable Python client instead of fragile browser scraping.

**Do NOT use when:** the site is static HTML (use `agent-browser read` or crawl4ai), or a documented public API exists (use it directly).

## Workflow

### 1. Open the target site with agent-browser

```bash
agent-browser open https://app.example.com/dashboard
agent-browser snapshot -i
```

If the endpoint is behind login, connect to your logged-in Chrome or use a profile:

```bash
agent-browser --cdp 9222 open https://app.example.com/dashboard
# or
agent-browser --profile Default open https://app.example.com/dashboard
```

### 2. Start HAR recording

```bash
agent-browser network har start /tmp/trace.har
```

### 3. Perform the action that loads the data

Click the button, run the search, navigate to the page — whatever triggers the network calls you want to capture.

```bash
agent-browser snapshot -i
agent-browser fill @e3 "search query"
agent-browser press Enter
agent-browser wait --load networkidle
```

### 4. Stop recording

```bash
agent-browser network har stop /tmp/trace.har
```

### 5. Analyze captured requests

List XHR/fetch calls with successful responses:

```bash
agent-browser network requests --type fetch,xhr --status 200
```

Inspect a specific request in full (headers, body, response):

```bash
agent-browser network request <requestId>
```

**Identify the data-bearing calls:** look for `Content-Type: application/json` responses to POST/GET requests against `/api/...` or `/graphql` endpoints. Filter out analytics, telemetry, and static assets:

```bash
agent-browser network requests --filter "**/api/**" --status 200
```

### 6. Extract auth headers / cookies

From the request detail, capture:
- **Authorization** header (bearer token, basic auth)
- **Cookies** (session ID, auth cookies)
- **Custom headers** (X-CSRF-Token, X-API-Key, X-Requested-With)

```bash
# Dump all cookies for the current origin
agent-browser cookies get

# Or read a specific request's headers from the capture
agent-browser network request <requestId>
```

If auth state lives in localStorage (common for SPAs), extract it via eval:

```bash
cat <<'EOF' | agent-browser eval --stdin
(() => {
  const keys = Object.keys(localStorage);
  return keys.reduce((acc, k) => {
    acc[k] = localStorage.getItem(k);
    return acc;
  }, {});
})()
EOF
```

### 7. Build the Python client

Use the discovered endpoint, method, headers, and body shape to write an httpx client

...(truncated)