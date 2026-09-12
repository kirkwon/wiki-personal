------

# Hermes Profile Management

> Configure Hermes agent profiles and providers with role-specific identity (SOUL.md), toolset (config.yaml), provider definitions, fallback routing, and skills (symlinks). Covers creating new profiles, adapting existing ones, adding LLM providers (Ollama, local models), selecting appropriate toolsets per role, and symlinking skills from a shared pool. Use when setting up profiles for specialized roles (developer, analyst, project manager, etc.), connecting local model backends, or customizing an existing profile's behavior.

## Overview

- **When to Use** — - Creating a new profile for a specialized role (backend developer, QA engineer, project manager, etc.) - Converting a bare/default profile into a real working instance - Adding coding CLI access to a profile that needs it - Adapting toolsets and reasoning effort per role - Setting up profiles for multi-agent orchestration (project manager delegates to specialists)
- **Profile Anatomy** — Each profile lives at `~/.hermes/profiles/<name>/` with this structure:
- **Provider Configuration** — Hermes config.yaml supports defining additional LLM providers (beyond the main `model` section) for fallback routing, subagent delegation, and smart model routing. These live at the top level of config.yaml.

## Further detail

### The Two-Layer Agent Model

When reasoning about agent access in this ecosystem, distinguish two layers:

### Profile Handoff Protocol

When switching between profiles for a multi-step workflow:

### Common Pitfalls (profile-specific)

1. **Profile skills are NOT inherited from default.** `~/.hermes/profiles/<name>/skills/` is completely independent of `~/.hermes/skills/` — symlink or copy explicitly. 2. **Permissions block symlinks.** Profile dirs may be `700`; `chmod 755` target dirs before symlinking. 3. **Symlinks must use absolute paths** — relative ones across the `~/.hermes` hierarchy don't resolve. 4. **config.yaml changes need a restart** — loaded at session start only. 5. **SOUL.md replaces the system prompt** — it doesn't append; make role identity self-contained. 6. **Stale skill manifests.** Profiles used once a

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-profile-configuration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
