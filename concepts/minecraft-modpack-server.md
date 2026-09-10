---
date: 2026-07-19
type: concept
title: Minecraft Modpack Server
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- minecraft
- gaming
- server
- neoforge
- forge
- modpack
sources:
- hermes://skill/minecraft-modpack-server
description: Host modded Minecraft servers (CurseForge, Modrinth).
---

# Minecraft Modpack Server

> Host modded Minecraft servers (CurseForge, Modrinth).

## Overview

- **When to use** — - User wants to set up a modded Minecraft server from a server pack zip - User needs help with NeoForge/Forge server configuration - User asks about Minecraft server performance tuning or backups
- **Gather User Preferences First** — Before starting setup, ask the user for: - **Server name / MOTD** — what should it say in the server list? - **Seed** — specific seed or random? - **Difficulty** — peaceful / easy / normal / hard? - **Gamemode** — survival / creative / adventure? - **Online mode** — true (Mojang auth, legit accounts) or false (LAN/cracked friendly)? - **Player count** — how many players expected? (affects RAM & view distance tuning) - **RAM allocation** — or let agent decide based on mod count & available RAM? - **View distance / simulation distance** — or let agent pick based on player count & hardware? - **P
- **Pitfalls** — - ALWAYS set `allow-flight=true` for modded — mods with jetpacks/flight will kick players otherwise - `max-tick-time=180000` or higher — modded servers often have long ticks during worldgen - First startup is SLOW (several minutes for big packs) — don't panic - "Can't keep up!" warnings on first launch are normal, settles after initial chunk gen - If online-mode=false, set enforce-secure-profile=false too or clients get rejected - The pack's startserver.sh often has an auto-restart loop — make a clean launch script without it - Delete the world/ folder to regenerate with a new seed - Some pack

## Further detail

### Verification

- `pgrep -fa neoforge` or `pgrep -fa minecraft` to check if running - Check logs: `tail -f ~/minecraft-server/server/logs/latest.log` - Look for "Done (Xs)!" in the log = server is ready - Test connection: player adds server IP in Multiplayer

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gaming/minecraft-modpack-server/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
