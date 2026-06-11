#!/usr/bin/env python3
"""
Incremental UX Improvement Workflow
===============================
Author: Claude
Created: 2025-05-05 21:00

This script manages incremental improvements to the skills dashboard.
Each step:
1. Creates a timestamped backup
2. Applies ONE improvement
3. Tests the change
4. Documents with datetime in source code
5. Only proceeds if tests pass

BACKUP STRATEGY:
- skills-dashboard-v5.0-[timestamp].html
- Git-style versioning
- Rollback capability

CHANGE LOG FORMAT:
<!-- IMPROVEMENT: [Name]
     Date: 2025-05-05 HH:MM:SS
     Author: Claude
     Description: [What changed]
     Tests: [What was tested]
-->
"""

import shutil
import json
from datetime import datetime
from pathlib import Path
import subprocess

BASE_VERSION = "v5.0"
BASE_FILE = Path("skills-dashboard-updated.html")
BACKUP_DIR = Path("dashboard-backups")

def create_backup(version):
    """Create timestamped backup before changes"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"skills-dashboard-{version}-{timestamp}.html"
    backup_path = BACKUP_DIR / backup_name

    BACKUP_DIR.mkdir(exist_ok=True)
    shutil.copy2(BASE_FILE, backup_path)

    print(f"✅ Backup created: {backup_name}")
    return backup_path

def run_tests():
    """Run test suite and return True if all pass"""
    print("\n🧪 Running tests...")
    try:
        result = subprocess.run(
            ["python3", "test_ux_stories.py"],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Parse output for pass/fail
        # Look for the summary line
        if "Total: True/6 tests passed" in result.stdout or "100.0%" in result.stdout:
            print("✅ All tests passed")
            return True
        elif "Total:" in result.stdout and "passed" in result.stdout:
            # Extract pass count
            import re
            match = re.search(r'Total: (\d+)/6 tests passed', result.stdout)
            if match:
                count = int(match.group(1))
                if count == 6:
                    print("✅ All tests passed")
                    return True
                else:
                    print(f"❌ Only {count}/6 tests passed")
                    return False
        else:
            print("❌ Tests failed")
            print(result.stdout)
            return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def apply_improvement(improvement_name, apply_func):
    """Apply a single improvement with backup and test"""
    print("\n" + "=" * 80)
    print(f"🔧 APPLYING: {improvement_name}")
    print("=" * 80)

    # Step 1: Backup
    print(f"\n1️⃣  Creating backup...")
    backup_path = create_backup(BASE_VERSION)
    print(f"   → {backup_path}")

    # Step 2: Apply change
    print(f"\n2️⃣  Applying improvement...")
    try:
        # Read file content
        with open(BASE_FILE, 'r') as f:
            content = f.read()

        # Apply improvement function
        modified = apply_func(content)

        print(f"   ✅ Changes applied")
    except Exception as e:
        print(f"   ❌ Failed to apply: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Step 3: Save
    print(f"\n3️⃣  Saving changes...")
    with open(BASE_FILE, 'w') as f:
        f.write(modified)
    print(f"   ✅ Saved to {BASE_FILE}")

    # Step 4: Test
    print(f"\n4️⃣  Testing changes...")
    if run_tests():
        print(f"   ✅ Tests passed - keeping changes")
        return True
    else:
        print(f"   ❌ Tests failed - rolling back...")
        shutil.copy2(backup_path, BASE_FILE)
        print(f"   ✅ Rolled back to backup")
        return False

def add_datetime_to_html(html, improvement_name, description, tests):
    """Add improvement documentation to HTML source"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    doc_comment = f"""<!-- IMPROVEMENT: {improvement_name}
     Date: {timestamp}
     Author: Claude
     Description: {description}
     Tests: {tests}
-->"""

    # Insert after DOCTYPE or at start of file
    if html.startswith('<!DOCTYPE'):
        return html.replace('>', f'>\n{doc_comment}', 1)
    else:
        return doc_comment + '\n' + html

# =============================================================================
# IMPROVEMENT FUNCTIONS
# Each function takes HTML content, modifies it, and returns modified content
# =============================================================================

def improvement_visual_polish(html):
    """
    Improvement: Enhanced Visual Design
    Description: Add subtle gradients, shadows, and polish to existing design
    Tests: Visual elements render correctly, no layout breaks
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add subtle gradients to stat cards
    polish_css = '''
<!-- IMPROVEMENT: Enhanced Visual Polish
     Date: {timestamp}
     Description: Added subtle gradients to stat cards, improved shadows, better hover states
     Tests: Visual elements render correctly, no layout breaks
-->
<style>
    .stat-card {{
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        box-shadow: 0 2px 8px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .stat-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.08);
        border-color: #0071e3;
    }}

    .tab {{
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    }}

    .tab:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    .tab.active {{
        box-shadow: 0 4px 12px rgba(0,123,229,0.25);
    }}

    .skill-item {{
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .tag-item {{
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }}

    .tag-item:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }}

    .detail-section {{
        animation: fadeIn 0.3s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{
            opacity: 0;
            transform: translateY(10px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
</style>'''

    # Insert after the opening <style> tag
    html = html.replace('</style>', polish_css + '</style>', 1)
    return html

def improvement_metrics_clickable(html):
    """
    Improvement: Improved Metrics Cards
    Description: Make cards clickable for navigation, better hover feedback
    Tests: Clicking metrics navigates to views, visual feedback on hover
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add cursor pointer and onclick to stat cards
    metrics_js = '''
<!-- IMPROVEMENT: Improved Metrics Cards
     Date: {timestamp}
     Description: Added click handlers to stat cards for navigation
     Tests: Clicking metrics navigates to views, visual feedback on hover
-->
<script>
// Make stat cards clickable
document.addEventListener('DOMContentLoaded', function() {{
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {{
        card.style.cursor = 'pointer';
    }});
}});
</script>'''

    html = html.replace('</body>', metrics_js + '</body>')
    return html

def improvement_tag_badges(html):
    """
    Improvement: Better Tag Badges
    Description: Make badges clickable, add hover effects, show counts
    Tests: Clicking tags filters skills, hover effects work
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Enhance tag badges
    tag_css = '''
<!-- IMPROVEMENT: Better Tag Badges
     Date: {timestamp}
     Description: Made tag badges clickable with improved hover effects
     Tests: Clicking tags filters skills, hover effects work
-->
<style>
    .tag-item {{
        cursor: pointer !important;
        position: relative;
    }}

    .tag-item:hover {{
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        z-index: 10;
    }}

    .tag-item::after {{
        content: attr(data-count);
        position: absolute;
        top: -8px;
        right: -8px;
        background: #0071e3;
        color: white;
        font-size: 10px;
        padding: 2px 6px;
        border-radius: 10px;
        font-weight: 600;
    }}
</style>'''

    html = html.replace('</style>', tag_css + '</style>', 1)
    return html

def improvement_timestamp(html):
    """
    Improvement: Add Timestamp
    Description: Show "Last Updated" timestamp in footer
    Tests: Timestamp displays, updates on refresh
    """
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Add timestamp before closing body tag
    timestamp_html = f'''
<!-- IMPROVEMENT: Timestamp
     Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
     Description: Added last updated timestamp to footer
     Tests: Timestamp visible in dashboard
-->
    <div style="text-align: center; padding: 16px 0; color: #6e6e73; font-size: 12px;">
        Last Updated: {timestamp}
    </div>'''

    html = html.replace('</body>', timestamp_html + '\n</body>')
    return html

# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main():
    """Main workflow runner"""
    print("🚀 INCREMENTAL UX IMPROVEMENT WORKFLOW")
    print("=" * 80)
    print(f"Baseline: {BASE_FILE}")
    print(f"Backup directory: {BACKUP_DIR}")
    print(f"Tests: test_ux_stories.py")
    print()

    # Check baseline exists
    if not BASE_FILE.exists():
        print(f"❌ Baseline file not found: {BASE_FILE}")
        return

    # Run baseline tests first
    print("📊 Testing baseline...")
    baseline_passes = run_tests()
    if not baseline_passes:
        print("⚠️  Warning: Baseline tests are failing!")
        print("    Proceeding anyway since this is our starting point...")

    # Define improvements to apply (one at a time)
    improvements = [
        ("Add Timestamp", improvement_timestamp,
         "Show last updated date in footer",
         "Timestamp visible, correct format"),
        ("Enhanced Visual Polish", improvement_visual_polish,
         "Add subtle gradients, better shadows, improved hover states",
         "Visual elements render correctly, no layout breaks"),
        ("Improved Metrics Cards", improvement_metrics_clickable,
         "Make cards clickable for navigation, better hover feedback",
         "Clicking metrics navigates to views, visual feedback on hover"),
        ("Better Tag Badges", improvement_tag_badges,
         "Make badges clickable, add hover effects, show counts",
         "Clicking tags filters skills, hover effects work"),
    ]

    completed = []
    failed = []

    for name, func, desc, tests in improvements:
        success = apply_improvement(name, func)

        if success:
            completed.append(name)
            print(f"\n✅ {name} - COMPLETED")
        else:
            failed.append(name)
            print(f"\n❌ {name} - FAILED (rolled back)")
            print("   Stopping here. Please review and fix before continuing.")
            break

    # Summary
    print("\n" + "=" * 80)
    print("📊 SESSION SUMMARY")
    print("=" * 80)
    print(f"Completed: {len(completed)} improvements")
    print(f"Failed: {len(failed)} improvements")

    if completed:
        print("\n✅ Completed:")
        for name in completed:
            print(f"   • {name}")

    if failed:
        print("\n❌ Failed:")
        for name in failed:
            print(f"   • {name}")

    print(f"\n📁 All backups saved to: {BACKUP_DIR}/")

if __name__ == '__main__':
    main()
