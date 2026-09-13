---
type: concept
title: Productivity Master
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - uncategorized
---

# productivity-master

"Meta-skill for operating your digital life — email, documents, notes, calendar, communication, and Apple ecosystem."

## Usage

# productivity-master

Meta-skill for operating your digital life — handle email, manage documents, write notes, communicate, and control Apple ecosystem tools.

Unlike knowledge-master (pipeline) and finance-master (toolkit), productivity is a **workspace** — each tool handles a different surface area of daily operations. The meta-master routes to the right tool based on the surface area.

## Decision Mechanisms

### A. Email & Inbox Routing

| User says | Dispatch to | Why |
|---|---|---|
| "Check email" | `gmail` | Search, read, list |
| "Send email" | `email-sending` or `gmail` | Both can send; gmail for composed, email-sending for quick |
| "Triage inbox" | `inbox-triage` | Automated categorization |
| "Any urgent messages?" | `gmail` + `inbox-triage` | Check + categorize |

**Fallback chain**: `gmail` → `inbox-triage`. Gmail gives raw access; inbox-triage adds Bayes filters.

### B. Documents & Files Routing

| User says | Dispatch to | Why |
|---|---|---|
| "Create a doc/spreadsheet" | `google-workspace` | GWorkspace create/write |
| "Edit PDF" | `nano-pdf` | PDF text editing |
| "Create a Word doc" | `docx` | .docx creation/editing |
| "Create a spreadsheet" | `xlsx` | .xlsx with formulas/formatting |
| "Create a presentation" | `pptx` | .pptx slide deck |
| "Process a PDF" | `pdf` | Read, merge, split, OCR, create PDFs |
| "Convert any document to markdown" | `markitdown` | Universal: PDF/DOCX/XLSX/PPTX/HTML → MD |
| "Compare docx/pptx/xlsx conversion quality" | `anydoc` | Rust-based second opinion when markitdown output looks off |
| "Extract text from scan" | `ocr-and-documents` | OCR pipeline |
| "Convert format" | `unify-document-formats` | Format conversion |
| "Fix workspace auth" | `google-workspace-troubleshooting` | OAuth/debugging |

**Decision tree for document tasks**:
```
"Handle this document"
    ├── PDF edit: nano-pdf
    ├── Scan/OCR: ocr-and-documents
    ├── Format convert: unify-document-formats
    ├── New doc/sheet: google-workspace
    └── Generic: google-workspace (broadest tool)
```

### C. Notes & Sessions Routing

| User says | Dispatch to | Why |
|---|---|---|
| "Log this session" | `session-logging` | Structured gbrain logging |
| "Take a note" | `apple-notes` | Apple Notes |
| "Set a reminder" | `apple-reminders` | Apple Reminders |
| "Review my notes" | `session-logging` + `conversation-logging-review` | Review cycle |

### D. System Documentation Routing

| User says | Dispatch to | Why |
|---|---|---|
| "Document this system" | `session-logging` (capture) + manifests | Capture system state from all masters |
| "Produce a manifest" | Structured markdown doc with supporting visuals | Write manifest + generate diagrams |
| "Show me the architecture" | Cross-reference `architecture-documentation` (heavy) OR manifest (lightweight) | Heavy archaeology vs light manifest |
| "What does the system look like?" | Manifest first, then diagrams via creativity-master | Text overview + visual supplement |
| "Visualize t

...(truncated)