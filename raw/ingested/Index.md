---
ingested: '2026-04-24'
sha256: b517339d19a6d04b4885be47ea1023d184eb2e8c461dd50d155d932e44646d72
source_path: Index.md
date: 2026-05-14
title: Personal Knowledge Vault
type: note
created: '2026-05-14'
updated: '2026-05-14'
---
-



# Personal Knowledge Vault

**Personal interests, clients, and local knowledge**

> *"The only way to do great work is to love what you do."* — Steve Jobs

---

## 🚀 Quick Start

1. **Browse by Portal** - Curated entry points for each domain
2. **Explore by Domain** - Organized folders for concepts, frameworks, resources
3. **Inbox** - Quick capture for new ideas and notes

---

## 📚 Portals

| Portal | Description | Topics |
|--------|-------------|--------|
| [[portal-gastronomy]] | Cooking techniques, recipes, flavor theory | Wok cooking, salmon collars, ingredients |
| [[portal-personal-clients]] | Client projects and notes | Work tracking, deliverables |
| [[portal-local-interests]] | Bay area and personal interests | Local businesses, activities |
| [[music-theory-jazz]] | Music theory, jazz history, improvisation | Miles Davis, jazz harmony, scales |
| [[quant-strategy]] | Factor investing, momentum, systematic trading | Factor analysis, algorithmic trading |
| [[cognitive-science-decisions]] | Decision-making frameworks, cognitive biases | Mental models, pre-mortem analysis |
| [[local-san-francisco]] | SF neighborhoods, restaurants, attractions | Sunset District, Ocean Beach, local guides |
| [[photography]] | Camera basics, composition, street photography | Fundamentals, editing, lighting |

---

## 📁 Browse by Domain

### Music Theory & Jazz
- [[Music Theory & Jazz/music-theory-fundamentals]] - Music theory basics
- [[Music Theory & Jazz/jazz-harmony]] - Jazz chords and progressions
- [[Music Theory & Jazz/miles-davis]] - Jazz legend biography and style

### Quant Strategy
- [[Quant Strategy/factor-investing]] - Value, momentum, quality factors
- [[Quant Strategy/momentum-strategy]] - Trend-following strategies

### Cognitive Science & Decisions
- [[Cognitive Science & Decisions/cognitive-biases-library]] - Systematic biases in thinking
- [[Cognitive Science & Decisions/decision-making-frameworks]] - Structured decision-making approaches

### Local San Francisco
- [[Local San Francisco/sunset-district]] - Sunset District neighborhood guide
- [[Local San Francisco/ocean-beach]] - Ocean Beach activities and tips
- [[Local San Francisco/golden-gate-heights]] - Hilltop neighborhood with views
- [[Local San Francisco/san-francisco-city-guide]] - Complete SF city guide
---

### Photography
- [[Photography/photography-fundamentals]] - Camera basics, exposure triangle, settings
- [[Photography/composition-techniques]] - Rule of thirds, leading lines, framing
- [[Photography/street-photography]] - Candid urban photography, ethics, techniques
- [[Photography/post-processing]] - Editing workflow, Lightroom, Photoshop
- [[Photography/golden-hour]] - Best lighting conditions, timing, planning

### Personal Clients
- [[Personal Clients/Concepts]] - Client domains and needs
- [[Personal Clients/Frameworks]] - Work processes and methodologies
- [[Personal Clients/Resources]] - Client materials, requirements
- [[Personal Clients/Notes]] - Project notes, meetings, follow-ups

### Gastronomy
- [[Gastronomy/Concepts]] - Cooking techniques, flavor theory
- [[Gastronomy/Frameworks]] - Recipe structures, prep workflows
- [[Gastronomy/Resources]] - Books, techniques, ingredient guides
- [[Gastronomy/Notes]] - Experiments, taste notes, ideas

### Local Interests
- [[Local Interests/Concepts]] - Local knowledge, neighborhood info
- [[Local Interests/Frameworks]] - Routines, workflows
- [[Local Interests/Resources]] - Local businesses, services
- [[Local Interests/Notes]] - Discovery notes, favorites

---

## 🏷️ Categories

- [[category-cooking-techniques]]
- [[category-recipes]]
- [[category-ingredients]]
- [[category-flavor-profiles]]
- [[category-client-projects]]
- [[category-local-businesses]]
- [[category-music-theory]]
- [[category-jazz-theory]]
- [[category-jazz-artists]]
- [[category-factor-investing]]
- [[category-momentum]]
- [[category-cognitive-biases]]
- [[category-decision-making]]
- [[category-neighborhoods]]
- [[category-beaches]]
- [[category-photography]]
- [[category-composition]]
- [[category-street-photography]]
- [[category-lighting]]

---

## 🛠️ Templates

| Template | Use Case |
|----------|----------|
| [[Templates/Concept]] | Ideas, techniques, definitions |
| [[Templates/Framework]] | Recipes, workflows, processes |
| [[Templates/Resource]] | Books, tools, client materials |

---

## 📥 Inbox

[[inbox]] - Quick capture zone for unstructured notes

---

## 🔍 Dataview Queries

### Recent Notes
```dataview
TABLE
  type,
  created,
  tags
FROM ""
WHERE created >= date(today) - dur(7 days)
SORT created DESC
```

### By Domain
```dataview
TABLE rows.file.link[0] AS "Note", type, status
FROM ""
GROUP BY file.folder
SORT file.folder ASC
```

---

*Vault created: 2026-04-20 | Last updated: 2026-04-20*
