---
type: concept
title: Hermes Themes
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - uncategorized
---

# hermes-themes

"Author a Hermes color theme that skins every surface."

## Usage

# Hermes Themes Skill

Author a Hermes **skin** — one YAML file that themes the CLI, the TUI, and the
desktop GUI at once. The skin engine (`hermes_cli/skin_engine.py`) resolves the
active skin and the gateway pushes it to every surface, so a file dropped in
`~/.hermes/skins/` is the theme analogue of a plugin: no code, all surfaces. This
skill covers writing a good skin and activating it; it does not build GUI theme
editors or ship built-in presets.

## When to Use

- The user asks for a custom look ("make me a synthwave theme", "dark forest
  vibes", "match my brand colors") for Hermes itself.
- The user wants the CLI/TUI/desktop to share one coordinated palette.
- The user wants to iterate live ("that coral is too loud, make it teal") — edit
  the active skin's YAML and every surface repaints as your tool finishes.

## Prerequisites

- Write access to the Hermes home dir — `~/.hermes` by default, or `$HERMES_HOME`
  / the active profile's dir. Skins live in `<hermes-home>/skins/`.
- Native tools: `write_file` (create the YAML), `read_file` / `search_files`
  (inspect existing skins), `terminal` (activate via `hermes config set`).

## How to Run

1. Pick a lowercase, hyphen-safe `name` (e.g. `synthwave`).
2. Copy `templates/skin.yaml` and fill in the palette (keep every key — missing
   keys inherit the `default` skin).
3. `write_file` it to `<hermes-home>/skins/<name>.yaml`.
4. Activate it (see Procedure). Confirm the change landed.

## Quick Reference — element → key

Hex (`#rrggbb`). Theming is **semantic**: one key colors every element that plays
that role, so match the element to its key. To recolor a specific element, set the
key in its row (element-specific keys fall back to the shared one when unset).

| Visible element | Key to set | Falls back to |
|---|---|---|
| App background (whole TUI + GUI) | `background` | terminal default |
| **Tool-call marker** (`●`, tool spinner) | `ui_tool` | `ui_accent` |
| **Thinking / reasoning text** | `ui_thinking` | `banner_dim` |
| Accent — headings, links, chevrons, `Σ` | `ui_accent` / `banner_accent` | — |
| Heading / primary text | `banner_title` / `ui_primary` | — |
| Body / label text, user messages | `ui_text` / `banner_text`, `ui_label` | — |
| Muted / secondary, tree connectors | `banner_dim` | — |
| Borders, rules, gutters | `ui_border` / `banner_border` | — |
| Prompt symbol color | `prompt` | `banner_text` |
| Success / warn / error | `ui_ok` / `ui_warn` / `ui_error` | — |
| Status bar text + usage | `status_bar_text`, `status_bar_good/warn/bad/critical` | — |
| Diff add/remove (line + word) | `diff_added` / `diff_removed` / `diff_added_word` / `diff_removed_word` | built-in |
| Code syntax (string/number/keyword/comment) | `syntax_string` / `syntax_number` / `syntax_keyword` / `syntax_comment` | accent/text/border/muted |
| Completion menu | `completion_menu_bg` / `completion_menu_current_bg` / `…_meta_bg` | — |

Note the sharing: `ui_accent` colors tool markers **and** headings/links/ch

...(truncated)