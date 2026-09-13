---
type: concept
title: Docker Management
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - development
---

# docker-management

>-

## Usage

# Docker Management — Containers, Compose, Builds, Cleanup

Tool-focused skill for managing Docker containers, images, volumes, and Compose stacks from the terminal. Covers the full lifecycle: inspect, run, build, compose, clean, and debug.

## Tools Used

| Tool | Purpose |
|------|---------|
| `terminal` | Run all docker, docker-compose, and podman commands |

> **Note on podman:** Podman is a drop-in replacement for Docker with CLI-compatible commands. If `podman` is installed but `docker` is not, alias `d=podman` or substitute `docker → podman` in all commands below. This skill uses `docker` as the canonical CLI.

---

## 1. Inspecting Containers: ps, inspect, logs

### docker ps — List Containers

```bash
# Running containers only
docker ps

# All containers (including stopped)
docker ps -a

# Show only container IDs (for scripting)
docker ps -q

# Filter by name, status, or label
docker ps --filter "name=myapp"
docker ps --filter "status=exited"
docker ps --filter "label=com.docker.compose.project=myproject"

# Show last N created containers
docker ps -n 5

# Custom format (useful for scripts)
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
docker ps --format "json"
```

### docker inspect — Detailed Container/Image Info

```bash
# Inspect a container (returns JSON)
docker inspect <container-name-or-id>

# Extract a specific field with --format
docker inspect <container-name> --format '{{.State.Status}}'
docker inspect <container-name> --format '{{.NetworkSettings.IPAddress}}'
docker inspect <container-name> --format '{{range $p, $conf := .NetworkSettings.Ports}}{{$p}}{{end}}'

# Inspect an image instead of a container
docker inspect <image-name>:<tag>

# Inspect multiple objects
docker inspect <container1> <container2> <image1>
```

### docker logs — View Container Output

```bash
# Tail recent logs (like `tail -f`)
docker logs <container-name>

# Follow log output in real time
docker logs -f <container-name>

# Last N lines
docker logs --tail 100 <container-name>

# With timestamps
docker logs -t <container-name>

# Since a specific time
docker logs --since "2025-01-01T00:00:00" <container-name>
docker logs --since "5m" <container-name>

# Until a time
docker logs --until "10m" <container-name>

# Combine: last 50 lines, follow, with timestamps
docker logs --tail 50 -ft <container-name>
```

### docker exec — Run Commands in a Running Container

```bash
# Interactive shell (most common)
docker exec -it <container-name> /bin/bash      # Debian/Ubuntu
docker exec -it <container-name> /bin/sh        # Alpine

# Run a single command and get output
docker exec <container-name> ls /app

# Set working directory
docker exec -w /var/log <container-name> cat app.log

# Set environment variable for one command
docker exec -e DEBUG=true <container-name> node app.js
```

---

## 2. Running Containers: docker run with Ports, Volumes, Env

### Basic Run

```bash
# Run a container and remove it after exit
docker run --rm <image>

# Run int

...(truncated)