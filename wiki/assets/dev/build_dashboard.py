#!/usr/bin/env python3
"""
Master Dashboard Build Script
=============================
Author: Claude
Created: 2026-05-05

This script integrates all HTML, Python, and Markdown files into one unified dashboard.
It creates a complete, self-contained skills dashboard with all features.

Usage:
    python build_dashboard.py --full          # Full rebuild with backup
    python build_dashboard.py --data-only     # Update data only
    python build_dashboard.py --backup        # Create backup
    python build_dashboard.py --rollback VER  # Restore version

Pipeline:
1. Create backup (if --full or --backup)
2. Normalize skills data from book JSONs
3. Generate enhanced descriptions
4. Clean and deduplicate skills
5. Build unified HTML dashboard
6. Run tests
7. Save with timestamp

"""

import json
import shutil
import re
import sys
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter

# Configuration
BASE_VERSION = "v6.0"
BACKUP_DIR = Path("dashboard-backups")
SOURCE_DATA_DIR = Path("/Users/kirkwon/Downloads/book_summaries/unified_books_improved")
OUTPUT_DIR = Path(".")
OUTPUT_HTML = OUTPUT_DIR / "skills-dashboard.html"
OUTPUT_JSON = OUTPUT_DIR / "skills_data_master.json"

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 80}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(80)}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 80}{Colors.END}\n")

def print_step(step_num, total, text):
    print(f"{Colors.CYAN}Step {step_num}/{total}: {Colors.BOLD}{text}{Colors.END}")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def create_backup():
    """Create timestamped backup of current dashboard"""
    if not OUTPUT_HTML.exists():
        print_warning("No existing dashboard to backup")
        return None

    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{OUTPUT_HTML.stem}-{BASE_VERSION}-{timestamp}.html"
    backup_path = BACKUP_DIR / backup_name

    shutil.copy2(OUTPUT_HTML, backup_path)
    print_success(f"Backup created: {backup_name}")
    return backup_path

def normalize_skills_data():
    """
    Extract and normalize skills from book JSONs
    Consolidates tags, filters generic terms, builds relationships
    """
    print_step(1, 5, "Normalizing skills data from book JSONs")

    if not SOURCE_DATA_DIR.exists():
        print_error(f"Source directory not found: {SOURCE_DATA_DIR}")
        return None

    # Data structures
    skills_by_tag = defaultdict(list)
    all_skills = defaultdict(list)
    skill_descriptions = {}
    book_tags = defaultdict(set)
    book_metadata = {}

    # Tag normalization mapping
    tag_normalization = {
        'habit-formation': 'habits', 'habit': 'habits',
        'mindset': 'psychology', 'personal-development': 'self-improvement',
        'time-management': 'productivity', 'decision-making': 'productivity',
        'mental-models': 'thinking', 'cognitive-bias': 'thinking',
        'first-principles': 'thinking', 'systems-thinking': 'thinking',
        'second-order': 'thinking', 'behavioral-economics': 'psychology',
        'behavioral-finance': 'finance', 'information-management': 'organization',
        'knowledge-management': 'organization', 'task-management': 'productivity',
        'project-management': 'productivity', 'deep-work': 'focus',
        'distraction': 'focus', 'attention': 'focus', 'single-tasking': 'focus',
        'prioritization': 'productivity', 'execution': 'productivity',
        'goals': 'productivity', 'compounding': 'habits',
        'procrastination': 'psychology', 'self-awareness': 'psychology',
        'learning': 'self-improvement', 'second-brain': 'organization',
        'gtd': 'organization', 'workflow': 'productivity',
        'uncertainty': 'risk-management', 'risk': 'risk-management',
        'probabilistic-thinking': 'decision-making', 'bias': 'thinking',
        'randomness': 'risk-management', 'black-swan': 'risk-management',
        'fragility': 'risk-management', 'resilience': 'risk-management',
        'antifragility': 'risk-management', 'sunk-cost': 'decision-making',
        'opportunity-cost': 'decision-making', 'negotiation': 'communication',
        'persuasion': 'communication', 'influence': 'communication',
        'social-proof': 'psychology', 'commitment': 'psychology',
        'authority': 'leadership', 'liking': 'psychology', 'scarcity': 'psychology',
        'choice-architecture': 'decision-making', 'default-options': 'decision-making',
        'opt-out-vs-opt-in': 'decision-making', 'salience': 'psychology',
        'loss-aversion': 'psychology', 'incentives': 'leadership',
        'bottleneck': 'productivity', 'theory-of-constraints': 'productivity',
        'subordination': 'productivity', 'local-vs-global-optimum': 'decision-making',
        'continuous-improvement': 'productivity', 'efficiency-vs-profit': 'productivity',
        'constraint-elevation': 'productivity', 'exploitation': 'productivity',
        'throughput': 'productivity', 'constraints': 'productivity',
        'communication': 'productivity', 'axios-format': 'communication',
        'logic': 'thinking', 'strategic': 'strategy', 'algorithms': 'thinking',
        'computer-science': 'thinking', 'optimization': 'productivity',
        'game-theory': 'strategy', 'sales': 'communication',
        'reciprocity': 'psychology', 'asymmetry': 'risk-management',
        'safety': 'risk-management', 'lindy-effect': 'risk-management',
        'via-negativa': 'thinking', 'accountability': 'leadership',
        'long-term': 'strategy', 'anxiety': 'psychology', 'overload': 'psychology',
        'filtering': 'organization', 'exit-strategy': 'decision-making',
        'quitting': 'decision-making', 'regret': 'psychology',
        'lifestyle-design': 'productivity', 'entrepreneurship': 'business',
        'automation': 'technology', 'money': 'finance', 'wealth': 'finance',
        'investing': 'finance', 'saving': 'finance', 'prediction': 'thinking',
        'skepticism': 'thinking', 'narrative': 'psychology', 'survivorship': 'thinking',
        'volatility': 'risk-management', 'extremistan': 'risk-management',
        'optionality': 'risk-management', 'bureaucracy': 'leadership',
        'information-filtering': 'organization', 'design': 'organization',
        'usability': 'design', 'ux': 'design', 'product-design': 'design',
        'human-centered': 'design', 'burnout': 'psychology', 'boundaries': 'psychology',
        'death-perspective': 'philosophy', 'philosophy': 'thinking',
        'business': 'strategy', 'leadership': 'strategy', 'strategy': 'strategy',
        'teamwork': 'leadership', 'management': 'leadership', 'ethics': 'philosophy',
        'purpose': 'leadership', 'values': 'philosophy', 'motivation': 'psychology',
        'action': 'productivity', 'success': 'self-improvement', 'failure': 'psychology',
        'change': 'psychology', 'adaptation': 'self-improvement', 'growth': 'self-improvement',
        'performance': 'productivity', 'optimal-experience': 'focus', 'flow': 'focus',
        'environment': 'productivity', 'routine': 'daily-rituals', 'morning-routine': 'daily-rituals',
        'leisure': 'energy',
    }

    def normalize_tag(tag):
        tag_lower = tag.lower().strip()
        tag_clean = re.sub(r'[^\w\s-]', '', tag_lower).strip()
        return tag_normalization.get(tag_clean, tag_clean)

    # Generic terms to skip
    generic_terms = {
        'technique', 'practice', 'design', 'management', 'learning', 'communication',
        'planning', 'improvement', 'analysis', 'description', 'concepts', 'concept',
        'changes', 'change', 'strategies', 'strategy', 'formation', 'points',
        'success', 'failure', 'game', 'principles', 'principle', 'framework',
        'system', 'systems', 'model', 'models', 'method', 'methods', 'approach',
        'tool', 'tools', 'process', 'processes', 'step', 'steps', 'action',
        'actions', 'result', 'results', 'outcome', 'outcomes', 'goal', 'goals',
        'habit', 'habits', 'skill', 'skills', 'behavior', 'behaviors', 'pattern',
        'patterns', 'frameworks', 'development', 'growth', 'performance', 'focus',
        'decision', 'decisions', 'thinking', 'thought', 'ideas', 'idea', 'value',
        'values', 'belief', 'beliefs', 'knowledge', 'information', 'data', 'time',
        'work', 'energy', 'power', 'control', 'balance', 'order', 'structure',
        'structures', 'organization', 'organize', 'manage', 'plan',
        'create', 'creation', 'creative', 'creativity', 'innovation',
        'innovate', 'innovative', 'improve', 'improving', 'develop',
        'building', 'build', 'execute', 'execution', 'implement',
        'implementation', 'apply', 'application', 'applying', 'use', 'using', 'utilize',
        'theory', 'challenges', 'challenge', 'life', 'purpose', 'tasks', 'trust',
        'relationships', 'importance', 'meaning', 'attitude',
    }

    # Process each book JSON
    json_files = list(SOURCE_DATA_DIR.glob("*.json"))
    print(f"   Found {len(json_files)} book files")

    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            metadata = data.get('metadata', {})
            book_title = metadata.get('title', json_file.stem.replace('_improved', ''))

            # Store book metadata
            book_metadata[book_title] = {
                'title': book_title,
                'author': metadata.get('author', 'Unknown'),
                'tags': metadata.get('tags', []),
                'category': metadata.get('category', 'General')
            }

            # Get and normalize tags
            tags = metadata.get('tags', [])
            normalized_tags = [normalize_tag(t) for t in tags]
            normalized_tags = [t for t in normalized_tags if t]

            for tag in normalized_tags:
                book_tags[book_title].add(tag)

            # Extract core skills
            agent_structure = data.get('agent_structure', {})
            core_skills = agent_structure.get('core_skills', [])

            for skill_data in core_skills:
                skill_name = skill_data.get('skill_name', '').strip()
                purpose = skill_data.get('purpose', '').strip()
                trigger = skill_data.get('trigger', '').strip()

                if not skill_name or skill_name.lower() in generic_terms:
                    continue
                if len(skill_name) < 3:
                    continue
                if skill_name.lower() in {'plan', 'do', 'make', 'get', 'take', 'use', 'create', 'build'}:
                    continue

                for tag in normalized_tags:
                    skills_by_tag[tag].append((skill_name, book_title))
                    all_skills[skill_name].append((book_title, tag))

                description = purpose
                if trigger and trigger != f"When you need to apply {skill_name.lower()}":
                    description = f"{purpose} (Trigger: {trigger})"

                if skill_name not in skill_descriptions:
                    skill_descriptions[skill_name] = description

        except Exception as e:
            print_warning(f"Error processing {json_file.name}: {e}")
            continue

    # Find overlaps and multi-tag skills
    overlaps = {}
    for skill, sources in all_skills.items():
        books = list(set(s[0] for s in sources))
        if len(books) > 1:
            overlaps[skill] = books

    multi_tag_skills = {}
    for skill, sources in all_skills.items():
        tags = list(set(tag for _, tag in sources))
        if len(tags) > 1:
            multi_tag_skills[skill] = tags

    all_skills_list = sorted(all_skills.keys())
    all_tags_list = sorted(set(skills_by_tag.keys()))

    print(f"   Extracted {len(all_skills_list)} unique skills")
    print(f"   Found {len(all_tags_list)} tag categories")
    print(f"   Identified {len(overlaps)} overlapping skills")

    return {
        "skills_by_tag": {k: [[s[0], s[1]] for s in v] for k, v in skills_by_tag.items()},
        "all_skills": all_skills_list,
        "all_tags": all_tags_list,
        "overlaps": overlaps,
        "multi_tag_skills": multi_tag_skills,
        "descriptions": skill_descriptions,
        "book_metadata": book_metadata,
        "stats": {
            "total_skills": len(all_skills_list),
            "total_tags": len(all_tags_list),
            "total_books": len(book_tags),
            "overlapping": len(overlaps),
            "multi_tag": len(multi_tag_skills)
        }
    }

def generate_enhanced_descriptions(data):
    """Enhance skill descriptions with multiple book perspectives"""
    print_step(2, 5, "Generating enhanced skill descriptions")

    # Load original book JSONs for context
    book_data = {}
    for json_file in SOURCE_DATA_DIR.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                book = json.load(f)
                title = book.get('metadata', {}).get('title', '')
                if title:
                    book_data[title] = book
        except:
            continue

    print(f"   Loaded {len(book_data)} books for context")

    enhanced_descriptions = {}

    for skill_name in data['all_skills']:
        # Get books that mention this skill
        if skill_name in data['overlaps']:
            books = data['overlaps'][skill_name]
        else:
            books = set()
            for tag, skills in data['skills_by_tag'].items():
                for skill, book in skills:
                    if skill == skill_name:
                        books.add(book)
            books = list(books)

        # Get tags
        tags = data.get('multi_tag_skills', {}).get(skill_name, [])
        if not tags:
            for tag, skills in data['skills_by_tag'].items():
                if any(skill == skill_name for skill, _ in skills):
                    tags.append(tag)

        # Generate description from book perspectives
        book_perspectives = []
        for book_title in books:
            if book_title in book_data:
                book = book_data[book_title]
                why_it_matters = book.get('quick_reference', {}).get('why_it_matters', '')
                big_picture = book.get('quick_reference', {}).get('the_big_picture', '')

                core_skills = book.get('agent_structure', {}).get('core_skills', [])
                for skill_data in core_skills:
                    if skill_data.get('skill_name', '').strip() == skill_name:
                        purpose = skill_data.get('purpose', '')
                        trigger = skill_data.get('trigger', '')
                        if purpose:
                            book_perspectives.append({
                                'book': book_title,
                                'purpose': purpose,
                                'trigger': trigger
                            })
                        break

                if not any(p['book'] == book_title for p in book_perspectives):
                    if why_it_matters and skill_name.lower() in why_it_matters.lower():
                        book_perspectives.append({
                            'book': book_title,
                            'purpose': why_it_matters,
                            'trigger': ''
                        })
                    elif big_picture and skill_name.lower() in big_picture.lower():
                        book_perspectives.append({
                            'book': big_picture,
                            'purpose': big_picture,
                            'trigger': ''
                        })

        # Build enhanced description
        if len(book_perspectives) == 0:
            enhanced_descriptions[skill_name] = data['descriptions'].get(skill_name, 'No description available.')
        elif len(book_perspectives) == 1:
            p = book_perspectives[0]
            if p['trigger']:
                enhanced_descriptions[skill_name] = f"{p['purpose']} (Trigger: {p['trigger']})"
            else:
                enhanced_descriptions[skill_name] = p['purpose']
        else:
            # Multiple books - aggregate
            parts = [f"**Perspectives from {len(book_perspectives)} sources:**\n"]
            for i, p in enumerate(book_perspectives[:3], 1):
                short_title = p['book'].split(' - ')[0] if ' - ' in p['book'] else p['book']
                desc = f"From {short_title}: {p['purpose']}"
                if p['trigger'] and p['trigger'] != f"When you need to apply {skill_name.lower()}":
                    desc += f"\n  Trigger: {p['trigger']}"
                parts.append(f"{i}. {desc}")

            if len(book_perspectives) > 3:
                parts.append(f"\n+ {len(book_perspectives) - 3} more perspective(s)")

            enhanced_descriptions[skill_name] = '\n'.join(parts)

    data['descriptions'] = enhanced_descriptions
    print(f"   Enhanced {len(enhanced_descriptions)} descriptions")
    return data

def build_unified_html(data):
    """Build the unified HTML dashboard"""
    print_step(3, 5, "Building unified HTML dashboard")

    # Read template from existing dashboard
    template_files = [
        "skills-dashboard-ux.html",
        "skills-dashboard-fixed.html",
        "skills-dashboard-updated.html"
    ]

    template_content = None
    for template_file in template_files:
        template_path = Path(template_file)
        if template_path.exists():
            with open(template_path, 'r') as f:
                template_content = f.read()
            print(f"   Using template: {template_file}")
            break

    if not template_content:
        print_error("No template file found")
        return None

    # Update the embedded data
    new_data_json = json.dumps({
        "skills_by_tag": data['skills_by_tag'],
        "all_skills": data['all_skills'],
        "all_tags": data['all_tags'],
        "overlaps": data['overlaps'],
        "multi_tag_skills": data['multi_tag_skills'],
        "descriptions": data['descriptions'],
        "stats": data['stats']
    }, indent=2)

    # Replace the skillsData object
    if 'const skillsData = {' in template_content:
        parts = template_content.split('const skillsData = {', 1)
        if len(parts) == 2:
            remaining = parts[1]
            end_idx = remaining.find('};', 2)
            if end_idx > 0:
                after_data = remaining[end_idx + 2:]
                template_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data

    # Update statistics
    stats = data['stats']
    template_content = re.sub(
        r'Interactive visualization of \d+ skills across \d+ categories',
        f'Interactive visualization of {stats["total_skills"]} skills across {stats["total_tags"]} categories (from {stats["total_books"]} books)',
        template_content
    )

    # Update subtitle
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    template_content = re.sub(
        r'<p class="subtitle">[^<]*</p>',
        f'<p class="subtitle">Unified skills dashboard v{BASE_VERSION} • Last updated: {timestamp}</p>',
        template_content
    )

    # Update stat cards
    template_content = re.sub(
        r'<div class="value">\d+</div>\s*</div>\s+<div class="stat-card"[^>]*>\s*<h3>Total Skills</h3>',
        f'<div class="value">{stats["total_skills"]}</div>\n            </div>\n            <div class="stat-card" onclick="showView(\'skills\')">\n                <h3>Total Skills</h3>',
        template_content
    )

    # Update all stat cards
    stat_updates = [
        ('Unique Tags', 'tags', stats["total_tags"]),
        ('Multi-Disciplinary', 'multitag', stats["multi_tag"]),
        ('Cross-Book', 'overlaps', stats["overlapping"])
    ]

    for label, view, value in stat_updates:
        template_content = re.sub(
            rf'<div class="stat-card"[^>]*>\s*<h3>{re.escape(label)}</h3>\s*<div class="value">\d+</div>',
            f'<div class="stat-card" onclick="showView(\'{view}\')" style="cursor: pointer;">\n                <h3>{label}</h3>\n                <div class="value">{value}</div>',
            template_content
        )

    # Update tab headers
    template_content = re.sub(r'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({stats["total_skills"]})</h2>', template_content)
    template_content = re.sub(r'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({stats["total_tags"]})</h2>', template_content)
    template_content = re.sub(r'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({stats["overlapping"]})</h2>', template_content)
    template_content = re.sub(r'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({stats["multi_tag"]})</h2>', template_content)

    print_success("HTML dashboard built successfully")
    return template_content

def save_outputs(data, html_content):
    """Save JSON data and HTML dashboard"""
    print_step(4, 5, "Saving outputs")

    # Save JSON data
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(data, f, indent=2)
    print_success(f"Data saved: {OUTPUT_JSON}")

    # Save HTML dashboard
    with open(OUTPUT_HTML, 'w') as f:
        f.write(html_content)
    print_success(f"Dashboard saved: {OUTPUT_HTML}")

def run_tests():
    """Run basic validation tests"""
    print_step(5, 5, "Running validation tests")

    tests_passed = 0
    tests_total = 5

    # Test 1: JSON file exists and is valid
    try:
        with open(OUTPUT_JSON, 'r') as f:
            data = json.load(f)
        print_success("JSON data is valid")
        tests_passed += 1
    except Exception as e:
        print_error(f"JSON validation failed: {e}")

    # Test 2: HTML file exists
    if OUTPUT_HTML.exists():
        print_success("HTML dashboard exists")
        tests_passed += 1
    else:
        print_error("HTML dashboard not found")

    # Test 3: Required data fields present
    required_fields = ['skills_by_tag', 'all_skills', 'all_tags', 'overlaps', 'multi_tag_skills', 'descriptions', 'stats']
    if all(field in data for field in required_fields):
        print_success("All required data fields present")
        tests_passed += 1
    else:
        print_error("Missing required data fields")

    # Test 4: Data consistency
    if len(data['all_skills']) == data['stats']['total_skills']:
        print_success("Data counts are consistent")
        tests_passed += 1
    else:
        print_error("Data count mismatch")

    # Test 5: HTML contains data
    with open(OUTPUT_HTML, 'r') as f:
        html = f.read()
    if 'const skillsData =' in html and 'skillsData.all_skills' in html:
        print_success("HTML contains embedded data")
        tests_passed += 1
    else:
        print_error("HTML missing embedded data")

    print(f"\n   Tests passed: {tests_passed}/{tests_total}")
    return tests_passed == tests_total

def main():
    parser = argparse.ArgumentParser(description='Build unified skills dashboard')
    parser.add_argument('--full', action='store_true', help='Full rebuild with backup')
    parser.add_argument('--data-only', action='store_true', help='Update data only')
    parser.add_argument('--backup', action='store_true', help='Create backup only')
    parser.add_argument('--rollback', type=str, metavar='VERSION', help='Rollback to version')

    args = parser.parse_args()

    print_header("🚀 SKILLS DASHBOARD BUILDER")

    if args.rollback:
        print(f"Rolling back to {args.rollback}...")
        # Implement rollback logic
        backup_files = list(BACKUP_DIR.glob(f"*{args.rollback}*"))
        if backup_files:
            shutil.copy2(backup_files[0], OUTPUT_HTML)
            print_success(f"Rolled back to {args.rollback}")
        else:
            print_error(f"Backup {args.rollback} not found")
        return

    if args.backup:
        backup_path = create_backup()
        return

    # Full build or data-only
    if args.full or args.data_only:
        if args.full:
            create_backup()

        # Step 1: Normalize data
        data = normalize_skills_data()
        if not data:
            print_error("Failed to normalize data")
            return

        # Step 2: Enhance descriptions
        data = generate_enhanced_descriptions(data)

        # Step 3: Save JSON data
        with open(OUTPUT_JSON, 'w') as f:
            json.dump(data, f, indent=2)
        print_success(f"Data saved: {OUTPUT_JSON}")

        if args.data_only:
            print_success("Data update complete")
            return

    # Build HTML dashboard
    if not args.data_only:
        # Load or build data
        if OUTPUT_JSON.exists():
            with open(OUTPUT_JSON, 'r') as f:
                data = json.load(f)
        else:
            data = normalize_skills_data()
            data = generate_enhanced_descriptions(data)

        html_content = build_unified_html(data)
        if not html_content:
            print_error("Failed to build HTML")
            return

        save_outputs(data, html_content)

        # Run tests
        all_passed = run_tests()

        print_header("📊 BUILD COMPLETE")
        print(f"Version: {Colors.BOLD}{BASE_VERSION}{Colors.END}")
        print(f"Dashboard: {OUTPUT_HTML}")
        print(f"Data: {OUTPUT_JSON}")
        print(f"Total Skills: {data['stats']['total_skills']}")
        print(f"Total Tags: {data['stats']['total_tags']}")
        print(f"Total Books: {data['stats']['total_books']}")
        print()

        if all_passed:
            print_success("All tests passed! ✨")
        else:
            print_warning("Some tests failed - please review")

        print(f"\nOpen in browser: file://{OUTPUT_HTML.absolute()}")

if __name__ == '__main__':
    main()
