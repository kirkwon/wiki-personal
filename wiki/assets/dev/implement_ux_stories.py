#!/usr/bin/env python3
"""
Implement all UX improvement stories.
Fixes broken functionality and adds missing features.
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Load data
with open('skills_data_fixed.json', 'r') as f:
    data = json.load(f)

# Load UX dashboard
with open('skills-dashboard-ux.html', 'r') as f:
    html = f.read()

print("🔧 Implementing UX Improvement Stories")
print("=" * 80)

# Story 1: Add timestamp
print("\n📅 Story 1: Adding timestamp...")
timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
timestamp_html = f'<div style="text-align: center; padding: 16px 0; color: #64748b; font-size: 12px;">Last Updated: {timestamp}</div>'

# Insert timestamp before closing body tag
html = html.replace('</body>', timestamp_html + '</body>')
print("✅ Story 1: Timestamp added")

# Story 2: Fix metrics click handlers
print("\n📊 Story 2: Fixing metrics click...")
# Update stat cards with onclick handlers
html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Total Skills</div>',
    '''<div class="stat-card" onclick="showView('skills')" style="cursor: pointer;">
        <div class="stat-label">Total Skills</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Categories</div>',
    '''<div class="stat-card" onclick="showView('tags')" style="cursor: pointer;">
        <div class="stat-label">Categories</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Multi-Disciplinary</div>',
    '''<div class="stat-card" onclick="showView('multitag')" style="cursor: pointer;">
        <div class="stat-label">Multi-Disciplinary</div>''',
    html
)

html = re.sub(
    r'<div class="stat-card">\s*<div class="stat-label">Cross-Book</div>',
    '''<div class="stat-card" onclick="showView('overlaps')" style="cursor: pointer;">
        <div class="stat-label">Cross-Book</div>''',
    html
)
print("✅ Story 2: Metrics click handlers fixed")

# Story 3: Fix tag filtering
print("\n🏷️  Story 3: Fixing tag filtering...")
# Update tag badge rendering to be clickable
html = re.sub(
    r'info\.tags\.map\(t => `<span class="tag-badge \${t}">\${t}</span>`\)',
    '''info.tags.map(t => `<span class="tag-badge ${t}" onclick="filterByTag('${t}')" style="cursor: pointer;">${t}</span>`)''',
    html
)

# Add filterByTag function if not exists
if 'function filterByTag' not in html:
    filter_function = '''
    function filterByTag(tagName) {
        const filtered = skillsData.all_skills.filter(skill => {
            const info = skillInfoMap[skill];
            return info && info.tags && info.tags.includes(tagName);
        });

        const tbody = document.getElementById('skillsTableBody');
        tbody.innerHTML = '';

        document.getElementById('pageTitle').textContent = `Skills: ${tagName}`;
        document.getElementById('pageSubtitle').textContent = `${filtered.length} skills tagged "${tagName}"`;

        filtered.forEach(skill => {
            const info = skillInfoMap[skill] || { tags: [], books: [] };
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><span class="skill-name" onclick="showSkillDetail('${skill}')">${skill}</span></td>
                <td>${info.tags.slice(0, 3).map(t => `<span class="tag-badge ${t}" onclick="filterByTag('${t}')">${t}</span>`).join(' ')} ${info.tags.length > 3 ? `+${info.tags.length - 3}` : ''}</td>
                <td>${info.books.length} book${info.books.length !== 1 ? 's' : ''}</td>
            `;
            tbody.appendChild(row);
        });
    }
    '''

    # Insert before closing script tag
    html = html.replace('</script>', filter_function + '</script>')
print("✅ Story 3: Tag filtering fixed")

# Story 4: Add accordion view for categories
print("\n📁 Story 4: Adding By Category accordion...")
# Add showTagAccordion function
accordion_function = '''
    function showTagAccordion() {
        document.getElementById('mainCardTitle').textContent = 'By Category';
        const content = document.getElementById('mainContent');

        let html = '<div class="accordion">';

        skillsData.all_tags.forEach(tag => {
            const skills = skillsData.skills_by_tag[tag] || [];
            html += `
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion('${tag}')">
                        <span class="accordion-title">${tag}</span>
                        <span class="accordion-count">${skills.length} skills</span>
                    </div>
                    <div class="accordion-content" id="accordion-${tag}">
                        <table class="skills-table">
                            ${skills.slice(0, 10).map(([skill, book]) => `
                                <tr>
                                    <td><span class="skill-name" onclick="showSkillDetail('${skill}')">${skill}</span></td>
                                    <td>${book}</td>
                                </tr>
                            `).join('')}
                        </table>
                    </div>
                </div>
            `;
        });

        html += '</div>';
        content.innerHTML = html;
    }

    function toggleAccordion(tag) {
        const content = document.getElementById(`accordion-${tag}`);
        const allContents = document.querySelectorAll('.accordion-content');

        allContents.forEach(c => {
            if (c !== content) c.style.display = 'none';
        });

        content.style.display = content.style.display === 'none' ? 'block' : 'none';
    }
    '''

html = html.replace('</script>', accordion_function + '</script>')

# Add accordion CSS
accordion_css = '''
    .accordion { margin-top: 16px; }
    .accordion-item { border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 8px; overflow: hidden; }
    .accordion-header { padding: 16px; background: var(--bg-tertiary); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .accordion-header:hover { background: #475569; }
    .accordion-title { font-weight: 500; }
    .accordion-count { font-size: 12px; color: var(--text-muted); }
    .accordion-content { display: none; }
    .accordion-content.show { display: block; }
'''

html = html.replace('</style>', accordion_css + '</style>')

# Update tags view to use accordion
html = html.replace("} else if (view === 'tags') {", "else if (view === 'tags') { showTagAccordion(); } else if (view === 'tags-old') {")
print("✅ Story 4: By Category accordion added")

# Story 6: Add AI integration
print("\n🤖 Story 6: Adding AI integration...")
# Update showSkillDetail to include AI menu
old_detail = '''<div class="detail-section">
            <h4>Description</h4>
            <p class="detail-description" id="detailDescription">Description here...</p>
        </div>'''

new_detail = '''<div class="detail-section">
            <h4>
                Description
                <button class="btn-icon" onclick="toggleAIMenu()" style="width: 24px; height: 24px; margin-left: 8px;" title="Get AI Help">
                    <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </button>
            </h4>
            <p class="detail-description" id="detailDescription">Description here...</p>
            <div id="aiMenu" style="display: none; margin-top: 12px; padding: 12px; background: var(--bg-tertiary); border-radius: 8px;">
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 8px;">Get help with this skill:</div>
                <a id="chatgptLink" target="_blank" style="display: block; padding: 8px 12px; background: #10a37f; color: white; border-radius: 6px; text-decoration: none; margin-bottom: 8px;">Open in ChatGPT →</a>
                <a id="claudeLink" target="_blank" style="display: block; padding: 8px 12px; background: #cc785c; color: white; border-radius: 6px; text-decoration: none;">Open in Claude →</a>
            </div>
        </div>'''

html = html.replace(old_detail, new_detail)

# Add AI menu toggle function
ai_toggle_function = '''
    function toggleAIMenu() {
        const menu = document.getElementById('aiMenu');
        menu.style.display = menu.style.display === 'none' ? 'block' : 'none';

        // Update links
        const skillName = document.getElementById('detailTitle').textContent;
        const description = document.getElementById('detailDescription').textContent;
        const info = skillInfoMap[skillName] || { tags: [], books: [] };

        const prompt = `Skill: ${skillName}\\nDescription: ${description}\\nTags: ${info.tags.join(', ')}\\nBooks: ${info.books.join(', ')}\\n\\nHelp me understand and apply this skill.`;
        const encoded = encodeURIComponent(prompt);

        document.getElementById('chatgptLink').href = `https://chatgpt.com/?q=${encoded}`;
        document.getElementById('claudeLink').href = `https://claude.ai/new?q=${encoded}`;
    }
'''

html = html.replace('</script>', ai_toggle_function + '</script>')
print("✅ Story 6: AI integration added")

# Story 7: Fix network visualization
print("\n🕸️  Story 7: Fixing network visualization...")
# Update drawNetwork function
old_network = 'function drawNetwork() {\n            const container = document.getElementById(\'networkContainer\');\n            if (container.offsetParent === null) return; // Hidden\n\n            container.innerHTML = \'<p style="padding: 40px; text-align: center; color: #94a3b8;">Network visualization will appear here when you have more tags.</p>\';\n        }'

new_network = '''function drawNetwork() {
            const container = document.getElementById('networkContainer');
            container.innerHTML = '';

            if (container.offsetParent === null) return;

            const width = container.offsetWidth;
            const height = 500;

            // Get all tags
            const tags = Object.entries(skillsData.skills_by_tag)
                .sort((a, b) => b[1].length - a[1].length);

            if (tags.length < 2) {
                container.innerHTML = '<p style="padding: 40px; text-align: center; color: #94a3b8;">Not enough tags to display network</p>';
                return;
            }

            const nodes = tags.map(([tag, skills]) => ({
                id: tag,
                value: skills.length,
                skills: skills.map(s => s[0])
            }));

            // Create links from multi-tag skills
            const links = [];
            const skillToTags = {};

            tags.forEach(([tag, skills]) => {
                skills.forEach(([skill, book]) => {
                    if (!skillToTags[skill]) skillToTags[skill] = [];
                    skillToTags[skill].push(tag);
                });
            });

            Object.entries(skillToTags).forEach(([skill, tags]) => {
                if (tags.length > 1) {
                    for (let i = 0; i < tags.length; i++) {
                        for (let j = i + 1; j < tags.length; j++) {
                            links.push({ source: tags[i], target: tags[j] });
                        }
                    }
                }
            });

            const svg = d3.select("#networkContainer")
                .append("svg")
                .attr("width", width)
                .attr("height", height);

            const simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-200))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(30));

            const link = svg.append("g")
                .selectAll("line")
                .data(links)
                .join("line")
                .attr("stroke", "#475569")
                .attr("stroke-width", 1);

            const node = svg.append("g")
                .selectAll("circle")
                .data(nodes)
                .join("circle")
                .attr("r", d => Math.sqrt(d.value) * 5)
                .attr("fill", (d, i) => ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ec4899'][i % 5])
                .attr("cursor", "pointer")
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended))
                .on("mouseover", function(event, d) {
                    d3.select(this).attr("stroke", "#fff").attr("stroke-width", 2);
                })
                .on("mouseout", function(event, d) {
                    d3.select(this).attr("stroke", null);
                });

            const label = svg.append("g")
                .selectAll("text")
                .data(nodes)
                .join("text")
                .text(d => d.id)
                .attr("font-size", "10px")
                .attr("text-anchor", "middle")
                .attr("fill", "#f1f5f9")
                .attr("dy", d => -Math.sqrt(d.value) * 5 - 5);

            simulation.on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node
                    .attr("cx", d => Math.max(30, Math.min(width - 30, d.x)))
                    .attr("cy", d => Math.max(30, Math.min(height - 30, d.y)));

                label
                    .attr("x", d => Math.max(30, Math.min(width - 30, d.x)))
                    .attr("y", d => Math.max(30, Math.min(height - 30, d.y)));
            });

            function dragstarted(event, d) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(event, d) {
                d.fx = event.x;
                d.fy = event.y;
            }

            function dragended(event, d) {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
        }'''

html = html.replace(old_network, new_network)
print("✅ Story 7: Network visualization fixed")

# Add multitag view to showView
print("\n📋 Adding multitag view support...")
# Update showView to handle multitag
html = html.replace(
    "renderView(view);",
    '''if (view === 'multitag') {
                document.getElementById('pageTitle').textContent = 'Multi-Disciplinary Skills';
                document.getElementById('mainCardTitle').textContent = 'Multi-Disciplinary';

                const multiSkills = Object.keys(skillsData.multi_tag_skills);
                const tbody = document.getElementById('skillsTableBody');
                tbody.innerHTML = '';

                multiSkills.slice(0, 50).forEach(skill => {
                    const info = skillInfoMap[skill] || { tags: [], books: [] };
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td><span class="skill-name" onclick="showSkillDetail('${skill}')">${skill}</span></td>
                        <td>${info.tags.map(t => `<span class="tag-badge ${t}">${t}</span>`).join(' ')}</td>
                        <td>${info.books.length} book${info.books.length !== 1 ? 's' : ''}</td>
                    `;
                    tbody.appendChild(row);
                });
            } else {
                renderView(view);
            }'''
)
print("✅ Multi-tag view added")

# Save updated HTML
with open('skills-dashboard-ux.html', 'w') as f:
    f.write(html)

print("\n" + "=" * 80)
print("✅ ALL STORIES IMPLEMENTED")
print("=" * 80)
print("📝 Changes:")
print("   ✅ Story 1: Timestamp added")
print("   ✅ Story 2: Metrics click fixed")
print("   ✅ Story 3: Tag filtering fixed")
print("   ✅ Story 4: Accordion view added")
print("   ✅ Story 5: Conflict Guide already present")
print("   ✅ Story 6: AI integration added")
print("   ✅ Story 7: Network visualization fixed")
print("\n📄 Saved: skills-dashboard-ux.html")
