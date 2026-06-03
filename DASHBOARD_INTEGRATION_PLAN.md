---
type: note
title: Skills Dashboard Integration Plan
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
-

# Skills Dashboard Integration Plan
## One-Page Unified Interface

**Created:** 2026-05-05  
**Status:** Planning  
**Goal:** Integrate all HTML versions, Python processing scripts, and documentation into one unified dashboard

---

## 📊 Current State Analysis

### HTML Dashboard Versions (Multiple Iterations)
1. **skills-dashboard-fixed.html** (431KB)
   - Full-featured dashboard with D3.js network visualization
   - 1370 skills across 9 categories from 140 books
   - Tab-based interface: All Skills, All Tags, Overlaps, Multi-tag, Network, Conflicts
   - Embedded skills data in JavaScript

2. **skills-dashboard-ux.html** (431KB)
   - Same data with UX improvements
   - Clickable metrics cards
   - Tag filtering functionality
   - AI integration (ChatGPT/Claude links)

3. **skills-dashboard-updated.html**
   - Updated statistics and descriptions
   - Enhanced skill descriptions from multiple books

4. **dashboard-backups/** (7 versions)
   - Version history tracking all changes
   - Timestamped backups for rollback capability

### Python Processing Scripts (Data Pipeline)
1. **normalize_skills_data.py**
   - Normalizes book summary JSONs into skills database
   - Tag consolidation (163 tags → normalized categories)
   - Filters generic terms and concepts
   - Generates skills_data_updated.json

2. **generate_skill_descriptions.py**
   - Creates comprehensive skill descriptions
   - Aggregates insights from multiple books
   - Enriches descriptions with "Perspectives from X books" format

3. **extract_real_skills.py**
   - Extracts skills from improved book JSONs
   - Handles core_skills and quick_reference sections

4. **clean_skills_and_update_dashboard.py**
   - Cleans and deduplicates skills
   - Updates HTML dashboard with cleaned data

5. **fix_dashboard_issues.py**
   - Fixes duplicate timestamps
   - Makes metrics cards clickable
   - Applies UX improvements

6. **implement_ux_stories.py**
   - Implements 7 UX improvement stories
   - Adds timestamp, fixes metrics, tag filtering
   - Adds accordion view and AI integration
   - Fixes network visualization

7. **incremental_ux_workflow.py**
   - Manages incremental improvements with backups
   - Test-driven workflow (apply → test → commit or rollback)
   - Git-style versioning with timestamps

### Test Scripts
- **test_dashboard.py** - Basic dashboard tests
- **test_dashboard_simple.py** - Simplified test suite
- **test_ux_stories.py** - UX functionality tests

### Data Files (JSON)
- **skills_data_updated.json** - Primary data source
- **skills_data_fixed.json** - Fixed version
- **skills_data_real.json** - Real data extract
- **skills_data_actionable.json** - Actionable skills
- **skills_data_final.json** - Final version

### Markdown Documentation (Obsidian Vault)
- **README.md** - Project overview
- **Index.md** - Main index
- **YouTube-Watch-Later.md** - Content curation
- Multiple topic-specific markdown files in raw/ingested/

---

## 🎯 Integration Plan

### Phase 1: Unified Data Layer
**Objective:** Single source of truth for all skills data

1. **Create Master Data Pipeline Script**
   - `build_master_dashboard.py`
   - Combines: normalize → generate_descriptions → clean → update
   - One command to regenerate entire dashboard
   - Outputs: `skills_data_master.json` + `skills-dashboard-master.html`

2. **Data Structure Standardization**
   ```json
   {
     "metadata": {
       "version": "6.0",
       "last_updated": "2026-05-05T20:00:00Z",
       "total_books": 140,
       "total_skills": 443,
       "total_tags": 15
     },
     "skills": { /* skill_id -> skill_data */ },
     "tags": { /* tag_id -> tag_data */ },
     "books": { /* book_id -> book_data */ },
     "relationships": {
       "skill_tags": [/* skill_id, tag_id */],
       "book_skills": [/* book_id, skill_id */],
       "overlaps": {/* skill_id -> [book_ids] */}
     }
   }
   ```

### Phase 2: Unified HTML Dashboard
**Objective:** Single HTML file with all features, no version conflicts

1. **Consolidate Best Features from All Versions**
   - From skills-dashboard-fixed.html: Network visualization, all tabs
   - From skills-dashboard-ux.html: Clickable metrics, tag filtering, AI integration
   - From skills-dashboard-updated.html: Enhanced descriptions

2. **Unified Dashboard Structure**
   ```html
   <html>
   <head>
     <!-- All CSS from best versions -->
     <!-- D3.js for network viz -->
   </head>
   <body>
     <!-- Header with version info & last updated -->
     <!-- Metrics cards (clickable) -->
     <!-- Navigation tabs -->
     
     <!-- Tab Contents:
          - All Skills (searchable, filterable)
          - By Category (accordion view)
          - Multi-Disciplinary (cross-tag skills)
          - Cross-Book (overlaps)
          - Network View (D3.js)
          - Conflict Resolution Guide
          - Data Sources (books list)
      -->
     
     <!-- Skill Detail Modal -->
     <!-- AI Integration Menu -->
     <!-- Footer with timestamp & version -->
   </body>
   <script>
     // Master data object
     // All view functions
     // All event handlers
   </script>
   </html>
   ```

3. **Add New Features**
   - **Data Management Panel**: Button to regenerate data from Python scripts
   - **Version Control UI**: View/restore previous versions from dashboard-backups/
   - **Export Options**: Download data as JSON, CSV, or filtered views
   - **Bookmarking**: Save current view/state as URL hash
   - **Search Across All Views**: Global search bar

### Phase 3: Python Integration Layer
**Objective:** Make dashboard self-updating from source data

1. **Web Server Mode (Optional)**
   - Run as local Flask/FastAPI server
   - Live data updates without page refresh
   - API endpoints for data access

2. **Dashboard Builder CLI**
   ```bash
   python build_dashboard.py --full          # Full rebuild
   python build_dashboard.py --data-only      # Update data only
   python build_dashboard.py --backup         # Create backup before update
   python build_dashboard.py --rollback VERSION  # Restore version
   ```

3. **Automated Testing**
   - Run tests before each deployment
   - Validate data integrity
   - Check for broken links/references

### Phase 4: Documentation Integration
**Objective:** Connect dashboard to Obsidian documentation

1. **Add Documentation Tab**
   - Render README.md content
   - Link to relevant markdown files
   - Show data pipeline documentation

2. **Skill Context Links**
   - Each skill links to related book notes
   - Backlinks to skills from markdown files
   - Tag-based navigation to related topics

3. **Export to Obsidian**
   - Generate skill pages as markdown
   - Create tag index pages
   - Update main Index.md

---

## 📁 File Structure After Integration

```
wiki-personal/
├── skills-dashboard.html          # ← UNIFIED DASHBOARD (main file)
├── build_dashboard.py              # ← Master build script
├── skills_data_master.json         # ← Master data file
│
├── dashboard-backups/              # Version history (preserved)
│   ├── skills-dashboard-v5.0-20260505_203212.html
│   ├── skills-dashboard-v5.0-20260505_203224.html
│   └── ...
│
├── scripts/                        # Python processing scripts
│   ├── normalize_skills_data.py
│   ├── generate_skill_descriptions.py
│   ├── extract_real_skills.py
│   ├── clean_skills_and_update_dashboard.py
│   └── test_dashboard.py
│
├── data/                           # Source data
│   ├── skills_data_updated.json
│   ├── skills_data_fixed.json
│   └── skills_data_final.json
│
├── docs/                           # Documentation
│   ├── README.md
│   ├── DASHBOARD_INTEGRATION_PLAN.md
│   ├── CHANGELOG.md
│   └── DATA_PIPELINE.md
│
└── raw/ingested/                   # Obsidian vault (unchanged)
    └── Users/kirkwon/obsidian_vaults/personal/
        ├── README.md
        ├── Index.md
        └── ...
```

---

## 🚀 Implementation Steps

### Step 1: Create Master Build Script
- [ ] Write `build_dashboard.py`
- [ ] Implement full pipeline: normalize → generate → clean → update
- [ ] Add backup creation with timestamp
- [ ] Add validation checks
- [ ] Test with existing data

### Step 2: Consolidate HTML Dashboard
- [ ] Merge best features from all HTML versions
- [ ] Ensure all JavaScript functions work
- [ ] Test all tabs and interactions
- [ ] Verify responsive design
- [ ] Check accessibility

### Step 3: Add New Features
- [ ] Data management panel
- [ ] Version control UI (view backups)
- [ ] Export functionality
- [ ] Global search
- [ ] URL hash navigation

### Step 4: Integrate Documentation
- [ ] Add Documentation tab
- [ ] Render markdown content
- [ ] Link to Obsidian files
- [ ] Add skill context links

### Step 5: Testing & Refinement
- [ ] Run all test scripts
- [ ] Fix any broken functionality
- [ ] Test with real data
- [ ] Performance optimization
- [ ] Browser compatibility testing

### Step 6: Deployment
- [ ] Create final backup
- [ ] Deploy unified dashboard
- [ ] Update documentation
- [ ] Archive old versions
- [ ] Create migration guide

---

## 📋 Success Criteria

✅ **Single HTML Dashboard**: One file that works standalone  
✅ **Complete Feature Set**: All best features from previous versions  
✅ **One-Command Build**: `python build_dashboard.py --full`  
✅ **Version History**: All backups preserved in dashboard-backups/  
✅ **Integrated Documentation**: Links to markdown files  
✅ **Data Integrity**: All skills, tags, and books accurately represented  
✅ **Test Coverage**: All functionality tested and working  
✅ **Export Options**: Download data in multiple formats  
✅ **User-Friendly**: Intuitive interface with clear navigation  

---

## 🔧 Technical Specifications

### Dashboard Features
- **Tab 1: All Skills** - Searchable table of 443 skills
- **Tab 2: By Category** - Accordion view of 15 categories
- **Tab 3: Multi-Disciplinary** - 352 cross-tag skills
- **Tab 4: Cross-Book** - Skills appearing in multiple books
- **Tab 5: Network View** - D3.js force-directed graph
- **Tab 6: Conflict Guide** - Decision framework for conflicting advice
- **Tab 7: Data Sources** - List of 140 books with metadata
- **Tab 8: Documentation** - Project docs and links to markdown

### Interactive Features
- Clickable metrics cards (navigate to views)
- Clickable skill names (show detail modal)
- Clickable tag badges (filter by tag)
- AI integration (ChatGPT/Claude links per skill)
- Network graph (drag nodes, hover for details)
- Global search (search across all views)
- Export data (JSON/CSV filtered views)
- Version control (view/restore backups)
- URL hash navigation (bookmarkable views)

### Data Pipeline
1. **Source**: 140 book JSONs in `/Downloads/book_summaries/unified_books_improved/`
2. **Normalize**: `normalize_skills_data.py` → extract skills, normalize tags
3. **Generate**: `generate_skill_descriptions.py` → enhance descriptions
4. **Clean**: `clean_skills_and_update_dashboard.py` → deduplicate, fix issues
5. **Build**: `build_dashboard.py` → generate unified dashboard

---

## 📝 Notes

- **Why 443 skills not 1370?**: After deduplication and generic term filtering, the actual unique skill count is 443. The 1370 number included duplicates and generic terms.
- **Tag Normalization**: 163 raw tags consolidated to 15 categories
- **Book Coverage**: 140 books processed from improved JSON format
- **Backup Strategy**: Keep all existing backups, add new ones with v6.0 prefix
- **Rollback Plan**: Each build creates timestamped backup before overwriting

---

## 🎨 Mockup / Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  📚 Book Skills Dashboard          v6.0  [Last Updated: Now]│
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │  443    │ │   15    │ │   352   │ │   5     │           │
│  │ Skills  │ │Categories│ │Multi-Disc│ │Cross-Book│         │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│                                                               │
│  [All Skills] [By Category] [Multi-Disc] [Cross-Book]       │
│  [Network] [Conflicts] [Data Sources] [Documentation]       │
│                                                               │
│  🔍 [Global Search Bar                          📤 Export]  │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │  [View Content - Depends on selected tab]           │   │
│  │                                                     │   │
│  │  - Tables with sortable headers                     │   │
│  │  - Accordion for categories                         │   │
│  │  - D3.js network graph                              │   │
│  │  - Search results                                   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  [🔄 Regenerate Data] [📜 View History] [❓ Help]           │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

**Next Step**: Implement `build_dashboard.py` to create the unified dashboard.
