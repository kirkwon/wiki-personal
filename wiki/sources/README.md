---
type: source
title: 'Source: README.md'
created: 2026-05-12
updated: 2026-05-12
sources:
- README.md
tags: []
related: []
---
-

# Source: README.md

The provided **README.md** document outlines a structured, Wikipedia-inspired personal knowledge vault system designed for organizing and managing information across three domains: **Gastronomy**, **Personal Clients**, and **Local Interests**. Below is a detailed analysis of its components, structure, and functionality:

---

### **1. Core Structure & Organization**
#### **Root Directory Layout**
- **Templates/**: Contains note templates for consistent formatting (Concepts, Frameworks, Resources).
- **Portals/**: Topic hubs for curated navigation (e.g., `Portal:Gastronomy.md`).
- **Categories/**: Organizational pages grouping related content (e.g., `Category:Cooking Techniques.md`).
- **Inbox/**: A catch-all for unstructured notes before categorization.
- **Settings/**: Vault configuration files.
- **[Domain]/**: Domain-specific folders with subfolders:
  - **Concepts/**: Definitions, techniques, and ideas.
  - **Frameworks/**: Recipes, workflows, and processes.
  - **Resources/**: Books, tools, and client materials.
  - **Notes/**: General observations and unstructured content.

#### **Naming Conventions**
- **Concepts**: PascalCase (e.g., `Wok Hei.md`).
- **Frameworks**: PascalCase (e.g., `Perfect Stir-Fry.md`).
- **Resources**: `Resource:[Title]` (e.g., `Resource:Salt Fat Acid Heat.md`).
- **Categories**: `Category:[Name]` (e.g., `Category:Cooking Techniques.md`).
- **Portals**: `Portal:[Name]` (e.g., `Portal:Gastronomy.md`).

---

### **2. Design Philosophy**
#### **Wikipedia-Inspired Frontmatter**
- Every note includes a `## Vault Overview` section with structured metadata:
  ```yaml
  - **Domain**: [[]]
  ### Type: [[]]
  - **Key Features**: [[]]
  - **Related**: [[]]
  ```
- **Portal Pages**: Act as hubs with:
  - Subtopic navigation.
  - Featured resources and techniques.
  - Learning paths and cross-references.
- **Category Pages**: Organize content by domain with:
  - Definitions and subcategories.
  - Key concepts, frameworks, and resources.
- **Cross-Linking**: Uses `[[WikiLink]]` format and `related: []` in frontmatter for internal linking.

---

### **3. Workflows**
#### **Adding New Content**
1. **Inbox Capture**: Start with unstructured notes in `Inbox/`.
2. **Categorization**: Move to domain-specific folders.
3. **Template Use**: Apply structured templates for consistency.
4. **Linking**: Add to Category and Portal pages for discoverability.

#### **Querying Content**
- Uses **Dataview** plugin for dynamic queries (e.g., filtering by domain, status, or tags):
  ```dataview
  TABLE type, status, tags
  FROM ""
  WHERE category = "Gastronomy"
  ```

---

### **4. Maintenance & Quality Standards**
#### **Regular Tasks**
- Weekly review of `Inbox/` items.
- Update Category and Portal pages with new content.
- Refresh "Featured" sections in Portals.
- Fix broken links using the **Links** plugin.

#### **Quality Standards**
- **Techniques**: Must include descriptions and examples.
- **Recipes**: Require ingredients, steps, and timing.

