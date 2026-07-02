---
type: source
source_url: https://github.com/ChristopherLyon/graphrag-workbench
sha256: 0f8fa542b9f44d69ed2566fe0ed2a5a2dd5a660732cabbbca046a074d661b48e
title: "Repo Analysis: christopherlyon-graphrag-workbench"
ingested: 2026-06-30 23:21
source: remote-clone:https://github.com/ChristopherLyon/graphrag-workbench
project_type: javascript
language: typescript
manifest: package.json
---

# Repo Analysis: christopherlyon-graphrag-workbench

> Ingested: 2026-06-30 | Source: remote-clone:https://github.com/ChristopherLyon/graphrag-workbench

## Project Profile

- **Type:** javascript
- **Language:** typescript
- **Build system:** npm/yarn
- **Manifest:** package.json
- **Docker:** No
- **CI:** No
- **Docs:** Yes
- **Total files:** 110
- **Total dirs:** 32

## Dependencies (top)

- @hookform/resolvers
- @radix-ui/react-accordion
- @radix-ui/react-alert-dialog
- @radix-ui/react-aspect-ratio
- @radix-ui/react-avatar
- @radix-ui/react-checkbox
- @radix-ui/react-collapsible
- @radix-ui/react-context-menu
- @radix-ui/react-dialog
- @radix-ui/react-dropdown-menu
- @radix-ui/react-hover-card
- @radix-ui/react-label
- @radix-ui/react-menubar
- @radix-ui/react-navigation-menu
- @radix-ui/react-popover
- @radix-ui/react-progress
- @radix-ui/react-radio-group
- @radix-ui/react-scroll-area
- @radix-ui/react-select
- @radix-ui/react-separator

## Directory Structure

**Top-level files:**

- LICENSE
- README.md
- components.json
- eslint.config.mjs
- next-env.d.ts
- next.config.ts
- package.json
- pnpm-lock.yaml
- postcss.config.mjs
- settings.yaml
- tsconfig.json
- tsconfig.tsbuildinfo

**Directories:**

- app/
- components/
- hooks/
- lib/
- prompts/
- public/
- types/

**Largest directories:**

- components/ui: 46 files
- (root): 15 files
- prompts: 13 files
- components: 7 files
- app: 4 files

## LICENSE

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## README.md

```
# GraphRAG Workbench


A modern, interactive web application for building and visualizing knowledge graphs using Microsoft's [GraphRAG](https://github.com/microsoft/graphrag) framework. Transform your documents into an explorable 3D knowledge graph with advanced AI-powered analysis and querying capabilities.

![GraphRAG Workbench](https://img.shields.io/badge/GraphRAG-Workbench-blue)
![Next.js](https://img.shields.io/badge/Next.js-15.5-black)
![React](https://img.shields.io/badge/React-19.1-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)


https://github.com/user-attachments/assets/1f588a45-07ca-4953-92ed-fc888fe28cff


## ✨ Features

### 📊 Interactive 3D Visualization
- **Immersive 3D Knowledge Graph**: Navigate through your data in a stunning 3D space with smooth animations
- **Community Detection**: Visualize hierarchical community structures with color-coded boundaries
- **Smart Node Sizing**: Entity importance reflected through dynamic node sizing based on centrality metrics
- **Advanced Filtering**: Filter by entity types, community levels, and relationship weights
- **Search & Highlight**: Real-time search with visual highlighting of matching entities

### 🗂️ Document Management
- **PDF Processing**: Drag-and-drop PDF upload with automatic text extraction
- **Batch Operations**: Process multiple documents simultaneously
- **Archive Management**: Save and restore different knowledge graph versions
- **Progress Tracking**: Real-time indexing progress with detailed logs

### 🤖 AI-Powered Analysis  
- **GraphRAG Integration**: Leverage Microsoft's GraphRAG for entity extraction and relationship mapping
- **Community Reports**: AI-generated summaries of detected communities
- **Chat Interface**: Query your knowledge graph using natural language
- **Multiple Search Modes**: Local, global, drift, and basic search strategies

### 🎯 Advanced Features
- **Community Isolator**: Focus on specific community hierarchies for detailed analysis
- **Relationship Weighting**: Visualize connection strength with dynamic link thickness
- **Bloom Effects**: Beautiful post-processing effects for enhanced visualization
- **Responsive Design**: Optimized for desktop and tablet usage

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- OpenAI API key
- Python 3.10+ (for GraphRAG backend)

### Installation


... (truncated, 303 lines total)

```

## File Index

- .env.example
- .gitattributes
- .gitignore
- LICENSE
- README.md
- app/api/chat/route.ts
- app/api/chat/stream/route.ts
- app/api/corpus/archive/create/route.ts
- app/api/corpus/archive/delete/route.ts
- app/api/corpus/archive/list/route.ts
- app/api/corpus/archive/rename/route.ts
- app/api/corpus/archive/restore/route.ts
- app/api/corpus/file/route.ts
- app/api/corpus/index/stop/route.ts
- app/api/corpus/index/stream/route.ts
- app/api/corpus/kg/rename/route.ts
- app/api/corpus/nuke/route.ts
- app/api/corpus/remove/route.ts
- app/api/corpus/state/route.ts
- app/api/corpus/upload/route.ts
- app/api/data/[name]/route.ts
- app/favicon.ico
- app/globals.css
- app/layout.tsx
- app/page.tsx
- components.json
- components/ChatPanel.tsx
- components/Controls.tsx
- components/CorpusPanel.tsx
- components/GalaxyBackground.tsx
- components/GraphVisualizer.tsx
- components/Inspector.tsx
- components/LoadingState.tsx
- components/ui/accordion.tsx
- components/ui/alert-dialog.tsx
- components/ui/alert.tsx
- components/ui/aspect-ratio.tsx
- components/ui/avatar.tsx
- components/ui/badge.tsx
- components/ui/breadcrumb.tsx
- components/ui/button.tsx
- components/ui/calendar.tsx
- components/ui/card.tsx
- components/ui/carousel.tsx
- components/ui/chart.tsx
- components/ui/checkbox.tsx
- components/ui/collapsible.tsx
- components/ui/command.tsx
- components/ui/context-menu.tsx
- components/ui/dialog.tsx
- components/ui/drawer.tsx
- components/ui/dropdown-menu.tsx
- components/ui/form.tsx
- components/ui/hover-card.tsx
- components/ui/input-otp.tsx
- components/ui/input.tsx
- components/ui/label.tsx
- components/ui/menubar.tsx
- components/ui/navigation-menu.tsx
- components/ui/pagination.tsx
- components/ui/popover.tsx
- components/ui/progress.tsx
- components/ui/radio-group.tsx
- components/ui/resizable.tsx
- components/ui/scroll-area.tsx
- components/ui/select.tsx
- components/ui/separator.tsx
- components/ui/sheet.tsx
- components/ui/sidebar.tsx
- components/ui/skeleton.tsx
- components/ui/slider.tsx
- components/ui/sonner.tsx
- components/ui/switch.tsx
- components/ui/table.tsx
- components/ui/tabs.tsx
- components/ui/textarea.tsx
- components/ui/toggle-group.tsx
- components/ui/toggle.tsx
- components/ui/tooltip.tsx
- eslint.config.mjs
- hooks/use-mobile.ts
- lib/forceSimulation.ts
- lib/graphData.ts
- lib/server/converters.ts
- lib/utils.ts
- next-env.d.ts
- next.config.ts
- package.json
- pnpm-lock.yaml
- postcss.config.mjs
- prompts/basic_search_system_prompt.txt
- prompts/community_report_graph.txt
- prompts/community_report_text.txt
- prompts/drift_reduce_prompt.txt
- prompts/drift_search_system_prompt.txt
- prompts/extract_claims.txt
- prompts/extract_graph.txt
- prompts/global_search_knowledge_system_prompt.txt
- prompts/global_search_map_system_prompt.txt
- prompts/global_search_reduce_system_prompt.txt
- prompts/local_search_system_prompt.txt
- prompts/question_gen_system_prompt.txt
- prompts/summarize_descriptions.txt
- public/graphrag-workbench.mp4
- public/logo.png
- settings.yaml
- tsconfig.json
- tsconfig.tsbuildinfo
- types/parquetjs-lite.d.ts
- types/pdf-parse.d.ts

## Symbol Map

> 469 symbols across the repo, ranked by cross-file reference count. Top entries matter most.

### lib/utils.ts

  ⚙️ `cn` — function (L4, refs: 268)

### app/api/corpus/archive/list/route.ts

  ⚙️ `items` — arrow-function (L30, refs: 136)
  ⚙️ `st` — arrow-function (L33, refs: 5)
  ⚙️ `dirs` — arrow-function (L29, refs: 4)

### components/ui/button.tsx

  ⚙️ `Button` — function (L38, refs: 64)

### components/GraphVisualizer.tsx

  ⚙️ `opacity` — arrow-function (L151, refs: 54)
  ⚙️ `ids` — arrow-function (L512, refs: 19)
  ⚙️ `radius` — arrow-function (L197, refs: 19)
  ⚙️ `filteredNodes` — arrow-function (L457, refs: 7)
  ⚙️ `GraphVisualizer` — function (L393, refs: 4)
  ⚙️ `filteredLinks` — arrow-function (L490, refs: 4)
  ⚙️ `Link` — function (L135, refs: 3)

### app/api/chat/route.ts

  ⚙️ `entities` — arrow-function (L105, refs: 46)
  ⚙️ `selected` — arrow-function (L58, refs: 26)
  🏷️ `Entity` — type-alias (L15, refs: 14)
  🏷️ `Relationship` — type-alias (L16, refs: 8)
  ⚙️ `normalize` — function (L23, refs: 5)
  ⚙️ `emap` — arrow-function (L57, refs: 4)
  🏷️ `Method` — type-alias (L91, refs: 3)

### app/api/corpus/remove/route.ts

  ⚙️ `raw` — arrow-function (L35, refs: 40)
  ⚙️ `body` — arrow-function (L18, refs: 28)
  🏛️ `UploadEntry` — class (L5, refs: 15)
  ⚙️ `idx` — arrow-function (L38, refs: 14)

### app/api/corpus/archive/rename/route.ts

  ⚙️ `raw` — arrow-function (L17, refs: 39)

### components/ChatPanel.tsx

  ⚙️ `send` — arrow-function (L68, refs: 39)
  ⚙️ `ChatPanel` — function (L19, refs: 3)

### app/api/corpus/index/stream/route.ts

  ⚙️ `raw` — arrow-function (L93, refs: 38)
  ⚙️ `raw` — arrow-function (L144, refs: 38)
  ⚙️ `send` — arrow-function (L27, refs: 18)
  ⚙️ `list` — arrow-function (L85, refs: 16)
  🏛️ `UploadEntry` — class (L7, refs: 13)
  ⚙️ `ents` — arrow-function (L39, refs: 10)

### lib/graphData.ts

  🏛️ `Community` — class (L28, refs: 36)
  🏛️ `Entity` — class (L3, refs: 18)
  🏛️ `Relationship` — class (L17, refs: 7)
  🏛️ `GraphData` — class (L68, refs: 5)
  🏛️ `GraphDataLoader` — class (L75, refs: 3)

### components/ui/card.tsx

  ⚙️ `Card` — function (L5, refs: 35)
  ⚙️ `CardContent` — function (L64, refs: 35)
  ⚙️ `CardHeader` — function (L18, refs: 23)
  ⚙️ `CardTitle` — function (L31, refs: 23)
  ⚙️ `CardDescription` — function (L41, refs: 5)

### components/ui/badge.tsx

  ⚙️ `Badge` — function (L28, refs: 30)

### app/api/corpus/nuke/route.ts

  ⚙️ `body` — arrow-function (L24, refs: 28)

### app/api/chat/stream/route.ts

  ⚙️ `selected` — arrow-function (L56, refs: 27)
  ⚙️ `send` — arrow-function (L121, refs: 27)
  ⚙️ `body` — arrow-function (L95, refs: 24)
  🏷️ `Entity` — type-alias (L7, refs: 14)
  🏷️ `Relationship` — type-alias (L8, refs: 8)
  ⚙️ `normalize` — function (L10, refs: 5)
  ⚙️ `emap` — arrow-function (L55, refs: 4)

### app/api/corpus/state/route.ts

  ⚙️ `files` — arrow-function (L20, refs: 26)
  🏛️ `UploadEntry` — class (L5, refs: 12)

### components/GalaxyBackground.tsx

  ⚙️ `material` — arrow-function (L61, refs: 24)
  ⚙️ `GalaxyBackground` — function (L15, refs: 3)

### lib/forceSimulation.ts

  🏛️ `Node3D` — class (L4, refs: 17)
  ⚙️ `childCommunity` — arrow-function (L538, refs: 11)
  ⚙️ `parentCommunity` — arrow-function (L518, refs: 7)
  🏛️ `Link3D` — class (L18, refs: 5)
  🏛️ `GraphLayout` — class (L26, refs: 4)
  🏛️ `ForceSimulation3D` — class (L56, refs: 3)

### components/ui/separator.tsx

  ⚙️ `Separator` — function (L8, refs: 15)

### components/CorpusPanel.tsx

  ⚙️ `files` — arrow-function (L494, refs: 15)
  ⚙️ `merged` — arrow-function (L550, refs: 4)
  ⚙️ `CorpusPanel` — function (L39, refs: 3)

### app/api/corpus/upload/route.ts

  ⚙️ `idx` — arrow-function (L31, refs: 15)
  🏛️ `UploadEntry` — class (L4, refs: 14)

### components/ui/label.tsx

  ⚙️ `Label` — function (L8, refs: 14)

### components/ui/sidebar.tsx

  ⚙️ `width` — arrow-function (L610, refs: 13)
  ⚙️ `handleKeyDown` — arrow-function (L98, refs: 5)

### components/ui/skeleton.tsx

  ⚙️ `Skeleton` — function (L3, refs: 12)

### app/page.tsx

  ⚙️ `visibleCommunities` — arrow-function (L330, refs: 12)
  ⚙️ `connectedLinks` — arrow-function (L217, refs: 7)
  ⚙️ `handleKeyDown` — arrow-function (L133, refs: 5)

### components/Inspector.tsx

  ⚙️ `childCommunity` — arrow-function (L69, refs: 11)
  ⚙️ `parentCommunity` — arrow-function (L50, refs: 7)
  ⚙️ `Inspector` — function (L22, refs: 6)

### app/api/corpus/archive/restore/route.ts

  ⚙️ `ents` — arrow-function (L13, refs: 10)

### components/ui/input.tsx

  ⚙️ `Input` — function (L5, refs: 9)

### components/ui/scroll-area.tsx

  ⚙️ `ScrollArea` — function (L14, refs: 9)

### hooks/use-mobile.ts

  ⚙️ `onChange` — arrow-function (L10, refs: 9)

### components/ui/table.tsx

  ⚙️ `TableRow` — function (L55, refs: 7)
  ⚙️ `TableCell` — function (L81, refs: 5)

### components/ui/tabs.tsx

  ⚙️ `TabsTrigger` — function (L37, refs: 7)

### components/ui/alert.tsx

  ⚙️ `Alert` — function (L22, refs: 6)
  ⚙️ `AlertDescription` — function (L50, refs: 6)

### components/ui/progress.tsx

  ⚙️ `Progress` — function (L8, refs: 6)

### components/ui/radio-group.tsx

  ⚙️ `RadioGroup` — function (L9, refs: 6)

### components/ui/dialog.tsx

  ⚙️ `Dialog` — function (L9, refs: 5)
  ⚙️ `DialogContent` — function (L49, refs: 3)
  ⚙️ `DialogDescription` — function (L119, refs: 3)
  ⚙️ `DialogHeader` — function (L83, refs: 3)
  ⚙️ `DialogTitle` — function (L106, refs: 3)

### components/ui/toggle.tsx

  ⚙️ `Toggle` — function (L31, refs: 5)

### components/ui/tooltip.tsx

  ⚙️ `Tooltip` — function (L21, refs: 5)

### types/pdf-parse.d.ts

  ⚙️ `pdfParse` — function (L11, refs: 4)

### components/ui/dropdown-menu.tsx

  ⚙️ `DropdownMenu` — function (L9, refs: 3)
  ⚙️ `DropdownMenuContent` — function (L34, refs: 3)
  ⚙️ `DropdownMenuLabel` — function (L146, refs: 3)
  ⚙️ `DropdownMenuTrigger` — function (L23, refs: 3)

## Open Questions / Notes

> _Add notes after reviewing the codebase._
