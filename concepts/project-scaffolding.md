---
date: 2026-07-19
type: concept
title: Project Scaffolding
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/project-scaffolding
description: A systematic, multi-stage workflow for transforming ad-hoc, unsorted,
  or semi-finished technical/experimental directories into a standardized, maintainable,
  and highly readable project structure. Ideal for scientific research, hackathons,
  and AI development environments with repository sprawl.
---

# Project Scaffolding

> A systematic, multi-stage workflow for transforming ad-hoc, unsorted, or semi-finished technical/experimental directories into a standardized, maintainable, and highly readable project structure. Ideal for scientific research, hackathons, and AI development environments with repository sprawl.

## Overview

- **Overview** — This skill provides a systematic, multi-stage workflow for transforming a collection of ad-hoc, unsorted, or semi-finished technical/experimental directories into a standardized, maintainable, and highly readable project structure. It is designed for research labs, hackathons, or AI development environments where rapid prototyping leads to repository sprawl.
- **Workflow** — The process MUST follow these steps to ensure structural integrity and high documentation quality:
- **Pitfalls & Best Practices** — - **Do not** copy raw code as documentation. Use pseudo-code or command examples. - When creating a new `README.md` for a directory, always prioritize the `Key Learning` section above all others; this captures the highest value for future self. - Always use absolute paths for any command references (`./sub-module/script.sh`). - **Use consistent project location:** Create new projects in `~/Downloads/10-projects/10-active-projects/` rather than ad-hoc locations like `~/clawd/` or workspace-specific directories. Follow the standard subdirectory structure: `repo/` for cloned repositories, `script

## Further detail

### Support Files

* **references/**: Store examples of input data formats or error code catalogs found during the process. * **templates/**: Store boilerplates for `README.md` structure or component package scaffolds. * **scripts/**: Scripts to automatically validate the directory structure (e.g., a script to check if all sub-modules contain a required boilerplate file).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/project-scaffolding/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
