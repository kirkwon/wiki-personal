#!/usr/bin/env python3
"""
Generate comprehensive skill descriptions by aggregating insights from all books.
For multi-book skills, creates a unified description showing different perspectives.
"""

import json
from pathlib import Path
from collections import defaultdict

# Load the data
data_file = Path("/Users/kirkwon/wiki-personal/skills_data_updated.json")
with open(data_file, 'r') as f:
    data = json.load(f)

# Load the original book JSONs to get more context
books_dir = Path("/Users/kirkwon/Downloads/book_summaries/unified_books_improved")
book_data = {}

for json_file in books_dir.glob("*.json"):
    try:
        with open(json_file, 'r') as f:
            book = json.load(f)
            title = book.get('metadata', {}).get('title', '')
            if title:
                book_data[title] = book
    except:
        continue

print(f"📚 Loaded {len(book_data)} books for context")

# Enhanced description generator
def generate_skill_description(skill_name, books, tags):
    """Generate comprehensive description by combining insights from all books."""

    # Try to get descriptions from each book's perspective
    book_perspectives = []

    for book_title in books:
        if book_title in book_data:
            book = book_data[book_title]

            # Check quick_reference
            why_it_matters = book.get('quick_reference', {}).get('why_it_matters', '')
            big_picture = book.get('quick_reference', {}).get('the_big_picture', '')
            bottom_line = book.get('quick_reference', {}).get('the_bottom_line', '')

            # Check core_skills for this skill
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

            # If no exact match in core_skills, use quick_reference
            if not any(p['book'] == book_title for p in book_perspectives):
                if why_it_matters and skill_name.lower() in why_it_matters.lower():
                    book_perspectives.append({
                        'book': book_title,
                        'purpose': why_it_matters,
                        'trigger': ''
                    })
                elif big_picture and skill_name.lower() in big_picture.lower():
                    book_perspectives.append({
                        'book': book_title,
                        'purpose': big_picture,
                        'trigger': ''
                    })

    # Build comprehensive description
    if len(book_perspectives) == 0:
        return None

    if len(book_perspectives) == 1:
        # Single book - simple description
        p = book_perspectives[0]
        if p['trigger'] and p['trigger'] != f"When you need to apply {skill_name.lower()}":
            return f"{p['purpose']} (Trigger: {p['trigger']})"
        return p['purpose']

    # Multiple books - aggregate perspectives
    description_parts = []
    description_parts.append(f"**Perspectives from {len(book_perspectives)} book{'s' if len(book_perspectives) > 1 else ''}:**\n")

    for i, p in enumerate(book_perspectives[:3], 1):  # Max 3 books to keep it readable
        short_title = p['book'].split(' - ')[0] if ' - ' in p['book'] else p['book']
        desc = f"From {short_title}: {p['purpose']}"
        if p['trigger'] and p['trigger'] != f"When you need to apply {skill_name.lower()}":
            desc += f"\n  Trigger: {p['trigger']}"
        description_parts.append(f"{i}. {desc}")

    if len(book_perspectives) > 3:
        description_parts.append(f"\n+ {len(book_perspectives) - 3} more perspective(s)")

    return '\n'.join(description_parts)

# Generate descriptions for all skills
print("📝 Generating comprehensive descriptions...")
enhanced_descriptions = {}

# Process all skills
for skill_name in data['all_skills']:
    # Get all books that mention this skill
    skill_sources = data.get('overlaps', {})
    if skill_name in skill_sources:
        books = skill_sources[skill_name]
    else:
        # Find from skills_by_tag
        books = set()
        for tag, skills in data['skills_by_tag'].items():
            for skill, book in skills:
                if skill == skill_name:
                    books.add(book)
        books = list(books)

    # Get tags for this skill
    tags = data.get('multi_tag_skills', {}).get(skill_name, [])
    if not tags:
        # Find tags from skills_by_tag
        for tag, skills in data['skills_by_tag'].items():
            if any(skill == skill_name for skill, _ in skills):
                tags.append(tag)

    # Generate description
    description = generate_skill_description(skill_name, books, tags)
    if description:
        enhanced_descriptions[skill_name] = description

print(f"✅ Generated {len(enhanced_descriptions)} enhanced descriptions")

# Update the data
data['descriptions'] = enhanced_descriptions

# Fix the counts
unique_skill_count = len(data['all_skills'])
unique_tag_count = len(data['all_tags'])
overlaps_count = len(data.get('overlaps', {}))
multi_tag_count = len(data.get('multi_tag_skills', {}))

data['stats'] = {
    'total_skills': unique_skill_count,
    'total_tags': unique_tag_count,
    'total_books': len(set(book for skills in data['skills_by_tag'].values() for _, book in skills)),
    'overlapping': overlaps_count,
    'multi_tag': multi_tag_count
}

# Save updated data
output_file = Path("/Users/kirkwon/wiki-personal/skills_data_updated.json")
with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"💾 Updated data saved to: {output_file}")

# Now update the HTML
html_file = Path("/Users/kirkwon/wiki-personal/skills-dashboard-updated.html")
with open(html_file, 'r') as f:
    html_content = f.read()

# Replace the data
import re

# Update the embedded JavaScript data
new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions']
}, indent=2)

if 'const skillsData = {' in html_content:
    parts = html_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        remaining = parts[1]
        end_idx = remaining.find('};', 2)
        if end_idx > 0:
            after_data = remaining[end_idx + 2:]
            html_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data

# Update subtitle
html_content = re.sub(
    r'Interactive visualization of \d+ skills across \d+ categories',
    f'Interactive visualization of {unique_skill_count} unique skills across {unique_tag_count} tag categories',
    html_content
)

# Update stat cards
html_content = re.sub(
    r'<div class="stat-card" onclick="showTab\(\'allSkills\'\)">\s+<h3>Total Skills</h3>\s+<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'allSkills\')">\n                <h3>Unique Skills</h3>\n                <div class="value">{unique_skill_count}</div>',
    html_content
)

html_content = re.sub(
    r'<div class="stat-card" onclick="showTab\(\'allTags\'\)">\s+<h3>Unique Tags</h3>\s+<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'allTags\')">\n                <h3>Tag Categories</h3>\n                <div class="value">{unique_tag_count}</div>',
    html_content
)

html_content = re.sub(
    r'<div class="stat-card" onclick="showTab\(\'overlaps\'\)">\s+<h3>Overlapping Skills</h3>\s+<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'overlaps\')">\n                <h3>Overlapping Skills</h3>\n                <div class="value">{overlaps_count}</div>',
    html_content
)

html_content = re.sub(
    r'<div class="stat-card" onclick="showTab\(\'multitag\'\)">\s+<h3>Multi-Tag Skills</h3>\s+<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'multitag\')">\n                <h3>Multi-Tag Skills</h3>\n                <div class="value">{multi_tag_count}</div>',
    html_content
)

# Update tab headers
html_content = re.sub(r'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({unique_skill_count})</h2>', html_content)
html_content = re.sub(r'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({unique_tag_count})</h2>', html_content)
html_content = re.sub(r'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({overlaps_count})</h2>', html_content)
html_content = re.sub(r'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({multi_tag_count})</h2>', html_content)

# Save updated HTML
with open(html_file, 'w') as f:
    f.write(html_content)

print(f"✅ Updated HTML dashboard: {html_file}")

print("\n" + "=" * 80)
print("DESCRIPTION ENHANCEMENT COMPLETE")
print("=" * 80)
print(f"📊 Unique skills: {unique_skill_count}")
print(f"🏷️  Tag categories: {unique_tag_count}")
print(f"📝 Enhanced descriptions: {len(enhanced_descriptions)}")
print(f"📚 Skills in multiple books: {overlaps_count}")

# Show some examples
print(f"\n📝 Sample enhanced descriptions:")
print("=" * 80)
for skill in list(data['overlaps'].keys())[:3]:
    if skill in enhanced_descriptions:
        print(f"\n🔹 {skill}")
        desc = enhanced_descriptions[skill]
        if len(desc) > 200:
            print(f"   {desc[:200]}...")
        else:
            print(f"   {desc}")
