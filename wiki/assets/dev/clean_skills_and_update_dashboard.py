#!/usr/bin/env python3
"""
Clean up the actionable skills data and update the dashboard.
"""

import json
from pathlib import Path

# Load the actionable skills data
with open('skills_data_actionable.json', 'r') as f:
    data = json.load(f)

# Further cleanup - remove fragments
def is_complete_skill(skill):
    """Check if skill is a complete phrase."""
    # Remove incomplete phrases
    if skill.endswith(('The', 'A', 'An', 'Of', 'In', 'To', 'For', 'With', 'About')):
        return False

    # Remove questions
    if skill.startswith(('Are', 'Is', 'Will', 'Can', 'Should', 'Do', 'Does')):
        return False

    # Must be at least 3 words or have good structure
    words = skill.split()
    if len(words) < 2:
        return False

    # Remove generic patterns
    if skill.startswith('Aligning Your') and len(skill.split()) < 5:
        return False

    return True

# Filter skills
clean_skills = [s for s in data['all_skills'] if is_complete_skill(s)]

# Rebuild data structure
clean_data = {
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": clean_skills,
    "all_tags": data['all_tags'],
    "overlaps": {k: v for k, v in data['overlaps'].items() if k in clean_skills},
    "multi_tag_skills": {k: v for k, v in data['multi_tag_skills'].items() if k in clean_skills},
    "descriptions": {k: v for k, v in data['descriptions'].items() if k in clean_skills},
    "stats": {
        "total_skills": len(clean_skills),
        "total_tags": len(data['all_tags']),
        "total_books": data['stats']['total_books'],
        "overlapping": len([k for k in clean_skills if k in data['overlaps']]),
        "multi_tag": len([k for k in clean_skills if k in data['multi_tag_skills']])
    }
}

print(f"📊 Cleaned skills: {len(clean_skills)} (removed {len(data['all_skills']) - len(clean_skills)} fragments)")

# Save cleaned data
output_file = Path("/Users/kirkwon/wiki-personal/skills_data_final.json")
with open(output_file, 'w') as f:
    json.dump(clean_data, f, indent=2)

print(f"💾 Saved to: {output_file}")

# Update the HTML dashboard
html_file = Path("/Users/kirkwon/wiki-personal/skills-dashboard-updated.html")
with open(html_file, 'r') as f:
    html_content = f.read()

# Replace the data
new_data_json = json.dumps({
    "skills_by_tag": clean_data['skills_by_tag'],
    "all_skills": clean_data['all_skills'],
    "all_tags": clean_data['all_tags'],
    "overlaps": clean_data['overlaps'],
    "multi_tag_skills": clean_data['multi_tag_skills'],
    "descriptions": clean_data['descriptions']
}, indent=2)

if 'const skillsData = {' in html_content:
    parts = html_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        remaining = parts[1]
        end_idx = remaining.find('};', 2)
        if end_idx > 0:
            after_data = remaining[end_idx + 2:]
            html_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data

# Update counts
skill_count = len(clean_data['all_skills'])
tag_count = len(clean_data['all_tags'])
overlaps_count = clean_data['stats']['overlapping']
multi_tag_count = clean_data['stats']['multi_tag']

html_content = html_content.replace(
    'Interactive visualization of 367 unique skills across 10 tag categories',
    f'Interactive visualization of {skill_count} actionable skills across {tag_count} categories'
)

html_content = html_content.replace(
    '<h3>Unique Skills</h3>\n                <div class="value">367</div>',
    f'<h3>Actionable Skills</h3>\n                <div class="value">{skill_count}</div>'
)

html_content = html_content.replace(
    f'<h3>Tag Categories</h3>\n                <div class="value">10</div>',
    f'<h3>Tag Categories</h3>\n                <div class="value">{tag_count}</div>'
)

html_content = html_content.replace(
    '<h3>Overlapping Skills</h3>\n                <div class="value">60</div>',
    f'<h3>Overlapping Skills</h3>\n                <div class="value">{overlaps_count}</div>'
)

html_content = html_content.replace(
    '<h3>Multi-Tag Skills</h3>\n                <div class="value">105</div>',
    f'<h3>Multi-Tag Skills</h3>\n                <div class="value">{multi_tag_count}</div>'
)

html_content = html_content.replace(f'<h2>All Skills (367)</h2>', f'<h2>All Skills ({skill_count})</h2>')
html_content = html_content.replace(f'<h2>All Tags (10)</h2>', f'<h2>All Tags ({tag_count})</h2>')
html_content = html_content.replace(f'<h2>Overlapping Skills (60)</h2>', f'<h2>Overlapping Skills ({overlaps_count})</h2>')
html_content = html_content.replace(f'<h2>Multi-Tag Skills (105)</h2>', f'<h2>Multi-Tag Skills ({multi_tag_count})</h2>')

# Save updated HTML
with open(html_file, 'w') as f:
    f.write(html_content)

print(f"✅ Updated HTML: {html_file}")

print("\n📝 Sample cleaned skills:")
print("=" * 80)
for i, skill in enumerate(clean_data['all_skills'][:20]):
    print(f"{i+1}. {skill}")

print(f"\n📊 Final Stats:")
print(f"   Actionable Skills: {skill_count}")
print(f"   Tag Categories: {tag_count}")
print(f"   Overlapping Skills: {overlaps_count}")
print(f"   Multi-Tag Skills: {multi_tag_count}")
