---
date: 2026-07-19
type: concept
title: Codebase Inspection
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- LOC
- Code Analysis
- pygount
- Codebase
- Metrics
- Repository
- github
sources:
- hermes://skill/codebase-inspection
description: 'Inspect codebases w/ pygount: LOC, languages, ratios.'
---

# Codebase Inspection

> Inspect codebases w/ pygount: LOC, languages, ratios.

## Overview

- **When to Use** — - User asks for LOC (lines of code) count - User wants a language breakdown of a repo - User asks about codebase size or composition - User wants code-vs-comment ratios - General "how big is this repo" questions
- **1. Basic Summary (Most Common)** — Get a full language breakdown with file counts, code lines, and comment lines:
- **2. Common Folder Exclusions** — Adjust based on the project type:

## Further detail

### 6. Interpreting Results

The summary table columns: - **Language** — detected programming language - **Files** — number of files of that language - **Code** — lines of actual code (executable/declarative) - **Comment** — lines that are comments or documentation - **%** — percentage of total

### Pitfalls

1. **Always exclude .git, node_modules, venv** — without `--folders-to-skip`, pygount will crawl everything and may take minutes or hang on large dependency trees. 2. **Markdown shows 0 code lines** — pygount classifies all Markdown content as comments, not code. This is expected behavior. 3. **JSON files show low code counts** — pygount may count JSON lines conservatively. For accurate JSON line counts, use `wc -l` directly. 4. **Large monorepos** — for very large repos, consider using `--suffix` to target specific languages rather than scanning everything.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/codebase-inspection/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
