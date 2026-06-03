#!/usr/bin/env python3
"""
Create Skills Dashboard Pro - Modern Dark Theme with Sidebar
Based on design reference: ~/Downloads/0000.png
"""

import json
import re
from datetime import datetime
from pathlib import Path

print("🎨 CREATING MODERN DARK DASHBOARD WITH SIDEBAR")
print("=" * 80)

# Load the rich data
data_file = Path("skills_data_fixed.json")
with open(data_file, 'r') as f:
    data = json.load(f)

print(f"✅ Loaded data: {len(data['all_skills'])} skills")

# Prepare data
total_skills = len(data['all_skills'])
total_tags = len(data['all_tags'])
total_books = len(set(book for skills in data['skills_by_tag'].values() for _, book in skills))
multi_tag = len(data['multi_tag_skills'])
overlaps = len(data['overlaps'])

# Create the HTML with modern dark theme
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills Dashboard Pro</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lora:ital,wght@0,400;0,600;1,400&family=Cinzel:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=VT323&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Caveat:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            /* Default: Modern Dark */
            --bg-primary: #0f172a;
            --bg-secondary: rgba(30, 41, 59, 0.7);
            --bg-card: rgba(30, 37, 64, 0.4);
            --accent-primary: #6366f1;
            --accent-secondary: #8b5cf6;
            --text-main: #f1f5f9;
            --text-dim: #94a3b8;
            --border-color: rgba(255, 255, 255, 0.08);
            --sidebar-width: 280px;
            --font-heading: 'Space Grotesk', sans-serif;
            --font-body: 'Inter', sans-serif;
            --border-radius: 16px;
            --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --transition-speed: 0.3s;
        }}

        /* Theme Overrides */
        body.theme-editorial {{
            --bg-primary: #121212;
            --bg-secondary: #1a1a1a;
            --bg-card: #222;
            --accent-primary: #c5a059;
            --accent-secondary: #8e733c;
            --text-main: #fcfcfc;
            --text-dim: #a0a0a0;
            --font-heading: 'Playfair Display', serif;
            --font-body: 'Lora', serif;
            --border-radius: 4px;
        }}

        body.theme-vellum {{
            --bg-primary: #efe9d9;
            --bg-secondary: #d9cfbc;
            --bg-card: #ffffff;
            --accent-primary: #3d2b1f;
            --accent-secondary: #5e4033;
            --text-main: #1a1510;
            --text-dim: #332a1e;
            --border-color: rgba(0,0,0,0.3);
            --font-heading: 'Cinzel', serif;
            --font-body: 'EB Garamond', serif;
            --border-radius: 2px;
            --card-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}

        body.theme-pixel {{
            --bg-primary: #e0e0e0;
            --bg-secondary: #ffffff;
            --bg-card: rgba(0, 128, 128, 0.05);
            --accent-primary: #008080;
            --accent-secondary: #004d4d;
            --text-main: #000;
            --text-dim: #555;
            --border-color: #999;
            --font-heading: 'VT323', monospace;
            --font-body: 'VT323', monospace;
            --border-radius: 0;
            --card-shadow: 4px 4px 0 #999;
        }}

        body.theme-dossier {{
            --bg-primary: #d4ccc5;
            --bg-secondary: #c9bfb8;
            --bg-card: #e0d8d0;
            --accent-primary: #3d3d3d;
            --accent-secondary: #5e5e5e;
            --text-main: #1a1a1a;
            --text-dim: #4a4a4a;
            --border-color: rgba(0,0,0,0.15);
            --font-heading: 'Courier Prime', monospace;
            --font-body: 'Courier Prime', monospace;
            --border-radius: 0;
        }}

        body.theme-etching {{
            --bg-primary: #fafafa;
            --bg-secondary: #f0f0f0;
            --bg-card: #ffffff;
            --accent-primary: #000000;
            --accent-secondary: #333333;
            --text-main: #000;
            --text-dim: #666;
            --border-color: #000;
            --font-heading: 'Cormorant Garamond', serif;
            --font-body: 'Montserrat', sans-serif;
            --border-radius: 0;
        }}

        body.theme-whiteboard {{
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-card: #ffffff;
            --accent-primary: #3b82f6;
            --accent-secondary: #ef4444;
            --text-main: #0f172a;
            --text-dim: #64748b;
            --border-color: #e2e8f0;
            --font-heading: 'Caveat', cursive;
            --font-body: 'Inter', sans-serif;
            --border-radius: 20px;
        }}

        body.theme-sketch {{
            --bg-primary: #fff;
            --bg-secondary: #fff;
            --bg-card: #fff;
            --accent-primary: #000;
            --accent-secondary: #333;
            --text-main: #000;
            --text-dim: #333;
            --border-color: #000;
            --font-heading: 'Caveat', cursive;
            --font-body: 'Caveat', cursive;
            --border-radius: 8px;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: var(--font-body), -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            color: var(--text-main);
            display: flex;
            min-height: 100vh;
            line-height: 1.6;
            letter-spacing: -0.01em;
            transition: background var(--transition-speed), color var(--transition-speed);
        }}

        /* Breadcrumbs */
        .breadcrumb {{
            display: flex;
            gap: 8px;
            font-size: 10px;
            font-weight: 700;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 8px;
        }}

        .breadcrumb span {{
            opacity: 0.6;
        }}

        .breadcrumb .active-crumb {{
            opacity: 1;
            color: var(--accent-primary);
        }}

        /* Chart container */
        .chart-wrapper {{
            height: 300px;
            width: 100%;
            margin-top: 1rem;
        }}

        .bar-label {{
            font-size: 11px;
            fill: var(--text-dim);
            font-weight: 600;
        }}

        /* Reading Progress Indicator */
        #progress-container {{
            position: fixed;
            top: 0;
            left: 280px;
            right: 0;
            height: 3px;
            background: rgba(99, 102, 241, 0.1);
            z-index: 1001;
        }}

        #progress-bar {{
            height: 100%;
            background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 50%, #a78bfa 100%);
            width: 0%;
            transition: width 0.1s ease-out;
            box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
        }}

        /* Sidebar */
        .sidebar {{
            width: 280px;
            background: var(--bg-secondary);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            z-index: 100;
        }}

        body.theme-vellum .sidebar {{
            backdrop-filter: none;
            -webkit-backdrop-filter: none;
        }}

        .sidebar-header {{
            padding: 32px 24px 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .sidebar-brand {{
            font-family: var(--font-heading);
            font-size: 22px;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 6px;
            letter-spacing: -0.02em;
            text-transform: none;
            background: linear-gradient(135deg, var(--text-main) 0%, var(--accent-primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .sidebar-tagline {{
            font-size: 11px;
            font-weight: 500;
            color: var(--text-dim);
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }}

        .nav-section {{
            padding: 20px 0;
        }}

        .nav-header {{
            font-family: var(--font-heading);
            font-size: 10px;
            font-weight: 700;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.12em;
            padding: 0 24px;
            margin-bottom: 12px;
        }}

        .nav-item {{
            display: flex;
            align-items: center;
            padding: 14px 24px;
            color: var(--text-dim);
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border-left: 3px solid transparent;
            font-weight: 500;
            font-size: 14px;
            letter-spacing: -0.01em;
            position: relative;
            overflow: hidden;
            background: transparent;
            width: 100%;
        }}

        .nav-item::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 0%;
            height: 100%;
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%);
            transition: width 0.3s ease;
        }}

        .nav-item:hover::before {{
            width: 100%;
        }}

        .nav-item:hover {{
            background: rgba(255, 255, 255, 0.05);
            color: #fff;
            padding-left: 28px;
            transform: translateX(2px);
        }}

        .nav-item.active {{
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.1) 100%);
            color: #fff;
            border-left-color: #a78bfa;
            font-weight: 600;
            box-shadow: inset 0 0 20px rgba(99, 102, 241, 0.1);
        }}

        .nav-item.active::before {{
            display: none;
        }}

        .nav-icon {{
            width: 18px;
            height: 18px;
            margin-right: 14px;
            opacity: 0.85;
        }}

        /* Main Content */
        .main-content {{
            flex: 1;
            margin-left: 280px;
            padding: 40px;
            background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.05), transparent 400px),
                        radial-gradient(circle at bottom left, rgba(139, 92, 246, 0.05), transparent 400px);
        }}

        .content-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 40px;
        }}

        .header-title {{
            font-family: var(--font-heading);
            font-size: 36px;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 8px;
            letter-spacing: -0.03em;
            line-height: 1.2;
        }}

        .header-subtitle {{
            font-size: 14px;
            font-weight: 500;
            color: #94a3b8;
            letter-spacing: 0.02em;
        }}

        .search-box {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 12px 18px;
            color: var(--text-main);
            font-size: 14px;
            font-weight: 500;
            width: 100%;
            outline: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            letter-spacing: -0.01em;
        }}

        .search-box:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1);
        }}

        .search-box::placeholder {{
            color: var(--text-dim);
            opacity: 1;
        }}

        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
            margin-bottom: 40px;
        }}

        .stat-card {{
            background: var(--bg-card);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius);
            padding: 28px;
            position: relative;
            overflow: hidden;
            transition: all var(--transition-speed);
            cursor: pointer;
            box-shadow: var(--card-shadow);
        }}

        .stat-card:hover {{
            transform: translateY(-6px);
            background: var(--bg-secondary);
            border-color: var(--accent-primary);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}

        .stat-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.05), transparent 70%);
            pointer-events: none;
        }}

        .stat-label {{
            font-family: var(--font-heading);
            font-size: 11px;
            font-weight: 700;
            color: var(--text-dim);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        .stat-value {{
            font-family: var(--font-heading);
            font-size: 48px;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 6px;
            letter-spacing: -0.04em;
            line-height: 1;
            background: linear-gradient(135deg, var(--text-main) 0%, var(--text-dim) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .stat-change {{
            font-size: 12px;
            font-weight: 500;
            color: #10b981;
            letter-spacing: 0.02em;
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        /* Content Sections */
        .section {{
            background: var(--bg-secondary);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius);
            padding: 28px;
            margin-bottom: 24px;
            box-shadow: var(--card-shadow);
            transition: all var(--transition-speed);
        }}

        .section-title {{
            font-family: var(--font-heading);
            font-size: 24px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 20px;
            letter-spacing: -0.02em;
        }}

        /* Theme Gallery */
        .theme-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 24px;
            margin-top: 20px;
        }}

        .theme-card {{
            background: var(--bg-secondary);
            border: 2px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .theme-card:hover {{
            transform: translateY(-8px);
            border-color: var(--accent-primary);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        }}

        .theme-card.active {{
            border-color: var(--accent-primary);
            background: rgba(99, 102, 241, 0.1);
            box-shadow: 0 0 0 2px var(--accent-primary);
        }}

        .theme-preview {{
            width: 100%;
            height: 100px;
            border-radius: 10px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-heading);
            font-size: 32px;
            color: white;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.2);
        }}

        .theme-name {{
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 16px;
            color: #fff;
            margin-bottom: 4px;
        }}

        .theme-desc {{
            font-size: 12px;
            color: var(--text-dim);
            line-height: 1.4;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 8px;
        }}

        th {{
            background: rgba(45, 55, 72, 0.4);
            padding: 16px 20px;
            text-align: left;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            color: #94a3b8;
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        th:first-child {{
            border-top-left-radius: 12px;
        }}

        th:last-child {{
            border-top-right-radius: 12px;
        }}

        td {{
            padding: 16px 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            color: #cbd5e1;
            font-size: 14px;
            transition: all 0.2s;
        }}

        tr {{
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        tr:hover td {{
            background: rgba(255, 255, 255, 0.03);
            color: #fff;
        }}

        tr:last-child td:first-child {{
            border-bottom-left-radius: 12px;
        }}

        tr:last-child td:last-child {{
            border-bottom-right-radius: 12px;
        }}

        .skill-link {{
            color: #6366f1;
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            letter-spacing: -0.01em;
            position: relative;
            display: inline-block;
            transition: all 0.3s ease;
        }}

        .skill-link::after {{
            content: '';
            position: absolute;
            width: 100%;
            height: 2px;
            bottom: -2px;
            left: 0;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.3s ease;
        }}

        .skill-link:hover {{
            color: #a78bfa;
            transform: translateY(-1px);
        }}

        .skill-link:hover::after {{
            transform: scaleX(1);
            transform-origin: left;
        }}

        .tag-badge {{
            display: inline-block;
            padding: 6px 16px;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: #fff;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 6px;
            cursor: pointer;
            letter-spacing: 0.02em;
            text-transform: uppercase;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .tag-badge::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s ease;
        }}

        .tag-badge:hover::before {{
            left: 100%;
        }}

        .tag-badge:hover {{
            background: linear-gradient(135deg, #818cf8 0%, #a78bfa 100%);
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
            padding: 6px 18px;
        }}

        /* Network Container */
        #networkContainer {{
            width: 100%;
            height: 500px;
            background: rgba(26, 31, 54, 0.5);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        /* View switching */
        .view {{
            display: none;
            animation: fadeIn 0.4s ease-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .view.active {{
            display: block;
        }}

        /* Detail Modal */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(10, 14, 28, 0.8);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .modal.active {{
            display: flex;
        }}

        .modal-content {{
            background: rgba(30, 37, 64, 0.9);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 40px;
            max-width: 800px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
            position: relative;
        }}

        .modal-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 24px;
            letter-spacing: -0.03em;
            line-height: 1.2;
            background: linear-gradient(135deg, #fff 0%, #a78bfa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .modal-section {{
            margin-bottom: 32px;
        }}

        .modal-label {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 10px;
            font-weight: 800;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 12px;
        }}

        .modal-text {{
            color: #cbd5e1;
            line-height: 1.8;
            font-size: 15px;
        }}

        .close-btn {{
            position: absolute;
            top: 24px;
            right: 24px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }}

        .close-btn:hover {{
            background: rgba(239, 68, 68, 0.2);
            border-color: rgba(239, 68, 68, 0.3);
            transform: rotate(90deg);
        }}

        /* Conflict Cards UX */
        .conflict-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 24px;
        }}

        .conflict-card {{
            background: rgba(30, 37, 64, 0.4);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 24px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .conflict-card:hover {{
            border-color: var(--accent-secondary);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
        }}

        .conflict-vs {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            margin-bottom: 24px;
        }}

        .vs-item {{
            flex: 1;
            text-align: center;
            padding: 12px;
            background: rgba(15, 23, 42, 0.5);
            border-radius: 12px;
            font-weight: 700;
            font-size: 14px;
            color: #fff;
            border: 1px solid var(--border-color);
        }}

        .vs-divider {{
            color: var(--accent-primary);
            font-weight: 900;
            font-style: italic;
            font-size: 12px;
        }}

        .conflict-instruction {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            font-size: 12px;
            margin-top: 16px;
        }}

        .instruction-box {{
            padding: 12px;
            background: rgba(255,255,255,0.02);
            border-radius: 10px;
        }}

        .instruction-title {{
            color: var(--accent-primary);
            font-weight: 800;
            margin-bottom: 6px;
            text-transform: uppercase;
            font-size: 10px;
            letter-spacing: 0.05em;
        }}

        .resolution-meta {{
            margin-top: 20px;
            padding-top: 16px;
            border-top: 1px solid var(--border-color);
            font-size: 11px;
            color: var(--text-dim);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .resolution-value {{
            color: var(--text-main);
            margin-left: 8px;
        }}

        .star-btn {{
            cursor: pointer;
            color: var(--text-dim);
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-right: 8px;
        }}

        .star-btn:hover {{
            transform: scale(1.2);
            color: #f59e0b;
        }}

        .star-btn.active {{
            color: #f59e0b;
        }}

        /* Solver Styles */
        .solver-container {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}

        .solver-input-group {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 32px;
        }}

        .solver-textarea {{
            width: 100%;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            color: var(--text-main);
            font-family: inherit;
            font-size: 15px;
            resize: vertical;
            min-height: 120px;
            margin-bottom: 16px;
            outline: none;
        }}

        .solver-textarea:focus {{
            border-color: var(--accent-primary);
        }}

        .solver-btn {{
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: #fff;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            font-family: 'Space Grotesk', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-size: 13px;
        }}

        .solver-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.3);
        }}

        /* Command Suggestions */
        .command-suggestions {{
            position: absolute;
            top: 100%;
            left: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            margin-top: 8px;
            z-index: 1000;
            display: none;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            overflow: hidden;
        }}

        .command-item {{
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: background 0.2s;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        .command-item:hover {{
            background: rgba(99, 102, 241, 0.2);
        }}

        .command-item:last-child {{
            border-bottom: none;
        }}

        .command-key {{
            background: rgba(99, 102, 241, 0.2);
            color: var(--accent-primary);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 12px;
            font-weight: 700;
        }}

        .command-desc {{
            font-size: 13px;
            color: var(--text-dim);
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: #1a1f36;
        }}

        ::-webkit-scrollbar-thumb {{
            background: #475569;
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: #64748b;
        }}

        /* Responsive */
        @media (max-width: 1024px) {{
            .sidebar {{
                width: 240px;
            }}
            .main-content {{
                margin-left: 240px;
            }}
        }}

        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                position: relative;
                height: auto;
            }}
            .main-content {{
                margin-left: 0;
            }}
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            .conflict-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-brand">Expertise OS</div>
            <div class="sidebar-tagline">{total_skills} skills • {total_books} books</div>
        </div>

        <div class="nav-section">
            <div class="nav-header">Workspace</div>
            <div class="nav-item active" onclick="showView('dashboard', 'Workspace')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                </svg>
                📊 Dashboard
            </div>
            <div class="nav-item" onclick="showView('health', 'System Health')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
                🛡️ OS Health
            </div>
            <div class="nav-item" onclick="showView('favorites', 'My Library')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.175 0l-3.976 2.888c-.783.57-1.838-.197-1.539-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.382-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
                </svg>
                ⭐ Favorites
            </div>
            <div class="nav-item" onclick="showView('themes', 'Visual Interface')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                </svg>
                🎨 Themes
            </div>
            <div class="nav-item" onclick="showView('network', 'Analytics')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
                🕸️ Network View
            </div>
        </div>

        <div class="nav-section">
            <div class="nav-header">Insights</div>
            <div class="nav-item" onclick="showView('solver', 'Expertise AI')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                </svg>
                🤖 Situation Solver
            </div>
            <div class="nav-item" onclick="showView('conflicts', 'Guidance')">
                <svg class="nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                💡 Conflict Guide
            </div>
        </div>
    </div>

    <!-- Progress Bar -->
    <div id="progress-container">
        <div id="progress-bar"></div>
    </div>

    <!-- Main Content -->
    <div class="main-content" id="mainContent">
        <div class="content-header">
            <div>
                <div class="breadcrumb">
                    <span>Expertise OS</span> / <span id="breadcrumb-active" class="active-crumb">Dashboard</span>
                </div>
                <h1 class="header-title" id="pageTitle">📊 Dashboard</h1>
                <p class="header-subtitle" id="pageSubtitle">Overview of your skills library</p>
            </div>
            <div style="position: relative; flex: 1; max-width: 400px;">
                <svg style="position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 16px; height: 16px; color: var(--text-dim);" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
                <input type="text" class="search-box" id="globalSearch" placeholder="Search (Cmd+K) or type '/' for commands..." onkeyup="globalSearchHandler()" style="padding-left: 42px; width: 100%;">
                <div id="commandSuggestions" class="command-suggestions"></div>
            </div>
        </div>

        <!-- Dashboard View -->
        <div id="dashboardView" class="view active">
            <div class="stats-grid">
                <div class="stat-card" onclick="showView('skills', 'Knowledge Base')" style="cursor: pointer;">
                    <div class="stat-label">📚 Total Skills</div>
                    <div class="stat-value">{total_skills}</div>
                    <div class="stat-change">✨ Actionable intelligence</div>
                </div>
                <div class="stat-card" onclick="showView('categories', 'Taxonomy')" style="cursor: pointer;">
                    <div class="stat-label">🏷️ Categories</div>
                    <div class="stat-value">{total_tags}</div>
                    <div class="stat-change">📌 Core domains</div>
                </div>
                <div class="stat-card" onclick="showView('multitag', 'Research')" style="cursor: pointer;">
                    <div class="stat-label">🔗 Interdisciplinary</div>
                    <div class="stat-value">{multi_tag}</div>
                    <div class="stat-change">🎯 Cross-domain leverage</div>
                </div>
                <div class="stat-card" onclick="showView('overlaps', 'Library')" style="cursor: pointer;">
                    <div class="stat-label">🔄 Source Overlaps</div>
                    <div class="stat-value">{overlaps}</div>
                    <div class="stat-change">📖 Multi-source validation</div>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px; margin-bottom: 24px;">
                <div class="section" style="margin-bottom: 0;">
                    <h2 class="section-title">📈 Category Distribution</h2>
                    <div id="categoryChart" class="chart-wrapper"></div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 24px;">
                    <div class="section" style="margin-bottom: 0; flex: 1;">
                        <h2 class="section-title">✨ Daily Focus</h2>
                        <p style="font-size: 11px; color: var(--text-dim); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.05em;">Skills to practice today</p>
                        <div id="dailyFocusContainer" style="display: flex; flex-direction: column; gap: 10px;">
                            <!-- Dynamic Focus Skills -->
                        </div>
                    </div>
                    <div class="section" style="margin-bottom: 0;">
                        <h2 class="section-title">⚡ Quick Access</h2>
                        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 16px;">
                            <button class="nav-item" style="border: 1px solid var(--border-color); border-radius: 12px; width: 100%; background: rgba(255,255,255,0.03);" onclick="showView('conflicts', 'Guidance')">Resolve Mental Conflicts</button>
                            <button class="nav-item" style="border: 1px solid var(--border-color); border-radius: 12px; width: 100%; background: rgba(255,255,255,0.03);" onclick="showSkill('Growth Mindset')">Explore: Growth Mindset</button>
                            <button class="nav-item" style="border: 1px solid var(--border-color); border-radius: 12px; width: 100%; background: rgba(255,255,255,0.03);" onclick="showView('network', 'Analytics')">Knowledge Clusters</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">🔥 High-Leverage Skills</h2>
                <table id="topSkillsTable">
                    <thead>
                        <tr>
                            <th>Skill Name</th>
                            <th>Categories</th>
                            <th>Books</th>
                        </tr>
                    </thead>
                    <tbody id="topSkillsBody">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Health View -->
        <div id="healthView" class="view">
            <div class="section">
                <h2 class="section-title">🛡️ Knowledge Linter (OS Health)</h2>
                <p style="color: var(--text-dim); margin-bottom: 24px;">Deterministic audit of your expertise graph. Identifying orphaned nodes, weak links, and data gaps.</p>
                
                <div class="stats-grid" id="healthStatsGrid">
                    <!-- Dynamic Health Stats -->
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
                    <div class="section" style="background: rgba(239, 68, 68, 0.05); border-color: rgba(239, 68, 68, 0.2);">
                        <h3 class="modal-label" style="color: #ef4444;">🚫 Orphaned Nodes</h3>
                        <p style="font-size: 12px; color: var(--text-dim); margin-bottom: 16px;">Skills with zero taxonomy tags. These lack context in the graph.</p>
                        <div id="orphanedList" style="max-height: 300px; overflow-y: auto;"></div>
                    </div>
                    <div class="section" style="background: rgba(245, 158, 11, 0.05); border-color: rgba(245, 158, 11, 0.2);">
                        <h3 class="modal-label" style="color: #f59e0b;">⚠️ Low Validation</h3>
                        <p style="font-size: 12px; color: var(--text-dim); margin-bottom: 16px;">Skills validated by only one source. Consider seeking cross-confirmation.</p>
                        <div id="weakLinksList" style="max-height: 300px; overflow-y: auto;"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Themes View -->
        <div id="themesView" class="view">
            <div class="section">
                <h2 class="section-title">🎨 Visual Interface Skins</h2>
                <p style="color: var(--text-dim); margin-bottom: 24px;">Transform the Expertise OS aesthetic with curated design templates.</p>
                
                <div class="theme-grid">
                    <div class="theme-card active" onclick="setTheme('modern', this)">
                        <div class="theme-preview" style="background: #0f172a; color: #6366f1;">✨</div>
                        <div class="theme-name">Modern Dark</div>
                        <div class="theme-desc">The original high-end SaaS aesthetic. Deep navy with purple accents.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('editorial', this)">
                        <div class="theme-preview" style="background: #121212; color: #c5a059; font-family: serif;">Aa</div>
                        <div class="theme-name">Editorial</div>
                        <div class="theme-desc">Sophisticated dark mode with high-contrast serif typography.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('vellum', this)">
                        <div class="theme-preview" style="background: #f5f2e6; color: #5c4033; font-family: serif;">📜</div>
                        <div class="theme-name">Vellum</div>
                        <div class="theme-desc">Light, parchment-like interface with classical classical typography.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('pixel', this)">
                        <div class="theme-preview" style="background: #e0e0e0; color: #008080; font-family: monospace;">[_]</div>
                        <div class="theme-name">Pixel</div>
                        <div class="theme-desc">Retro 90s tech vibe with "Bondi Blue" iMac-inspired accents.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('dossier', this)">
                        <div class="theme-preview" style="background: #d4ccc5; color: #3d3d3d; font-family: monospace;">📠</div>
                        <div class="theme-name">Dossier</div>
                        <div class="theme-desc">Vintage typewriter aesthetic with earth tones and rigid structure.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('etching', this)">
                        <div class="theme-preview" style="background: #fafafa; color: #000; font-family: serif;">✒️</div>
                        <div class="theme-name">Etching</div>
                        <div class="theme-desc">Clean, minimalist light mode with sketch-like fine-line strokes.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('whiteboard', this)">
                        <div class="theme-preview" style="background: #fff; color: #3b82f6;">🖍️</div>
                        <div class="theme-name">Whiteboard</div>
                        <div class="theme-desc">Ultra-clean light mode with marker-drawn accents and casual feel.</div>
                    </div>
                    <div class="theme-card" onclick="setTheme('sketch', this)">
                        <div class="theme-preview" style="background: #fff; color: #000; font-family: cursive;">✏️</div>
                        <div class="theme-name">Sketch</div>
                        <div class="theme-desc">High-contrast black & white with hand-drawn charcoal aesthetics.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Favorites View -->
        <div id="favoritesView" class="view">
            <div class="section">
                <h2 class="section-title">⭐ My Favorite Skills</h2>
                <p style="color: var(--text-dim); margin-bottom: 24px;">Your hand-picked collection of high-impact skills.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Skill Name</th>
                                <th>Categories</th>
                                <th>Sources</th>
                            </tr>
                        </thead>
                        <tbody id="favoritesBody">
                            <!-- Dynamic Favorites -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Solver View -->
        <div id="solverView" class="view">
            <div class="solver-container">
                <div class="solver-input-group">
                    <h2 class="section-title">🤖 Situation Solver</h2>
                    <p style="color: var(--text-dim); margin-bottom: 20px;">Describe your situation, problem, or goal, and the OS will surface relevant skills from your library.</p>
                    <textarea class="solver-textarea" id="situationInput" placeholder="e.g., I'm feeling overwhelmed by too many projects and I'm losing focus..."></textarea>
                    <button class="solver-btn" onclick="solveSituation()">Surface Relevant Skills</button>
                </div>

                <div class="section" id="solverResultsSection" style="display: none;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                        <h2 class="section-title" style="margin-bottom: 0;">✨ Recommended Skills</h2>
                        <div style="display: flex; gap: 12px;">
                            <button class="solver-btn" style="background: #10a37f;" onclick="openSolverInAI('chatgpt')">Synthesize in ChatGPT</button>
                            <button class="solver-btn" style="background: var(--accent-primary);" onclick="openSolverInAI('claude')">Deconstruct in Claude</button>
                        </div>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Skill Name</th>
                                    <th>Match Relevance</th>
                                    <th>Categories</th>
                                </tr>
                            </thead>
                            <tbody id="solverResultsBody">
                                <!-- Dynamic Results -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Network View -->
        <div id="networkView" class="view">
            <div class="section">
                <h2 class="section-title">🕸️ Network Visualization</h2>
                <div id="networkContainer"></div>
            </div>
        </div>

        <!-- All Skills View -->
        <div id="skillsView" class="view">
            <div class="section">
                <h2 class="section-title">📚 All Skills</h2>
                <input type="text" class="search-box" id="skillsSearch" placeholder="Filter skills..." style="width: 100%; margin-bottom: 16px;" onkeyup="renderSkills(this.value)">
                <table id="skillsTable">
                    <thead>
                        <tr>
                            <th>Skill Name</th>
                            <th>Categories</th>
                            <th>Books</th>
                        </tr>
                    </thead>
                    <tbody id="skillsBody">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Categories View -->
        <div id="categoriesView" class="view">
            <div class="section">
                <h2 class="section-title">🏷️ By Category</h2>
                <table id="categoriesTable">
                    <thead>
                        <tr>
                            <th>Category</th>
                            <th>Skills</th>
                            <th>Sample Skills</th>
                        </tr>
                    </thead>
                    <tbody id="categoriesBody">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Overlaps View -->
        <div id="overlapsView" class="view">
            <div class="section">
                <h2 class="section-title">🔄 Overlapping Skills</h2>
                <table id="overlapsTable">
                    <thead>
                        <tr>
                            <th>Skill Name</th>
                            <th>Source Books</th>
                            <th>Categories</th>
                        </tr>
                    </thead>
                    <tbody id="overlapsBody">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Conflicts View -->
        <div id="conflictsView" class="view">
            <div class="section">
                <h2 class="section-title">💡 Conflict Resolution Guide</h2>
                <p style="color: var(--text-dim); margin-bottom: 24px;">Decision frameworks for resolving collisions between powerful but seemingly opposite mental models.</p>
                
                <div class="conflict-grid" id="conflictContainer">
                    <!-- Dynamic Conflict Cards -->
                </div>

                <h3 style="margin-top: 40px; color: var(--text-main); font-family: var(--font-heading);">🛠️ Decision Framework</h3>
                <div style="background: var(--bg-card); backdrop-filter: blur(8px); padding: 32px; border-radius: 16px; margin: 24px 0; border: 1px solid var(--border-color); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <ol style="color: var(--text-main); line-height: 2; padding-left: 24px;">
                        <li><strong style="color: var(--accent-primary);">Assess context</strong>: What type of problem? (Kind/Wicked)</li>
                        <li><strong style="color: var(--accent-primary);">Check domain</strong>: Is this in my Circle of Competence?</li>
                        <li><strong style="color: var(--accent-primary);">Evaluate match quality</strong>: Am I in the right area?</li>
                        <li><strong style="color: var(--accent-primary);">Consider timing</strong>: Early exploration vs. late execution?</li>
                        <li><strong style="color: var(--accent-primary);">Apply appropriate model</strong>: Use conflict resolution above</li>
                    </ol>
                </div>
            </div>
        </div>

        <!-- Multi-Tag Skills View -->
        <div id="multitagView" class="view">
            <div class="section">
                <h2 class="section-title">🔗 Multi-Disciplinary Skills ({multi_tag})</h2>
                <p style="color: #94a3b8; margin-bottom: 20px;">Skills that span multiple categories, showing interdisciplinary connections.</p>
                <table>
                    <thead>
                        <tr>
                            <th>Skill Name</th>
                            <th>Tags</th>
                        </tr>
                    </thead>
                    <tbody id="multitagBody">
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Skill Detail Modal -->
    <div id="skillModal" class="modal">
        <div class="modal-content" style="position: relative;">
            <button class="close-btn" onclick="closeModal()">&times;</button>
            <h2 class="modal-title" id="modalTitle">Skill Name</h2>
            <div class="modal-section">
                <div class="modal-label">Description</div>
                <div class="modal-text" id="modalDescription">Description here...</div>
            </div>
            <div class="modal-section">
                <div class="modal-label">Action Center</div>
                <div id="modalAIButtons" style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <!-- Dynamic Buttons -->
                </div>
            </div>
            <div class="modal-section">
                <div class="modal-label">Taxonomy Tags</div>
                <div id="modalTags" style="margin-bottom: 8px;"></div>
            </div>
            <div class="modal-section">
                <div class="modal-label">Evidence Timeline (Sources)</div>
                <div class="modal-text" id="modalBooks"></div>
            </div>
            <div class="modal-section">
                <div class="modal-label">Synergy Hub (Cross-Source)</div>
                <div id="modalSynergy" style="display: flex; flex-wrap: wrap; gap: 8px;"></div>
            </div>
            <div class="modal-section">
                <div class="modal-label">Related Skills</div>
                <div id="modalRelated"></div>
            </div>
        </div>
    </div>

    <script>
        // Data
        const skillsData = {json.dumps(data, indent=2)};

        // Color Palette for Categories
        const categoryColors = {{
            'thinking': '#6366f1',      // Indigo
            'strategy': '#8b5cf6',      // Violet
            'finance': '#10b981',       // Emerald
            'productivity': '#f59e0b',  // Amber
            'self-improvement': '#ec4899', // Pink
            'focus': '#3b82f6',         // Blue
            'psychology': '#f43f5e',    // Rose
            'general': '#94a3b8'        // Slate
        }};

        function getTagColor(tag) {{
            return categoryColors[tag.toLowerCase()] || '#6366f1';
        }}

        // Robust Skill Info Map Construction
        const skillInfoMap = {{}};

        // Utility to ensure a skill is initialized
        function initSkill(skill) {{
            if (!skillInfoMap[skill]) {{
                skillInfoMap[skill] = {{ 
                    tags: [], 
                    books: [], 
                    description: (skillsData.descriptions && skillsData.descriptions[skill]) || null 
                }};
            }}
        }}

        // 1. Process all_skills
        skillsData.all_skills.forEach(initSkill);

        // 2. Process skills_by_tag
        Object.entries(skillsData.skills_by_tag).forEach(([tag, skills]) => {{
            skills.forEach(([skill, book]) => {{
                initSkill(skill);
                if (!skillInfoMap[skill].tags.includes(tag)) skillInfoMap[skill].tags.push(tag);
                if (!skillInfoMap[skill].books.includes(book)) skillInfoMap[skill].books.push(book);
            }});
        }});

        // 3. Process overlaps dictionary
        if (skillsData.overlaps) {{
            Object.entries(skillsData.overlaps).forEach(([skill, books]) => {{
                initSkill(skill);
                books.forEach(book => {{
                    if (!skillInfoMap[skill].books.includes(book)) skillInfoMap[skill].books.push(book);
                }});
            }});
        }}

        // 4. Process multi_tag_skills
        if (skillsData.multi_tag_skills) {{
            Object.entries(skillsData.multi_tag_skills).forEach(([skill, tags]) => {{
                initSkill(skill);
                tags.forEach(tag => {{
                    if (!skillInfoMap[skill].tags.includes(tag)) skillInfoMap[skill].tags.push(tag);
                }});
            }});
        }}

        // Theme Engine
        let currentTheme = localStorage.getItem('expertise_theme') || 'modern';

        function setTheme(themeName, el = null) {{
            // Remove all theme classes
            document.body.classList.remove('theme-modern', 'theme-editorial', 'theme-vellum', 'theme-pixel', 'theme-dossier', 'theme-etching', 'theme-whiteboard', 'theme-sketch');
            
            // Add new theme class
            if (themeName !== 'modern') {{
                document.body.classList.add(`theme-${{themeName}}`);
            }}
            
            currentTheme = themeName;
            localStorage.setItem('expertise_theme', themeName);
            
            // Update UI cards if in themes view
            if (el) {{
                document.querySelectorAll('.theme-card').forEach(c => c.classList.remove('active'));
                el.classList.add('active');
            }}
            
            // Re-draw D3 components as they might need to adapt to new colors
            setTimeout(() => {{
                if (document.getElementById('dashboardView').classList.contains('active')) drawCategoryChart();
                if (document.getElementById('networkView').classList.contains('active')) drawNetwork();
            }}, 100);
        }}

        // Initialize Theme on load
        function initTheme() {{
            if (currentTheme !== 'modern') {{
                document.body.classList.add(`theme-${{currentTheme}}`);
            }}
            // Mark active card in gallery if visible
            const cards = document.querySelectorAll('.theme-card');
            cards.forEach(card => {{
                if (card.getAttribute('onclick').includes(`'${{currentTheme}}'`)) {{
                    card.classList.add('active');
                }} else {{
                    card.classList.remove('active');
                }}
            }});
        }}

        // Slash Command Registry
        const slashCommands = [
            {{ key: '/lint', desc: 'Audit knowledge graph integrity', view: 'health' }},
            {{ key: '/fav', desc: 'View starred favorites', view: 'favorites' }},
            {{ key: '/themes', desc: 'Visual Interface Skins', view: 'themes' }},
            {{ key: '/graph', desc: 'Interactive node visualization', view: 'network' }},
            {{ key: '/solve', desc: 'Situation Solver (Expertise AI)', view: 'solver' }},
            {{ key: '/conflicts', desc: 'Conflict resolution guide', view: 'conflicts' }},
            {{ key: '/all', desc: 'Full skills database', view: 'skills' }}
        ];

        // Favorites Logic
        let favorites = JSON.parse(localStorage.getItem('expertise_favorites') || '[]');

        function toggleFavorite(skill) {{
            if (favorites.includes(skill)) {{
                favorites = favorites.filter(f => f !== skill);
            }} else {{
                favorites.push(skill);
            }}
            localStorage.setItem('expertise_favorites', JSON.stringify(favorites));
            
            // Re-render all data-driven components to keep UI in sync
            const query = document.getElementById('globalSearch').value;
            renderTopSkills(query);
            renderSkills(query);
            renderFavorites();
            renderOverlaps();
            
            // Special case for solver if active
            const solverResults = document.getElementById('solverResultsBody');
            if (solverResults && solverResults.children.length > 0) {{
                // This is a bit heavy but ensures the star updates
                const input = document.getElementById('situationInput').value;
                if (input) solveSituation();
            }}
        }}

        function isFavorite(skill) {{
            return favorites.includes(skill);
        }}

        function renderFavorites() {{
            const tbody = document.getElementById('favoritesBody');
            if (!tbody) return;

            if (favorites.length === 0) {{
                tbody.innerHTML = '<tr><td colspan="3" style="text-align: center; color: var(--text-dim); padding: 40px;">No favorites yet. Star some skills to build your library!</td></tr>';
                return;
            }}

            tbody.innerHTML = favorites.map(skill => {{
                const info = skillInfoMap[skill];
                if (!info) return '';
                return `
                    <tr>
                        <td>${{renderSkillNameWithStar(skill)}}</td>
                        <td>${{renderTagBadges(info.tags)}}</td>
                        <td>${{renderSourceLinks(info.books)}}</td>
                    </tr>
                `;
            }}).join('');
        }}

        // Situation Solver Logic
        function solveSituation() {{
            const input = document.getElementById('situationInput').value.toLowerCase();
            if (!input.trim()) return;

            const results = [];
            const keywords = input.split(/[\\s,.]+/).filter(w => w.length > 3);

            skillsData.all_skills.forEach(skill => {{
                const info = skillInfoMap[skill];
                let score = 0;
                
                // Score based on skill name
                if (skill.toLowerCase().split(' ').some(w => keywords.includes(w))) score += 5;
                
                // Score based on tags
                info.tags.forEach(tag => {{
                    if (input.includes(tag.toLowerCase())) score += 10;
                }});
                
                // Score based on description
                if (info.description) {{
                    const descWords = info.description.toLowerCase().split(/[\\s,.]+/);
                    keywords.forEach(word => {{
                        if (descWords.includes(word)) score += 2;
                    }});
                }}

                if (score > 0) {{
                    results.push({{ skill, score, tags: info.tags }});
                }}
            }});

            results.sort((a, b) => b.score - a.score);

            const resultsSection = document.getElementById('solverResultsSection');
            const tbody = document.getElementById('solverResultsBody');
            
            resultsSection.style.display = 'block';
            
            if (results.length === 0) {{
                tbody.innerHTML = '<tr><td colspan="3" style="text-align: center; color: var(--text-dim); padding: 40px;">No specific matches found. Try describing your situation with different keywords.</td></tr>';
            }} else {{
                tbody.innerHTML = results.slice(0, 10).map(r => `
                    <tr>
                        <td>${{renderSkillNameWithStar(r.skill)}}</td>
                        <td style="font-weight: 700; color: var(--accent-primary);">${{r.score > 20 ? 'High' : r.score > 10 ? 'Medium' : 'Low'}} Match</td>
                        <td>${{renderTagBadges(r.tags)}}</td>
                    </tr>
                `).join('');
            }}
            
            // Scroll to results
            resultsSection.scrollIntoView({{ behavior: 'smooth' }});
        }}

        // Helper for skill link with star
        function renderSkillNameWithStar(skill) {{
            const activeClass = isFavorite(skill) ? 'active' : '';
            return `<span class="star-btn ${{activeClass}}" onclick="toggleFavorite('${{skill}}')">★</span>
                    <a class="skill-link" onclick="showSkill('${{skill}}')">${{skill}}</a>`;
        }}

        // Update render functions to use the star helper
        // (I will update renderTopSkills and renderSkills in a moment)
        // Filter by Tag
        function filterByTag(tag) {{
            const searchBox = document.getElementById('globalSearch');
            searchBox.value = tag;
            showView('skills', 'Knowledge Base');
            renderSkills(tag.toLowerCase());
        }}

        // Source Deep Dive Logic
        function filterBySource(sourceName) {{
            const searchBox = document.getElementById('globalSearch');
            searchBox.value = sourceName;
            showView('skills', 'Library Deep Dive');
            renderSkills(sourceName.toLowerCase());
        }}

        function renderSourceLinks(sources) {{
            return sources.map(source => {{
                const cleanSource = source.replace(/\\\\\\[\\[|\\\\\\]\\\\\\]/g, '');
                return `<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                            <a class="skill-link" style="font-size: 13px;" onclick="event.stopPropagation(); filterBySource('${{cleanSource}}')">${{cleanSource}}</a>
                            <a href="https://www.goodreads.com/search/search?q=${{encodeURIComponent(cleanSource)}}" target="_blank" title="View on Goodreads" style="opacity: 0.5; text-decoration: none;">📚</a>
                            <a href="https://www.amazon.com/s?k=${{encodeURIComponent(cleanSource)}}&tag=YOUR_TAG_HERE" target="_blank" title="View on Amazon" style="opacity: 0.5; text-decoration: none;">🛒</a>
                        </div>`;
            }}).join('');
        }}

        // Helper to render tag badges
        function renderTagBadges(tags) {{
            return tags.map(tag => {{
                const color = getTagColor(tag);
                return `<span class="tag-badge" 
                              style="background: ${{color}}15; border-color: ${{color}}40; color: ${{color}};" 
                              onclick="event.stopPropagation(); filterByTag('${{tag}}')">${{tag}}</span>`;
            }}).join('');
        }}

        // Daily Focus Logic (Deterministic Randomizer)
        function renderDailyFocus() {{
            const container = document.getElementById('dailyFocusContainer');
            if (!container) return;

            // Use current date as seed for daily consistency
            const today = new Date().toISOString().split('T')[0];
            const seed = today.split('-').reduce((acc, val) => acc + parseInt(val), 0);
            
            // Filter high-leverage skills (multi-source or starred)
            const candidates = Object.keys(skillInfoMap).filter(s => 
                skillInfoMap[s].books.length > 1 || favorites.includes(s)
            );

            // Deterministic pick of 3 skills
            const daily = [];
            let currentSeed = seed;
            for (let i = 0; i < 3 && candidates.length > 0; i++) {{
                const index = currentSeed % candidates.length;
                daily.push(candidates.splice(index, 1)[0]);
                currentSeed = (currentSeed * 16807) % 2147483647; // Simple LCG
            }}

            container.innerHTML = daily.map(skill => `
                <div style="background: var(--bg-secondary); padding: 12px; border-radius: 10px; border-left: 3px solid var(--accent-primary); cursor: pointer;" onclick="showSkill('${{skill}}')">
                    <div style="font-size: 13px; font-weight: 600; color: var(--text-main);">${{skill}}</div>
                    <div style="font-size: 10px; color: var(--text-dim); margin-top: 4px;">${{skillInfoMap[skill].tags[0] || 'Uncategorized'}}</div>
                </div>
            `).join('');
        }}

        // Render top skills
        function renderTopSkills(filter = '') {{
            const tbody = document.getElementById('topSkillsBody');
            if (!tbody) return;

            const filteredSkills = skillsData.all_skills.filter(s => s.toLowerCase().includes(filter.toLowerCase()));
            const skills = filteredSkills.slice(0, 10);

            tbody.innerHTML = skills.map(skill => {{
                const info = skillInfoMap[skill];
                if (!info) return '';
                return `
                    <tr>
                        <td>${{renderSkillNameWithStar(skill)}}</td>
                        <td>${{renderTagBadges(info.tags.slice(0, 3))}} ${{info.tags.length > 3 ? `<span style="font-size: 10px; color: var(--text-dim);">+${{info.tags.length - 3}}</span>` : ''}}</td>
                        <td>
                            <div style="font-size: 12px; font-weight: 700; color: var(--accent-primary); margin-bottom: 4px;">${{info.books.length}} Sources</div>
                            ${{renderSourceLinks(info.books.slice(0, 2))}}
                            ${{info.books.length > 2 ? `<div style="font-size: 10px; color: var(--text-dim); margin-top: 4px;">+ ${{info.books.length - 2}} more sources</div>` : ''}}
                        </td>
                    </tr>
                `;
            }}).join('');
        }}

        // Render all skills
        function renderSkills(filter = '') {{
            const tbody = document.getElementById('skillsBody');
            if (!tbody) return;

            const filteredSkills = skillsData.all_skills.filter(skill => {{
                const info = skillInfoMap[skill];
                const searchStr = filter.toLowerCase();
                return skill.toLowerCase().includes(searchStr) || 
                       (info && info.tags.some(t => t.toLowerCase().includes(searchStr))) ||
                       (info && info.books.some(b => b.toLowerCase().includes(searchStr)));
            }});

            tbody.innerHTML = filteredSkills.map(skill => {{
                const info = skillInfoMap[skill];
                if (!info) return '';
                return `
                    <tr>
                        <td>${{renderSkillNameWithStar(skill)}}</td>
                        <td>${{renderTagBadges(info.tags)}}</td>
                        <td>${{renderSourceLinks(info.books)}}</td>
                    </tr>
                `;
            }}).join('');
        }}

        // GBrain Logic: Knowledge Linting & Semantic Merges
        function runLint() {{
            const orphans = [];
            const weakLinks = [];
            const mergeProposals = [];
            let totalDescriptions = 0;

            const allSkills = Object.keys(skillInfoMap);
            allSkills.forEach((skill, i) => {{
                const info = skillInfoMap[skill];
                if (info.tags.length === 0) orphans.push(skill);
                if (info.books.length === 1) weakLinks.push(skill);
                if (info.description) totalDescriptions++;

                // Simple semantic similarity check (Jaccard)
                for (let j = i + 1; j < allSkills.length; j++) {{
                    const other = allSkills[j];
                    const sim = getSimilarity(skill, other);
                    if (sim > 0.6) {{
                        mergeProposals.push({{ s1: skill, s2: other, sim: Math.round(sim * 100) }});
                    }}
                }}
            }});

            // Theme Accessibility Diagnostic
            const sidebar = document.querySelector('.sidebar');
            const diagnostics = [];

            if (sidebar) {{
                const sideBg = getComputedStyle(sidebar).backgroundColor;
                const sideText = getComputedStyle(document.querySelector('.nav-item')).color;
                const mainBg = getComputedStyle(document.body).backgroundColor;
                const mainText = getComputedStyle(document.body).color;

                const sideRatio = getContrastRatio(sideBg, sideText);
                const mainRatio = getContrastRatio(mainBg, mainText);

                if (sideRatio < 3) diagnostics.push(`Sidebar contrast critical (${{sideRatio.toFixed(2)}}:1)`);
                else if (sideRatio < 4.5) diagnostics.push(`Sidebar contrast low (${{sideRatio.toFixed(2)}}:1)`);
                
                if (mainRatio < 4.5) diagnostics.push(`Main content contrast low (${{mainRatio.toFixed(2)}}:1)`);
            }}

            const statsGrid = document.getElementById('healthStatsGrid');
            if (statsGrid) {{
                const completeness = Math.round((totalDescriptions / skillsData.all_skills.length) * 100);
                statsGrid.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-label">Graph Integrity</div>
                        <div class="stat-value">${{completeness}}%</div>
                        <div class="stat-change" style="color: ${{completeness > 80 ? '#10b981' : '#f59e0b'}};">${{totalDescriptions}} defined nodes</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Linter Warnings</div>
                        <div class="stat-value">${{orphans.length + weakLinks.length + diagnostics.length}}</div>
                        <div class="stat-change" style="color: #ef4444;">${{mergeProposals.length}} potential merges</div>
                    </div>
                `;
            }}

            const orphanedList = document.getElementById('orphanedList');
            if (orphanedList) {{
                let html = orphans.length > 0 
                    ? orphans.map(s => `<div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">${{renderSkillNameWithStar(s)}}</div>`).join('')
                    : '<div style="color: #10b981; font-size: 13px;">No orphaned nodes!</div>';
                
                if (diagnostics.length > 0) {{
                    html = `<div style="background: rgba(239, 68, 68, 0.1); padding: 12px; border-radius: 8px; margin-bottom: 16px; border: 1px solid #ef4444; color: #ef4444; font-size: 11px; font-weight: 700;">
                                🛑 ACCESSIBILITY DIAGNOSTICS:<br>
                                ${{diagnostics.join('<br>')}}
                            </div>` + html;
                }}
                orphanedList.innerHTML = html;
            }}

            document.getElementById('weakLinksList').innerHTML = mergeProposals.length > 0
                ? mergeProposals.slice(0, 15).map(m => `
                    <div style="padding: 12px; background: var(--bg-secondary); border-radius: 8px; margin-bottom: 8px; border-left: 3px solid var(--accent-primary);">
                        <div style="font-size: 11px; color: var(--text-dim); margin-bottom: 4px;">PROPOSED MERGE (${{m.sim}}% similarity)</div>
                        <div style="display: flex; flex-direction: column; gap: 4px;">
                            <span style="font-size: 13px; font-weight: 600; color: var(--text-main);">${{m.s1}}</span>
                            <span style="font-size: 11px; color: var(--text-dim);">+ ${{m.s2}}</span>
                        </div>
                    </div>
                `).join('')
                : '<div style="color: var(--text-dim); font-size: 13px;">No high-similarity clusters found.</div>';
        }}

        function getContrastRatio(rgb1, rgb2) {{
            const lum1 = getLuminance(rgb1);
            const lum2 = getLuminance(rgb2);
            const brightest = Math.max(lum1, lum2);
            const darkest = Math.min(lum1, lum2);
            return (brightest + 0.05) / (darkest + 0.05);
        }}

        function getLuminance(rgb) {{
            const parts = rgb.match(/\\d+/g);
            if (!parts) return 0;
            const [r, g, b] = parts.map(c => {{
                let v = c / 255;
                return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
            }});
            return 0.2126 * r + 0.7152 * g + 0.0722 * b;
        }}

        function getSimilarity(s1, s2) {{
            const set1 = new Set(s1.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\s+/));
            const set2 = new Set(s2.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\s+/));
            const intersection = new Set([...set1].filter(x => set2.has(x) && x.length > 2));
            return intersection.size / Math.max(set1.size, set2.size);
        }}

        // GBrain Logic: Traverse Node
        function traverseNode(skillName) {{
            const info = skillInfoMap[skillName];
            if (!info) return;
            
            closeModal();
            const searchBox = document.getElementById('globalSearch');
            // Traverse by finding all shared tags
            const primaryTag = info.tags[0] || '';
            searchBox.value = primaryTag;
            showView('skills', `Traversing: ${{skillName}}`);
            renderSkills(primaryTag.toLowerCase());
            
            // Highlight the origin skill in results
            setTimeout(() => {{
                const links = document.querySelectorAll('.skill-link');
                links.forEach(l => {{
                    if (l.textContent === skillName) {{
                        const row = l.closest('tr');
                        if (row) {{
                            row.style.background = 'rgba(99, 102, 241, 0.2)';
                            row.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                        }}
                    }}
                }});
            }}, 300);
        }}

        // View switching
        function showView(viewName, context = 'Workspace') {{
            document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
            const targetView = document.getElementById(viewName + 'View');
            if (targetView) targetView.classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            const navItems = document.querySelectorAll('.nav-item');
            navItems.forEach(item => {{
                const onclick = item.getAttribute('onclick');
                if (onclick && onclick.includes(`'${{viewName}}'`)) item.classList.add('active');
            }});

            const activeCrumb = document.getElementById('breadcrumb-active');
            if (activeCrumb) activeCrumb.textContent = context;
            
            const titles = {{
                'dashboard': '📊 Dashboard',
                'health': '🛡️ OS Health',
                'themes': '🎨 Interface Skins',
                'favorites': '⭐ Favorites',
                'network': '🕸️ Network View',
                'skills': '📚 All Skills',
                'categories': '🏷️ By Category',
                'overlaps': '🔄 Overlapping Skills',
                'multitag': '🔗 Multi-Tag Skills',
                'conflicts': '💡 Conflict Guide',
                'solver': '🤖 Situation Solver'
            }};
            
            const pageTitle = document.getElementById('pageTitle');
            if (pageTitle) pageTitle.textContent = titles[viewName] || 'Dashboard';

            if (viewName === 'network') setTimeout(drawNetwork, 100);
            if (viewName === 'dashboard') setTimeout(drawCategoryChart, 100);
            if (viewName === 'health') runLint();
            if (viewName === 'favorites') renderFavorites();
            if (viewName === 'skills' && context === 'Knowledge Base') renderSkills('');
            
            // Close command suggestions if open
            const sug = document.getElementById('commandSuggestions');
            if (sug) sug.style.display = 'none';

            window.scrollTo(0, 0);
        }}

        // Global search handler (Slash Commands & Hints)
        function globalSearchHandler() {{
            const input = document.getElementById('globalSearch');
            const sugContainer = document.getElementById('commandSuggestions');
            if (!input || !sugContainer) return;
            
            const query = input.value.toLowerCase().trim();
            
            // Show suggestions for slash
            if (query === '/') {{
                sugContainer.innerHTML = slashCommands.map(c => `
                    <div class="command-item" onclick="document.getElementById('globalSearch').value='${{c.key}}'; globalSearchHandler();">
                        <span class="command-key">${{c.key}}</span>
                        <span class="command-desc">${{c.desc}}</span>
                    </div>
                `).join('');
                sugContainer.style.display = 'block';
                return;
            }} else {{
                sugContainer.style.display = 'none';
            }}
            
            // Handle Commands
            if (query.startsWith('/')) {{
                const cmd = slashCommands.find(c => c.key === query);
                if (cmd) {{
                    showView(cmd.view, 'Command Line');
                    input.value = '';
                    return;
                }}
            }}

            if (query.length > 0) {{
                showView('skills', 'Search Results');
                renderSkills(query);
            }}
        }}

        // Render categories
        function renderCategories() {{
            const tbody = document.getElementById('categoriesBody');
            if (!tbody) return;
            const tags = Object.entries(skillsData.skills_by_tag).sort((a, b) => b[1].length - a[1].length);

            tbody.innerHTML = tags.map(([tag, skills]) => `
                <tr>
                    <td>${{renderTagBadges([tag])}}</td>
                    <td style="font-weight: 700;">${{skills.length}}</td>
                    <td style="font-size: 13px;">${{skills.slice(0, 3).map(s => `<a class="skill-link" onclick="showSkill('${{s[0]}}')" style="font-size: 13px;">${{s[0]}}</a>`).join(', ')}} ${{skills.length > 3 ? '...' : ''}}</td>
                </tr>
            `).join('');
        }}

        // Render overlaps
        function renderOverlaps() {{
            const tbody = document.getElementById('overlapsBody');
            if (!tbody) return;

            const overlappingSkills = Object.keys(skillInfoMap)
                .filter(s => skillInfoMap[s].books.length > 1)
                .sort((a, b) => skillInfoMap[b].books.length - skillInfoMap[a].books.length);

            tbody.innerHTML = overlappingSkills.map(skill => {{
                const info = skillInfoMap[skill];
                return `
                    <tr>
                        <td>${{renderSkillNameWithStar(skill)}}</td>
                        <td>${{renderSourceLinks(info.books)}}</td>
                        <td>${{renderTagBadges(info.tags)}}</td>
                    </tr>
                `;
            }}).join('');
        }}

        // Render multi-tag skills
        function renderMultitag() {{
            const tbody = document.getElementById('multitagBody');
            if (!tbody) return;

            tbody.innerHTML = Object.entries(skillsData.multi_tag_skills)
                .filter(([skill, tags]) => tags.length > 1)
                .map(([skill, tags]) => `
                    <tr>
                        <td>${{renderSkillNameWithStar(skill)}}</td>
                        <td>${{renderTagBadges(tags)}}</td>
                    </tr>
                `).join('');
        }}

        // Category Bar Chart (D3)
        function drawCategoryChart() {{
            const container = document.getElementById('categoryChart');
            if (!container) return;
            container.innerHTML = '';
            
            const rawData = Object.entries(skillsData.skills_by_tag)
                .map(([name, skills]) => ({{name, value: skills.length}}))
                .sort((a, b) => b.value - a.value)
                .slice(0, 10);

            const margin = {{top: 10, right: 30, bottom: 30, left: 140}};
            const width = container.offsetWidth - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;

            const svg = d3.select("#categoryChart").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", `translate(${{margin.left}},${{margin.top}})`);

            const x = d3.scaleLinear().domain([0, d3.max(rawData, d => d.value)]).range([0, width]);
            const y = d3.scaleBand().range([0, height]).domain(rawData.map(d => d.name)).padding(.2);

            svg.append("g")
                .call(d3.axisLeft(y).tickSize(0))
                .attr("color", "#94a3b8")
                .selectAll("text")
                .style("font-size", "11px")
                .style("font-weight", "600")
                .style("font-family", "'Space Grotesk', sans-serif");

            svg.selectAll(".bar")
                .data(rawData)
                .join("rect")
                .attr("x", x(0))
                .attr("y", d => y(d.name))
                .attr("width", d => x(d.value))
                .attr("height", y.bandwidth())
                .attr("fill", "url(#barGradient)")
                .attr("rx", 6);

            const lg = svg.append("defs").append("linearGradient").attr("id", "barGradient").attr("x1", "0%").attr("x2", "100%");
            lg.append("stop").attr("offset", "0%").attr("stop-color", "#6366f1");
            lg.append("stop").attr("offset", "100%").attr("stop-color", "#8b5cf6");
        }}

        // Show skill modal (GBrain Style: Compiled Truth vs Evidence)
        function showSkill(skillName) {{
            const info = skillInfoMap[skillName];
            if (!info) return;

            document.getElementById('modalTitle').textContent = skillName;
            
            // Compiled Truth
            document.getElementById('modalDescription').innerHTML = `
                <div style="background: var(--bg-secondary); padding: 20px; border-radius: 12px; border-left: 4px solid var(--accent-primary);">
                    <p style="color: var(--text-main); font-size: 16px; font-weight: 500;">${{info.description || 'Synthesis pending...'}}</p>
                </div>
            `;
            
            document.getElementById('modalTags').innerHTML = renderTagBadges(info.tags);
            
            // Evidence Timeline
            document.getElementById('modalBooks').innerHTML = `
                <div style="margin-top: 10px;">
                    ${{renderSourceLinks(info.books)}}
                </div>
            `;

            // Action Center
            const promptText = `Analyze skill: ${{skillName}}\\nContext: ${{info.description || 'N/A'}}\\nSources: ${{info.books.join(', ')}}`;
            const encodedPrompt = encodeURIComponent(promptText);
            
            const actionContainer = document.getElementById('modalAIButtons');
            if (actionContainer) {{
                actionContainer.innerHTML = `
                    <a href="https://chatgpt.com/?prompt=${{encodedPrompt}}" target="_blank" class="solver-btn" style="background: #10a37f; text-decoration: none; color: #fff;">GPT Synthesis</a>
                    <a href="https://claude.ai/new?prompt=${{encodedPrompt}}" target="_blank" class="solver-btn" style="background: var(--accent-primary); text-decoration: none; color: #fff;">Claude Logic</a>
                    <button class="solver-btn" style="background: var(--border-color); color: var(--text-main);" onclick="traverseNode('${{skillName}}')">Explore Cluster</button>
                `;
            }}

            // Synergy Hub (Cross-Source Complementaries)
            const synergyContainer = document.getElementById('modalSynergy');
            const synergists = Object.keys(skillInfoMap).filter(s => 
                s !== skillName && 
                skillInfoMap[s].tags.some(t => info.tags.includes(t)) && 
                !skillInfoMap[s].books.some(b => info.books.includes(b)) // Different sources
            ).slice(0, 8);

            if (synergyContainer) {{
                synergyContainer.innerHTML = synergists.length > 0
                    ? synergists.map(s => `<span class="tag-badge" style="cursor: pointer; background: rgba(99, 102, 241, 0.1); border-color: var(--accent-primary);" onclick="showSkill('${{s}}')">🔗 ${{s}}</span>`).join('')
                    : '<span style="color: var(--text-dim); font-size: 12px;">Seeking interdisciplinary links...</span>';
            }}

            // Related Nodes
            const relatedSkills = skillsData.all_skills
                .filter(s => s !== skillName && skillInfoMap[s] && skillInfoMap[s].tags.some(t => info.tags.includes(t)))
                .slice(0, 15);

            document.getElementById('modalRelated').innerHTML = relatedSkills.length > 0
                ? relatedSkills.map(s => `<span class="tag-badge" style="cursor: pointer; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);" onclick="showSkill('${{s}}')">${{s}}</span>`).join(' ')
                : '<span style="color: #94a3b8;">Standalone node.</span>';

            document.getElementById('skillModal').classList.add('active');
        }}

        function closeModal() {{
            document.getElementById('skillModal').classList.remove('active');
        }}

        // Network visualization with enhanced styling
        function drawNetwork() {{
            const container = document.getElementById('networkContainer');
            container.innerHTML = '';

            const width = container.offsetWidth;
            const height = 500;

            const tags = Object.entries(skillsData.skills_by_tag)
                .sort((a, b) => b[1].length - a[1].length);

            const nodes = tags.map(([tag, skills]) => ({{
                id: tag,
                value: skills.length,
                skills: skills.map(s => s[0])
            }}));

            const links = [];
            const skillToTags = {{}};

            tags.forEach(([tag, skills]) => {{
                skills.forEach(([skill, book]) => {{
                    if (!skillToTags[skill]) skillToTags[skill] = [];
                    skillToTags[skill].push(tag);
                }});
            }});

            Object.entries(skillToTags).forEach(([skill, tags]) => {{
                if (tags.length > 1) {{
                    for (let i = 0; i < tags.length; i++) {{
                        for (let j = i + 1; j < tags.length; j++) {{
                            links.push({{ source: tags[i], target: tags[j] }});
                        }}
                    }}
                }}
            }});

            // Enhanced color palette with transparency
            const colorScale = d3.scaleOrdinal()
                .domain(nodes.map(d => d.id))
                .range([
                    'rgba(99, 102, 241, 0.7)',   // Purple
                    'rgba(236, 72, 153, 0.7)',   // Pink
                    'rgba(59, 130, 246, 0.7)',   // Blue
                    'rgba(16, 185, 129, 0.7)',   // Green
                    'rgba(245, 158, 11, 0.7)',   // Orange
                    'rgba(139, 92, 246, 0.7)',   // Violet
                    'rgba(239, 68, 68, 0.7)',    // Red
                    'rgba(20, 184, 166, 0.7)',   // Teal
                    'rgba(249, 115, 22, 0.7)',   // Amber
                    'rgba(168, 85, 247, 0.7)',   // Purple
                    'rgba(34, 197, 94, 0.7)',    // Green
                    'rgba(6, 182, 212, 0.7)',    // Cyan
                    'rgba(234, 179, 8, 0.7)',    // Yellow
                    'rgba(244, 63, 94, 0.7)',    // Rose
                    'rgba(99, 102, 241, 0.7)'    // Indigo
                ]);

            const svg = d3.select("#networkContainer")
                .append("svg")
                .attr("width", width)
                .attr("height", height)
                .style("background", "linear-gradient(135deg, #1a1f36 0%, #2d3748 100%)")
                .style("border-radius", "8px");

            // Add gradient defs
            const defs = svg.append("defs");

            simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => d.id).distance(120))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(45));

            // Draw links with gradient
            const link = svg.append("g")
                .selectAll("line")
                .data(links)
                .join("line")
                .attr("stroke", "rgba(71, 85, 105, 0.3)")
                .attr("stroke-width", 1.5);

            // Create node groups
            const nodeGroups = svg.append("g")
                .selectAll("g")
                .data(nodes)
                .join("g")
                .attr("cursor", "pointer")
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));

            // Outer semi-transparent circles (main nodes)
            nodeGroups.append("circle")
                .attr("r", d => Math.sqrt(d.value) * 5)
                .attr("fill", d => colorScale(d.id))
                .attr("stroke", d => colorScale(d.id).replace('0.7', '1'))
                .attr("stroke-width", 2)
                .attr("opacity", 0.8);

            // Small transparent circles in the middle
            nodeGroups.append("circle")
                .attr("r", d => Math.sqrt(d.value) * 2.5)
                .attr("fill", d => colorScale(d.id).replace('0.7', '0.3'))
                .attr("stroke", "rgba(255, 255, 255, 0.5)")
                .attr("stroke-width", 1);

            // Inner center circle (most transparent)
            nodeGroups.append("circle")
                .attr("r", d => Math.sqrt(d.value) * 0.8)
                .attr("fill", "rgba(255, 255, 255, 0.2)")
                .attr("stroke", "rgba(255, 255, 255, 0.6)")
                .attr("stroke-width", 1.5);

            // Labels
            const label = svg.append("g")
                .selectAll("text")
                .data(nodes)
                .join("text")
                .text(d => d.id)
                .attr("font-size", "11px")
                .attr("font-weight", "500")
                .attr("text-anchor", "middle")
                .attr("fill", "#e2e8f0")
                .attr("dy", d => -Math.sqrt(d.value) * 5 - 8)
                .attr("text-shadow", "0 1px 3px rgba(0,0,0,0.5)");

            // Skill count badges
            const badges = svg.append("g")
                .selectAll("text")
                .data(nodes)
                .join("text")
                .text(d => d.value)
                .attr("font-size", "10px")
                .attr("font-weight", "700")
                .attr("text-anchor", "middle")
                .attr("fill", "#ffffff")
                .attr("dy", 4)
                .attr("text-shadow", "0 1px 2px rgba(0,0,0,0.8)");

            simulation.on("tick", () => {{
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                nodeGroups
                    .attr("transform", d => `translate(${{d.x}},${{d.y}})`);

                label
                    .attr("x", d => d.x)
                    .attr("y", d => d.y);

                badges
                    .attr("x", d => d.x)
                    .attr("y", d => d.y);
            }});

            function dragstarted(event, d) {{
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }}

            function dragged(event, d) {{
                d.fx = event.x;
                d.fy = event.y;
            }}

            function dragended(event, d) {{
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }}
        }}

        // Conflicts Data
        const conflictData = [
            {{ id: 1, s1: "💸 Sunk Cost", s2: "🧗 Grit", r1: "When evidence shows poor results or bad fit", r2: "When project has clear path & good match quality", strategy: "Match Quality Meta-Framework" }},
            {{ id: 2, s1: "🛑 Strategic Quitting", s2: "🧗 Grit", r1: "When in wicked domain or exploring fit", r2: "When you're in a kind domain with clear path", strategy: "Kind/Wicked Assessment" }},
            {{ id: 3, s1: "🎯 Specialization", s2: "🌐 Generalization", r1: "Kind problems: stable rules, clear feedback", r2: "Wicked problems: changing rules, ambiguity", strategy: "Domain Complexity Audit" }},
            {{ id: 4, s1: "🔍 Focus", s2: "🧭 Exploration", r1: "Deep work needed, executing known strategy", r2: "Learning stage, solving novel problems", strategy: "Time-box: Explore then Focus" }},
            {{ id: 5, s1: "⚡ Speed", s2: "🧘 Deliberate Practice", r1: "Learning routine skills or kind problems", r2: "Developing expertise in complex domains", strategy: "Fast for breadth, Slow for depth" }},
            {{ id: 6, s1: "🧠 Intuition", s2: "🎲 Probabilistic Thinking", r1: "In circle of competence with experience", r2: "Outside circle of competence, high-stakes", strategy: "Circle of Competence Boundaries" }},
            {{ id: 7, s1: "🧱 First Principles", s2: "🌉 Analogy", r1: "Novel problems, innovation, or failure", r2: "Routine problems in stable domains", strategy: "Innovation vs. Communication" }}
        ];

        function renderConflicts() {{
            const container = document.getElementById('conflictContainer');
            if (!container) return;
            container.innerHTML = conflictData.map(c => `
                <div class="conflict-card">
                    <div class="conflict-vs">
                        <div class="vs-item" style="color: var(--text-main); background: var(--bg-secondary);">${{c.s1}}</div>
                        <div class="vs-divider">VS</div>
                        <div class="vs-item" style="color: var(--text-main); background: var(--bg-secondary);">${{c.s2}}</div>
                    </div>
                    <div class="conflict-instruction">
                        <div class="instruction-box">
                            <div class="instruction-title">Prioritize ${{c.s1.split(' ').pop()}}</div>
                            <p style="color: var(--text-main);">${{c.r1}}</p>
                        </div>
                        <div class="instruction-box">
                            <div class="instruction-title">Prioritize ${{c.s2.split(' ').pop()}}</div>
                            <p style="color: var(--text-main);">${{c.r2}}</p>
                        </div>
                    </div>
                    <div class="resolution-meta">
                        Resolution Strategy: <span class="resolution-value" style="color: var(--accent-primary);">${{c.strategy}}</span>
                    </div>
                </div>
            `).join('');
        }}

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {{
            initTheme();
            renderDailyFocus();
            renderTopSkills();
            renderSkills();
            renderCategories();
            renderOverlaps();
            renderMultitag();
            renderConflicts();
            drawCategoryChart();

            // Global Shortcuts (Cmd+K)
            document.addEventListener('keydown', (e) => {{
                if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{
                    e.preventDefault();
                    document.getElementById('globalSearch').focus();
                }}
            }});
        }});
        </script>
        </body>
        </html>
'''

# Save the file
output_file = Path("skills-dashboard-ux.html")
with open(output_file, 'w') as f:
    f.write(html)

print(f"✅ Created modern dark dashboard: {output_file}")
print(f"\\n🎨 Design Features:")
print(f"   • Dark theme with navy background")
print(f"   • Fixed sidebar navigation")
print(f"   • Purple accent colors")
print(f"   • Modern card design")
print(f"   • Statistics grid (2×2)")
print(f"   • All views working")
print(f"\\nOpen: file://{output_file.absolute()}")
