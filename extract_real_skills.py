#!/usr/bin/env python3
"""
Extract REAL skills from book data.
A skill must be an actionable ability that transforms one state into another.
Format: [Action Verb] + [Object/Outcome] = "Transform X into Y"
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Load book data
books_dir = Path("/Users/kirkwon/Downloads/book_summaries/unified_books_improved")
book_data = {}

print("📚 Loading book data...")
for json_file in books_dir.glob("*.json"):
    try:
        with open(json_file, 'r') as f:
            book = json.load(f)
            title = book.get('metadata', {}).get('title', '')
            if title:
                book_data[title] = book
    except:
        continue

print(f"   Loaded {len(book_data)} books")

# Skill patterns: Action verbs that indicate transformation
SKILL_VERBS = {
    # Core transformation verbs
    'transform', 'convert', 'change', 'turn', 'make', 'create', 'build', 'develop',
    'improve', 'enhance', 'optimize', 'maximize', 'increase', 'boost', 'strengthen',
    'reduce', 'minimize', 'decrease', 'eliminate', 'remove', 'avoid', 'prevent',

    # Cognitive/mental actions
    'decide', 'choose', 'select', 'determine', 'assess', 'evaluate', 'analyze', 'examine',
    'think', 'reason', 'solve', 'overcome', 'master', 'learn', 'understand', 'recognize',
    'identify', 'discover', 'find', 'detect', 'notice', 'observe', 'monitor', 'track',

    # Behavioral actions
    'practice', 'apply', 'use', 'implement', 'execute', 'perform', 'do', 'take',
    'establish', 'build', 'create', 'design', 'construct', 'form', 'start', 'begin',
    'maintain', 'sustain', 'keep', 'preserve', 'protect', 'secure', 'ensure',

    # Social/interpersonal
    'communicate', 'persuade', 'influence', 'lead', 'manage', 'organize', 'coordinate',
    'collaborate', 'negotiate', 'resolve', 'mediate', 'facilitate', 'guide', 'mentor',

    # Strategic/decision
    'plan', 'schedule', 'prioritize', 'allocate', 'organize', 'systematize', 'structure',
    'invest', 'save', 'spend', 'allocate', 'budget', 'leverage', 'capitalize'
}

# Non-skill patterns to exclude
NON_SKILL_PATTERNS = {
    # Pure nouns (no action)
    r'^(mindset|attitude|belief|concept|idea|theory|principle|framework|model|system|method)$',
    r'^(habit|routine|practice|pattern|behavior|tendency)$',
    r'^(success|failure|result|outcome|achievement|goal|objective|target)$',
    r'^(knowledge|information|data|wisdom|insight|understanding|awareness)$',
    r'^(time|money|energy|focus|attention|effort|resource)$',
    r'^(life|work|business|career|relationship|family|team)$',
    r'^(problem|challenge|obstacle|barrier|difficulty|issue)$',

    # Author names
    r'^[A-Z][a-z]+ [A-Z][a-z]+$',
    r'^[A-Z]\. [A-Z][a-z]+$',

    # Generic terms
    r'^(everything|nothing|something|anything)$',
    r'^(process|approach|strategy|tactic|technique)$',

    # Book titles
    r'.* - .*$',
    r'^The .*$',
    r'^How to .*$'
}

def is_skill(text):
    """Check if text is a real skill (actionable transformation)."""
    text_lower = text.lower().strip()

    # Check exclusions
    for pattern in NON_SKILL_PATTERNS:
        if re.match(pattern, text, re.IGNORECASE):
            return False

    # Must contain an action verb
    words = text_lower.split()
    first_word = words[0] if words else ''

    # Check if starts with skill verb
    if first_word in SKILL_VERBS:
        return True

    # Check if contains "to " + verb (gerund form)
    if ' to ' in text_lower:
        after_to = text_lower.split(' to ', 1)[1]
        if any(verb in after_to for verb in SKILL_VERBS):
            return True

    # Check gerund forms (ending in -ing)
    if text_lower.endswith('ing'):
        # Remove -ing and check if it's a skill verb
        base_verb = text_lower[:-3]
        if base_verb in SKILL_VERBS:
            return True

    return False

def extract_skills_from_text(text, book_title):
    """Extract skill phrases from text."""
    skills = []

    # Split into sentences/phrases
    sentences = re.split(r'[.!?;\n]', text)

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 10 or len(sentence) > 100:
            continue

        # Look for skill patterns
        # Pattern 1: "How to [verb]..."
        match = re.match(r'How to ([^.]+)', sentence, re.IGNORECASE)
        if match:
            skill = match.group(1).strip()
            if is_skill(skill):
                skills.append(skill)
                continue

        # Pattern 2: "[Verb] the..."
        match = re.match(r'([A-Z][a-z]+) (?:the|your|a|an) ([^.]+)', sentence)
        if match:
            verb = match.group(1).lower()
            if verb in SKILL_VERBS:
                skill = f"{verb} {match.group(2)}".strip()
                if is_skill(skill):
                    skills.append(skill)
                    continue

        # Pattern 3: Imperative at start
        words = sentence.split()
        if len(words) >= 3:
            first_three = ' '.join(words[:3]).lower()
            first_word = words[0].lower()
            if first_word in SKILL_VERBS:
                skill = ' '.join(words[:5]).strip()  # Take first 5 words
                skill = skill[0].upper() + skill[1:]  # Capitalize
                if is_skill(skill):
                    skills.append(skill)
                    continue

    return list(set(skills))  # Remove duplicates

def extract_skills_from_book(book):
    """Extract skills from a single book."""
    skills = []

    # Get metadata
    metadata = book.get('metadata', {})
    book_title = metadata.get('title', '')
    tags = metadata.get('tags', [])

    # Method 1: Check agent_structure.core_skills for purpose/trigger
    core_skills = book.get('agent_structure', {}).get('core_skills', [])
    for skill_data in core_skills:
        purpose = skill_data.get('purpose', '')
        trigger = skill_data.get('trigger', '')

        # Extract from purpose
        for sent in purpose.split('.'):
            extracted = extract_skills_from_text(sent, book_title)
            skills.extend(extracted)

        # Extract from trigger
        for sent in trigger.split('.'):
            extracted = extract_skills_from_text(sent, book_title)
            skills.extend(extracted)

    # Method 2: Check quick_reference
    quick_ref = book.get('quick_reference', {})
    for field in ['why_it_matters', 'the_big_picture', 'the_bottom_line']:
        text = quick_ref.get(field, '')
        extracted = extract_skills_from_text(text, book_title)
        skills.extend(extracted)

    # Method 3: Check chapter summaries and key takeaways
    if 'summary' in book:
        for chapter in book['summary'].get('chapters', []):
            # Summary
            summary = chapter.get('summary', '')
            extracted = extract_skills_from_text(summary, book_title)
            skills.extend(extracted)

            # Key takeaways
            for takeaway in chapter.get('key_takeaways', []):
                extracted = extract_skills_from_text(takeaway, book_title)
                skills.extend(extracted)

    # Remove duplicates while preserving order
    seen = set()
    unique_skills = []
    for skill in skills:
        skill_clean = skill.lower().strip()
        if skill_clean and skill_clean not in seen:
            seen.add(skill_clean)
            unique_skills.append(skill.strip())

    return unique_skills

# Extract all skills
print("\n🔍 Extracting real skills...")
all_skills = defaultdict(list)  # skill -> [(book, tags), ...]
skills_by_tag = defaultdict(list)  # tag -> [(skill, book), ...]

for book_title, book in book_data.items():
    print(f"   Processing: {book_title[:50]}...")

    # Get tags
    tags = book.get('metadata', {}).get('tags', [])

    # Extract skills
    skills = extract_skills_from_book(book)

    print(f"      Found {len(skills)} skills")

    # Store skills
    for skill in skills:
        all_skills[skill].append((book_title, tags))
        for tag in tags:
            skills_by_tag[tag].append((skill, book_title))

print(f"\n✅ Extracted {len(all_skills)} unique skills")

# Filter to only get high-quality skills
# Keep skills that appear in at least 1 book
filtered_skills = {skill: sources for skill, sources in all_skills.items() if len(sources) >= 1}

print(f"📊 Final count: {len(filtered_skills)} skills")

# Save results
output_data = {
    "skills_by_tag": {k: [[s[0], s[1]] for s in v] for k, v in skills_by_tag.items()},
    "all_skills": sorted(filtered_skills.keys()),
    "all_tags": sorted(skills_by_tag.keys()),
    "overlaps": {k: list(set(s[0] for s in v)) for k, v in filtered_skills.items() if len(set(s[0] for s in v)) > 1},
    "multi_tag_skills": {},
    "descriptions": {},
    "stats": {
        "total_skills": len(filtered_skills),
        "total_tags": len(skills_by_tag),
        "total_books": len(book_data),
        "overlapping": len([k for k, v in filtered_skills.items() if len(set(s[0] for s in v)) > 1])
    }
}

# Generate multi-tag skills
for skill, sources in filtered_skills.items():
    all_tags = set()
    for _, tags in sources:
        all_tags.update(tags)
    if len(all_tags) > 1:
        output_data["multi_tag_skills"][skill] = list(all_tags)

output_file = Path("/Users/kirkwon/wiki-personal/skills_data_real.json")
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"💾 Saved to: {output_file}")

# Show sample
print(f"\n📝 Sample extracted skills:")
print("=" * 80)
for i, skill in enumerate(list(filtered_skills.keys())[:10]):
    sources = filtered_skills[skill]
    print(f"{i+1}. {skill} (from {len(sources)} book{'s' if len(sources) > 1 else ''})")
