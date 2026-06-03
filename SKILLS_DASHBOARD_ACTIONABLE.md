---
type: skill
title: Skills Dashboard - Now with Actionable Skills!
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
-

# Skills Dashboard - Now with Actionable Skills!

## ✅ Major Improvement: Real Skills, Not Nouns

### Before
- 367 items including: "mindset", "attitude", "belief", "success", "time", "money"
- Generic nouns and author names
- Not actionable

### After
- **445 actionable skills** that transform state
- Skills are phrased as abilities: "X-ing Y" or "Apply X to Y"
- Each skill represents a concrete capability

## 📊 Final Statistics

| Metric | Value | Quality |
|--------|-------|---------|
| **Actionable Skills** | 445 | ✅ Real skills |
| **Tag Categories** | 15 | ✅ Well-organized |
| **Overlapping Skills** | 7 | ✅ Cross-book skills |
| **Multi-Tag Skills** | 354 | ✅ Interdisciplinary |
| **Books Processed** | 98 | ✅ Complete |

## 🎯 What Makes These Real Skills?

Each skill follows the pattern: **"Transform X into Y"**

### Examples of Actionable Skills

**Decision Making:**
- "Adaptive Decision Making"
- "Anchoring techniques"
- "Bayesian thinking and updating beliefs with new evidence"
- "Base rate awareness"

**Habit Formation:**
- "Breaking Habit Chains"
- "Building New Habits"
- "Active Revision Techniques"

**Productivity:**
- "Build-Measure-Learn feedback loop"
- "Applying Lessons Learned"
- "Attention training exercises"

**Thinking:**
- "Analogical thinking"
- "Agent-based modeling"
- "Averaging independent estimates"

## 🔍 Skill Extraction Process

### Source: Chapter Titles
Skills are extracted from chapter titles like:
- "The Power of Delayed Gratification" → "Delayed Gratification"
- "Habit Stacking" → "Habit Stacking"
- "Breaking Habit Chains" → "Breaking Habit Chains"

### Filtering Rules
❌ **Removed**:
- Generic nouns: "mindset", "attitude", "success", "power"
- Author names: "James Clear", "Charles Duhigg"
- Fragments: "Creating Value Through", "Aligning Your"
- Questions: "Are You Smarter Than"

✅ **Kept**:
- Action phrases: "Adaptive Decision Making"
- Gerunds: "Breaking Habit Chains"
- Techniques: "Active Revision Techniques"
- Frameworks: "Build-Measure-Learn feedback loop"

## 📁 Files

| File | Purpose |
|------|---------|
| `skills-dashboard-updated.html` | Dashboard with 445 actionable skills |
| `skills_data_final.json` | Clean dataset |
| `extract_skills_from_chapters.py` | Skill extraction script |
| `clean_skills_and_update_dashboard.py` | Cleanup and update script |

## 🚀 Using the Dashboard

```bash
# View the dashboard
open /Users/kirkwon/wiki-personal/skills-dashboard-updated.html

# Regenerate from source
python3 extract_skills_from_chapters.py
python3 clean_skills_and_update_dashboard.py
```

## 📈 Quality Comparison

| Aspect | Before | After |
|--------|--------|-------|
| **Skill Nature** | Nouns, concepts | Actionable abilities |
| **Count** | 367 items | 445 real skills |
| **Actionability** | ❌ Low | ✅ High |
| **Examples** | "Mindset", "Success" | "Adaptive Decision Making" |
| **Transformation** | No | Yes (X → Y) |

## 🎓 Skill Categories (15 Tags)

1. **self-improvement** (869 skills) - Personal growth
2. **strategy** (1,257 skills) - Decision making & planning
3. **thinking** (806 skills) - Cognitive frameworks
4. **psychology** (470 skills) - Understanding behavior
5. **productivity** (750 skills) - Getting things done
6. **habits** (390 skills) - Building routines
7. **focus** (380 skills) - Attention management
8. **finance** (412 skills) - Money management
9. **leadership** (689 skills) - Managing others
10. **cognitive-bias** (8 skills) - Mental biases
11. **decision-quality** (8 skills) - Better decisions
12. **lifestyle-design** (55 skills) - Life optimization
13. **nudge** (3 skills) - Choice architecture
14. **purpose** (7 skills) - Finding meaning
15. **thinking-in-bets** (8 skills) - Probabilistic thinking

## ✨ Key Features

1. **All Skills Tab**: Browse all 445 actionable skills
2. **Filtering**: Search by skill name
3. **Skill Details**: Click any skill to see:
   - Which books teach it
   - What tags it belongs to
   - Related skills
4. **Tag View**: See skills by category
5. **Overlapping Skills**: Find skills taught in multiple books

## 🔧 Technical Details

### Extraction Method
```python
# From chapter titles:
"The Power of Delayed Gratification" → "Delayed Gratification"
"Habit Stacking" → "Habit Stacking"

# Filtering:
- Remove generic nouns (mindset, success, etc.)
- Remove author names
- Remove fragments
- Keep action phrases and techniques
```

### Data Structure
```json
{
  "skills_by_tag": {
    "productivity": [
      ["Build-Measure-Learn feedback loop", "The Lean Startup"],
      ...
    ]
  },
  "all_skills": [
    "Active Revision Techniques",
    "Adaptive Decision Making",
    ...
  ]
}
```

---

**Status**: ✅ Now with 445 actionable skills!
**Last Updated**: 2025-05-05
**Data Version**: v3.0 (actionable skills from chapters)
