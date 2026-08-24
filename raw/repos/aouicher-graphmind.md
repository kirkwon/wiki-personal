---
date: 2026-06-30

type: source
source_url: https://github.com/aouicher/graphmind
sha256: 32e14fb056df1004d1bb0306053534af1ff7f5cc3dda74367fc80a9747131b3c
title: "Repo Analysis: aouicher-graphmind"
ingested: 2026-06-30 19:57
source: remote-clone:https://github.com/aouicher/graphmind
project_type: rust
language: rust
manifest: Cargo.toml
created: 2026-07-26
updated: 2026-07-26
---

# Repo Analysis: aouicher-graphmind

> Ingested: 2026-06-30 | Source: remote-clone:https://github.com/aouicher/graphmind

## Project Profile

- **Type:** rust
- **Language:** rust
- **Build system:** cargo
- **Manifest:** Cargo.toml
- **Tests:** tests
- **Docker:** No
- **CI:** No
- **Docs:** Yes
- **Total files:** 211
- **Total dirs:** 56

## Directory Structure

**Top-level files:**

- CLAUDE.md
- Cargo.lock
- Cargo.toml
- LICENSE
- README.md
- SECURITY.md
- SKILL.md
- graphmind-demo-cli.gif
- graphmind-demo-desktop.gif
- graphmind-demo.gif

**Directories:**

- assets/
- crates/
- scripts/
- tests/

**Largest directories:**

- crates/graphmind-core/src/languages: 28 files
- crates/graphmind-cli/src/commands: 20 files
- (root): 13 files
- crates/graphmind-cli/tests: 12 files
- crates/graphmind-desktop/src-tauri/src/commands: 11 files

## LICENSE

```
MIT License

Copyright (c) 2026 Alexandre Ouicher

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
# graphmind

[![CI](https://github.com/aouicher/graphmind/actions/workflows/ci.yml/badge.svg)](https://github.com/aouicher/graphmind/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> Your codebase has a shape. Now your AI can see it. And remember it.

GraphMind turns your codebase into a knowledge graph your AI can query, navigate, and remember. Ask about dead code, dependencies, or blast radius — and get answers grounded in your actual architecture.

Up to **5,700× fewer tokens** than raw search (~10M tokens saved per session). Works with Claude Code, Cursor, Windsurf, Cline, Zed, Continue, and any MCP-compatible AI assistant.

<table><tr>
<td><img src="graphmind-demo-cli.gif" width="400" alt="GraphMind CLI demo" /></td>
<td><img src="graphmind-demo-desktop.gif" width="400" alt="GraphMind Desktop app" /></td>
</tr>
<tr>
<td align="center"><sub>CLI + Claude MCP integration</sub></td>
<td align="center"><sub>Desktop app — Mac &amp; Windows</sub></td>
</tr></table>

## Why GraphMind

Every new AI session starts from zero. Your assistant re-reads the entire codebase, re-discovers architecture, and forgets every decision you explained last time. Across multiple projects, there's zero visibility into shared dependencies.

**graphmind** fixes this with four layers:
1. **Structural graph** — function-level knowledge graph per repo (AST-based, tree-sitter, 30+ languages)
2. **Semantic embeddings** — vector search over symbols (local ONNX, OpenAI, or Voyage AI)
3. **Persistent memory** — declarative store for decisions, patterns, conventions — survives across sessions
4. **Cross-project links** — dependencies and relationships between registered repos

Everything runs locally. No cloud. No open ports by default. No telemetry.

## Benchmark

![grep vs graphmind](assets/benchmark.png)

Comparison of token usage: `grep -r` (raw file search) vs `graphmind search` for the same query on a ~100k LOC codebase. graphmind returns ranked, structured results in under 300 tokens vs 1.5M+ for raw grep output.

## Install

### Desktop app (macOS) — recommended

Download the `.dmg` from [Releases](https://github.com/aouicher/graphmind/releases). The app installs the CLI for you and runs a guided onboarding that configures MCP, hooks, skill, and embeddings — no terminal needed.

![GraphMind desktop app](assets/screenshot-desktop.png)

| Platform | Asset |
|----------|-------|
| macOS (Apple Silicon) | `GraphMind-macos-arm64.dmg` |
| macOS (Intel) | `GraphMind-macos-x64.dmg` |

... (truncated, 706 lines total)

```

## File Index

- .gitignore
- .mcp.json
- .npmignore
- CLAUDE.md
- Cargo.lock
- Cargo.toml
- LICENSE
- README.md
- SECURITY.md
- SKILL.md
- assets/benchmark.png
- assets/screenshot-desktop.png
- crates/graphmind-cli/Cargo.toml
- crates/graphmind-cli/src/commands/auth.rs
- crates/graphmind-cli/src/commands/build.rs
- crates/graphmind-cli/src/commands/claude_hook.rs
- crates/graphmind-cli/src/commands/clean.rs
- crates/graphmind-cli/src/commands/cross.rs
- crates/graphmind-cli/src/commands/diff_impact.rs
- crates/graphmind-cli/src/commands/exclude.rs
- crates/graphmind-cli/src/commands/export.rs
- crates/graphmind-cli/src/commands/hooks.rs
- crates/graphmind-cli/src/commands/install_skill.rs
- crates/graphmind-cli/src/commands/memory.rs
- crates/graphmind-cli/src/commands/mod.rs
- crates/graphmind-cli/src/commands/notices.rs
- crates/graphmind-cli/src/commands/query.rs
- crates/graphmind-cli/src/commands/register.rs
- crates/graphmind-cli/src/commands/search.rs
- crates/graphmind-cli/src/commands/session.rs
- crates/graphmind-cli/src/commands/setup.rs
- crates/graphmind-cli/src/commands/sync.rs
- crates/graphmind-cli/src/commands/update.rs
- crates/graphmind-cli/src/lib.rs
- crates/graphmind-cli/src/main.rs
- crates/graphmind-cli/tests/cli_auth_e2e.rs
- crates/graphmind-cli/tests/cli_build_e2e.rs
- crates/graphmind-cli/tests/cli_clean_e2e.rs
- crates/graphmind-cli/tests/cli_exclude_e2e.rs
- crates/graphmind-cli/tests/cli_export_e2e.rs
- crates/graphmind-cli/tests/cli_memory_e2e.rs
- crates/graphmind-cli/tests/cli_memory_persistence_e2e.rs
- crates/graphmind-cli/tests/cli_query_e2e.rs
- crates/graphmind-cli/tests/cli_register_e2e.rs
- crates/graphmind-cli/tests/cli_session_e2e.rs
- crates/graphmind-cli/tests/cli_sync_e2e.rs
- crates/graphmind-cli/tests/common/mod.rs
- crates/graphmind-cli/tests/setup_e2e.rs
- crates/graphmind-config/Cargo.toml
- crates/graphmind-config/src/breaking.rs
- crates/graphmind-config/src/config.rs
- crates/graphmind-config/src/lib.rs
- crates/graphmind-config/src/paths.rs
- crates/graphmind-config/src/resolve.rs
- crates/graphmind-core/Cargo.toml
- crates/graphmind-core/build.rs
- crates/graphmind-core/src/extractor.rs
- crates/graphmind-core/src/languages/bash.rs
- crates/graphmind-core/src/languages/c.rs
- crates/graphmind-core/src/languages/cpp.rs
- crates/graphmind-core/src/languages/csharp.rs
- crates/graphmind-core/src/languages/css.rs
- crates/graphmind-core/src/languages/dart.rs
- crates/graphmind-core/src/languages/dockerfile.rs
- crates/graphmind-core/src/languages/go.rs
- crates/graphmind-core/src/languages/graphql.rs
- crates/graphmind-core/src/languages/hcl.rs
- crates/graphmind-core/src/languages/html.rs
- crates/graphmind-core/src/languages/java.rs
- crates/graphmind-core/src/languages/kotlin.rs
- crates/graphmind-core/src/languages/mod.rs
- crates/graphmind-core/src/languages/objc.rs
- crates/graphmind-core/src/languages/perl.rs
- crates/graphmind-core/src/languages/php.rs
- crates/graphmind-core/src/languages/powershell.rs
- crates/graphmind-core/src/languages/python.rs
- crates/graphmind-core/src/languages/r.rs
- crates/graphmind-core/src/languages/ruby.rs
- crates/graphmind-core/src/languages/rust.rs
- crates/graphmind-core/src/languages/scala.rs
- crates/graphmind-core/src/languages/scss.rs
- crates/graphmind-core/src/languages/sql.rs
- crates/graphmind-core/src/languages/swift.rs
- crates/graphmind-core/src/languages/toml.rs
- crates/graphmind-core/src/languages/yaml.rs
- crates/graphmind-core/src/lib.rs
- crates/graphmind-core/src/parser.rs
- crates/graphmind-core/src/registry.rs
- crates/graphmind-core/src/resolver.rs
- crates/graphmind-core/tests/all_languages.rs
- crates/graphmind-core/tests/golden_edge_cases.rs
- crates/graphmind-core/tests/golden_extraction.rs
- crates/graphmind-core/tests/golden_multilang.rs
- crates/graphmind-db/Cargo.toml
- crates/graphmind-db/benches/pipeline_bench.rs
- crates/graphmind-db/src/builder.rs
- crates/graphmind-db/src/cache.rs
- crates/graphmind-db/src/lib.rs
- crates/graphmind-db/src/markdown.rs
- crates/graphmind-db/src/queries.rs
- crates/graphmind-db/src/schema.rs
- crates/graphmind-db/tests/golden_pipeline.rs
- crates/graphmind-desktop/gen/schemas/acl-manifests.json
- crates/graphmind-desktop/gen/schemas/capabilities.json
- crates/graphmind-desktop/gen/schemas/desktop-schema.json
- crates/graphmind-desktop/gen/schemas/macOS-schema.json
- crates/graphmind-desktop/index.html
- crates/graphmind-desktop/package-lock.json
- crates/graphmind-desktop/package.json
- crates/graphmind-desktop/src-tauri/Cargo.toml
- crates/graphmind-desktop/src-tauri/build.rs
- crates/graphmind-desktop/src-tauri/capabilities/default.json
- crates/graphmind-desktop/src-tauri/gen/schemas/acl-manifests.json
- crates/graphmind-desktop/src-tauri/gen/schemas/capabilities.json
- crates/graphmind-desktop/src-tauri/gen/schemas/desktop-schema.json
- crates/graphmind-desktop/src-tauri/gen/schemas/macOS-schema.json
- crates/graphmind-desktop/src-tauri/icons/128x128.png
- crates/graphmind-desktop/src-tauri/icons/128x128@2x.png
- crates/graphmind-desktop/src-tauri/icons/32x32.png
- crates/graphmind-desktop/src-tauri/icons/icon.icns
- crates/graphmind-desktop/src-tauri/icons/icon.ico
- crates/graphmind-desktop/src-tauri/icons/icon.png
- crates/graphmind-desktop/src-tauri/src/commands/graph.rs
- crates/graphmind-desktop/src-tauri/src/commands/indexing.rs
- crates/graphmind-desktop/src-tauri/src/commands/integrations.rs
- crates/graphmind-desktop/src-tauri/src/commands/license.rs
- crates/graphmind-desktop/src-tauri/src/commands/mod.rs
- crates/graphmind-desktop/src-tauri/src/commands/notices.rs
- crates/graphmind-desktop/src-tauri/src/commands/projects.rs
- crates/graphmind-desktop/src-tauri/src/commands/settings.rs
- crates/graphmind-desktop/src-tauri/src/commands/setup.rs
- crates/graphmind-desktop/src-tauri/src/commands/updater.rs
- crates/graphmind-desktop/src-tauri/src/commands/watcher.rs
- crates/graphmind-desktop/src-tauri/src/lib.rs
- crates/graphmind-desktop/src-tauri/src/main.rs
- crates/graphmind-desktop/src-tauri/src/state.rs
- crates/graphmind-desktop/src-tauri/src/tray.rs
- crates/graphmind-desktop/src-tauri/src/types.rs
- crates/graphmind-desktop/src-tauri/tauri.conf.json
- crates/graphmind-desktop/src/App.tsx
- crates/graphmind-desktop/src/assets/logo.png
- crates/graphmind-desktop/src/components/layout/Sidebar.tsx
- crates/graphmind-desktop/src/components/ui/Badge.tsx
- crates/graphmind-desktop/src/components/ui/Button.tsx
- crates/graphmind-desktop/src/components/ui/ProgressBar.tsx
- crates/graphmind-desktop/src/components/ui/Spinner.tsx
- crates/graphmind-desktop/src/hooks/useClients.ts
- crates/graphmind-desktop/src/hooks/useProjects.ts
- crates/graphmind-desktop/src/hooks/useTauriEvent.ts
- crates/graphmind-desktop/src/index.css
- crates/graphmind-desktop/src/lib/tauri.ts
- crates/graphmind-desktop/src/main.tsx
- crates/graphmind-desktop/src/pages/Integrations.tsx
- crates/graphmind-desktop/src/pages/Projects.tsx
- crates/graphmind-desktop/src/pages/Settings.tsx
- crates/graphmind-desktop/src/pages/Setup.tsx
- crates/graphmind-desktop/src/vite-env.d.ts
- crates/graphmind-desktop/tsconfig.json
- crates/graphmind-desktop/vite.config.ts
- crates/graphmind-embeddings/Cargo.toml
- crates/graphmind-embeddings/src/engine.rs
- crates/graphmind-embeddings/src/factory.rs
- crates/graphmind-embeddings/src/lib.rs
- crates/graphmind-embeddings/src/local.rs
- crates/graphmind-embeddings/src/openai.rs
- crates/graphmind-embeddings/src/search.rs
- crates/graphmind-embeddings/src/store.rs
- crates/graphmind-embeddings/src/voyage.rs
- crates/graphmind-embeddings/tests/embedding_pipeline.rs
- crates/graphmind-license/Cargo.toml
- crates/graphmind-license/src/fingerprint.rs
- crates/graphmind-license/src/lib.rs
- crates/graphmind-mcp/Cargo.toml
- crates/graphmind-mcp/src/export_helpers.rs
- crates/graphmind-mcp/src/formatting.rs
- crates/graphmind-mcp/src/graph_helpers.rs
- crates/graphmind-mcp/src/handlers/analysis.rs
- crates/graphmind-mcp/src/handlers/cross.rs
- crates/graphmind-mcp/src/handlers/export.rs
- crates/graphmind-mcp/src/handlers/graph.rs
- crates/graphmind-mcp/src/handlers/memory.rs
- crates/graphmind-mcp/src/handlers/meta.rs
- crates/graphmind-mcp/src/handlers/mod.rs
- crates/graphmind-mcp/src/handlers/search.rs
- crates/graphmind-mcp/src/lib.rs
- crates/graphmind-mcp/src/search_helpers.rs
- crates/graphmind-mcp/src/server.rs
- crates/graphmind-mcp/tests/mcp_handlers.rs
- crates/graphmind-memory/Cargo.toml
- crates/graphmind-memory/src/cross_infer.rs
- crates/graphmind-memory/src/cross_links.rs
- crates/graphmind-memory/src/index.rs
- crates/graphmind-memory/src/lib.rs
- crates/graphmind-memory/src/search.rs
- crates/graphmind-memory/src/store.rs
- crates/graphmind-memory/tests/memory_store.rs
- graphmind-demo-cli.gif
- graphmind-demo-desktop.gif
- graphmind-demo.gif
- scripts/build-desktop.sh
- scripts/cl_wrapper.py
- scripts/install.sh
- tests/fixtures/sample-project/src/index.ts
- tests/fixtures/sample-project/src/routes/wallet.ts
- tests/fixtures/sample-project/src/services/wallet.go
- tests/fixtures/sample-project/src/services/wallet.py
- tests/fixtures/sample-project/src/services/wallet.rb
- tests/fixtures/sample-project/src/services/wallet.rs
- tests/fixtures/sample-project/src/services/wallet.ts
- tests/fixtures/sample-project/src/utils/logger.ts
- tests/fixtures/sample-project/src/utils/validator.ts

## Symbol Map

> 920 symbols across the repo, ranked by cross-file reference count. Top entries matter most.

### crates/graphmind-cli/src/commands/query.rs

  ⚙️ `map` — function (L291, refs: 318)

### crates/graphmind-core/src/languages/graphql.rs

  ⚙️ `node_text` — function (L63, refs: 249)
  ⚙️ `collect_symbols` — function (L17, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/toml.rs

  ⚙️ `node_text` — function (L42, refs: 249)
  ⚙️ `collect_symbols` — function (L17, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/yaml.rs

  ⚙️ `node_text` — function (L80, refs: 249)

### crates/graphmind-core/src/languages/bash.rs

  ⚙️ `node_text` — function (L70, refs: 247)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/css.rs

  ⚙️ `node_text` — function (L81, refs: 247)
  ⚙️ `collect_symbols` — function (L19, refs: 79)

### crates/graphmind-core/src/languages/powershell.rs

  ⚙️ `node_text` — function (L112, refs: 246)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/html.rs

  ⚙️ `node_text` — function (L100, refs: 246)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/scss.rs

  ⚙️ `node_text` — function (L92, refs: 246)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/dockerfile.rs

  ⚙️ `node_text` — function (L81, refs: 246)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/perl.rs

  ⚙️ `node_text` — function (L112, refs: 245)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/r.rs

  ⚙️ `node_text` — function (L116, refs: 245)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/c.rs

  ⚙️ `node_text` — function (L140, refs: 245)
  ⚙️ `collect_symbols` — function (L21, refs: 79)

### crates/graphmind-core/src/resolver.rs

  ⚙️ `node_text` — function (L97, refs: 244)
  📐 `ResolvedImport` — struct (L8, refs: 101)

### crates/graphmind-core/src/languages/sql.rs

  ⚙️ `node_text` — function (L109, refs: 244)
  ⚙️ `collect_symbols` — function (L19, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/dart.rs

  ⚙️ `node_text` — function (L138, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/cpp.rs

  ⚙️ `node_text` — function (L145, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/java.rs

  ⚙️ `node_text` — function (L145, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/scala.rs

  ⚙️ `node_text` — function (L134, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/swift.rs

  ⚙️ `node_text` — function (L130, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/kotlin.rs

  ⚙️ `node_text` — function (L133, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/objc.rs

  ⚙️ `node_text` — function (L181, refs: 242)
  ⚙️ `collect_symbols` — function (L32, refs: 79)

### crates/graphmind-core/src/languages/csharp.rs

  ⚙️ `node_text` — function (L137, refs: 242)
  ⚙️ `collect_symbols` — function (L21, refs: 79)

### crates/graphmind-core/src/languages/hcl.rs

  ⚙️ `node_text` — function (L156, refs: 240)
  ⚙️ `collect_symbols` — function (L17, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/php.rs

  ⚙️ `node_text` — function (L158, refs: 240)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/ruby.rs

  ⚙️ `node_text` — function (L178, refs: 239)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/python.rs

  ⚙️ `node_text` — function (L224, refs: 235)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/rust.rs

  ⚙️ `node_text` — function (L249, refs: 232)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/languages/go.rs

  ⚙️ `node_text` — function (L255, refs: 231)
  ⚙️ `collect_symbols` — function (L21, refs: 79)
  ⚙️ `extract_symbols` — function (L5, refs: 67)

### crates/graphmind-core/src/extractor.rs

  ⚙️ `node_text` — function (L437, refs: 227)
  📐 `Symbol` — struct (L18, refs: 194)
  📋 `SymbolKind` — enum (L8, refs: 141)
  📐 `CallSite` — struct (L29, refs: 106)
  ⚙️ `collect_symbols` — function (L58, refs: 78)
  ⚙️ `extract_symbols` — function (L46, refs: 67)

### crates/graphmind-cli/src/commands/register.rs

  ⚙️ `status` — function (L71, refs: 123)
  ⚙️ `list` — function (L43, refs: 90)

### crates/graphmind-cli/src/commands/auth.rs

  ⚙️ `status` — function (L70, refs: 115)

### crates/graphmind-cli/src/commands/build.rs

  ⚙️ `build` — function (L17, refs: 111)

### crates/graphmind-memory/src/search.rs

  ⚙️ `search` — function (L3, refs: 110)

### crates/graphmind-cli/src/commands/memory.rs

  ⚙️ `search` — function (L65, refs: 108)
  ⚙️ `list` — function (L100, refs: 89)

### crates/graphmind-cli/src/commands/search.rs

  ⚙️ `search` — function (L10, refs: 106)

### crates/graphmind-core/tests/golden_edge_cases.rs

  ⚙️ `process` — function (L209, refs: 101)

### crates/graphmind-config/src/paths.rs

  ⚙️ `config_path` — function (L11, refs: 94)

### crates/graphmind-cli/src/commands/exclude.rs

  ⚙️ `list` — function (L80, refs: 91)

### crates/graphmind-cli/src/commands/export.rs

  ⚙️ `export` — function (L7, refs: 77)

### crates/graphmind-db/src/queries.rs

  📐 `GraphQueries` — struct (L106, refs: 76)

### crates/graphmind-config/src/config.rs

  📐 `Registry` — struct (L215, refs: 75)

### crates/graphmind-cli/src/commands/setup.rs

  ⚙️ `setup` — function (L12, refs: 75)

### crates/graphmind-core/src/parser.rs

  ⚙️ `parse` — function (L11, refs: 70)

## Open Questions / Notes

> _Add notes after reviewing the codebase._
