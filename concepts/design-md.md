---
type: concept
title: Design Md
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Design Md
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- design
- design-system
- tokens
- ui
- accessibility
- wcag
- tailwind
- dtcg
- google
- creative
sources:
- hermes://skill/design-md
description: Author/validate/export Google's DESIGN.md token spec files.
---

# Design Md

> Author/validate/export Google's DESIGN.md token spec files.

## Overview

- **When to use this skill** — - User asks for a DESIGN.md file, design tokens, or a design system spec - User wants consistent UI/brand across multiple projects or tools - User pastes an existing DESIGN.md and asks to lint, diff, export, or extend it - User asks to port a style guide into a format agents can consume - User wants contrast / WCAG accessibility validation on their color palette
- **Overview** — Architectural Minimalism meets Journalistic Gravitas...
- **Colors** — - **Primary (#1A1C1E):** Deep ink for headlines and core text. - **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.

## Further detail

### Typography

Public Sans for everything except small all-caps labels...

### Components

`button-primary` is the only high-emphasis action on a page...

### Token types

| Type | Format | Example | |------|--------|---------| | Color | any CSS color (hex, `rgb()`, `oklch()`, named) | `"#1A1C1E"`, `"oklch(62% 0.18 250)"` | | Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `-0.02em` | | Token reference | `{path.to.token}` | `{colors.primary}` | | Typography | object with `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation` | see above |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/design-md/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
