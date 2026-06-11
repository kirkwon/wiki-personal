#!/usr/bin/env python3
"""
Compare old and new skills datasets to understand discrepancies
"""

import json
from pathlib import Path
from collections import Counter

print("🔍 COMPARING DATASETS")
print("=" * 80)

# Load old data
old_data_file = Path("skills_data_fixed.json")
if old_data_file.exists():
    with open(old_data_file, 'r') as f:
        old_data = json.load(f)
    print(f"✅ Loaded old data: {old_data_file}")
    print(f"   Skills: {len(old_data.get('all_skills', []))}")
    print(f"   Tags: {len(old_data.get('all_tags', []))}")
else:
    print("❌ Old data file not found")
    old_data = None

# Load new data
new_data_file = Path("skills_data_master.json")
if new_data_file.exists():
    with open(new_data_file, 'r') as f:
        new_data = json.load(f)
    print(f"\n✅ Loaded new data: {new_data_file}")
    print(f"   Skills: {len(new_data.get('all_skills', []))}")
    print(f"   Tags: {len(new_data.get('all_tags', []))}")
else:
    print("❌ New data file not found")
    new_data = None

if not old_data or not new_data:
    print("\n❌ Cannot compare - missing data files")
    exit(1)

# Compare skills
print("\n" + "=" * 80)
print("SKILLS COMPARISON")
print("=" * 80)

old_skills = set(old_data.get('all_skills', []))
new_skills = set(new_data.get('all_skills', []))

print(f"\nOld skills: {len(old_skills)}")
print(f"New skills: {len(new_skills)}")
print(f"Difference: {len(old_skills) - len(new_skills)} fewer in new dataset")

# Skills in old but not in new
missing_skills = old_skills - new_skills
print(f"\n❌ Skills in OLD but NOT in NEW ({len(missing_skills)}):")
print("-" * 80)

# Categorize missing skills
generic_terms = {
    'technique', 'practice', 'design', 'management', 'learning', 'communication',
    'planning', 'improvement', 'analysis', 'description', 'concepts', 'concept',
    'changes', 'change', 'strategies', 'strategy', 'formation', 'points',
    'success', 'failure', 'game', 'principles', 'principle', 'framework',
    'system', 'systems', 'model', 'models', 'method', 'methods', 'approach',
    'tool', 'tools', 'process', 'processes', 'step', 'steps', 'action',
    'actions', 'result', 'results', 'outcome', 'outcomes', 'goal', 'goals',
    'habit', 'habits', 'skill', 'skills', 'behavior', 'behaviors', 'pattern',
    'patterns', 'frameworks', 'development', 'growth', 'performance', 'focus',
    'decision', 'decisions', 'thinking', 'thought', 'ideas', 'idea', 'value',
    'values', 'belief', 'beliefs', 'knowledge', 'information', 'data', 'time',
    'work', 'energy', 'power', 'control', 'balance', 'order', 'structure',
    'structures', 'organization', 'organize', 'manage', 'plan',
}

filtered_by_generic = [s for s in missing_skills if s.lower() in generic_terms]
other_missing = [s for s in missing_skills if s.lower() not in generic_terms]

print(f"\n1. Filtered as GENERIC TERMS ({len(filtered_by_generic)}):")
for skill in sorted(filtered_by_generic)[:20]:
    print(f"   - {skill}")
if len(filtered_by_generic) > 20:
    print(f"   ... and {len(filtered_by_generic) - 20} more")

print(f"\n2. Other missing skills ({len(other_missing)}):")
for skill in sorted(other_missing)[:50]:
    print(f"   - {skill}")
if len(other_missing) > 50:
    print(f"   ... and {len(other_missing) - 50} more")

# Skills in new but not in old
new_only = new_skills - old_skills
if new_only:
    print(f"\n✨ Skills in NEW but NOT in OLD ({len(new_only)}):")
    for skill in sorted(new_only)[:20]:
        print(f"   + {skill}")

# Compare tags
print("\n" + "=" * 80)
print("TAGS COMPARISON")
print("=" * 80)

old_tags = set(old_data.get('all_tags', []))
new_tags = set(new_data.get('all_tags', []))

print(f"\nOld tags: {len(old_tags)}")
print(f"New tags: {len(new_tags)}")

missing_tags = old_tags - new_tags
if missing_tags:
    print(f"\n❌ Tags in OLD but NOT in NEW ({len(missing_tags)}):")
    for tag in sorted(missing_tags):
        print(f"   - {tag}")

new_only_tags = new_tags - old_tags
if new_only_tags:
    print(f"\n✨ Tags in NEW but NOT in OLD ({len(new_only_tags)}):")
    for tag in sorted(new_only_tags):
        print(f"   + {tag}")

# Analyze skill length distribution
print("\n" + "=" * 80)
print("SKILL LENGTH ANALYSIS")
print("=" * 80)

old_lengths = [len(s) for s in old_skills]
new_lengths = [len(s) for s in new_skills]

print(f"\nOld skills - Avg length: {sum(old_lengths)/len(old_lengths):.1f} chars")
print(f"New skills - Avg length: {sum(new_lengths)/len(new_lengths):.1f} chars")

print(f"\nOld skills - Min/Max: {min(old_lengths)}/{max(old_lengths)}")
print(f"New skills - Min/Max: {min(new_lengths)}/{max(new_lengths)}")

# Short skills that might have been filtered
short_old = [s for s in old_skills if len(s) < 5]
short_new = [s for s in new_skills if len(s) < 5]

print(f"\nOld skills with <5 chars: {len(short_old)}")
print(f"New skills with <5 chars: {len(short_new)}")

if short_old:
    print(f"\nShort skills in OLD (might be filtered):")
    for skill in sorted(short_old)[:30]:
        print(f"   - '{skill}' (len={len(skill)})")

# Sample descriptions
print("\n" + "=" * 80)
print("SAMPLE DESCRIPTIONS")
print("=" * 80)

old_desc = old_data.get('descriptions', {})
new_desc = new_data.get('descriptions', {})

print(f"\nOld descriptions: {len(old_desc)}")
print(f"New descriptions: {len(new_desc)}")

# Show a few examples
sample_skills = list(new_skills)[:5]
print(f"\nSample skill descriptions from NEW dataset:")
for skill in sample_skills:
    desc = new_desc.get(skill, "No description")
    if len(desc) > 100:
        desc = desc[:100] + "..."
    print(f"\n🔹 {skill}")
    print(f"   {desc}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

print(f"\n📊 SUMMARY:")
print(f"   Old dataset: {len(old_skills)} skills, {len(old_tags)} tags")
print(f"   New dataset: {len(new_skills)} skills, {len(new_tags)} tags")
print(f"   Missing skills: {len(missing_skills)}")
print(f"   - Filtered as generic: {len(filtered_by_generic)}")
print(f"   - Other missing: {len(other_missing)}")
print(f"   New skills added: {len(new_only)}")
