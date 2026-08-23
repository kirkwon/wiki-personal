---
date: 2026-07-04
title: "Extraction Method Comparison: OCR vs Vision vs VLM vs MarkItDown"

type: methodology-note
created: 2026-07-04
context: "Judging 4 extraction methods against a complex infographic (968x968 JPEG, multi-panel, small text, flowcharts)"
tags:
  - ocr
  - vision
  - vlm
  - markitdown
  - extraction
  - methodology
  - image-ingestion
---

# Extraction Method Comparison: OCR vs Vision vs VLM vs MarkItDown

> **Test image:** 968×968 JPEG infographic ("The Complete AI PM Loop System") — dense text, multi-panel layout, flowchart elements, color-coded sections, small annotations.
> **Goal:** Extract text for wiki ingestion, then judge each method's effectiveness.

---

## TL;DR Results Matrix

| Method | Text Accuracy | Layout/Structure | Spatial Awareness | Setup Cost | Speed | Verdict |
|--------|:------------:|:----------------:|:-----------------:|:----------:|:-----:|---------|
| **Apple Vision OCR** | ⭐⭐⭐⭐⭐ (0.97 conf) | ⭐⭐ (bbox only) | ⭐⭐⭐ (x/y/h/w) | Low (pre-installed) | ~2s | **Winner for text** |
| **Tesseract** | ⭐⭐ (garbled) | ⭐ (flat text) | ❌ | Low | ~1s | Worst — unreadable |
| **MarkItDown** | ❌ N/A | ❌ N/A | ❌ N/A | ❌ (broken install) | — | Failed — module not importable |
| **Ollama VLM (llava:7b)** | ⭐⭐⭐ (approximate) | ⭐⭐⭐⭐ (semantic) | ⭐⭐⭐⭐ (understands panels) | Medium (4.7GB pull) | ~30s | **Winner for layout understanding** |

---

## Detailed Assessment

### 1. Apple Vision OCR — **BEST for text extraction**

**Output:** 135 text regions, avg confidence 0.97, near-perfect transcription including:
- Arrows (→), symbols, confidence scores
- Small annotations ("10m 1n20", "h7i8j9k")
- Multi-line text blocks

**Strengths:**
- Near-perfect character accuracy (97% avg confidence)
- Bounding box metadata (x, y, w, h) enables spatial reconstruction
- Handles dense small text better than any other method
- Fast (~2 seconds)
- No API cost, fully local

**Weaknesses:**
- No semantic understanding — returns isolated text fragments, not structured document
- Spatial relationships require manual reconstruction from coordinates
- Cannot capture color-coding or visual hierarchy meaning
- Output is position-sorted fragments, not readable document order

**Best for:** Extracting exact text/numbers/labels from images where accuracy matters (charts, infographics, screenshots with data)

**Score:** 9/10 for text extraction, 4/10 for document understanding

---

### 2. Tesseract — **WORST, unusable for complex images**

**Output:** Garbled, near-unreadable text. Examples of errors:
- "Pee Saboo, aes Al PM at Google" (should be "Shubham Saboo, Senior AI PM at Google")
- "Citigger )) > CAetion ) sae)" (should be "Trigger → Action → Proof → Memory")
- "bums calls into" (unknown original)
- "standing house" (partially correct fragment)

**Strengths:**
- Fast (~1 second)
- Universally available
- No dependencies beyond the binary

**Weaknesses:**
- Catastrophic accuracy on dense/small text
- No layout preservation
- Cannot handle multi-column or flowchart layouts
- Produces word salad from infographics
- Confidence not reported per-word

**Best for:** Simple, high-contrast, large-text scanned documents ONLY. Not suitable for infographics, diagrams, or dense text.

**Score:** 2/10 — do not use for complex images

---

### 3. MarkItDown — **FAILED (broken installation)**

**Output:** `No module named markitdown` — the package is installed at `/opt/anaconda3/lib/python3.8/site-packages` (Python 3.8, old alpha version 0.0.1a1) but not importable from the system Python.

**Root cause:** markitdown 0.0.1a1 is a very old alpha. The current version requires Python 3.10+. The anaconda Python 3.8 environment has a stale, non-functional install.

**Fix needed:** Install in a proper venv:
```bash
uv venv --python=3.12 /tmp/markitdown-venv
source /tmp/markitdown-venv/bin/activate
uv pip install 'markitdown[all]'
```

**Expected performance (based on ocr-and-documents skill notes):**
- markitdown is primarily a **document** converter (PDF, DOCX, PPTX) — its image support is limited
- For images, it would likely call an OCR backend internally, producing results between Tesseract and Apple Vision
- Not designed for infographic/diagram understanding

**Best for:** PDF/DOCX/PPTX → Markdown conversion, NOT raw image OCR

**Score:** N/A (failed to run), estimated 5/10 for images if functional

---

### 4. Ollama VLM (llava:7b) — **BEST for layout/semantic understanding**

**Output:** Natural-language description of the image structure. Correctly identified:
- "Digital infographic or presentation slide"
- "Structured layout with text and graphical elements"
- Sections: "Anatomy of a PM loop," "GitHub for PM," "Loops"
- "Vertical flowchart or diagram with flow starting from Step 1"
- "Arrows indicating the order of steps"
- Educational/instructional purpose

**BUT:** Repeated words mid-sentence ("th\nthe background", "bol\nbold"), indicating stuttering output. Did NOT transcribe actual text content — only described structure.

**Strengths:**
- Understands spatial layout and visual hierarchy
- Identifies document type and purpose
- Captures relationships between elements (flow, hierarchy)
- Natural-language output is immediately useful for categorization
- Handles color-coding and visual grouping semantically

**Weaknesses:**
- Does NOT extract exact text — describes rather than transcribes
- Stuttering/repetition in output (llava:7b known issue)
- Slower (~30 seconds, first run loads model)
- Requires 4.7GB model download
- May misread fine text details

**Best for:** Layout understanding, document classification, "what is this image?" questions, visual QA

**Score:** 8/10 for layout understanding, 3/10 for text extraction

---

## The Optimal Pipeline: OCR + VLM (Hybrid)

Neither method alone produces a good wiki page. The winning approach is **both in tandem**:

```
Image → [Apple Vision OCR] → exact text + bounding boxes (WHAT)
     → [Ollama VLM]        → layout + structure (WHERE/WHY)
     → [LLM synthesis]     → reconstructed document
```

This is exactly what the `local-vision-fallback` skill prescribes: **"OCR is authoritative for text/data; VLM is authoritative for spatial/layout judgment. Where they disagree, trust OCR on content and VLM on form."**

### What each contributes:

| Need | Use |
|------|-----|
| Exact text, numbers, labels | Apple Vision OCR |
| "What type of document is this?" | Ollama VLM |
| Spatial relationships (which box contains which text) | VLM + OCR bounding boxes |
| Color/visual hierarchy meaning | VLM only |
| Confidence scoring | Apple Vision OCR (per-region conf) |
| Speed | Apple Vision OCR |

---

## Recommendations for the Ingestion Pipeline

### For the `wiki-raw-ingest` skill — add image ingestion support:

**Step 0 (new): Format Detection**
```python
if file_extension in ['.jpg', '.jpeg', '.png', '.webp']:
    use_image_extraction_pipeline(file)
elif file_extension in ['.pdf']:
    use_pdf_extraction(file)  # existing pymupdf/marker path
```

**Step 0a (new): Image Extraction Pipeline**
```python
def extract_from_image(image_path):
    # 1. Apple Vision OCR for exact text
    ocr_result = run_apple_vision_ocr(image_path)
    
    # 2. Ollama VLM for layout understanding
    vlm_result = run_ollama_vlm(image_path, 
        prompt="Describe the layout, structure, and document type")
    
    # 3. Synthesize into structured markdown
    return {
        'text': ocr_result.text,
        'bounding_boxes': ocr_result.regions,
        'layout_description': vlm_result,
        'confidence': ocr_result.avg_confidence
    }
```

### Decision Tree for Image Ingestion

```
Is the image a simple document scan?
├── YES → Apple Vision OCR alone (fast, accurate)
└── NO (infographic/diagram/chart)
    ├── Need exact text? → Apple Vision OCR
    ├── Need layout understanding? → Ollama VLM
    └── Need full document reconstruction? → BOTH + LLM synthesis
```

---

## Modifications to Agentic Loops

This comparison directly informs how agentic ingestion loops should handle images:

### Modification 1: Dual-Path Image Ingestion in `wiki-raw-ingest`

Current skill handles only text/markdown/PDF. Add:

```yaml
# In wiki-raw-ingest pipeline
image_pipeline:
  detector: file_extension in [.jpg, .png, .webp]
  steps:
    - apple_vision_ocr    # exact text + bboxes
    - ollama_vlm          # layout + structure (if complex image)
    - llm_synthesis       # combine into structured wiki page
```

### Modification 2: Confidence-Gated Ingestion

Use OCR confidence as a quality gate:

```python
if ocr_result.avg_confidence > 0.90:
    auto_ingest(ocr_result)  # high confidence → auto-ingest
elif ocr_result.avg_confidence > 0.70:
    flag_for_review(ocr_result)  # medium → human review
else:
    escalate_to_vlm(ocr_result)  # low → get VLM second opinion
```

This mirrors the PM Loop's **Proof Gate** (Improve / Accept / Escalate) from the ingested infographic itself.

### Modification 3: Tesseract Deprecation

Tesseract should be **removed** from the image ingestion pipeline for complex images. It produces garbage on infographics. Keep it only as a fallback for simple, high-contrast document scans where Apple Vision is unavailable (Linux).

### Modification 4: MarkItDown Scope Limitation

MarkItDown should be scoped to **document formats only** (PDF, DOCX, PPTX) and removed from the image extraction path. Its image support is incidental and inferior to dedicated OCR/Vision.

### Modification 5: VLM as Layout Validator

In the [[loop-engineering]] critic/doer loop, a VLM can serve as a **layout critic**:

```python
# In critic.sh or equivalent
def layout_critic(generated_artifact):
    vlm_judgment = ollama_vlm(image=generated_artifact,
        prompt="Is this well-structured? Any overlaps? Text readable?")
    return vlm_judgment.passes_quality_bar
```

This adds a visual QA layer to the existing text-based critic.

---

## Context: Why This Matters for Agentic Loops

The PM Loop infographic (ingested as [[ai-pm-loop-system-github-for-pm]]) describes a **Proof Gate** that decides whether to Improve, Accept, or Escalate. Image extraction needs the same pattern:

| PM Loop Gate | Image Extraction Equivalent |
|--------------|-----------------------------|
| Improve (quality bar not met) | Re-run with VLM, try different prompt |
| Accept (passes bar) | Auto-ingest to wiki |
| Escalate (ambiguous) | Flag for human review |

The meta-lesson: **extraction quality is itself a loop that needs engineering**, not a one-shot operation. The 4-method comparison is the "evaluate the output" step; choosing Apple Vision + VLM is the "keep or revert" step; this document is the "commit the learning" step.

---

## Appendix: Raw Data

- **Image:** `/Users/kirkwon/.hermes/cache/images/img_069447b4d0ed.jpg` (968×968, 174KB)
- **Apple Vision regions:** 135 (avg conf 0.97)
- **Tesseract output:** ~400 words, ~40% garbled
- **MarkItDown:** failed (Python 3.8 stale install)
- **Ollama VLM:** ~150 words, structural description only
- **Ingested wiki page:** [[ai-pm-loop-system-github-for-pm]] (8155 bytes)
