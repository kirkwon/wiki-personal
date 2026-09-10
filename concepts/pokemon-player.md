---
date: 2026-07-19
type: concept
title: Pokemon Player
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gaming
- pokemon
- emulator
- pyboy
- gameplay
- gameboy
sources:
- hermes://skill/pokemon-player
description: Play Pokemon via headless emulator + RAM reads.
---

# Pokemon Player

> Play Pokemon via headless emulator + RAM reads.

## Overview

- **When to Use** — - User says "play pokemon", "start pokemon", "pokemon game" - User asks about Pokemon Red, Blue, Yellow, FireRed, etc. - User wants to watch an AI play Pokemon - User references a ROM file (.gb, .gbc, .gba)
- **Action Reference** — - press_a — confirm, talk, select - press_b — cancel, close menu - press_start — open game menu - walk_up/down/left/right — move one tile - hold_b_N — hold B for N frames (use for speeding through text) - wait_60 — wait about 1 second (60 frames) - a_until_dialog_end — press A repeatedly until dialog clears
- **Memory Conventions** — | Prefix | Purpose | Example | |--------|---------|---------| | PKM:OBJECTIVE | Current goal | Get Parcel from Viridian Mart | | PKM:MAP | Navigation knowledge | Viridian: mart is northeast | | PKM:STRATEGY | Battle/team plans | Need Grass type before Misty | | PKM:PROGRESS | Milestone tracker | Beat rival, heading to Viridian | | PKM:STUCK | Stuck situations | Ledge at y=28 go right to bypass | | PKM:TEAM | Team notes | Squirtle Lv6, Tackle + Tail Whip |

## Further detail

### Progression Milestones

- Choose starter - Deliver Parcel from Viridian Mart, receive Pokedex - Boulder Badge — Brock (Rock) → use Water/Grass - Cascade Badge — Misty (Water) → use Grass/Electric - Thunder Badge — Lt. Surge (Electric) → use Ground - Rainbow Badge — Erika (Grass) → use Fire/Ice/Flying - Soul Badge — Koga (Poison) → use Ground/Psychic - Marsh Badge — Sabrina (Psychic) → hardest gym - Volcano Badge — Blaine (Fire) → use Water/Ground - Earth Badge — Giovanni (Ground) → use Water/Grass/Ice - Elite Four → Champion!

### Stopping Play

1. Save the game with a descriptive name via POST /save 2. Update memory with PKM:PROGRESS 3. Tell user: "Game saved as [name]! Say 'play pokemon' to resume." 4. Kill the server and tunnel background processes

### Pitfalls

- NEVER download or provide ROM files - Do NOT send more than 4-5 actions without checking vision - Always sidestep after exiting buildings before going north - Always add wait_60 x2-3 after door/stair warps - Dialog detection via RAM is unreliable — verify with screenshots - Save BEFORE risky encounters - The tunnel URL changes each time you restart it

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gaming/pokemon-player/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
