---
date: 2026-04-29
type: concept
title: Markdown to Presentation Conversion
description: "--
Markdown to Presentation Conversion"
created: 2026-04-29
updated: 2026-04-29
tags:
- markdown
- presentation
- slides
- documentation
- visual-design
sources:
- MARP Presentation Creation.md
related:
- marp-presentation-creation
- framework-template
- markdown-documentation
- knowledge-synthesis
---
--
# Markdown to Presentation Conversion

Converting Markdown documents into structured presentations using the MARP framework. This approach transforms linear documentation into engaging, navigable slide decks without requiring traditional presentation software.

## Core Process

The conversion pipeline follows a five-step workflow:

1. **Frontmatter Setup** — Enable MARP processor with custom theme and CSS variables for color theming
2. **Slide Organization** — Structure content using `---` as slide separators into logical sections
3. **Visual Hierarchy** — Apply size, weight, color coding, and highlight boxes to guide viewer attention
4. **Navigation & Flow** — Create logical progression through sequential, thematic, or problem-solution patterns
5. **Output Generation** — Convert to HTML, PDF, or PNG formats from a single Markdown source

## Key Techniques

### Slide Separators
Use `---` to divide content into individual slides. Each slide can have different layouts including title slides, content slides, comparison tables, and flow diagrams.

### Visual Hierarchy Rules
- Main heading should be 1.5-2x larger than subheadings
- Use color to distinguish related vs. contrasting concepts
- Highlight boxes should summarize key takeaways
- Grid layouts for side-by-side comparisons
- Emoji icons for quick scanning (1-2 per slide maximum)

### Content Constraints
- 20-50 words per slide maximum
- 10-20 slides for a 20-40 minute presentation
- 1-3 minutes per slide average
- ≤4 main colors for coherence

## Export Formats
MARP supports HTML (web viewing), PDF (sharing/printing), and PNG (individual slides) from a single Markdown source file.

## Related Concepts
- [[marp-presentation-creation]] — The full MARP workflow
- [[framework-template]] — Template structures for documentation
- [[markdown-documentation]] — Structured writing in Markdown
- [[visual-design]] — Creating clear, hierarchical layouts