---
date: 2026-07-19
type: concept
title: Gbrain Skillify
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- gbrain
- skillify
- skills
- meta-skill
- durable
- research
sources:
- hermes://skill/gbrain-skillify
description: Meta-skill to turn failures into durable skills. Scaffold, audit, and
  maintain GBrain skills with 10-item checklist, resolver audit, and routing evaluation.
  v0.19+.
---

# Gbrain Skillify

> Meta-skill to turn failures into durable skills. Scaffold, audit, and maintain GBrain skills with 10-item checklist, resolver audit, and routing evaluation. v0.19+.

## Overview

- **When This Skill Activates** — Use this skill when the user: - Says "skillify it!" or "make this a skill" - Wants to create a new GBrain skill from a fix or workflow - Needs to audit existing skills for conformance - Asks about `gbrain skillify`, `gbrain check-resolvable`, or `gbrain routing-eval` - Wants to install curated skill bundles (`gbrain skillpack install`)
- **Skillpack (Curated Bundle)** — Install 25 curated skills into your workspace with dependency closure.
- **Works on Your OpenClaw, Not Just GBrain's Repo** — v0.19 teaches `gbrain check-resolvable` to accept `AGENTS.md` as a resolver file alongside `RESOLVER.md`, at either the skills directory OR one level up (OpenClaw-native workspace-root layout).

## Further detail

### Anti-Patterns Skillify Catches

1. **Checklists decay** — Without the 10-item audit, tests drift, resolver entries go stale 2. **SKILLIFY_STUB sentinels remain** — Sentinels in scripts mean the skill isn't actually implemented 3. **Resolver gaps** — Skills exist but no intent routes to them (15% of tree can be dark) 4. **MECE violations** — Overlapping triggers cause ambiguous routing 5. **DRY violations** — Inlined rules that should be in shared conventions

### Pitfalls

- **SKILLIFY_STUB sentinels** — Sentinels in scripts mean "not implemented yet". The 10-item audit fails until all sentinels are replaced with real logic - **`gbrain check-resolvable` reads AGENTS.md OR RESOLVER.md** — If both exist, it may pick the wrong one. Be explicit about which is your resolver - **`OPENCLAW_WORKSPACE` must be set** for OpenClaw layouts — Without it, `check-resolvable` won't find `AGENTS.md` at workspace root - **`gbrain skillpack install --all` prunes** — Only the all flag deletes skills gbrain didn't install. Per-skill install is additive only - **`gbrain routing-eval

### Commands Quick Reference

| Command | Purpose | |---------|---------| | `gbrain skillify scaffold <name>` | Create 5 stub files + resolver row | | `gbrain skillify check <path>` | 10-item audit of a skill | | `gbrain check-resolvable [--strict]` | Resolver audit (MECE, DRY, routing) | | `gbrain routing-eval [--llm] [--json]` | Intent→skill routing accuracy | | `gbrain skillpack list` | Show 25 curated skills | | `gbrain skillpack install <name>` | Copy skill + conventions to workspace | | `gbrain skillpack install --all` | Install full curated bundle | | `gbrain skillpack diff <name>` | Compare bundle vs local copy |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/gbrain-skillify/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[github-to-skill-integration]]

[[hermes-skill-development-workflow]]
