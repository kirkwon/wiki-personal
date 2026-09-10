---
date: 2026-07-19
type: concept
title: Spotify
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- spotify
- music
- playback
- playlists
- media
sources:
- hermes://skill/spotify
description: 'Spotify: play, search, queue, manage playlists and devices.'
---

# Spotify

> Spotify: play, search, queue, manage playlists and devices.

## Overview

- **When to use this skill** — The user says something like "play X", "pause", "skip", "queue up X", "what's playing", "search for X", "add to my X playlist", "make a playlist", "save this to my library", etc.
- **The 7 tools** — - `spotify_playback` — play, pause, next, previous, seek, set_repeat, set_shuffle, set_volume, get_state, get_currently_playing, recently_played - `spotify_devices` — list, transfer - `spotify_queue` — get, add - `spotify_search` — search the catalog - `spotify_playlists` — list, get, create, add_items, remove_items, update_details - `spotify_albums` — get, tracks - `spotify_library` — list/save/remove with `kind: "tracks"|"albums"`
- **Critical failure modes** — **`403 Forbidden — No active device found`** on any playback action means Spotify isn't running anywhere. Tell the user: "Open Spotify on your phone/desktop/web player first, start any track for a second, then retry." Don't retry the tool call blindly — it will fail the same way. You can call `spotify_devices list` to confirm; an empty list means no active device.

## Further detail

### URI and ID formats

Spotify uses three interchangeable ID formats. The tools accept all three and normalize:

### What NOT to do

- **Don't call `get_state` before every action.** Spotify accepts play/pause/skip without preflight. Only inspect state when the user asked "what's playing" or you need to reason about device/track. - **Don't describe search results unless asked.** If the user said "play X", search, grab the top URI, play it. They'll hear it's wrong if it's wrong. - **Don't retry on `403 Premium required` or `403 No active device`.** Those are permanent until user action. - **Don't use `spotify_search` to find a playlist by name** — that searches the public Spotify catalog. User playlists come from `spotify_pl

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/media/spotify/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
