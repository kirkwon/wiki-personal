#!/usr/bin/env python3
"""
Generate better skill descriptions using chapter summaries and key takeaways.
"""

import json
from pathlib import Path
from collections import defaultdict

# Load the data
data_file = Path("/Users/kirkwon/wiki-personal/skills_data_updated.json")
with open(data_file, 'r') as f:
    data = json.load(f)

# Load the original book JSONs
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

def find_skill_in_chapters(skill_name, book):
    """Search for skill mentions in chapter summaries and key takeaways."""
    mentions = []

    if 'summary' not in book or 'chapters' not in book['summary']:
        return mentions

    skill_lower = skill_name.lower()

    for chapter in book['summary']['chapters']:
        chapter_title = chapter.get('title', '')
        chapter_summary = chapter.get('summary', '')
        key_takeaways = chapter.get('key_takeaways', [])

        # Check chapter title
        if skill_lower in chapter_title.lower():
            mentions.append({
                'source': f"Chapter: {chapter_title}",
                'content': chapter_summary[:200] if chapter_summary else ''
            })
            continue

        # Check key takeaways
        for i, takeaway in enumerate(key_takeaways):
            if skill_lower in takeaway.lower():
                mentions.append({
                    'source': f"Chapter '{chapter_title}' - Key Takeaway {i+1}",
                    'content': takeaway[:200]
                })

        # Check summary
        if skill_lower in chapter_summary.lower():
            # Extract relevant sentence
            sentences = chapter_summary.split('.')
            for sentence in sentences:
                if skill_lower in sentence.lower():
                    mentions.append({
                        'source': f"Chapter: {chapter_title}",
                        'content': sentence.strip()[:200]
                    })
                    break

    return mentions

def generate_smart_description(skill_name, books):
    """Generate description by aggregating insights from chapter content."""

    all_mentions = []

    for book_title in books:
        if book_title not in book_data:
            continue

        book = book_data[book_title]

        # First try to find in chapters
        chapter_mentions = find_skill_in_chapters(skill_name, book)
        all_mentions.extend([(m, book_title) for m in chapter_mentions])

        # Also check quick_reference for high-level context
        why_matters = book.get('quick_reference', {}).get('why_it_matters', '')
        big_picture = book.get('quick_reference', {}).get('the_big_picture', '')
        bottom_line = book.get('quick_reference', {}).get('the_bottom_line', '')

        if skill_name.lower() in why_matters.lower() or skill_name.lower() in big_picture.lower():
            all_mentions.append(({
                'source': f"Book Overview ({book_title.split(' - ')[0]})",
                'content': f"{big_picture}. {bottom_line}"
            }, book_title))

    if not all_mentions:
        return None

    # Build description
    if len(all_mentions) == 1:
        mention, _ = all_mentions[0]
        content = mention.get('content', '')
        return content if content else None

    # Multiple mentions - aggregate
    parts = [f"**Found in {len(all_mentions)} location{'s' if len(all_mentions) > 1 else ''}:**\n"]

    for i, (mention, book_title) in enumerate(all_mentions[:5], 1):
        source = mention['source']
        content = mention['content']

        # Clean up book title in source
        if ' - ' in book_title:
            short_title = book_title.split(' - ')[0]
            source = source.replace(book_title, short_title)

        parts.append(f"{i}. {source}")
        if content:
            parts.append(f"   {content}...")

    if len(all_mentions) > 5:
        parts.append(f"\n+ {len(all_mentions) - 5} more reference(s)")

    return '\n'.join(parts)

# Generate descriptions
print("📝 Generating smart descriptions from chapter content...")
smart_descriptions = {}

# Focus on multi-book skills first (highest value)
multi_book_skills = list(data.get('overlaps', {}).keys())
print(f"   Processing {len(multi_book_skills)} multi-book skills...")

for skill_name in multi_book_skills:
    books = data['overlaps'][skill_name]
    description = generate_smart_description(skill_name, books)
    if description:
        smart_descriptions[skill_name] = description

# Then process remaining skills
all_skills = set(data['all_skills']) - set(multi_book_skills)
print(f"   Processing {len(all_skills)} remaining skills...")

processed = 0
for skill_name in all_skills:
    # Find books for this skill
    books = set()
    for tag, skills in data['skills_by_tag'].items():
        for skill, book in skills:
            if skill == skill_name:
                books.add(book)

    if books:
        description = generate_smart_description(skill_name, list(books))
        if description:
            smart_descriptions[skill_name] = description

    processed += 1
    if processed % 50 == 0:
        print(f"   Processed {processed}/{len(all_skills)}...")

print(f"✅ Generated {len(smart_descriptions)} smart descriptions")

# Update data
data['descriptions'] = smart_descriptions

# Save
output_file = Path("/Users/kirkwon/wiki-personal/skills_data_updated.json")
with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"💾 Saved to: {output_file}")

# Update HTML
html_file = Path("/Users/kirkwon/wiki-personal/skills-dashboard-updated.html")
with open(html_file, 'r') as f:
    html_content = f.read()

new_data_json = json.dumps({
    "skills_by_tag": data['skills_by_tag'],
    "all_skills": data['all_skills'],
    "all_tags": data['all_tags'],
    "overlaps": data['overlaps'],
    "multi_tag_skills": data['multi_tag_skills'],
    "descriptions": data['descriptions']
}, indent=2)

if 'const skillsData = {' in html_content:
    parts = html_content.split('const skillsData = {', 1)
    if len(parts) == 2:
        remaining = parts[1]
        end_idx = remaining.find('};', 2)
        if end_idx > 0:
            after_data = remaining[end_idx + 2:]
            html_content = parts[0] + 'const skillsData = ' + new_data_json + ';' + after_data

with open(html_file, 'w') as f:
    f.write(html_content)

print(f"✅ Updated HTML: {html_file}")

# Show samples
print("\n📝 SAMPLE SMART DESCRIPTIONS")
print("=" * 80)

# Show multi-book skill
for skill in list(data['overlaps'].keys())[:2]:
    if skill in smart_descriptions:
        print(f"\n🔹 {skill} (multi-book)")
        desc = smart_descriptions[skill]
        print(desc[:400])
        print('...' if len(desc) > 400 else '')
        break

# Show single-book skill
for skill in list(data['all_skills']):
    if skill in smart_descriptions and skill not in data.get('overlaps', {}):
        print(f"\n🔹 {skill} (single-book)")
        desc = smart_descriptions[skill]
        print(desc[:400])
        print('...' if len(desc) > 400 else '')
        break

print(f"\n📊 Stats:")
print(f"   Multi-book skills with descriptions: {sum(1 for s in multi_book_skills if s in smart_descriptions)}/{len(multi_book_skills)}")
print(f"   Total descriptions: {len(smart_descriptions)}/{len(data['all_skills'])}")
