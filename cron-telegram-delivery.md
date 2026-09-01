---
type: concept
title: Cron Telegram Delivery
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - devops
---

# cron-telegram-delivery

"Format no_agent cron output as Telegram HTML."

## Usage

# cron-telegram-delivery

Format `no_agent` cron job stdout so it renders richly in Telegram. Telegram's Bot API supports `parseMode=HTML` — the cron harness passes stdout through as-is, so the script itself produces HTML.

## What Telegram HTML supports

Telegram's HTML parseMode is **selective** — not full HTML/CSS. Supported tags:

| Tag | Renders | Notes |
|-----|---------|-------|
| `<b>` / `<strong>` | **bold** | Use for labels, titles, emphasis |
| `<i>` / `<em>` | *italic* | Use for de-emphasized metadata, source lines |
| `<code>` / `<tt>` | monospace | Use for numbers, tickers, paths, dollar amounts |
| `<u>` / `<ins>` | underlined | Limited use — avoid for large blocks |
| `<s>` / `<strike>` / `<del>` | ~~strikethrough~~ | Useful for "was X, now Y" |
| `<a href="...">` | clickable link | Only on real URLs; no `href="#"` |
| `<span>` with `style=` | inline color | `style="color:#555"` works; color classes do NOT |

**Tags that do NOT render** (Telegram strips them silently):

- `<div>`, `<p>`, `<br>`, `<hr>`, `<h1>`-`<h6>` — block layout tags
- `class=` attributes on any element — stripped on render (the raw HTML retains them, but Telegram ignores them). Don't waste effort on CSS classes.
- `<tr>`, `<td>`, `<th>`, `<table>` — table layout tags. Use inline layout instead.
- Any tag not in the supported list above.

**Inline `style=` on `<span>`**: Telegram does honor `style="color:#hex"` on span elements. Use it for semantic coloring (positive/negative deltas, warnings). Keep it minimal — one color per span, no complex CSS.

## Delivery mechanics

`no_agent` cron jobs deliver stdout verbatim to Telegram. The harness sets `parseMode=HTML` automatically for jobs with `deliver='telegram'`. No extra config needed — just produce HTML in the script.

For `agent` cron jobs (LLM-driven), the agent's final text response is delivered as plain text. To get HTML, the agent must produce HTML in its final response, but this is fragile — prefer `no_agent` scripts for formatted output.

## Common delivery shapes

### Stat dashboard (one-row metrics)

```
<b>Title</b> — <b>date</b>
<b>Label:</b> <code>value</code> <span style="color:green">+5</span> | <b>Label2:</b> <code>value2</code>
```

One logical line per metric group, pipe-separated. Avoid newlines mid-statement — Telegram wraps long lines but breaking mid-statistic loses coherence.

### Sectioned report

```
<b>Section</b>
  <b>Item:</b> <code>value</code>
  <i>metadata</i>
```

Use blank lines between sections. Indent with 2 spaces for sub-items.

### Progress bars (visual %)

Since `<table>` and CSS don't render, use Unicode block characters in `<span>` with color:

```
<span style="color:#555">█████████</span><span style="color:#999">░</span> <span class="pct">95%</span>
```

Filled = dark gray (`#555`), empty = light gray (`#999`). The `%` label goes in its own span.

### Delta indicators

For changes vs previous period:

- Positive delta: `<b>+5</b>` (bold draws attention)
- Negative delta: 

...(truncated)