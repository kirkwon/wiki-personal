#!/usr/bin/env python3
"""
Update the ORIGINAL UX dashboard (skills-dashboard-ux.html)
with the rich 443-skill data WITHOUT changing the UI structure.
"""

import json
import re
from pathlib import Path

print("🔄 UPDATING ORIGINAL UX DASHBOARD WITH RICH DATA")
print("=" * 80)

# Load the rich data
data_file = Path("skills_data_fixed.json")
with open(data_file, 'r') as f:
    data = json.load(f)

print(f"✅ Loaded rich data: {len(data['all_skills'])} skills")

# Read the original UX dashboard
ux_file = Path("skills-dashboard-ux.html")
with open(ux_file, 'r') as f:
    ux_content = f.read()

print(f"✅ Loaded original UX dashboard")

# The original UX has malformed HTML but it works somehow
# We just need to update the embedded data

# Find and replace the skillsData object
# The UX file has: const skillsData = {...};
new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions']
}, indent=2)

# Find the skillsData and replace it
if 'const skillsData =' in ux_content:
    # Find the start
    start_idx = ux_content.find('const skillsData =')
    if start_idx > 0:
        # Find the end (closing };)
        search_from = start_idx + len('const skillsData =')
        end_idx = ux_content.find('};', search_from)
        if end_idx > 0:
            # Replace everything between = and };
            before = ux_content[:start_idx + len('const skillsData =')]
            after = ux_content[end_idx + 2:]  # Skip }; and go to next
            ux_content = before + ' ' + new_data_json + ';' + after
            print("✅ Updated embedded data")

# Update statistics in the HTML
ux_content = re.sub(
    r'<div class="stat-value" id="statTotalSkills">\d+</div>',
    f'<div class="stat-value" id="statTotalSkills">{len(data["all_skills"])}</div>',
    ux_content
)

ux_content = re.sub(
    r'<div class="stat-value" id="statCategories">\d+</div>',
    f'<div class="stat-value" id="statCategories">{len(data["all_tags"])}</div>',
    ux_content
)

ux_content = re.sub(
    r'<div class="stat-value" id="statMultiTag">\d+</div>',
    f'<div class="stat-value" id="statMultiTag">{len(data["multi_tag_skills"])}</div>',
    ux_content
)

ux_content = re.sub(
    r'<div class="stat-value" id="statOverlaps">\d+</div>',
    f'<div class="stat-value" id="statOverlaps">{len(data["overlaps"])}</div>',
    ux_content
)

# Save the updated file
with open(ux_file, 'w') as f:
    f.write(ux_content)

print(f"✅ Saved updated UX dashboard: {ux_file}")

print("\n" + "=" * 80)
print("📊 UPDATE COMPLETE")
print("=" * 80)
print(f"Total Skills: {len(data['all_skills'])}")
print(f"Total Tags: {len(data['all_tags'])}")
print(f"Multi-Disciplinary: {len(data['multi_tag_skills'])}")
print(f"Overlapping: {len(data['overlaps'])}")
print(f"\nOpen in browser: file://{ux_file.absolute()}")
