---
type: concept
title: Docx
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Docx
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- productivity
- docx
- word
- documents
- office
- reports
sources:
- hermes://skill/docx
description: 'Create, read, edit, and manipulate Word documents (.docx files). Use
  for reports, memos, letters, templates, or any professional document with formatting
  (TOC, headings, tables, images, tracked changes). Uses docx-js (npm) for creation
  and python-docx/pandoc for reading. Triggers on: ''.docx'', ''Word doc'', ''report'',
  ''memo'', ''letter'', ''template'', ''create a document''.'
---

# Docx

> Create, read, edit, and manipulate Word documents (.docx files). Use for reports, memos, letters, templates, or any professional document with formatting (TOC, headings, tables, images, tracked changes). Uses docx-js (npm) for creation and python-docx/pandoc for reading. Triggers on: '.docx', 'Word doc', 'report', 'memo', 'letter', 'template', 'create a document'.

## Overview

- **Overview** — A `.docx` file is a ZIP archive containing XML files. Two approaches: - **docx-js** (npm): Best for creating new documents from scratch - **python-docx** or **pandoc**: Best for reading/analyzing content
- **Quick Reference** — | Task | Approach | |------|----------| | Read/analyze content | `pandoc --track-changes=all document.docx -o output.md` | | Create new document | `npm install -g docx` → Node.js script (see below) | | Edit existing document | `python3 -c "from docx import Document; doc = Document('file.docx')"` |
- **Creating New Documents (docx-js)** — Use the `docx` npm package for professional documents.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/docx/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
