#!/usr/bin/env python3
"""
Wiki Broken Link Checker
========================
Author: Gemini CLI
Created: 2026-06-03

This script scans Markdown files for wiki links [[Link]] and identifies those 
that point to non-existent files. It can either list the broken links,
export them to a report file, or automatically create stub files for them.

Usage:
    python check_wiki_links.py [directory]
    python check_wiki_links.py [directory] --create-stubs
    python check_wiki_links.py [directory] --report-file broken_links.md
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_info(msg):
    print(f"{Colors.BLUE}[INFO]{Colors.ENDC} {msg}")

def log_success(msg):
    print(f"{Colors.GREEN}[SUCCESS]{Colors.ENDC} {msg}")

def log_warning(msg):
    print(f"{Colors.YELLOW}[WARNING]{Colors.ENDC} {msg}")

def log_error(msg):
    print(f"{Colors.RED}[ERROR]{Colors.ENDC} {msg}")

def check_wiki_links(root_dir, create_stubs=False, report_file=None, overwrite_stubs=False):
    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        log_error(f"Directory not found: {root_dir}")
        return

    log_info(f"Scanning directory: {root_path}")

    # 1. Gather all markdown files to build a lookup index
    md_files = {}
    stems = {}
    
    for p in root_path.rglob('*.md'):
        try:
            rel_path = p.relative_to(root_path)
            rel_str = str(rel_path).replace(os.sep, '/')
            md_files[rel_str] = p
            
            stem = p.stem
            if stem not in stems:
                stems[stem] = []
            stems[stem].append(p)
        except ValueError:
            pass

    # 2. Regex for wiki links
    wiki_link_pattern = re.compile(r'\[\[([^\]|#]*)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]')

    # Map target link -> list of source files
    broken_links_map = defaultdict(list)
    
    md_file_count = len(md_files)
    log_info(f"Found {md_file_count} markdown files.")

    # 3. Scan each file
    for rel_path_str, full_path in md_files.items():
        try:
            # Skip reading files that were just created as stubs if we are just starting
            # But we need them for backlinks. 
            # However, if we want to "fix" stubs that already exist, we need to know
            # they ARE stubs.
            
            is_stub = False
            content = ""
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if "Created by Broken Link Checker" in content:
                    is_stub = True
            
            # If it's a stub and we are NOT overwriting, it's not "broken" anymore.
            # But if we want to RE-STUB it with backlinks, we treat it as broken.
            
            links = wiki_link_pattern.findall(content)
            for link in links:
                link = link.strip()
                if not link: continue
                
                exists = False
                link_md = link if link.endswith('.md') else f"{link}.md"
                link_md_norm = link_md.replace('\\', '/')
                
                # Check if it exists in our index
                if link_md_norm in md_files:
                    target_path = md_files[link_md_norm]
                    # If target is a stub, we might want to treat it as broken to update it
                    if overwrite_stubs:
                        with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
                            target_content = f.read()
                            if "Created by Broken Link Checker" not in target_content:
                                exists = True
                    else:
                        exists = True

                if not exists:
                    link_stem = Path(link).stem
                    if link_stem in stems:
                        # Check if ANY of the files with this stem are real files
                        for p in stems[link_stem]:
                            if overwrite_stubs:
                                with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                                    if "Created by Broken Link Checker" not in f.read():
                                        exists = True
                                        break
                            else:
                                exists = True
                                break
                
                if not exists:
                    source_dir = full_path.parent
                    rel_to_source = (source_dir / link_md).resolve()
                    if rel_to_source.exists() and rel_to_source.is_file():
                        if overwrite_stubs:
                            with open(rel_to_source, 'r', encoding='utf-8', errors='ignore') as f:
                                if "Created by Broken Link Checker" not in f.read():
                                    exists = True
                        else:
                            exists = True

                if not exists:
                    # Case-insensitive
                    link_md_lower = link_md_norm.lower()
                    for mdf, p in md_files.items():
                        if mdf.lower() == link_md_lower:
                            if overwrite_stubs:
                                with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                                    if "Created by Broken Link Checker" not in f.read():
                                        exists = True
                            else:
                                exists = True
                            break
                
                if not exists:
                    broken_links_map[link].append(rel_path_str)
                    
        except Exception as e:
            log_error(f"Error processing {rel_path_str}: {e}")

    # 4. Output results
    if not broken_links_map:
        log_success("No broken links found!")
        return

    unique_broken = sorted(list(broken_links_map.keys()))

    if report_file:
        try:
            report_path = Path(report_file)
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write("# Broken Wiki Links Report\n\n")
                f.write(f"Total Broken Links: {len(unique_broken)}\n\n")
                for link in unique_broken:
                    f.write(f"- [[{link}]]\n")
            log_success(f"Report saved to: {report_file}")
        except Exception as e:
            log_error(f"Failed to save report: {e}")

    if create_stubs:
        log_info(f"Creating/Updating stubs for {len(unique_broken)} unique broken links...")
        created_count = 0
        updated_count = 0
        
        for link in unique_broken:
            stub_rel_path = link if link.endswith('.md') else f"{link}.md"
            stub_full_path = root_path / stub_rel_path
            
            exists_already = stub_full_path.exists()
            
            try:
                stub_full_path.parent.mkdir(parents=True, exist_ok=True)
                title = stub_full_path.stem
                
                # Build backlink list
                backlinks = sorted(list(set(broken_links_map[link])))
                backlinks_str = "\n".join([f"- [[{b.replace('.md', '')}]]" for b in backlinks])
                
                stub_content = f"# {title}\n\n"
                stub_content += f"Definition for {title} goes here.\n\n"
                stub_content += "## Backlinks\n"
                stub_content += f"{backlinks_str}\n\n"
                stub_content += "---\nCreated by Broken Link Checker."
                
                with open(stub_full_path, 'w', encoding='utf-8') as f:
                    f.write(stub_content)
                
                if exists_already:
                    updated_count += 1
                else:
                    created_count += 1
            except Exception as e:
                log_error(f"Failed to create stub for {link}: {e}")
                
        log_success(f"Finished: {created_count} created, {updated_count} updated.")

    if not create_stubs and not report_file:
        log_warning(f"Found {len(unique_broken)} unique broken links:")
        for link in unique_broken:
            print(f"[[{link}]]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find broken wiki links in Markdown files.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan (default: current)")
    parser.add_argument("--create-stubs", action="store_true", help="Create stub files for broken links")
    parser.add_argument("--report-file", help="File to save the list of broken links to (e.g., broken_links.md)")
    parser.add_argument("--overwrite-stubs", action="store_true", help="Overwrite existing stubs created by this script")
    
    args = parser.parse_args()
    
    try:
        check_wiki_links(args.directory, args.create_stubs, args.report_file, args.overwrite_stubs)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
