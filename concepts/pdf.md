---
date: 2026-07-19
type: concept
title: Pdf
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- productivity
- pdf
- documents
- ocr
- extraction
sources:
- hermes://skill/pdf
description: 'Process PDF files — read, extract text/tables, merge, split, rotate,
  encrypt/decrypt, watermark, OCR scanned PDFs, and create new PDFs. Uses pypdf, pdfplumber,
  reportlab, and pytesseract. Triggers on: ''.pdf'', ''PDF'', ''scan'', ''merge PDFs'',
  ''extract from PDF'', ''OCR''.'
---

# Pdf

> Process PDF files — read, extract text/tables, merge, split, rotate, encrypt/decrypt, watermark, OCR scanned PDFs, and create new PDFs. Uses pypdf, pdfplumber, reportlab, and pytesseract. Triggers on: '.pdf', 'PDF', 'scan', 'merge PDFs', 'extract from PDF', 'OCR'.

## Overview

- **Quick Reference** — | Task | Tool | Command | |------|------|---------| | Read/extract text | pypdf | `PdfReader("doc.pdf").pages[0].extract_text()` | | Extract tables | pdfplumber | `page.extract_tables()` | | Merge PDFs | pypdf | `writer.add_page(page)` loop | | Split PDFs | pypdf | One page per file | | Create PDFs | reportlab | `canvas.Canvas("out.pdf")` | | OCR scanned PDF | pytesseract | Convert to image → OCR | | Encrypt/decrypt | pypdf | `writer.encrypt(password)` | | Add watermark | pypdf | `page.merge_page(watermark)` | | CLI merge | qpdf | `qpdf --empty --pages a.pdf b.pdf -- merged.pdf` |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/pdf/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
