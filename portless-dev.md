---
type: concept
title: Portless Dev
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - uncategorized
---

# portless-dev

Stable HTTPS URLs for local dev apps.

## Usage

# Portless for Local Development

## What It Solves

**Problem:** Multiple local dev apps compete for ports. Remembering which port each app uses is tedious. Port conflicts force you to kill/restart processes.

**Solution:** Portless replaces `http://localhost:3000` with stable named URLs like `https://buzz.localhost`. It runs a proxy on port 443 that routes named hostnames to your running apps on auto-assigned ports (4000-4999).

| Before | After |
|--------|-------|
| `http://localhost:3000` (Buzz) | `https://buzz.localhost` |
| `http://localhost:3000` (Dify, conflict!) | `https://dify.localhost` |
| `http://localhost:3001` (if lucky) | `https://api.buzz.localhost` |

---

## Quick Start

### 1. Install

```bash
npm install -g portless
```

### 2. Start the Proxy (requires sudo on macOS)

**First run only:** Portless will generate a local CA and prompt to trust it. Accept to avoid browser warnings.

```bash
sudo portless proxy start --https
```

### 3. Run Your App Through Portless

```bash
cd ~/buzz
portless buzz just desktop-dev
# → https://buzz.localhost
```

Portless auto-assigns a port (4000-4999), registers it with the proxy, and you access it via the stable URL.

---

## Common Patterns

### Multiple Apps (No Port Conflicts)

```bash
# Terminal 1: Start proxy once
sudo portless proxy start --https

# Terminal 2: Start Buzz
cd ~/buzz
portless buzz just desktop-dev
# → https://buzz.localhost (port auto-assigned)

# Terminal 3: Start Dify (Docker app)
cd ~/dify
docker-compose up -d
portless dify --app-port 3000
# → https://dify.localhost (port 3000 fixed)
```

### Subdomains

```bash
portless api.buzz just desktop-dev
# → https://api.buzz.localhost

portless docs.buzz next dev
# → https://docs.buzz.localhost
```

### Unprivileged Port (No sudo required)

```bash
portless proxy start --port 1355 --https
# → URLs include :1355 (e.g., https://buzz.localhost:1355)
```

### Docker Apps

For Docker Compose apps that expose a fixed port:

```bash
# Start Docker app normally
cd ~/dify
docker-compose up -d

# Register the running app with portless
portless dify --app-port 3000
# → https://dify.localhost
```

### Monorepo with Workspace Config

Create `portless.json` at the workspace root:

```json
{
  "name": "kirkwon",
  "apps": {
    "apps/buzz": { "name": "buzz", "script": "desktop-dev" },
    "apps/dify": { "name": "dify", "script": "dev" }
  }
}
```

Then run from anywhere in the workspace:

```bash
cd /path/to/workspace
portless buzz    # Runs apps/buzz desktop-dev
portless dify    # Runs apps/dify dev
```

---

## Configuration

### `portless.json` (Workspace-level)

```json
{
  "name": "myorg",
  "apps": {
    "path/to/app": {
      "name": "appname",
      "script": "dev",
      "appPort": 3000
    }
  }
}
```

### `package.json` (Per-project)

```json
{
  "name": "@myorg/web",
  "portless": "myapp"
}
```

Or with options:

```json
{
  "name": "@myorg/web",
  "portless": {
    "name": "myapp",
    "script": "dev:app"
  }
}
```

---

## Adva

...(truncated)