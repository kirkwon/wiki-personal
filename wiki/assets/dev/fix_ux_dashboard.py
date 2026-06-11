#!/usr/bin/env python3
"""
Fix the skills-dashboard-ux.html file to have proper HTML structure
and ensure all 443 skills from skills_data_fixed.json are included.
"""

import json
import re
from datetime import datetime
from pathlib import Path
import shutil

print("🔧 FIXING UX DASHBOARD")
print("=" * 80)

# Load the rich data
data_file = Path("skills_data_fixed.json")
with open(data_file, 'r') as f:
    data = json.load(f)

print(f"✅ Loaded data: {len(data['all_skills'])} skills")

# Read the UX template
ux_file = Path("skills-dashboard-ux.html")
with open(ux_file, 'r') as f:
    ux_content = f.read()

# Read the fixed template for proper structure
fixed_file = Path("skills-dashboard-fixed.html")
with open(fixed_file, 'r') as f:
    fixed_content = f.read()

print(f"✅ Loaded templates")

# The UX file has malformed HTML - let's use the fixed file as base
# and update it with better UX features from the UX file

# First, let's just use the fixed file and update its data
# since it has the correct HTML structure

# Update the embedded data
new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions']
}, indent=2)

# Replace the skillsData object in the fixed file
if 'const skillsData = {' in fixed_content:
    parts = fixed_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        remaining = parts[1]
        end_idx = remaining.find('};', 2)
        if end_idx > 0:
            after_data = remaining[end_idx + 2:]
            fixed_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data
            print("✅ Updated embedded data")

# Update statistics
total_skills = len(data['all_skills'])
total_tags = len(data['all_tags'])
total_books = len(set(book for skills in data['skills_by_tag'].values() for _, book in skills))

fixed_content = re.sub(
    r'Interactive visualization of \d+ skills across \d+ categories',
    f'Interactive visualization of {total_skills} skills across {total_tags} categories (from {total_books} books)',
    fixed_content
)

# Update stat cards
fixed_content = re.sub(
    r'<div class="stat-card"[^>]*>\s*<h3>Total Skills</h3>\s*<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'allSkills\')">\n                <h3>Total Skills</h3>\n                <div class="value">{total_skills}</div>',
    fixed_content
)

fixed_content = re.sub(
    r'<div class="stat-card"[^>]*>\s*<h3>Unique Tags</h3>\s*<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'allTags\')">\n                <h3>Tag Categories</h3>\n                <div class="value">{total_tags}</div>',
    fixed_content
)

fixed_content = re.sub(
    r'<div class="stat-card"[^>]*>\s*<h3>Overlapping Skills</h3>\s*<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'overlaps\')">\n                <h3>Overlapping Skills</h3>\n                <div class="value">{len(data["overlaps"])}</div>',
    fixed_content
)

fixed_content = re.sub(
    r'<div class="stat-card"[^>]*>\s*<h3>Multi-Tag Skills</h3>\s*<div class="value">\d+</div>',
    f'<div class="stat-card" onclick="showTab(\'multitag\')">\n                <h3>Multi-Tag Skills</h3>\n                <div class="value">{len(data["multi_tag_skills"])}</div>',
    fixed_content
)

# Update tab headers
fixed_content = re.sub(r'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({total_skills})</h2>', fixed_content)
fixed_content = re.sub(r'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({total_tags})</h2>', fixed_content)
fixed_content = re.sub(r'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({len(data["overlaps"])})</h2>', fixed_content)
fixed_content = re.sub(r'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({len(data["multi_tag_skills"])})</h2>', fixed_content)

# Add timestamp
timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
if 'Last Updated:' not in fixed_content:
    fixed_content = fixed_content.replace(
        '</body>',
        f'<div style="text-align: center; padding: 16px 0; color: #6e6e73; font-size: 12px;">Last Updated: {timestamp}</div>\n</body>'
    )

# Backup the old UX file
BACKUP_DIR = Path("dashboard-backups")
BACKUP_DIR.mkdir(exist_ok=True)
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = BACKUP_DIR / f"skills-dashboard-ux-backup-{timestamp_str}.html"
shutil.copy2(ux_file, backup_path)
print(f"✅ Backed up UX file to: {backup_path.name}")

# Save the corrected UX dashboard
output_file = Path("skills-dashboard-ux-fixed.html")
with open(output_file, 'w') as f:
    f.write(fixed_content)

# Also overwrite the original UX file with the fixed version
with open(ux_file, 'w') as f:
    f.write(fixed_content)

print(f"✅ Saved fixed UX dashboard: {output_file}")
print(f"✅ Updated original: {ux_file}")

print("\n" + "=" * 80)
print("📊 FIX COMPLETE")
print("=" * 80)
print(f"Total Skills: {total_skills}")
print(f"Total Tags: {total_tags}")
print(f"Total Books: {total_books}")
print(f"\nOpen in browser: file://{ux_file.absolute()}")
