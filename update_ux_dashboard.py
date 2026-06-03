#!/usr/bin/env python3
"""
Update the UX dashboard with real data
"""

import json

# Load the fixed data
with open('skills_data_fixed.json', 'r') as f:
    data = json.load(f)

# Load the UX template
with open('skills-dashboard-ux.html', 'r') as f:
    html = f.read()

# Update the embedded data
new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions']
}, indent=2)

# Replace the sample data with real data
import re
match = re.search(r'const skillsData = ({.*?});', html, re.DOTALL)
if match:
    html = html[:match.start()] + 'const skillsData = ' + new_data_json + ';' + html[match.end():]

# Update stats
skill_count = len(data['all_skills'])
tag_count = len(data['all_tags'])
multi_tag_count = len(data['multi_tag_skills'])
overlaps_count = len(data['overlaps'])

html = html.replace('id="statTotalSkills">443</div>', f'id="statTotalSkills">{skill_count}</div>')
html = html.replace('id="statCategories">15</div>', f'id="statCategories">{tag_count}</div>')
html = html.replace('id="statMultiTag">352</div>', f'id="statMultiTag">{multi_tag_count}</div>')
html = html.replace('id="statOverlaps">5</div>', f'id="statOverlaps">{overlaps_count}</div>')
html = html.replace('443 skills from 98 books</p>', f'{skill_count} skills from 98 books</p>')

# Save the updated dashboard
with open('skills-dashboard-ux.html', 'w') as f:
    f.write(html)

print(f"✅ UX Dashboard updated with real data")
print(f"   Skills: {skill_count}")
print(f"   Tags: {tag_count}")
print(f"   Multi-tag: {multi_tag_count}")
print(f"   Overlaps: {overlaps_count}")
