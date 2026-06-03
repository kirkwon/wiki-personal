#!/usr/bin/env python3
"""
Fix issues from incremental improvements
1. Remove duplicate timestamps (keep only most recent)
2. Fix CSS variables that weren't substituted
"""

import re
from datetime import datetime
from pathlib import Path

# Load current file
html_file = Path("skills-dashboard-updated.html")
with open(html_file, 'r') as f:
    html = f.read()

print("🔧 Fixing Issues...")

# Fix 1: Remove duplicate timestamps
print("\n1️⃣  Fixing duplicate timestamps...")
# Find all timestamps
timestamps = re.findall(r'Last Updated: ([^<]+)</div>', html)
print(f"   Found {len(timestamps)} timestamps")

# Remove all of them
html = re.sub(r'<div style="text-align: center; padding: 16px 0; color: #6e6e73; font-size: 12px;">\s*Last Updated: [^<]+</div>', '', html)
print(f"   Removed all timestamps")

# Add single timestamp
timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
single_timestamp = f'''
    <div style="text-align: center; padding: 16px 0; color: #6e6e73; font-size: 12px;">
        Last Updated: {timestamp}
    </div>'''

html = html.replace('</body>', single_timestamp + '</body>')
print(f"   Added single timestamp: {timestamp}")

# Fix 2: Fix CSS variables
print("\n2️⃣  Fixing CSS variables...")
# Replace {timestamp} with actual value
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
html = html.replace('{timestamp}', current_time)
print(f"   Fixed timestamp variables: {current_time}")

# Fix 3: Ensure CSS is properly applied
print("\n3️⃣  Ensuring CSS is applied...")
# Check if the new CSS exists
if 'linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%)' in html:
    print("   ✅ Visual polish CSS found")
else:
    print("   ⚠️  Visual polish CSS not found - adding now")
    # Add the polish CSS properly
    polish_css = '''
<style>
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .stat-card:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.08) !important;
        border-color: #0071e3 !important;
    }

    .tag-item {
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }

    .tag-item:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
    }
</style>'''

    # Insert before closing head
    html = html.replace('</head>', polish_css + '</head>')

# Save fixed version
with open(html_file, 'w') as f:
    f.write(html)

print("\n✅ Fixed!")
print(f"\nChanges:")
print("  • Removed duplicate timestamps")
print("  • Added single timestamp")
print("  • Fixed CSS variables")
print("  • Enhanced CSS with !important to override")

# Create backup first
import shutil
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"skills-dashboard-before-fix-{timestamp}.html"
backup_path = Path("dashboard-backups") / backup_name
backup_path.parent.mkdir(exist_ok=True)
shutil.copy2(html_file, backup_path)
print(f"\n📁 Backup created: {backup_name}")

print(f"\n✅ Saved: {html_file}")
