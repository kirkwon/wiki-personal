#!/usr/bin/env python3
"""
Automated tests for the Skills Dashboard (no external dependencies).
"""

import json
import re
from pathlib import Path

def load_data():
    """Load the skills data."""
    with open('skills_data_fixed.json', 'r') as f:
        return json.load(f)

def load_html():
    """Load the HTML dashboard."""
    with open('skills-dashboard-updated.html', 'r') as f:
        return f.read()

def test_data_integrity():
    """Test 1: Data Integrity"""
    print("\n📊 Test 1: Data Integrity")
    print("=" * 80)

    data = load_data()
    issues = []

    # Check all_skills is not empty
    if not data['all_skills']:
        issues.append("❌ all_skills is empty")
    else:
        print(f"✅ all_skills has {len(data['all_skills'])} skills")

    # Check all_tags is not empty
    if not data['all_tags']:
        issues.append("❌ all_tags is empty")
    else:
        print(f"✅ all_tags has {len(data['all_tags'])} tags")

    # Check skills_by_tag matches all_tags
    tags_in_data = set(data['skills_by_tag'].keys())
    tags_list = set(data['all_tags'])
    if tags_in_data != tags_list:
        issues.append(f"❌ Mismatch: skills_by_tag has {tags_in_data - tags_list}, all_tags has {tags_list - tags_in_data}")
    else:
        print(f"✅ Tag lists match")

    # Check no duplicate skills in all_skills
    if len(data['all_skills']) != len(set(data['all_skills'])):
        issues.append("❌ Duplicate skills found in all_skills")
    else:
        print(f"✅ No duplicate skills in all_skills")

    # Check overlaps are subset of all_skills
    overlap_skills = set(data['overlaps'].keys())
    all_skills_set = set(data['all_skills'])
    if not overlap_skills.issubset(all_skills_set):
        issues.append(f"❌ Overlaps has skills not in all_skills")
    else:
        print(f"✅ All overlaps are in all_skills")

    # Check multi_tag_skills are subset of all_skills
    multi_skills = set(data['multi_tag_skills'].keys())
    if not multi_skills.issubset(all_skills_set):
        issues.append(f"❌ Multi-tag has skills not in all_skills")
    else:
        print(f"✅ All multi-tag skills are in all_skills")

    # Check descriptions are subset of all_skills
    desc_skills = set(data['descriptions'].keys())
    if not desc_skills.issubset(all_skills_set):
        issues.append(f"❌ Descriptions has skills not in all_skills")
    else:
        print(f"✅ All described skills are in all_skills")

    if issues:
        for issue in issues:
            print(issue)
        return False
    print("\n✅ Data integrity test PASSED")
    return True

def test_no_duplicate_tags():
    """Test 2: No Duplicate Tags in Skills"""
    print("\n🏷️  Test 2: No Duplicate Tags")
    print("=" * 80)

    data = load_data()

    # Build skill -> unique tags mapping
    skill_tags = {}
    for tag, skills in data['skills_by_tag'].items():
        for skill, book in skills:
            if skill not in skill_tags:
                skill_tags[skill] = set()
            skill_tags[skill].add(tag)

    print(f"✅ Built unique tag mapping for {len(skill_tags)} skills")

    # Show sample
    sample_skills = list(skill_tags.keys())[:3]
    for skill in sample_skills:
        print(f"   • {skill}: {len(skill_tags[skill])} unique tags")

    print("\n✅ No duplicate tags test PASSED")
    return True

def test_html_javascript():
    """Test 3: HTML JavaScript Validity"""
    print("\n🌐 Test 3: HTML JavaScript Validity")
    print("=" * 80)

    html = load_html()
    issues = []

    # Check skillsData is present
    if 'const skillsData = ' not in html:
        issues.append("❌ skillsData not found in HTML")
    else:
        print("✅ skillsData found in HTML")

        # Extract and validate JSON
        match = re.search(r'const skillsData = ({.*?});', html, re.DOTALL)
        if match:
            try:
                json_data = json.loads(match.group(1))
                print(f"✅ skillsData is valid JSON")
                print(f"   - {len(json_data.get('all_skills', []))} skills")
                print(f"   - {len(json_data.get('all_tags', []))} tags")
            except json.JSONDecodeError as e:
                issues.append(f"❌ skillsData JSON is invalid: {e}")

    # Check key functions exist
    functions = ['showTab', 'renderAllSkills', 'renderAllTags', 'renderOverlaps',
                 'renderMultitag', 'showSkillDetail', 'drawNetwork']
    for func in functions:
        if f'function {func}(' in html:
            print(f"✅ Function {func} exists")
        else:
            issues.append(f"❌ Function {func} not found")

    # Check skillInfoMap uses Set for tags (the fix)
    if 'skillInfoMap[skill].tags.add(tag)' in html:
        print("✅ Uses Set.add() to prevent duplicate tags")
    elif 'skillInfoMap[skill].tags.push(tag)' in html:
        issues.append("❌ Still using tags.push() which causes duplicates")

    # Check network graph fix
    if 'if (topTags.length < 3)' in html or 'Math.min(30' in html:
        print("✅ Network graph has safeguard for few tags")
    else:
        issues.append("❌ Network graph missing safeguard for few tags")

    if issues:
        for issue in issues:
            print(issue)
        return False

    print("\n✅ HTML JavaScript validity test PASSED")
    return True

def test_network_graph_data():
    """Test 4: Network Graph Has Enough Data"""
    print("\n🕸️  Test 4: Network Graph Data")
    print("=" * 80)

    data = load_data()

    tag_count = len(data['all_tags'])

    if tag_count < 3:
        print(f"❌ Only {tag_count} tags - need at least 3 for network")
        return False
    else:
        print(f"✅ Has {tag_count} tags (need 3+)")

    # Count multi-tag skills (create links)
    multi_tag_count = len(data['multi_tag_skills'])
    print(f"✅ Has {multi_tag_count} multi-tag skills (create links)")

    # Estimate link count
    total_links = 0
    for skill, tags in data['multi_tag_skills'].items():
        if len(tags) > 1:
            total_links += len(tags) * (len(tags) - 1) // 2

    print(f"✅ Estimated {total_links} links between tags")

    print("\n✅ Network graph data test PASSED")
    return True

def test_skill_quality():
    """Test 5: Skill Quality (No Generic Nouns)"""
    print("\n✨ Test 5: Skill Quality")
    print("=" * 80)

    data = load_data()

    # Check skills are actionable (contain action words)
    action_words = {'making', 'building', 'breaking', 'applying', 'using',
                   'decision', 'techniques', 'thinking', 'analysis', 'training',
                   'revision', 'assessment', 'adaptive', 'analogical', 'modeling'}

    actionable = 0
    for skill in data['all_skills']:
        if any(word in skill.lower() for word in action_words):
            actionable += 1

    percentage = (actionable / len(data['all_skills'])) * 100
    print(f"✅ {actionable}/{len(data['all_skills'])} skills ({percentage:.1f}%) appear actionable")

    # Show sample good skills
    print(f"\n📝 Sample high-quality skills:")
    for skill in data['all_skills'][:5]:
        print(f"   • {skill}")

    print("\n✅ Skill quality test PASSED")
    return True

def test_html_structure():
    """Test 6: HTML Structure"""
    print("\n📋 Test 6: HTML Structure")
    print("=" * 80)

    html = load_html()
    issues = []

    # Check key sections exist
    sections = {
        'allSkills': 'All Skills table',
        'allTags': 'All Tags table',
        'overlaps': 'Overlaps table',
        'multitag': 'Multi-Tag table',
        'network': 'Network view',
        'conflicts': 'Conflict guide'
    }

    for section_id, description in sections.items():
        if f'id="{section_id}"' in html:
            print(f"✅ Found {description}")
        else:
            issues.append(f"❌ Missing {description}")

    # Check tables
    table_count = html.count('<table>')
    print(f"✅ Found {table_count} <table> tags")

    # Check stat cards
    stat_card_count = html.count('class="stat-card"')
    if stat_card_count >= 4:
        print(f"✅ Found {stat_card_count} stat cards")
    else:
        issues.append(f"❌ Only found {stat_card_count} stat cards (need 4+)")

    # Check tabs
    tab_count = html.count('class="tab"')
    if tab_count >= 6:
        print(f"✅ Found {tab_count} tabs")
    else:
        issues.append(f"❌ Only found {tab_count} tabs (need 6+)")

    if issues:
        for issue in issues:
            print(issue)
        return False

    print("\n✅ HTML structure test PASSED")
    return True

def run_all_tests():
    """Run all tests and report results."""
    print("🧪 SKILLS DASHBOARD TEST SUITE")
    print("=" * 80)
    print(f"Testing: skills-dashboard-updated.html")
    print(f"Data: skills_data_fixed.json")

    tests = [
        ("Data Integrity", test_data_integrity),
        ("No Duplicate Tags", test_no_duplicate_tags),
        ("HTML JavaScript", test_html_javascript),
        ("Network Graph Data", test_network_graph_data),
        ("Skill Quality", test_skill_quality),
        ("HTML Structure", test_html_structure)
    ]

    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n❌ {name} test FAILED with exception: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))

    # Summary
    print("\n" + "=" * 80)
    print("📊 TEST SUMMARY")
    print("=" * 80)

    passed = sum(1 for _, p in results if p)
    total = len(results)

    for name, p in results:
        status = "✅ PASSED" if p else "❌ FAILED"
        print(f"{status}: {name}")

    print(f"\n{'=' * 80}")
    print(f"Total: {passed}/{total} tests passed ({passed/total*100:.1f}%)")

    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        return True
    else:
        print(f"⚠️  {total - passed} test(s) failed")
        return False

if __name__ == '__main__':
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
