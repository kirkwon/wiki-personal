---
created: 2026-08-23
updated: 2026-08-23
---

--
# MARP Presentation Creation

Creating structured, slide-based markdown presentations using the MARP framework with custom styling, emoji icons, and visual hierarchy.

## Purpose
Transform linear documentation into engaging, navigable presentation format. Ideal for knowledge synthesis, teaching, and explaining complex topics.

## Five-Step Workflow

### Step 1: Frontmatter Setup
Enable MARP processor with custom theme and CSS variables for color theming. Use `marp: true`, `theme: default/gaia/uncover`, `paginate: true`, and a `style:` block.

### Step 2: Organize into Slides
Structure content using `---` as slide separators. Slide types include title slides, content slides, comparison slides, and flow/chain slides.

### Step 3: Visual Hierarchy
Apply size, weight, color coding, and highlight boxes to guide viewer attention. Follow rules: 1.5-2x heading size ratio, ≤4 main colors, 1-2 emojis per slide.

### Step 4: Navigation & Flow
Create logical progression through sequential, thematic, or problem-solution patterns. Use section footers and clear headings.

### Step 5: Generate Output
Convert to HTML, PDF, or PNG using the MARP CLI: `marp presentation.md`, `marp presentation.md --pdf`, `marp presentation.md --images`.

## Metrics & Constraints
- 10-20 slides for 20-40 min presentation
- 20-50 words per slide max
- 1-3 minutes per slide
- ≤4 main colors for coherence
- 1-2 emojis per slide maximum
- Font size ≥12pt for code blocks

## When to Use
- Explaining complex topics to others
- Creating training materials or tutorials
- Synthesizing research into digestible format
- Building knowledge graphs or system explanations
- Teaching step-by-step processes
- Comparing alternatives or frameworks
- Documenting project overviews

## When to Stop Using
- Live audience presentations (use dedicated software)
- Advanced animations needed (MARP has limited support)
- Content changes rapidly (manual rebuild is slow)
- Collaborative editing required
- Interactive elements needed

## Tools
- MARP CLI (`@marp-team/marp-cli`)
- Markdown editors: VS Code, Obsidian, Typora
- Optional: marp-vscode extension, marpit for advanced customization

## Related
- [[markdown-to-presentation-conversion]] — Core conversion process
- [[visual-hierarchy-in-slides]] — Visual design techniques
- [[slide-organization-patterns]] — Structuring content
- [[css-variables-for-theming]] — Color theming approach
- [[framework-template]] — Template structures
- [[markdown-documentation]] — Structured writing
- [[knowledge-synthesis]] — Combining sources

See also: [[technical-writing]]
