------

# Architecture As Code

> Architecture-as-code with LikeC4: models, diagrams, and sync enforcement from source.

## Overview

- **When to Use** — - Documenting a software system's architecture for a team or wiki - Enforcing that documentation stays current as code changes - Auto-generating diagrams from a Python codebase (no manual drawing) - Producing Mermaid embeds for GitHub READMEs - Modeling workspace topology (multiple projects, data flows, cron pipelines)
- **LikeC4 DSL — Critical Syntax Rules** — These rules were learned through repeated validation failures across 3 projects. **Read this section before writing any `.c4` file.**
- **The 3-Layer Sync Enforcement Pattern** — This is the core value of architecture-as-code. Three layers prevent diagram drift, from weakest to strongest:

## Further detail

### Auto-Generation from Python Source

The strongest enforcement: regenerate `.c4` files from source code on every build. The model literally IS the code — drift is impossible.

### Verified Results

| Project | Elements | Views | Sync Layer | Status | |---------|----------|-------|------------|--------| | Architecture-Safe | 18 | 4 | Script parity | ✅ 7/7 criteria | | Architecture-Workspace | 60+ | 7 | Folder parity | ✅ 8 PNGs | | Architecture-AutoGen | 4-9 (auto) | 3 | Full regeneration | ✅ 3 codebases |

### Embedding Diagrams in READMEs

Use Mermaid files (not PNGs) for GitHub READMEs — they render inline:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/architecture-as-code/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[system-prompt-architecture-patterns]]

[[requesting-code-review]]
