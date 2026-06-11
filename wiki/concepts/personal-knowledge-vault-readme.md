---
created: '2026-04-24'
sources:
- raw/ingested/README.md
tags:
- general
title: Personal Knowledge Vault - README
type: concept
updated: '2026-04-24'
---
-
# Personal Knowledge Vault - README

## Overview
This is a Wikipedia-inspired declarative knowledge vault for personal interests including Gastronomy, Personal Clients, and Local Interests.

## Structure

### 📁 Root Directory
- `Templates/` - Note templates (Concept, Framework, Resource)
- `Portals/` - Topic hubs with curated navigation
- `Categories/` - Category pages for organizing content
- `Inbox/` - Quick capture zone for unstructured notes
- `Settings/` - Vault configuration
- `[Domain]/` - Domain-specific folders with subfolders
  - `Concepts/` - Ideas, techniques, definitions
  - `Frameworks/` - Recipes, workflows, processes
  - `Resources/` - Books, tools, client materials
  - `Notes/` - General notes and observations

### 🏷️ Naming Conventions
- **Concepts**: PascalCase (e.g., `Wok Hei.md`)
- **Frameworks**: PascalCase (e.g., `Perfect Stir-Fry.md`)
- **Resources**: `Resource:[Title]` (e.g., `Resource:Salt Fat Acid Heat.md`)
- **Categories**: `Category:[Name]` (e.g., `Category:Cooking Techniques.md`)
- **Portals**: `Portal:[Name]` (e.g., `Portal:Gastronomy.md`)

## Wikipedia-Inspired Design

### Infobox Frontmatter
Every note includes an `## Vault Overview` section with structured metadata:
```yaml
- **Domain**: [[]]
### Type: [[]]
- **Key Features**: [[]]
- **Related**: [[]]
```

### Portal Pages
Topic hubs that provide:
- Quick navigation to subtopics
- Featured resources and techniques
- Learning paths
- Cross-references to related portals

### Category Pages
Organized by domain with:
- Overview and definition
- Subcategories
- Key concepts and frameworks
- Related resources

### Cross-Linking
- Use `[[WikiLink]]` format for internal links
- Add relevant pages to `related: []` in frontmatter
- Maintain "See Also" sections at bottom of notes

## Workflows

### Adding New Content
1. Start in `Inbox/` for quick notes
2. Move to appropriate domain folder
3. Use templates for structured notes
4. Add to relevant Category and Portal pages

### Using Templates
1. Open template from `Templates/`
2. Fill in frontmatter fields
3. Populate each section
4. Add internal links to related pages

### Querying Content
Use Dataview queries (requires Dataview plugin):
```dataview
TABLE type, status, tags
FROM ""
WHERE category = "Gastronomy"
```

## Maintenance

### Regular Tasks
- Review and process Inbox items weekly
- Update category pages with new content
- Refresh portal "Featured" sections
- Fix broken links

### Quality Standards
- Every technique needs description and examples
- Every recipe needs ingredients and steps
- Every resource needs summary and key takeaways
- All notes must have proper frontmatter

## Domain-Specific Guidelines

### Gastronomy
- Focus on techniques, not just recipes
- Document flavor theory and ingredient pairings
- Include prep workflows and mise en place
- Note temperature and timing precisely

### Personal Clients
- Track project status and deliverables
- Document client preferences and requirements
- Maintain meeting notes and follow-ups
- Link relevant work products

### Local Interests
- Document discoveries and favorites
- Track local business information
- Note routines and workflows
- Maintain personal preferences

## Tools & Plugins

### Recommended Obsidian Plugins
- **Dataview** - Query vault content dynamically
- **Templater** - Template automation (optional)
- **Links** - Update broken links automatically
- **Tag Wrangler** - Manage tags easily

### Dataview Queries
See `Index.md` for example queries for:
- Recent notes
- Notes by status
- Notes by domain

## Getting Started

1. Open `Index.md` for vault overview
2. Browse by Portal or Domain
3. Use Templates for new notes
4. Add content to Categories and Portals

---

**Created:** 2026-04-20
**Last Updated:** 2026-04-20
