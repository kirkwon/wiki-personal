---
type: concept
title: Notebooklm Cli
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - uncategorized
---

# notebooklm-cli

Comprehensive CLI for Google NotebookLM including notebooks, sources, audio podcasts, reports, quizzes, flashcards, mind maps, slides, infographics, videos, and data tables. Use when working with NotebookLM programmatically: managing notebooks/sources, generating audio overviews (podcasts), creating study materials (quizzes, flashcards), producing presentations (slides, infographics), or querying sources via chat.

## Usage

# NotebookLM CLI

## Overview

This skill provides complete access to Google NotebookLM through a command-line interface. Manage notebooks, sources, and generate various content formats including audio podcasts, reports, quizzes, flashcards, mind maps, slides, infographics, videos, and data tables.

## When to Use This Skill

Use this skill when:
- Managing NotebookLM notebooks and sources programmatically
- Generating audio overviews (podcasts) from notebook sources
- Creating study materials: quizzes, flashcards, reports
- Producing visual content: slides, infographics, mind maps, videos
- Querying sources via chat or one-shot questions
- Researching and importing new sources automatically

## Quick Start

### Authentication

```bash
nlm login
```

Launches Chrome, navigates to NotebookLM, and extracts session cookies. Requires Google Chrome installed.

### List Notebooks

```bash
nlm notebook list
```

### Create Notebook and Add Sources

```bash
nlm notebook create "My Research"
nlm source add <notebook-id> --url "https://example.com/article"
nlm source add <notebook-id> --text "Your content here" --title "My Notes"
```

### Generate Content (All Types)

All generation commands require `--confirm` or `-y`:

```bash
nlm audio create <id> --confirm          # Podcast
nlm report create <id> --confirm         # Briefing doc or study guide
nlm quiz create <id> --confirm           # Quiz questions
nlm flashcards create <id> --confirm     # Flashcards
nlm mindmap create <id> --confirm        # Mind map
nlm slides create <id> --confirm         # Slide deck
nlm infographic create <id> --confirm    # Infographic
nlm video create <id> --confirm          # Video overview
nlm data-table create <id> "description" --confirm  # Data table
```

## Authentication

| Command | Description |
|---------|-------------|
| `nlm login` | Authenticate with NotebookLM (opens Chrome) |
| `nlm login --check` | Verify current credentials |
| `nlm auth status` | Check session validity |
| `nlm auth list` | List all profiles |
| `nlm auth delete <profile> --confirm` | Delete a profile |
| `nlm login --profile <name>` | Login to specific profile |

Sessions last ~20 minutes. Re-authenticate with `nlm login` if commands fail.

## Notebook Management

| Command | Description |
|---------|-------------|
| `nlm notebook list` | List all notebooks |
| `nlm notebook create "Title"` | Create a new notebook |
| `nlm notebook get <id>` | Get notebook details |
| `nlm notebook describe <id>` | AI-generated summary |
| `nlm notebook query <id> "question"` | Chat with sources |
| `nlm notebook delete <id> --confirm` | Delete a notebook |

## Source Management

| Command | Description |
|---------|-------------|
| `nlm source list <notebook-id>` | List sources in notebook |
| `nlm source list <notebook-id> --drive` | Show Drive sources with freshness |
| `nlm source add <id> --url "..."` | Add URL or YouTube source |
| `nlm source add <id> --text "..." --title "..."` | Add pasted text |


...(truncated)