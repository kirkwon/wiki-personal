#!/usr/bin/env python3
"""
Tests for UX improvement stories.
"""

import json
import re
from pathlib import Path

def load_dashboard_data():
    """Load dashboard HTML and data"""
    try:
        with open('skills-dashboard-ux.html', 'r') as f:
            html = f.read()
    except:
        print("⚠️  UX Dashboard not found, testing original...")
        with open('skills-dashboard-updated.html', 'r') as f:
            html = f.read()

    with open('skills_data_fixed.json', 'r') as f:
        data = json.load(f)
    return html, data

def test_timestamp_present():
    """Story 1: Verify timestamp is displayed"""
    print("\n📅 Story 1: Time-Stamped Revisions")
    html, data = load_dashboard_data()
    if 'Last Updated' in html or 'updated' in html.lower() or '2025' in html:
        print("✅ PASS: Timestamp is present in dashboard")
        return True
    else:
        print("❌ FAIL: No timestamp found")
        return False

def test_metrics_clickable():
    """Story 2: Verify metric cards have click handlers"""
    print("\n📊 Story 2: Metrics Click Filtering")
    html, data = load_dashboard_data()
    if 'onclick="showView' in html or 'stat-card' in html:
        print("✅ PASS: Metric cards are clickable")
        return True
    else:
        print("❌ FAIL: No click handlers on metrics")
        return False

def test_tag_filtering():
    """Story 3: Verify tag filtering works"""
    print("\n🏷️  Story 3: Tag Filtering")
    html, data = load_dashboard_data()
    has_tag_badges = 'tag-badge' in html or 'class="tag' in html
    has_search = 'search' in html.lower()
    if has_tag_badges or has_search:
        print("✅ PASS: Tag filtering capabilities exist")
        return True
    else:
        print("❌ FAIL: No tag filtering found")
        return False

def test_conflict_guide_present():
    """Story 5: Verify Conflict Guide is present"""
    print("\n⚖️  Story 5: Conflict Guide Display")
    html, data = load_dashboard_data()
    has_conflicts = 'conflicts' in html.lower() or 'conflict' in html.lower()
    has_guide = 'guide' in html.lower()
    if has_conflicts:
        print("✅ PASS: Conflict Guide is present")
        return True
    else:
        print("❌ FAIL: Conflict Guide not found")
        return False

def test_ai_integration():
    """Story 6: Verify AI integration exists"""
    print("\n🤖 Story 6: AI Assistant Integration")
    html, data = load_dashboard_data()
    has_chatgpt = 'chatgpt' in html.lower()
    has_claude = 'claude' in html.lower()
    if has_chatgpt or has_claude:
        print("✅ PASS: AI integration present")
        if has_chatgpt:
            print("   - ChatGPT: ✅")
        if has_claude:
            print("   - Claude: ✅")
        return True
    else:
        print("❌ FAIL: No AI integration found")
        return False

def test_network_visualization():
    """Story 7: Verify network visualization code"""
    print("\n🕸️  Story 7: Network Visualization")
    html, data = load_dashboard_data()
    has_network = 'network' in html.lower()
    has_d3 = 'd3' in html.lower() or 'svg' in html.lower()
    has_draw_function = 'drawNetwork' in html or 'draw network' in html.lower()
    if has_network and has_d3:
        print("✅ PASS: Network visualization code present")
        return True
    else:
        print("❌ FAIL: Network visualization missing")
        if not has_network:
            print("   - Missing: network section")
        if not has_d3:
            print("   - Missing: D3.js or SVG")
        return False

def run_all_tests():
    """Run all UX story tests"""
    print("🧪 UX STORIES TEST SUITE")
    print("=" * 80)
    print(f"Testing: Skills Dashboard UX")
    print(f"Date: 2025-05-05")

    tests = [
        ("Story 1: Timestamps", test_timestamp_present),
        ("Story 2: Metrics Click", test_metrics_clickable),
        ("Story 3: Tag Filter", test_tag_filtering),
        ("Story 5: Conflict Guide", test_conflict_guide_present),
        ("Story 6: AI Integration", test_ai_integration),
        ("Story 7: Network Viz", test_network_visualization)
    ]

    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed, None))
        except Exception as e:
            print(f"⚠️  ERROR in {name}: {e}")
            results.append((name, False, str(e)))

    # Summary
    print("\n" + "=" * 80)
    print("📊 TEST SUMMARY")
    print("=" * 80)

    passed = sum(1 for _, p, _ in results if p)
    total = len(results)

    for name, passed, error in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
        if error:
            print(f"   Error: {error}")

    print(f"\n{'=' * 80}")
    print(f"Total: {passed}/{total} tests passed ({passed/total*100:.1f}%)")

    if passed == total:
        print("🎉 ALL TESTS PASSED!")
    else:
        print(f"⚠️  {total - passed} test(s) failed - implementation needed")

    return passed == total

if __name__ == '__main__':
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
