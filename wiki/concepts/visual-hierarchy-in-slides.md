---
type: concept
title: Visual Hierarchy in Slides
description: "--
Visual Hierarchy in Slides"
created: 2026-04-29
updated: 2026-04-29
tags:
- presentation
- visual-design
- slides
- markdown
sources:
- MARP Presentation Creation.md
related:
- marp-presentation-creation
- markdown-to-presentation-conversion
- data-visualization
---
--
# Visual Hierarchy in Slides

Guiding viewer attention through deliberate use of size, weight, color, and layout elements in slide-based presentations.

## Techniques

### Size and Weight
- H1 for main titles (largest)
- H2 for section titles (medium)
- H3 for subtitles (small)
- **Bold** for emphasis
- *Italic* for subordination

### Color Coding
Use CSS variables to assign consistent meaning to colors across slides:
- Primary color for main concepts
- Secondary color for supporting elements
- Warm colors for warnings or important notes
- Cool colors for contextual information

### Highlight Boxes
Structured callout boxes that summarize key insights, using gradients and border styling to draw attention.

### Grid Layouts
Side-by-side comparisons using CSS grid for presenting related concepts or alternatives.

## Rules
1. Main heading should be 1.5-2x larger than subheadings
2. Use color to distinguish related vs. contrasting concepts
3. Highlight boxes should summarize key takeaway
4. Grid layouts for side-by-side comparisons
5. Emoji icons for quick scanning (use consistently)

## Metrics
- ≤4 main colors for coherence
- 1-2 emojis per slide maximum
- Font size ≥12pt for code blocks
- 20-50 words per slide maximum

## Related
- [[marp-presentation-creation]] — Full presentation workflow
- [[data-visualization]] — Charts and graphs in presentations
- [[visual-design]] — Creating clear, hierarchical layouts