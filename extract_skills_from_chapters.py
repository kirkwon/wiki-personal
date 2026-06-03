#!/usr/bin/env python3
"""
Extract skills from chapter titles and structured content.
Skills are named concepts/methods that represent actionable abilities.
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

# Non-skill patterns (nouns, author names, generic terms)
NON_SKILL = {
    'mindset', 'attitude', 'belief', 'concept', 'idea', 'theory', 'principle',
    'success', 'failure', 'result', 'outcome', 'achievement', 'goal',
    'knowledge', 'information', 'data', 'wisdom', 'insight', 'understanding',
    'time', 'money', 'energy', 'focus', 'attention', 'effort',
    'life', 'work', 'business', 'career', 'relationship', 'family', 'team',
    'problem', 'challenge', 'obstacle', 'barrier', 'difficulty', 'issue',
    'introduction', 'conclusion', 'summary', 'overview', 'background',
    'description', 'definition', 'example', 'note', 'comment',
    # Added common generic nouns
    'role', 'importance', 'analysis', 'power', 'value', 'process',
    'approach', 'strategy', 'method', 'technique', 'system', 'model',
    'framework', 'structure', 'pattern', 'behavior', 'action',
    'creating', 'making', 'building', 'developing', 'improving',
    'through', 'for', 'about', 'regarding', 'concerning'
}

def is_valid_skill_name(text):
    """Check if text is a valid skill name."""
    text = text.strip()

    # Too short or too long
    if len(text) < 4 or len(text) > 60:
        return False

    # Exclude non-skills
    text_lower = text.lower()
    if text_lower in NON_SKILL:
        return False

    # Author names
    if re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+$', text):
        return False

    # Pure numbers
    if re.match(r'^\d+$', text):
        return False

    # Must be meaningful - contain at least one vowel
    if not re.search(r'[aeiou]', text_lower):
        return False

    return True

def extract_skills_from_chapter_title(title):
    """Extract skill names from chapter titles."""
    skills = []

    # Remove common prefixes
    title = re.sub(r'^(Chapter|Part|Section)\s+\d+[:\s]*', '', title, flags=re.IGNORECASE)
    title = title.strip()

    # Remove trailing descriptors
    title = re.sub(r'\s*[-:]\s*(An?|The|Your|How to|A Guide to|Overview|Introduction).*$', '', title, flags=re.IGNORECASE)

    # Extract "The X of Y" patterns
    match = re.match(r'The (.+?) (?:of|for|in|to)', title, re.IGNORECASE)
    if match:
        skill = match.group(1).strip()
        if is_valid_skill_name(skill):
            skills.append(skill)

    # Extract "How to X" patterns
    match = re.match(r'How to (.+)', title, re.IGNORECASE)
    if match:
        skill = match.group(1).strip()
        if is_valid_skill_name(skill):
            skills.append(skill)

    # Extract gerund phrases (X-ing Y)
    match = re.match(r'([A-Z][a-z]+ing [A-Z][a-z]+(?: [A-Z][a-z]+)?)', title)
    if match:
        skill = match.group(1).strip()
        if is_valid_skill_name(skill):
            skills.append(skill)

    # Extract action phrases
    match = re.match(r'([A-Z][a-z]+(?: [A-Z][a-z]+){1,3})', title)
    if match:
        skill = match.group(1).strip()
        if is_valid_skill_name(skill):
            skills.append(skill)

    return skills

def extract_skills_from_book(book):
    """Extract skills from a book."""
    skills = []

    # Method 1: Chapter titles
    if 'summary' in book and 'chapters' in book['summary']:
        for chapter in book['summary']['chapters']:
            title = chapter.get('title', '')
            chapter_skills = extract_skills_from_chapter_title(title)
            skills.extend(chapter_skills)

    # Method 2: core_skills (skip generic ones)
    core_skills = book.get('agent_structure', {}).get('core_skills', [])
    for skill_data in core_skills:
        skill_name = skill_data.get('skill_name', '').strip()

        # Skip generic skill names
        if skill_name.lower() in ['technique', 'practice', 'design', 'management',
                                   'learning', 'communication', 'planning', 'improvement']:
            continue

        if is_valid_skill_name(skill_name):
            skills.append(skill_name)

    # Remove duplicates
    seen = set()
    unique_skills = []
    for skill in skills:
        skill_lower = skill.lower()
        if skill_lower not in seen:
            seen.add(skill_lower)
            unique_skills.append(skill)

    return unique_skills

# Extract all skills
print("\n🔍 Extracting skills from chapter titles...")
all_skills = defaultdict(list)  # skill -> [(book, tags), ...]
skills_by_tag = defaultdict(list)  # tag -> [(skill, book), ...]

for book_title, book in book_data.items():
    print(f"   Processing: {book_title[:50]}...")

    tags = book.get('metadata', {}).get('tags', [])
    skills = extract_skills_from_book(book)

    print(f"      Found {len(skills)} skills")

    for skill in skills:
        all_skills[skill].append((book_title, tags))
        for tag in tags:
            skills_by_tag[tag].append((skill, book_title))

print(f"\n✅ Extracted {len(all_skills)} unique skills")

# Filter: keep skills with meaningful names
filtered_skills = {}
for skill, sources in all_skills.items():
    # Keep if skill name is meaningful
    if is_valid_skill_name(skill):
        filtered_skills[skill] = sources

print(f"📊 Final count: {len(filtered_skills)} skills")

# Show samples
print(f"\n📝 Sample extracted skills:")
print("=" * 80)
for i, skill in enumerate(list(filtered_skills.keys())[:20]):
    sources = filtered_skills[skill]
    books = list(set(s[0] for s in sources))
    print(f"{i+1}. {skill} (from {len(books)} book{'s' if len(books) > 1 else ''})")

# Normalize tags
tag_normalization = {
    'habit-formation': 'habits',
    'mindset': 'psychology',
    'personal-development': 'self-improvement',
    'time-management': 'productivity',
    'decision-making': 'strategy',
    'mental-models': 'thinking',
    'behavioral-economics': 'psychology',
    'information-management': 'organization',
    'knowledge-management': 'organization',
    'deep-work': 'focus',
    'attention': 'focus',
    'prioritization': 'productivity',
    'execution': 'productivity',
    'goals': 'productivity',
    'learning': 'self-improvement',
    'second-brain': 'organization',
    'gtd': 'productivity',
    'workflow': 'productivity',
    'uncertainty': 'strategy',
    'risk': 'finance',
    'probabilistic-thinking': 'thinking',
    'bias': 'psychology',
    'randomness': 'thinking',
    'black-swan': 'thinking',
    'fragility': 'psychology',
    'resilience': 'psychology',
    'antifragility': 'psychology',
    'sunk-cost': 'strategy',
    'opportunity-cost': 'strategy',
    'negotiation': 'communication',
    'persuasion': 'communication',
    'influence': 'leadership',
    'social-proof': 'psychology',
    'commitment': 'psychology',
    'authority': 'leadership',
    'scarcity': 'psychology',
    'choice-architecture': 'strategy',
    'incentives': 'leadership',
    'bottleneck': 'productivity',
    'theory-of-constraints': 'productivity',
    'systems': 'thinking',
    'communication': 'leadership',
    'leadership': 'leadership',
    'business': 'strategy',
    'strategy': 'strategy',
    'management': 'leadership',
    'ethics': 'philosophy',
    'philosophy': 'thinking',
    'motivation': 'psychology',
    'action': 'productivity',
    'performance': 'productivity',
    'flow': 'focus',
    'environment': 'productivity',
    'routine': 'habits',
    'innovation': 'productivity',
}

# Apply tag normalization
normalized_skills_by_tag = defaultdict(list)
for tag, skills in skills_by_tag.items():
    normalized_tag = tag_normalization.get(tag.lower(), tag.lower())
    for skill, book in skills:
        normalized_skills_by_tag[normalized_tag].append((skill, book))

# Generate output
all_skills_list = sorted(filtered_skills.keys())
all_tags_list = sorted(set(normalized_skills_by_tag.keys()))

overlaps = {}
for skill, sources in filtered_skills.items():
    books = list(set(s[0] for s in sources))
    if len(books) > 1:
        overlaps[skill] = books

multi_tag_skills = {}
for skill, sources in filtered_skills.items():
    tags = set()
    for _, skill_tags in sources:
        for t in skill_tags:
            normalized = tag_normalization.get(t.lower(), t.lower())
            tags.add(normalized)
    if len(tags) > 1:
        multi_tag_skills[skill] = list(tags)

# Generate basic descriptions
descriptions = {}
for skill in all_skills_list:
    books = list(set(s[0] for s in filtered_skills[skill]))[:2]
    book_str = " and ".join(books)
    descriptions[skill] = f"A skill from {book_str}"

output_data = {
    "skills_by_tag": {k: [[s[0], s[1]] for s in v] for k, v in normalized_skills_by_tag.items()},
    "all_skills": all_skills_list,
    "all_tags": all_tags_list,
    "overlaps": overlaps,
    "multi_tag_skills": multi_tag_skills,
    "descriptions": descriptions,
    "stats": {
        "total_skills": len(all_skills_list),
        "total_tags": len(all_tags_list),
        "total_books": len(book_data),
        "overlapping": len(overlaps),
        "multi_tag": len(multi_tag_skills)
    }
}

output_file = Path("/Users/kirkwon/wiki-personal/skills_data_actionable.json")
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"\n💾 Saved to: {output_file}")
print(f"📊 Stats: {len(all_skills_list)} skills, {len(all_tags_list)} tags, {len(overlaps)} overlapping")
