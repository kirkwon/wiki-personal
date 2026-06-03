#!/usr/bin/env python3
"""
Normalize the improved book summaries data and generate skills dashboard.
Extracts skills from the new JSON format and creates the visualization.
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter

# Paths
new_data_dir = Path("/Users/kirkwon/Downloads/book_summaries/unified_books_improved")
output_dir = Path("/Users/kirkwon/wiki-personal")
output_html = output_dir / "skills-dashboard-updated.html"
output_json = output_dir / "skills_data_updated.json"

# Data structures
skills_by_tag = defaultdict(list)  # tag -> [(skill, book), ...]
all_skills = defaultdict(list)  # skill -> [(book, tag), ...]
skill_descriptions = {}  # skill -> description
book_tags = defaultdict(set)  # book -> set of tags

# Tag normalization mapping (to consolidate similar tags)
tag_normalization = {
    'habit-formation': 'habits',
    'habit': 'habits',
    'mindset': 'psychology',
    'personal-development': 'self-improvement',
    'time-management': 'productivity',
    'decision-making': 'productivity',
    'mental-models': 'thinking',
    'cognitive-bias': 'thinking',
    'first-principles': 'thinking',
    'systems-thinking': 'thinking',
    'second-order': 'thinking',
    'behavioral-economics': 'psychology',
    'behavioral-finance': 'finance',
    'information-management': 'organization',
    'knowledge-management': 'organization',
    'task-management': 'productivity',
    'project-management': 'productivity',
    'deep-work': 'focus',
    'distraction': 'focus',
    'attention': 'focus',
    'single-tasking': 'focus',
    'prioritization': 'productivity',
    'execution': 'productivity',
    'goals': 'productivity',
    'compounding': 'habits',
    'procrastination': 'psychology',
    'self-awareness': 'psychology',
    'learning': 'self-improvement',
    'second-brain': 'organization',
    'gtd': 'organization',
    'workflow': 'productivity',
    'uncertainty': 'risk-management',
    'risk': 'risk-management',
    'probabilistic-thinking': 'decision-making',
    'bias': 'thinking',
    'randomness': 'risk-management',
    'black-swan': 'risk-management',
    'fragility': 'risk-management',
    'resilience': 'risk-management',
    'antifragility': 'risk-management',
    'sunk-cost': 'decision-making',
    'opportunity-cost': 'decision-making',
    'negotiation': 'communication',
    'persuasion': 'communication',
    'influence': 'communication',
    'social-proof': 'psychology',
    'commitment': 'psychology',
    'authority': 'leadership',
    'liking': 'psychology',
    'scarcity': 'psychology',
    'choice-architecture': 'decision-making',
    'default-options': 'decision-making',
    'opt-out-vs-opt-in': 'decision-making',
    'salience': 'psychology',
    'loss-aversion': 'psychology',
    'incentives': 'leadership',
    'bottleneck': 'productivity',
    'theory-of-constraints': 'productivity',
    'subordination': 'productivity',
    'local-vs-global-optimum': 'decision-making',
    'continuous-improvement': 'productivity',
    'efficiency-vs-profit': 'productivity',
    'constraint-elevation': 'productivity',
    'exploitation': 'productivity',
    'throughput': 'productivity',
    'constraints': 'productivity',
    'communication': 'productivity',
    'axios-format': 'communication',
    'logic': 'thinking',
    'first-principles': 'thinking',
    'mental-models': 'thinking',
    'strategic': 'strategy',
    'algorithms': 'thinking',
    'computer-science': 'thinking',
    'optimization': 'productivity',
    'game-theory': 'strategy',
    'sales': 'communication',
    'reciprocity': 'psychology',
    'asymmetry': 'risk-management',
    'safety': 'risk-management',
    'lindy-effect': 'risk-management',
    'via-negativa': 'thinking',
    'accountability': 'leadership',
    'long-term': 'strategy',
    'anxiety': 'psychology',
    'overload': 'psychology',
    'filtering': 'organization',
    'exit-strategy': 'decision-making',
    'quitting': 'decision-making',
    'regret': 'psychology',
    'lifestyle-design': 'productivity',
    'entrepreneurship': 'business',
    'automation': 'technology',
    'money': 'finance',
    'wealth': 'finance',
    'investing': 'finance',
    'saving': 'finance',
    'prediction': 'thinking',
    'skepticism': 'thinking',
    'narrative': 'psychology',
    'survivorship': 'thinking',
    'volatility': 'risk-management',
    'extremistan': 'risk-management',
    'optionality': 'risk-management',
    'bureaucracy': 'leadership',
    'information-filtering': 'organization',
    'design': 'organization',
    'usability': 'design',
    'ux': 'design',
    'product-design': 'design',
    'human-centered': 'design',
    'burnout': 'psychology',
    'boundaries': 'psychology',
    'death-perspective': 'philosophy',
    'philosophy': 'thinking',
    'business': 'strategy',
    'leadership': 'strategy',
    'strategy': 'strategy',
    'teamwork': 'leadership',
    'management': 'leadership',
    'ethics': 'philosophy',
    'purpose': 'leadership',
    'values': 'philosophy',
    'motivation': 'psychology',
    'action': 'productivity',
    'success': 'self-improvement',
    'failure': 'psychology',
    'change': 'psychology',
    'adaptation': 'self-improvement',
    'growth': 'self-improvement',
    'performance': 'productivity',
    'optimal-experience': 'focus',
    'flow': 'focus',
    'environment': 'productivity',
    'routine': 'daily-rituals',
    'morning-routine': 'daily-rituals',
    'leisure': 'energy',
}

def normalize_tag(tag):
    """Normalize tag to consolidated category."""
    tag_lower = tag.lower().strip()
    # Remove special characters and convert to lowercase
    tag_clean = re.sub(r'[^\w\s-]', '', tag_lower).strip()
    # Use normalization mapping
    return tag_normalization.get(tag_clean, tag_clean)

def extract_book_title(filepath):
    """Extract clean book title from filename."""
    # Remove _improved.json suffix and extract title
    title = filepath.stem.replace('_improved', '')
    # Remove author name if present
    if ' - ' in title:
        title = title.split(' - ')[0]
    return title

print("🔍 Scanning for JSON files...")
json_files = list(new_data_dir.glob("*.json"))
print(f"   Found {len(json_files)} files")

# Process each JSON file
for json_file in json_files:
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Extract metadata
        metadata = data.get('metadata', {})
        book_title = metadata.get('title', extract_book_title(json_file))

        # Get tags from metadata
        tags = metadata.get('tags', [])
        normalized_tags = [normalize_tag(t) for t in tags]
        normalized_tags = [t for t in normalized_tags if t]  # Remove empty

        # Store book's tags
        for tag in normalized_tags:
            book_tags[book_title].add(tag)

        # Extract core skills from agent_structure
        agent_structure = data.get('agent_structure', {})
        core_skills = agent_structure.get('core_skills', [])

        # Generic/non-descriptive terms to skip
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
            # Additional generic terms
            'theory', 'challenges', 'challenge', 'life', 'purpose', 'tasks', 'trust',
            'relationships', 'importance', 'meaning', 'attitude', 'duhigg', 'clear',
            'allen', 'david', 'sinek', 'frankl', 'viktor', 'kelly', 'galloway', 'scott'
        }

        for skill_data in core_skills:
            skill_name = skill_data.get('skill_name', '').strip()
            purpose = skill_data.get('purpose', '').strip()
            trigger = skill_data.get('trigger', '').strip()

            # Skip generic skill names
            if not skill_name or skill_name.lower() in generic_terms:
                continue

            # Skip single character or very short skill names
            if len(skill_name) < 3:
                continue

            # Skip if skill name is just a verb with no object
            if skill_name.lower() in {'plan', 'do', 'make', 'get', 'take', 'use', 'create', 'build'}:
                continue

            # Store skill with each normalized tag
            for tag in normalized_tags:
                skills_by_tag[tag].append((skill_name, book_title))
                all_skills[skill_name].append((book_title, tag))

            # Store description (combine purpose and trigger)
            description = purpose
            if trigger and trigger != f"When you need to apply {skill_name.lower()}":
                description = f"{purpose} (Trigger: {trigger})"

            if skill_name not in skill_descriptions:
                skill_descriptions[skill_name] = description

        # Also extract from quick_reference core_concepts (with filtering)
        quick_ref = data.get('quick_reference', {})
        core_concepts = quick_ref.get('core_concepts', [])

        # Generic concepts to skip
        generic_concepts = {
            'habits', 'habit', 'change', 'concept', 'concepts', 'changes', 'strategies',
            'strategy', 'formation', 'points', 'framework', 'frameworks', 'principles',
            'principle', 'systems', 'system', 'models', 'model', 'patterns', 'pattern',
            'tools', 'tool', 'methods', 'method', 'approaches', 'approach', 'skills',
            'skill', 'techniques', 'technique', 'process', 'processes', 'steps', 'step'
        }

        for concept in core_concepts:
            concept = concept.strip()

            # Skip generic concepts
            if not concept or len(concept) <= 3 or concept.lower() in generic_concepts:
                continue

            # Skip if it's in the generic terms list
            if concept.lower() in generic_terms:
                continue

            # Use first tag for concept
            if normalized_tags:
                tag = normalized_tags[0]
                skills_by_tag[tag].append((concept, book_title))
                all_skills[concept].append((book_title, tag))

                # Add a generic description if none exists
                if concept not in skill_descriptions:
                    skill_descriptions[concept] = f"Core concept from {book_title}"

    except Exception as e:
        print(f"   ⚠️  Error processing {json_file.name}: {e}")
        continue

print(f"✅ Processed {len(all_skills)} unique skills from {len(book_tags)} books")

# Find overlapping skills (appear in multiple books)
overlaps = {}
for skill, sources in all_skills.items():
    books = list(set(s[0] for s in sources))
    if len(books) > 1:
        overlaps[skill] = books

# Find skills in multiple tags
multi_tag_skills = {}
for skill, sources in all_skills.items():
    tags = list(set(tag for _, tag in sources))
    if len(tags) > 1:
        multi_tag_skills[skill] = tags

# Prepare data
all_skills_list = sorted(all_skills.keys())
all_tags_list = sorted(set(skills_by_tag.keys()))

print(f"\n📊 Statistics:")
print(f"   Total skills: {len(all_skills_list)}")
print(f"   Total tags: {len(all_tags_list)}")
print(f"   Overlapping skills: {len(overlaps)}")
print(f"   Multi-tag skills: {len(multi_tag_skills)}")

# Show top tags
print(f"\n🏷️  Top 10 tags by skill count:")
for tag, skills in sorted(skills_by_tag.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
    print(f"   {tag}: {len(skills)} skills")

# Save JSON data
output_data = {
    "skills_by_tag": {k: [[s[0], s[1]] for s in v] for k, v in skills_by_tag.items()},
    "all_skills": all_skills_list,
    "all_tags": all_tags_list,
    "overlaps": overlaps,
    "multi_tag_skills": multi_tag_skills,
    "descriptions": skill_descriptions,
    "stats": {
        "total_skills": len(all_skills_list),
        "total_tags": len(all_tags_list),
        "total_books": len(book_tags),
        "overlapping": len(overlaps),
        "multi_tag": len(multi_tag_skills)
    }
}

with open(output_json, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"\n💾 Saved data to: {output_json}")

# Now generate the HTML dashboard (using the same template as before)
print(f"\n🎨 Generating HTML dashboard...")

# Read the original HTML to get the template
original_html = Path("/Users/kirkwon/wiki-personal/skills-dashboard-fixed.html")
with open(original_html, 'r') as f:
    html_content = f.read()

# Replace the embedded data with new data
import re

# Find and replace the skillsData object
# Use a simpler approach: split on the const skillsData line and rebuild
if 'const skillsData = {' in html_content:
    parts = html_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        # Find the end of the data object (closing };)
        remaining = parts[1]
        end_idx = remaining.find('};', 2)  # Skip past the first {
        if end_idx > 0:
            # Keep everything after the data object
            after_data = remaining[end_idx + 2:]

            # Create new data
            new_data_json = json.dumps({
                "skills_by_tag": {k: [[s[0], s[1]] for s in v] for k, v in skills_by_tag.items()},
                "all_skills": all_skills_list,
                "all_tags": all_tags_list,
                "overlaps": overlaps,
                "multi_tag_skills": multi_tag_skills,
                "descriptions": skill_descriptions
            }, indent=2)

            # Rebuild HTML
            html_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data

# Update statistics in the HTML
html_content = re.sub(r'Interactive visualization of \d+ skills across \d+ categories',
                    f'Interactive visualization of {len(all_skills_list)} skills across {len(all_tags_list)} categories',
                    html_content)

html_content = re.sub(r'<div class="value">\d+</div>\s*</div>\s+<div class="stat-card" onclick="showTab\(\'allSkills\'\)">\s+<h3>Total Skills</h3>',
                    f'<div class="value">{len(all_skills_list)}</div>\n            </div>\n            <div class="stat-card" onclick="showTab(\'allSkills\')">\n                <h3>Total Skills</h3>',
                    html_content)

html_content = re.sub(r'<div class="value">9</div>\s*</div>\s+<div class="stat-card" onclick="showTab\(\'allTags\'\)">\s+<h3>Unique Tags</h3>',
                    f'<div class="value">{len(all_tags_list)}</div>\n            </div>\n            <div class="stat-card" onclick="showTab(\'allTags\')">\n                <h3>Unique Tags</h3>',
                    html_content)

html_content = re.sub(r'<div class="value">33</div>\s*</div>\s+<div class="stat-card" onclick="showTab\(\'overlaps\'\)">\s+<h3>Overlapping Skills</h3>',
                    f'<div class="value">{len(overlaps)}</div>\n            </div>\n            <div class="stat-card" onclick="showTab(\'overlaps\')">\n                <h3>Overlapping Skills</h3>',
                    html_content)

html_content = re.sub(r'<div class="value">561</div>\s*</div>\s+<div class="stat-card" onclick="showTab\(\'multitag\'\)">\s+<h3>Multi-Tag Skills</h3>',
                    f'<div class="value">{len(multi_tag_skills)}</div>\n            </div>\n            <div class="stat-card" onclick="showTab(\'multitag\')">\n                <h3>Multi-Tag Skills</h3>',
                    html_content)

# Update tab headers with counts
html_content = re.sub(r'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({len(all_skills_list)})</h2>', html_content)
html_content = re.sub(r'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({len(all_tags_list)})</h2>', html_content)
html_content = re.sub(r'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({len(overlaps)})</h2>', html_content)
html_content = re.sub(r'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({len(multi_tag_skills)})</h2>', html_content)

# Save updated HTML
with open(output_html, 'w') as f:
    f.write(html_content)

print(f"✅ Created updated dashboard: {output_html}")
print(f"   Open in browser: file://{output_html}")

print("\n" + "=" * 80)
print("NORMALIZATION COMPLETE")
print("=" * 80)
print(f"📁 Input directory: {new_data_dir}")
print(f"📊 Output JSON: {output_json}")
print(f"🎨 Output HTML: {output_html}")
print(f"📚 Books processed: {len(book_tags)}")
print(f"🎯 Skills extracted: {len(all_skills_list)}")
print(f"🏷️  Tags after normalization: {len(all_tags_list)}")
