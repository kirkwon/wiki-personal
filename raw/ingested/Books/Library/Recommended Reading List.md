---
ingested: '2026-04-24'
sha256: 9054940141671efbcfa079f0f44d98428ada400b722a45d3731df7ecf13dbabe
source_path: Books/Library/Recommended Reading List.md
title: Recommended Reading List
type: note
created: '2026-05-14'
updated: '2026-05-14'
---
-



# Recommended Reading List


## Quick Reference

### Source**: Apple Notes Migration
### Total Books**: 26
### Categories**: 8
### Status**: To-Read
### Source Note**: "For each book I have 2 artifacts..."



## Summary

This reading list was extracted from Apple Notes and represents a curated collection covering behavioral economics, systems thinking, philosophy, productivity, business strategy, and mental models.

## Categories

### Behavioral Economics & Decision-Making

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | Predictably Irrational | Dan Ariely | to-read |
| 2 | The Signal and the Noise | Nate Silver | to-read |
| 3 | The Art of Thinking Clearly | Rolf Dobelli | to-read |
| 4 | Range | David Epstein | to-read |
| 5 | The Wisdom of Crowds | James Surowiecki | to-read |

### Systems & Complexity

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | Systems Thinking for Social Change | David Peter Stroh | to-read |
| 2 | Out of Control | Kevin Kelly | to-read |
| 3 | The Beginning of Infinity | David Deutsch | to-read |
| 4 | The Systems Bible | John Gall | to-read |

### Antifragility & Uncertainty

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | The Art of War | Sun Tzu | to-read |
| 2 | Meditations | Marcus Aurelius | to-read |
| 3 | Letters from a Stoic | Seneca | to-read |
| 4 | On the Shortness of Life | Seneca | to-read |
| 5 | Man's Search for Meaning | Viktor Frankl | to-read |

### Productivity & Focus

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | Indistractable | Nir Eyal | to-read |
| 2 | Hyperfocus | Chris Bailey | to-read |
| 3 | The Power of Habit | Charles Duhigg | to-read |
| 4 | Make Time | Jake Knapp & John Zeratsky | to-read |

### Leadership & Organizations

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | The Five Dysfunctions of a Team | Patrick Lencioni | to-read |

### Business Strategy & Innovation

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | The Lean Startup | Eric Ries | to-read |
| 2 | Blue Ocean Strategy | W. Chan Kim & Renee Mauborgne | to-read |
| 3 | Hooked | Nir Eyal | to-read |

### Mental Models & Learning

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | Super Thinking | Gabriel Weinberg | to-read |
| 2 | The Model Thinker | Scott E. Page | to-read |
| 3 | How to Solve It | George Polya | to-read |

### Philosophy & Wisdom

| # | Title | Author | Status |
|---|-------|--------|--------|
| 1 | Beyond Good and Evil | Friedrich Nietzsche | to-read |

## Learning Path

### Phase 1: Foundations (Decision-Making)
1. [[predictably-irrational]] - Dan Ariely - Understanding behavioral economics
2. [[the-art-of-thinking-clearly]] - Rolf Dobelli - Cognitive bias primer
3. [[super-thinking]] - Gabriel Weinberg - Mental models

### Phase 2: Systems (Complexity Thinking)
1. [[the-systems-bible]] - John Gall - System dynamics
2. [[out-of-control]] - Kevin Kelly - Emergent behavior
3. [[the-model-thinker]] - Scott E. Page - Multi-model thinking

### Phase 3: Wisdom (Philosophy & Resilience)
1. [[meditations]] - Marcus Aurelius - Stoic philosophy
2. [[man-s-search-for-meaning]] - Viktor Frankl - Existential psychology
3. [[the-art-of-war]] - Sun Tzu - Strategy and antifragility

### Phase 4: Application (Productivity & Business)
1. [[indistractable]] - Nir Eyal - Focus mastery
2. [[the-lean-startup]] - Eric Ries - Business strategy
3. [[the-five-dysfunctions-of-a-team]] - Patrick Lencioni - Leadership

## Individual Book Entries

Each book should have:
- YAML frontmatter with title, author, category
- 1500-word summary in specific format
- Frameworks/skills extracted into separate files
- Key takeaways and practical applications
- Related concepts and cross-references

## Dataview Queries

### By Category
```dataview
TABLE
  author,
  category,
  status
FROM "Books/Library"
SORT category ASC, title ASC
```

### By Status
```dataview
TABLE
  author,
  category
FROM "Books/Library"
WHERE status = "to-read"
SORT category ASC
```

### Reading Progress
```dataview
TABLE
  count as "Books",
  status
FROM "Books/Library"
GROUP BY category
```

## Migration Notes

- **Source**: Apple Notes migration (April 2025)
- **Original Note**: "For each book I have 2 artifacts..."
- **Next Steps**: Create individual book entries with summaries and skill extractions

## See Also

- [[index]] - Personal vault index
- [[Gastronomy/Index]] - Other interests
- [[Cognitive/Index]] - Mental models and biases

---
*Migrated from Apple Notes • Created: 2025-04-20*

---
