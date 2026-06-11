#!/usr/bin/env python3
"""
Fix dashboard issues:
1. Remove duplicate tags (use Set instead of array)
2. Fix network graph visualization
3. Clean up remaining fragments
"""

import json
from pathlib import Path
from collections import defaultdict

# Load the data
with open('skills_data_final.json', 'r') as f:
    data = json.load(f)

print("🔧 Fixing Dashboard Issues")
print("=" * 80)

# Issue 1: Further clean up fragments
def is_complete_skill(skill):
    """Check if skill is a complete phrase."""
    # Remove incomplete phrases
    if skill.endswith(('The', 'A', 'An', 'Of', 'In', 'To', 'For', 'With', 'About', 'Vs', 'Or')):
        return False

    # Remove single words
    if len(skill.split()) < 2:
        return False

    # Remove generic words
    generic = ['secret', 'science', 'future', 'decision', 'basics']
    if skill.lower() in generic:
        return False

    # Must have meaningful content
    if skill.startswith(('Assessing Our', 'Aligning Your')) and len(skill.split()) < 5:
        return False

    return True

print("\n1️⃣ Cleaning up remaining fragments...")
clean_skills = [s for s in data['all_skills'] if is_complete_skill(s)]
removed = len(data['all_skills']) - len(clean_skills)
print(f"   Removed {removed} fragments")
print(f"   Remaining: {len(clean_skills)} skills")

# Rebuild skills_by_tag with unique tags only
print("\n2️⃣ Rebuilding tag structure (removing duplicates)...")

# Build unique skill-tag-book mapping
unique_skills_data = defaultdict(lambda: defaultdict(set))  # skill -> tag -> set of books

for tag, skills in data['skills_by_tag'].items():
    for skill, book in skills:
        if skill in clean_skills:
            unique_skills_data[skill][tag].add(book)

# Convert to final structure
skills_by_tag_unique = defaultdict(list)
for skill, tags_books in unique_skills_data.items():
    for tag, books in tags_books.items():
        # Add skill once per tag (not per book)
        skills_by_tag_unique[tag].append([skill, list(books)[0]])  # Use first book as reference

print(f"   Built unique structure: {len(skills_by_tag_unique)} tags")

# Build all_skills with unique tags
all_skills_final = []
skill_info_map = {}  # skill -> {tags: set(), books: set()}

for skill in clean_skills:
    tags = set()
    books = set()

    for tag, skills in skills_by_tag_unique.items():
        for s, b in skills:
            if s == skill:
                tags.add(tag)
                books.add(b)

    skill_info_map[skill] = {
        'tags': list(tags),
        'books': list(books)
    }
    all_skills_final.append(skill)

print(f"   Processed {len(all_skills_final)} skills with unique tags")

# Find overlaps and multi-tag skills
overlaps = {}
multi_tag_skills = {}

for skill, info in skill_info_map.items():
    if len(info['books']) > 1:
        overlaps[skill] = info['books']
    if len(info['tags']) > 1:
        multi_tag_skills[skill] = info['tags']

print(f"   Overlapping skills: {len(overlaps)}")
print(f"   Multi-tag skills: {len(multi_tag_skills)}")

# Generate descriptions
descriptions = {}
for skill in all_skills_final:
    info = skill_info_map[skill]
    if len(info['books']) > 1:
        descriptions[skill] = f"Taught in {len(info['books'])} books: {', '.join(info['books'][:3])}{'...' if len(info['books']) > 3 else ''}"
    else:
        descriptions[skill] = f"A skill from {info['books'][0] if info['books'] else 'various books'}"

# Build final data
final_data = {
    "skills_by_tag": {k: v for k, v in skills_by_tag_unique.items()},
    "all_skills": sorted(all_skills_final),
    "all_tags": sorted(skills_by_tag_unique.keys()),
    "overlaps": overlaps,
    "multi_tag_skills": multi_tag_skills,
    "descriptions": descriptions
}

print(f"\n3️⃣ Final statistics:")
print(f"   Skills: {len(final_data['all_skills'])}")
print(f"   Tags: {len(final_data['all_tags'])}")
print(f"   Overlaps: {len(final_data['overlaps'])}")
print(f"   Multi-tag: {len(final_data['multi_tag_skills'])}")

# Save fixed data
output_file = Path("/Users/kirkwon/wiki-personal/skills_data_fixed.json")
with open(output_file, 'w') as f:
    json.dump(final_data, f, indent=2)

print(f"\n💾 Saved to: {output_file}")

# Now update the HTML with fixed JavaScript
print("\n4️⃣ Updating HTML dashboard...")

html_file = Path("/Users/kirkwon/wiki-personal/skills-dashboard-updated.html")
with open(html_file, 'r') as f:
    html_content = f.read()

# Update the embedded data
new_data_json = json.dumps(final_data, indent=2)

if 'const skillsData = {' in html_content:
    parts = html_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        remaining = parts[1]
        end_idx = remaining.find('};', 2)
        if end_idx > 0:
            after_data = remaining[end_idx + 2:]
            html_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data
            print("   ✓ Updated embedded data")

# Fix the skillInfoMap building logic to prevent duplicate tags
old_build_logic = r'''Object.entries(skillsData.skills_by_tag).forEach(([tag, skills]) => {
            skills.forEach(([skill, book]) => {
                if (!skillInfoMap[skill]) {
                    skillInfoMap[skill] = { tags: [], books: [], description: skillsData.descriptions[skill] || null };
                }
                skillInfoMap[skill].tags.push(tag);
                if (!skillInfoMap[skill].books.includes(book)) {
                    skillInfoMap[skill].books.push(book);
                }
            });
        });'''

new_build_logic = r'''Object.entries(skillsData.skills_by_tag).forEach(([tag, skills]) => {
            skills.forEach(([skill, book]) => {
                if (!skillInfoMap[skill]) {
                    skillInfoMap[skill] = { tags: new Set(), books: [], description: skillsData.descriptions[skill] || null };
                }
                skillInfoMap[skill].tags.add(tag);  // Use Set to prevent duplicates
                if (!skillInfoMap[skill].books.includes(book)) {
                    skillInfoMap[skill].books.push(book);
                }
            });
        });

        // Convert Sets to Arrays for display
        Object.keys(skillInfoMap).forEach(skill => {
            skillInfoMap[skill].tags = Array.from(skillInfoMap[skill].tags);
        });'''

if old_build_logic in html_content:
    html_content = html_content.replace(old_build_logic, new_build_logic)
    print("   ✓ Fixed duplicate tags in skillInfoMap")
elif 'skillsData.skills_by_tag' in html_content:
    # Find and replace the section
    import re
    pattern = r'Object\.entries\(skillsData\.skills_by_tag\)\.forEach.*?\}\);'
    html_content = re.sub(pattern, new_build_logic, html_content, flags=re.DOTALL)
    print("   ✓ Fixed duplicate tags using regex")

# Fix network graph - handle case where we have fewer than 30 tags
old_network = '''// Get top 30 tags by skill count
            const topTags = Object.entries(skillsData.skills_by_tag)
                .sort((a, b) => b[1].length - a[1].length)
                .slice(0, 30);'''

new_network = '''// Get all tags (we have fewer than 30)
            const allTags = Object.entries(skillsData.skills_by_tag)
                .sort((a, b) => b[1].length - a[1].length);

            const topTags = allTags.slice(0, Math.min(30, allTags.length));

            // Skip network if too few tags
            if (topTags.length < 3) {
                document.getElementById('networkContainer').innerHTML =
                    '<p style="padding: 40px; text-align: center; color: #666;">Not enough tags to display network</p>';
                return;
            }'''

if old_network in html_content:
    html_content = html_content.replace(old_network, new_network)
    print("   ✓ Fixed network graph initialization")
else:
    print("   ! Network graph code pattern changed, manual update may be needed")

# Update statistics in HTML
skill_count = len(final_data['all_skills'])
tag_count = len(final_data['all_tags'])
overlaps_count = len(final_data['overlaps'])
multi_tag_count = len(final_data['multi_tag_skills'])

html_content = html_content.replace(
    r'Interactive visualization of \d+ actionable skills',
    f'Interactive visualization of {skill_count} actionable skills'
)

# Update stat cards
stat_updates = [
    (rf'<div class="value">{skill_count - 10}</div>', f'<div class="value">{skill_count}</div>'),
    (rf'<h3>Actionable Skills</h3>', '<h3>Actionable Skills</h3>'),
    (rf'<h3>Tag Categories</h3>\s*<div class="value">\d+</div>',
     f'<h3>Tag Categories</h3>\n                <div class="value">{tag_count}</div>'),
    (rf'<h3>Overlapping Skills</h3>\s*<div class="value">\d+</div>',
     f'<h3>Overlapping Skills</h3>\n                <div class="value">{overlaps_count}</div>'),
    (rf'<h3>Multi-Tag Skills</h3>\s*<div class="value">\d+</div>',
     f'<h3>Multi-Tag Skills</h3>\n                <div class="value">{multi_tag_count}</div>'),
]

for old, new in stat_updates:
    html_content = html_content.replace(old, new)

# Update headers
header_updates = [
    (rf'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({skill_count})</h2>'),
    (rf'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({tag_count})</h2>'),
    (rf'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({overlaps_count})</h2>'),
    (rf'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({multi_tag_count})</h2>'),
]

for old, new in header_updates:
    html_content = html_content.replace(old, new)

# Save updated HTML
with open(html_file, 'w') as f:
    f.write(html_content)

print(f"✅ Updated HTML: {html_file}")

# Show sample
print(f"\n📝 Sample skills with unique tags:")
print("=" * 80)
for skill in list(final_data['all_skills'])[:5]:
    info = skill_info_map[skill]
    print(f"• {skill}")
    print(f"  Tags: {', '.join(info['tags'])}")
    print(f"  Books: {len(info['books'])}")
    print()
