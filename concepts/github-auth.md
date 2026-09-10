---
date: 2026-07-19
type: concept
title: Github Auth
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- GitHub
- Authentication
- Git
- gh-cli
- SSH
- Setup
- github
sources:
- hermes://skill/github-auth
description: 'GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.'
---

# Github Auth

> GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.

## Overview

- **Detection Flow** — When a user asks you to work with GitHub, run this check first:
- **Method 1: Git-Only Authentication (No gh, No sudo)** — This works on any machine with `git` installed. No root access needed.
- **Method 2: gh CLI Authentication** — If `gh` is installed, it handles both API access and git credentials in one step.

## Further detail

### MCP Server Access

Two MCP servers can provide GitHub/Git access:

### Troubleshooting

| Problem | Solution | |---------|----------| | `git push` asks for password | GitHub disabled password auth. Use a personal access token as the password, or switch to SSH | | `remote: Permission to X denied` | Token may lack `repo` scope — regenerate with correct scopes | | `fatal: Authentication failed` | Cached credentials may be stale — run `git credential reject` then re-authenticate | | `ssh: connect to host github.com port 22: Connection refused` | Try SSH over HTTPS port: add `Host github.com` with `Port 443` and `Hostname ssh.github.com` to `~/.ssh/config` | | Credentials not persisti

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/github/github-auth/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
