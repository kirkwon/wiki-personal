---
date: 2026-07-19
type: concept
title: Ocr And Documents
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- PDF
- Documents
- Research
- Arxiv
- Text-Extraction
- OCR
- productivity
sources:
- hermes://skill/ocr-and-documents
description: Extract text from PDFs/scans (pymupdf, marker-pdf).
---

# Ocr And Documents

> Extract text from PDFs/scans (pymupdf, marker-pdf).

## Overview

- **Microsoft MarkItDown (recommended for PDF→Markdown)** — **New option (2026-05-06):** Microsoft's `markitdown` (121k+ stars) handles PDF, DOCX, PPTX, Excel, images, audio, and more. Requires Python 3.10+.
- **Step1: Remote URL Available?** — If the document has a URL, **always try `web_extract` first**:
- **Step 2: Choose Local Extractor** — | Feature | pymupdf (~25MB) | marker-pdf (~3-5GB) | |---------|-----------------|---------------------| | **Text-based PDF** | ✅ | ✅ | | **Scanned PDF (OCR)** | ❌ | ✅ (90+ languages) | | **Tables** | ✅ (basic) | ✅ (high accuracy) | | **Equations / LaTeX** | ❌ | ✅ | | **Code blocks** | ❌ | ✅ | | **Forms** | ❌ | ✅ | | **Headers/footers removal** | ❌ | ✅ | | **Reading order detection** | ❌ | ✅ | | **Images extraction** | ✅ (embedded) | ✅ (with context) | | **Images → text (OCR)** | ❌ | ✅ | | **EPUB** | ✅ | ✅ | | **Markdown output** | ✅ (via pymupdf4llm) | ✅ (native, higher quality) | | **Install

## Further detail

### pymupdf (lightweight)

> **⚠️ Compatibility Note (2026-05-06):** `pymupdf4llm` requires `pymupdf>=1.26.1`, but the latest available version is currently 1.24.11. If `pip install pymupdf pymupdf4llm` fails, use one of these alternatives: > - `pip install pymupdf` alone + extract plain text (no markdown) via `python3 -c "import pymupdf; doc=pymupdf.open('file.pdf'); print(doc[0].get_text())"` > - Use `marker-pdf` (see below) for markdown output with OCR support > - For GBrain ingestion: upload raw PDF via `gbrain files upload-raw`, extract text later when deps are available

### marker-pdf (high-quality OCR)

**Via helper script**:

### Split, Merge & Search

pymupdf handles these natively — use `execute_code` or inline Python:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/ocr-and-documents/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
