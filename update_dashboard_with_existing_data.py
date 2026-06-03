#!/usr/bin/env python3
"""
Update unified dashboard using existing rich data (skills_data_fixed.json)
This preserves the 443 skills from the original extraction.
"""

import json
import re
from datetime import datetime
from pathlib import Path

print("🔄 UPDATING DASHBOARD WITH EXISTING RICH DATA")
print("=" * 80)

# Load the rich data
source_data_file = Path("skills_data_fixed.json")
if not source_data_file.exists():
    print(f"❌ Source data not found: {source_data_file}")
    exit(1)

with open(source_data_file, 'r') as f:
    data = json.load(f)

print(f"✅ Loaded data from: {source_data_file}")
print(f"   Skills: {len(data['all_skills'])}")
print(f"   Tags: {len(data['all_tags'])}")
print(f"   Overlaps: {len(data['overlaps'])}")
print(f"   Multi-tag: {len(data['multi_tag_skills'])}")

# Load template HTML
template_files = [
    "skills-dashboard-ux.html",
    "skills-dashboard-fixed.html",
]

template_content = None
for template_file in template_files:
    template_path = Path(template_file)
    if template_path.exists():
        with open(template_path, 'r') as f:
            template_content = f.read()
        print(f"\n✅ Using template: {template_file}")
        break

if not template_content:
    print("❌ No template file found")
    exit(1)

# Update the embedded data
new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions'],
    "stats": data.get('stats', {
        "total_skills": len(data['all_skills']),
        "total_tags": len(data['all_tags']),
        "total_books": len(set(book for skills in data['skills_by_tag'].values() for _, book in skills)),
        "overlapping": len(data['overlaps']),
        "multi_tag": len(data['multi_tag_skills'])
    })
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
            print("✅ Updated embedded data")

# Update statistics
stats = data.get('stats', {})
total_skills = stats.get('total_skills', len(data['all_skills']))
total_tags = stats.get('total_tags', len(data['all_tags']))
total_books = stats.get('total_books', len(set(book for skills in data['skills_by_tag'].values() for _, book in skills)))

template_content = re.sub(
    r'Interactive visualization of \d+ skills across \d+ categories',
    f'Interactive visualization of {total_skills} skills across {total_tags} categories (from {total_books} books)',
    template_content
)

# Update subtitle with version info
timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
template_content = re.sub(
    r'<p class="subtitle">[^<]*</p>',
    f'<p class="subtitle">Unified skills dashboard v6.0 • Last updated: {timestamp}</p>',
    template_content
)

# Update stat cards
stats_to_update = [
    ('Total Skills', 'skills', total_skills),
    ('Categories', 'tags', total_tags),
    ('Multi-Disciplinary', 'multitag', len(data['multi_tag_skills'])),
    ('Cross-Book', 'overlaps', len(data['overlaps'])),
]

for label, view, value in stats_to_update:
    # Handle both stat-label and h3 formats
    template_content = re.sub(
        rf'<div class="stat-card"[^>]*>\s*<(div class="stat-label"|h3)>{re.escape(label)}</(?:div class="stat-label"|h3)>\s*<div class="value">\d+</div>',
        f'<div class="stat-card" onclick="showView(\'{view}\')" style="cursor: pointer;">\n                <h3>{label}</h3>\n                <div class="value">{value}</div>',
        template_content
    )

# Update tab headers
template_content = re.sub(r'<h2>All Skills \(\d+\)</h2>', f'<h2>All Skills ({total_skills})</h2>', template_content)
template_content = re.sub(r'<h2>All Tags \(\d+\)</h2>', f'<h2>All Tags ({total_tags})</h2>', template_content)
template_content = re.sub(r'<h2>Overlapping Skills \(\d+\)</h2>', f'<h2>Overlapping Skills ({len(data["overlaps"])})</h2>', template_content)
template_content = re.sub(r'<h2>Multi-Tag Skills \(\d+\)</h2>', f'<h2>Multi-Tag Skills ({len(data["multi_tag_skills"])})</h2>', template_content)

# Save outputs
output_html = Path("skills-dashboard.html")
output_json = Path("skills_data_master.json")

# Save JSON
with open(output_json, 'w') as f:
    json.dump(data, f, indent=2)
print(f"\n✅ Saved data: {output_json}")

# Save HTML
with open(output_html, 'w') as f:
    f.write(template_content)
print(f"✅ Saved dashboard: {output_html}")

# Create backup
BACKUP_DIR = Path("dashboard-backups")
BACKUP_DIR.mkdir(exist_ok=True)
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"{output_html.stem}-v6.0-{timestamp_str}.html"
backup_path = BACKUP_DIR / backup_name
import shutil
shutil.copy2(output_html, backup_path)
print(f"✅ Created backup: {backup_name}")

print("\n" + "=" * 80)
print("📊 UPDATE COMPLETE")
print("=" * 80)
print(f"Version: v6.0")
print(f"Dashboard: {output_html}")
print(f"Data: {output_json}")
print(f"Total Skills: {total_skills}")
print(f"Total Tags: {total_tags}")
print(f"Total Books: {total_books}")
print(f"Overlapping: {len(data['overlaps'])}")
print(f"Multi-tag: {len(data['multi_tag_skills'])}")
print(f"\nOpen in browser: file://{output_html.absolute()}")
