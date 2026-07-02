---
type: source
source_url: https://github.com/BuilderIO/skills
sha256: 9c48c099024fc2cbcb85bb2cc44c0a0b03f65b42b1f19985cd37dba87973c7f8
title: "Repo Analysis: builderio-skills"
ingested: 2026-06-30 23:32
source: remote-clone:https://github.com/BuilderIO/skills
project_type: unknown
language: unknown
---

# Repo Analysis: builderio-skills

> Ingested: 2026-06-30 | Source: remote-clone:https://github.com/BuilderIO/skills

## Project Profile

- **Type:** unknown
- **Language:** unknown
- **Build system:** N/A
- **Manifest:** N/A
- **Docker:** No
- **CI:** No
- **Docs:** Yes
- **Total files:** 43
- **Total dirs:** 21

## Directory Structure

**Top-level files:**

- CONTRIBUTING.md
- LICENSE
- README.md
- package.json

**Directories:**

- media/
- scripts/
- skills/

**Largest directories:**

- skills/visual-plan/references: 6 files
- (root): 4 files
- skills/visual-recap/references: 3 files
- skills/efficient-fable/assets: 3 files
- skills/visual-recap: 2 files

## CONTRIBUTING.md

```
# Contributing to BuilderIO/skills

Thank you for your interest in contributing! We welcome contributors of all types — code, tests, documentation, and design — and appreciate your time and effort. This document explains how to report issues, propose changes, and get your pull requests reviewed and merged quickly.

---

## Table of contents
- [How can I contribute?](#how-can-i-contribute)
- [Code of conduct](#code-of-conduct)
- [Filing issues](#filing-issues)
- [Proposing changes (pull requests)](#proposing-changes-pull-requests)
- [Development setup](#development-setup)
- [Repository workflows & checks](#repository-workflows--checks)
- [Code style & commit messages](#code-style--commit-messages)
- [Review process & expectations](#review-process--expectations)
- [License](#license)

---

## How can I contribute?

You can help in many ways:

- Report bugs with a minimal reproducible example.
- Add or improve documentation and skill guidelines.
- Fix bugs and implement small features via PRs.
- Review other people's PRs.

If you're unsure where to start, check the repository issues and look for labels like `good first issue` or `help wanted`.

## Code of conduct

This project follows an inclusive code of conduct. Please be respectful and considerate in all interactions. If there is no CODE_OF_CONDUCT.md in this repo yet, please follow standard community etiquette (be constructive, assume good intent, and be patient).

## Filing issues

When filing an issue, please include:

- A clear, descriptive title.
- A concise description of the problem or request.
- Steps to reproduce (minimum reproducible example preferred).
- Expected vs. actual behavior.
- Environment details (OS, Node version, browser if relevant).
- Any relevant logs, stack traces, or screenshots.

If you're proposing a feature, explain the use case and suggested API or UX.

---

## Proposing changes (Pull Requests)

... (truncated, 131 lines total)

```

## LICENSE

```
MIT License

Copyright (c) 2026 Builder.io

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## README.md

```
# Skills for coding agents

Small, composable skills for coding agents.

These skills are for teams that want the agent to stay sharp where judgment
matters: orchestration, review, planning, validation, docs discipline, and clear
communication. They are not a giant process framework. Install the pieces you
want, adapt them to your project, and let the model keep room to think.

### Quick install recommended skills

```sh
npx @agent-native/skills@latest add
```

The interactive picker puts `/visual-plan` and `/visual-recap` first and selects
only those by default. See the [full CLI docs below](#install).

## Skills

### [`/visual-plan`](skills/visual-plan/README.md)

Turn ordinary text plans into rich interactive visual plans with diagrams, file
maps, annotated code, open questions, and UI/prototype review when useful.

Solves for plans that are too important to bury in chat. The output is
scannable, commentable, and intuitive enough for a human to approve before code
changes start.

<picture>
  <img alt="Visual plan review surface" src="media/visual-plan.png">
</picture>

Visual plans are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

### [`/visual-recap`](skills/visual-recap/README.md)

Turn a branch, commit, or PR diff into an interactive visual recap with
annotated diffs, diagrams, API/schema summaries, file maps, UI state summaries,
and focused review notes.

Solves for diffs that hide the shape of the change. Reviewers can understand
contracts, architecture moves, schema changes, and UI impact before diving into
raw line-by-line review.

<picture>
  <img alt="Visual recap review surface animation" src="media/visual-recap.gif">
</picture>

Visual recaps are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

... (truncated, 214 lines total)

```

## File Index

- CONTRIBUTING.md
- LICENSE
- README.md
- media/visual-plan.png
- media/visual-recap.gif
- package.json
- scripts/sync-agent-native-plan-skills.mjs
- skills/agent-watchdog/README.md
- skills/agent-watchdog/SKILL.md
- skills/agent-watchdog/agents/openai.yaml
- skills/efficient-fable/README.md
- skills/efficient-fable/SKILL.md
- skills/efficient-fable/assets/fable-orchestrator-dark.png
- skills/efficient-fable/assets/fable-orchestrator.excalidraw
- skills/efficient-fable/assets/fable-orchestrator.png
- skills/efficient-frontier/README.md
- skills/efficient-frontier/SKILL.md
- skills/plan-arbiter/README.md
- skills/plan-arbiter/SKILL.md
- skills/plan-arbiter/agents/openai.yaml
- skills/plow-ahead/README.md
- skills/plow-ahead/SKILL.md
- skills/plow-ahead/agents/openai.yaml
- skills/quick-recap/README.md
- skills/quick-recap/SKILL.md
- skills/read-the-damn-docs/README.md
- skills/read-the-damn-docs/SKILL.md
- skills/read-the-damn-docs/agents/openai.yaml
- skills/stay-within-limits/README.md
- skills/stay-within-limits/SKILL.md
- skills/visual-plan/README.md
- skills/visual-plan/SKILL.md
- skills/visual-plan/references/canvas.md
- skills/visual-plan/references/connection.md
- skills/visual-plan/references/document-quality.md
- skills/visual-plan/references/exemplar.md
- skills/visual-plan/references/local-files.md
- skills/visual-plan/references/wireframe.md
- skills/visual-recap/README.md
- skills/visual-recap/SKILL.md
- skills/visual-recap/references/connection.md
- skills/visual-recap/references/local-files.md
- skills/visual-recap/references/wireframe.md

## Open Questions / Notes

> _Add notes after reviewing the codebase._
