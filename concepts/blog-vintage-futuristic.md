---
date: 2026-08-02
type: concept
title: Blog Vintage Futuristic
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/blog-vintage-futuristic
description: Generates a luxury vintage-futuristic developer blog structure (HTML/CSS/JS)
  for an existing Clawd project.
---

# Blog Vintage Futuristic

> Generates a luxury vintage-futuristic developer blog structure (HTML/CSS/JS) for an existing Clawd project.

## Overview

- **When to Use** — - You have run `project_scaffolder` to create a project structure (e.g., `~/clawd/NNN.blog-name/`) - You want to add a blog frontend with the specified vintage-futuristic design - You plan to write blog posts in Markdown under `content/blogs/`
- **What It Creates** — When run from the project root, this skill creates:
- **Execution Steps** — Run this skill from the root of your Clawd project (where `INDEX.md` and `AGENTS.md` reside):

## Further detail

### Customization

- **Pedestal Models**: Place additional SVG models in `assets/models/` and edit `js/main.js` to rotate through them. - **Styling**: Adjust colors in `css/style.css` (look for `--bg-primary`, `--accent-gold`, etc. if you prefer CSS variables). - **Markdown Rendering**: Replace the `<pre>` block in `js/main.js` with a Markdown-to-HTML converter (e.g., using `marked.js`) for rich content. - **Extending the Grid**: Add more `<div class="card" data-md-src="content/blogs/your-post.md"></div>` to `index.html`.

### Integration Notes

- **Project Structure**: Assumes the standard Clawd project layout from `project_scaffolder`. Does not modify `INDEX.md`, `AGENTS.md`, or other project files. - **Assets**: The skill does not create `assets/models/` by default; add your own SVG models there or edit `js/main.js` to use embedded SVGs. - **Dependencies**: Zero external dependencies—plain HTML, CSS, and JavaScript. Works in any modern browser. - **Performance**: All assets are lightweight; the page loads instantly.

### Pitfalls to Avoid

- **Running Outside a Project**: This skill expects to be run in a Clawd project root. Running elsewhere may create misplaced files. - **Overwriting Existing Files**: The skill will overwrite `index.html`, `css/style.css`, and `js/main.js` if they exist. Back up first if you have customizations. - **Missing Model SVGs**: The pedestal swap expects SVG files in `assets/models/`. If missing, the pedestal will show a missing image placeholder. Either add SVGs or edit `js/main.js` to use a single model or alternative effect. - **Markdown Safety**: The current implementation displays raw Markdown. F

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/blog-vintage-futuristic/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
