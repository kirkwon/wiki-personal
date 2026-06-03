#!/usr/bin/env python3
"""
Fix specific issues in UX dashboard
1. Remove duplicate timestamps, keep only one
2. Fix metrics cards to be clickable and navigate to views
"""

from datetime import datetime
import re
from pathlib import Path

# Load the UX dashboard
html_file = Path("skills-dashboard-ux.html")
with open(html_file, 'r') as f:
    html = f.read()

print("🔧 Fixing UX Dashboard Issues")
print("=" * 80)

# Fix 1: Remove duplicate timestamps
print("\n1️⃣  Fixing duplicate timestamps...")
html = re.sub(
    r'<div style="text-align: center; padding: 16px 0; color: #64748b; font-size: 12px;">\s*Last Updated: [^<]+</div>\s*<div style="text-align: center; padding: 16px 0; color: #64748b; font-size: 12px;">\s*Last Updated: [^<]+</div>',
    '<div style="text-align: center; padding: 16px 0; color: #64748b; font-size: 12px;">Last Updated: May 5, 2025 at 9:00 PM</div>',
    html
)
print("   ✅ Single timestamp")

# Fix 2: Make stat cards clickable with proper onclick
print("\n2️⃣  Making metrics cards clickable...")

# Replace the stat cards with clickable versions
html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Total Skills</div>\s*<div class="stat-value" id="statTotalSkills">443</div>',
    '''<div class="stat-card" onclick="showView('skills')" style="cursor: pointer;">
        <div class="stat-label">Total Skills</div>
        <div class="stat-value" id="statTotalSkills">443</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Categories</div>\s*<div class="stat-value" id="statCategories">15</div>',
    '''<div class="stat-card" onclick="showView('tags')" style="cursor: pointer;">
        <div class="stat-label">Categories</div>
        <div class="stat-value" id="statCategories">15</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Multi-Disciplinary</div>\s*<div class="stat-value" id="statMultiTag">352</div>',
    '''<div class="stat-card" onclick="showView('multitag')" style="cursor: pointer;">
        <div class="stat-label">Multi-Disciplinary</div>
        <div class="stat-value" id="statMultiTag">352</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Cross-Book</div>\s*<div class="stat-value" id="statOverlaps">5</div>',
    '''<div class="stat-card" onclick="showView('overlaps')" style="cursor: pointer;">
        <div class="stat-label">Cross-Book</div>
        <div class="stat-value" id="statOverlaps">5</div>''',
    html
)

print("   ✅ Metrics now clickable")

# Save fixed version
with open(html_file, 'w') as f:
    f.write(html)

print("\n✅ Fixed and saved!")
print(f"\nChanges made:")
print("  • Single timestamp (not multiples)")
print("  • Metrics cards are clickable")
print("  • Clicking navigates to appropriate views")
print(f"\n📄 Saved: {html_file}")
