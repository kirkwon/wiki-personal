---
source_url: https://marp.app/
ingested: 2026-04-29
sha256: a1b2c3d4e5f6789012345678901234567890abcd1234567890abcdef12345678
title: MARP Presentation Creation
type: note
created: '2026-05-14'
updated: '2026-05-14'
---
-

# MARP Presentation Creation

**Purpose**: Create structured, slide-based markdown presentations using MARP framework with custom styling, emoji icons, and visual hierarchy.

## Quick Reference

**Why it Matters**: Transform linear documentation into engaging, navigable presentation format. Perfect for knowledge synthesis, teaching, and explaining complex topics.

**The Big Picture**: Write markdown with MARP frontmatter → organize into slides → convert to HTML/PDF → present.

**The Bottom Line**: Use markdown authoring + MARP styling = beautiful presentations without PowerPoint.

## When to Use This Skill

- Explaining complex topics to others
- Creating training materials or tutorials
- Synthesizing research into digestible format
- Building knowledge graphs or system explanations
- Teaching step-by-step processes
- Comparing alternatives or frameworks
- Documenting project overviews

## The Loop

### Step 1: MARP Frontmatter Setup

**Goal**: Enable MARP processor with custom theme and styling.

**Basic structure**:
```markdown
---
marp: true
theme: default
paginate: true
style: |
  /* Custom CSS variables */
  :root {
    --color-primary: #5b8ff9;
    --color-secondary: #61ddaa;
    --color-accent: #f6bd16;
    --color-warm: #f76b6b;
    --color-cool: #5d7092;
  }
  
  /* Highlight boxes */
  .highlight {
    padding: 1rem;
    background: linear-gradient(135deg, rgba(91, 143, 249, 0.1), rgba(97, 221, 170, 0.1));
    border-left: 4px solid var(--color-primary);
    border-radius: 4px;
  }
  
  .highlight-warm {
    padding: 1rem;
    background: linear-gradient(135deg, rgba(247, 107, 107, 0.1), rgba(246, 189, 22, 0.1));
    border-left: 4px solid var(--color-warm);
    border-radius: 4px;
  }
  
  /* Section headers */
  section[data-auto-scaling] h1 {
    color: var(--color-primary);
  }
---
```

**Frontmatter options**:
- `marp: true` - Enable MARP processor
- `theme: default`/`gaia`/`uncover` - Choose built-in theme
- `paginate: true` - Show slide numbers
- `style: |` - Add custom CSS

**Best practices**:
- ✅ Use CSS variables for colors (easy to change theme)
- ✅ Define highlight boxes with gradients
- ✅ Set consistent fonts and spacing
- ❌ Don't use external stylesheets (portability issues)

---

### Step 2: Organize into Slides

**Goal**: Structure content into logical sections.

**Slide separator**: `---`

**Slide types**:

#### Title Slide
```markdown
<!-- _class: lead -->
# Main Title

### *Subtitle or description*

<br>

<div class="highlight">
**Key insight or value proposition**
</div>
```

#### Content Slide
```markdown
<!-- _footer: 'SECTION NAME' -->
## Section Title

### *Subtitle or context*

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.8rem;">
  <div style="padding: 0.6rem; background: rgba(91, 143, 249, 0.1); border-radius: 6px;">
    Content A
  </div>
  <div style="padding: 0.6rem; background: rgba(97, 221, 170, 0.1); border-radius: 6px;">
    Content B
  </div>
</div>
```

#### Comparison Slide
```markdown
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th>Aspect A</th>
      <th>Aspect B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Value 1</td>
      <td>Value 2</td>
    </tr>
  </tbody>
</table>
```

#### Flow/Chain Slide
```markdown
<div style="display: flex; flex-direction: column; gap: 0.5rem;">
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <span>Step 1</span>
    <span style="font-size: 1.2em;">→</span>
    <span>Step 2</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <span>Step 2</span>
    <span style="font-size: 1.2em;">→</span>
    <span>Step 3</span>
  </div>
</div>
```

**Slide organization tips**:
- ✅ Use `<!-- _footer: 'NAME' -->` to track sections
- ✅ Add inline comments for context
- ✅ Use emojis as visual anchors (🎯, 🧠, ⚙️)
- ✅ Keep slide count reasonable (10-20 for 20-40 min talks)
- ❌ Don't cram too much text per slide

---

### Step 3: Visual Hierarchy

**Goal**: Guide viewer's eye and emphasize key points.

**Techniques**:

#### Size & Weight
```markdown
# H1 - Main title (largest)
## H2 - Section title (medium)
### H3 - Subtitle (small)
**bold** - Emphasis
*italic* - Subordination
```

#### Color Coding
```markdown
<span style="color: var(--color-primary);">Primary concept</span>
<span style="color: var(--color-secondary);">Secondary concept</span>
<span style="color: var(--color-warm);">Warning/Important</span>
```

#### Highlight Boxes
```markdown
<div class="highlight">
**Key insight**<br>
<span style="font-size: 0.8em; color: #666;">Supporting details</span>
</div>
```

**Visual hierarchy rules**:
1. Main heading should be 1.5-2x larger than subheadings
2. Use color to distinguish related vs. contrasting concepts
3. Highlight boxes should summarize key takeaway
4. Grid layouts for side-by-side comparisons
5. Emoji icons for quick scanning (use consistently)

---

### Step 4: Navigation & Flow

**Goal**: Create logical progression through content.

**Flow patterns**:

#### Sequential Progression
```markdown
## Part 1: Foundation
<!-- Concepts A, B, C -->

---

## Part 2: Application
<!-- Concepts D, E, F -->

---

## Part 3: Synthesis
<!-- Combines A-F -->
```

#### Thematic Groups
```markdown
## Theme 1: Systems
<!-- All systems-related content -->

---

## Theme 2: Habits
<!-- All habit-related content -->

---

## Theme 3: Decisions
<!-- All decision-related content -->
```

#### Problem-Solution
```markdown
## The Problem
<!-- Describe the issue -->

---

## The Solution
<!-- Present your approach -->

---

## Implementation
<!-- How to apply it -->
```

**Navigation best practices**:
- ✅ Add section footers for tracking
- ✅ Use clear headings that preview content
- ✅ Include summary slide at end
- ✅ Reference previous slides when building on concepts
- ❌ Don't jump between unrelated topics

---

### Step 5: Generate Output

**Goal**: Convert markdown to presentable format.

**Install MARP**:
```bash
npm install -g @marp-team/marp-cli
```

**Generate HTML** (for web viewing):
```bash
marp presentation.md
# Opens in browser
```

**Export PDF** (for sharing/printing):
```bash
marp presentation.md --pdf
# Creates presentation.pdf
```

**Export PNGs** (for slides):
```bash
marp presentation.md --images
# Creates slide-001.png, slide-002.png, etc.
```

**Export with custom theme**:
```bash
marp presentation.md --theme gaia
marp presentation.md --style-path custom.css
```

---

## Tools Required

- **MARP CLI**: Presentation framework
- **Markdown editor**: VS Code, Obsidian, Typora (any with markdown support)
- **Browser**: For HTML preview
- **PDF viewer**: For exported PDFs

**Optional tools**:
- **marp-vscode**: VS Code extension for live preview
- **marp-team/marpit**: Advanced customization

---

## Timeline

**Immediate**: Set up MARP frontmatter structure (<10 min)
**Short-term**: Draft content in markdown (1-4 hours)
**Medium-term**: Apply styling and visual hierarchy (<30 min)
**Long-term**: Generate and refine PDF/PNG outputs (<30 min)
**Continuous**: Update content and regenerate as needed

---

## Metrics & Improvement

- **Slide count**: 10-20 slides for 20-40 min presentation
- **Word count per slide**: 20-50 words max
- **Average slide length**: 1-3 minutes per slide
- **Color consistency**: Use ≤4 main colors for coherence
- **Emoji usage**: 1-2 per slide maximum
- **Code readability**: Font size ≥12pt for code blocks

---

## Common Mistakes

| Mistake | Why It Happens | Correct Approach |
|---------|------------------|------------------|
| Too much text per slide | Hard to read quickly | 20-50 words max, use visuals |
| No visual hierarchy | Viewer doesn't know where to look | Use size, weight, color consistently |
| Jumping between topics | Confusing progression | Use clear transitions and section footers |
| Inconsistent styling | Looks unprofessional | Define CSS variables, use throughout |
| Missing context slides | Doesn't stand alone | Add summary, recap frequently |
| No examples | Too abstract | Add concrete examples for each concept |
| Poor contrast | Hard to read | Test colors, use gradients carefully |

---

## When to Stop Using This Skill

- When presenting to live audiences → use dedicated presentation software
- When need advanced animations → MARP has limited animation support
- When content changes rapidly → manual rebuild is too slow
- When collaborative editing required → markdown can get messy
- When you need interactive elements → MARP is static export

---

## Related Skills

- [[Markdown Documentation]] - Writing structured documentation
- [[Technical Writing]] - Explaining complex concepts clearly
- [[Visual Design]] - Creating clear, hierarchical layouts
- [[Knowledge Synthesis]] - Combining multiple sources into coherent narrative
- [[Data Visualization]] - Creating charts and graphs to support presentation

---

## Templates

### Presentation Template
```markdown
---
marp: true
theme: default
paginate: true
style: |
  :root {
    --color-primary: #007acc;
  }
  .highlight {
    padding: 1rem;
    border-left: 4px solid var(--color-primary);
    border-radius: 4px;
  }
---

<!-- _class: lead -->
# Your Title Here

### *Subtitle or description*

---

<!-- _footer: 'SECTION 1' -->
## Section 1: Context

### *Background or setup*

<div class="highlight">
**Key point**<br>
Supporting detail
</div>

---

<!-- _footer: 'SECTION 2' -->
## Section 2: Analysis

### *Examination or comparison*

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.8rem;">
  <div style="padding: 0.6rem; background: rgba(91, 143, 249, 0.1); border-radius: 6px;">
    Aspect A
  </div>
  <div style="padding: 0.6rem; background: rgba(97, 221, 170, 0.1); border-radius: 6px;">
    Aspect B
  </div>
</div>

---

<!-- _footer: 'CONCLUSION' -->
## Key Takeaways

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem;">
  <div style="padding: 0.5rem; border-left: 3px solid var(--color-primary); border-radius: 4px;">
    **Takeaway 1**
  </div>
  <div style="padding: 0.5rem; border-left: 3px solid var(--color-secondary); border-radius: 4px;">
    **Takeaway 2**
  </div>
</div>

<!-- _class: lead -->
## Thank You!

### *Questions?*

<div class="highlight">
**Remember**: Your main point
</div>
```

### Comparison Template
```markdown
## Comparison

<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th>Feature</th>
      <th>Option A</th>
      <th>Option B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Criterion 1</td>
      <td>Value 1</td>
      <td>Value 2</td>
    </tr>
    <tr>
      <td>Criterion 2</td>
      <td>Value 3</td>
      <td>Value 4</td>
    </tr>
  </tbody>
</table>

<div class="highlight">
**Recommendation**: Option A (or B) based on criteria
</div>
```

---

## Sources

- MARP Documentation: https://marp.app/
- MARP CLI: https://github.com/marp-team/marp-cli
- Marpit Core: https://github.com/marp-team/marpit
- Common Markdown: https://commonmark.org/
- Presentation Best Practices: Slide:ology and Nancy Duarte
