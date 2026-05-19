#!/usr/bin/env python3
"""
Recover missing handouts by extracting content from existing HTML files
and creating markdown sources.
"""

import re
import json
from pathlib import Path

HANDOUTS_BASE_DIR = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/patient-tools/handouts")
MAPPING_FILE = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/HANDOUT_CONVERSION_MAPPING.json")

# Load mapping to get categories
with open(MAPPING_FILE, 'r') as f:
    mapping = json.load(f)

handout_to_category = mapping.get('handout_to_category_map', {})

# Handouts to recover
HANDOUTS_TO_RECOVER = {
    'eating-well': {'title': 'Eating well on real terms', 'category': 'lifestyle'},
    'health-myths': {'title': 'Common health myths explained', 'category': 'general'},
    'acc': {'title': 'ACC and injury cover in New Zealand', 'category': 'general'},
}

def extract_body_from_html(html_file):
    """Extract page-body div content from HTML file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find page-body div
        match = re.search(r'<div class="page-body">(.*?)</div>\s*<div class="(?:refs-section|alert-box|page-footer)', content, re.DOTALL)
        if not match:
            print(f"  Could not find page-body in {html_file}")
            return None

        body_html = match.group(1).strip()

        # Clean up the HTML - remove old CSS classes and simplify structure
        # Replace .glance divs with simple content
        body_html = re.sub(r'<div class="glance">.*?</div>\s*', '', body_html, flags=re.DOTALL)

        # Simplify accordion items to simple sections
        body_html = re.sub(r'<div class="acc-item[^"]*">\s*<div class="acc-head">(.*?)<span class="chevron">.*?</span></div>\s*<div class="acc-body">(.*?)</div>\s*</div>',
                          r'<h2>\1</h2>\2', body_html, flags=re.DOTALL)

        # Remove .myth-section divs but preserve content
        body_html = re.sub(r'<div class="myth-section">\s*<strong>(.*?)</strong>\s*(.*?)</div>',
                          r'<p><strong>\1</strong>\2</p>', body_html, flags=re.DOTALL)

        # Clean up .data-table, .alert-box, .resources classes
        body_html = re.sub(r'class="data-table"', 'class="data-table"', body_html)
        body_html = re.sub(r'class="alert-box"', 'class="alert-box"', body_html)
        body_html = re.sub(r'class="resources"', 'class="resources"', body_html)
        body_html = re.sub(r'<div class="[^"]*-head">', '', body_html)
        body_html = re.sub(r'<div class="[^"]*-desc">', '', body_html)
        body_html = re.sub(r'class="[^"]*-(label|value|desc)"', '', body_html)
        body_html = re.sub(r'<div class="section-(h2|lead)">', '', body_html)
        body_html = re.sub(r'</div>\s*<div class="[^"]*">', '', body_html)

        # Remove multiple consecutive whitespace
        body_html = re.sub(r'\n\s*\n+', '\n\n', body_html)

        return body_html

    except Exception as e:
        print(f"  Error extracting from {html_file}: {e}")
        return None


def create_markdown(handout_name, title, category, body_html):
    """Create markdown file for handout."""

    # Get description from first paragraph
    description_match = re.search(r'<p[^>]*>(.*?)</p>', body_html)
    description = description_match.group(1) if description_match else ""

    # Clean HTML descriptions
    description = re.sub(r'<[^>]*>', '', description)
    description = description[:200].rstrip() + "..."

    front_matter = f"""---
title: {title}
layout: topic.njk
pageType: handout
description: {description}
---
"""

    markdown = front_matter + "\n" + body_html

    return markdown


def recover_handouts():
    """Recover missing handouts."""
    print("Recovering missing handouts...")
    print("-" * 60)

    for handout_name, info in HANDOUTS_TO_RECOVER.items():
        handout_dir = HANDOUTS_BASE_DIR / handout_name
        html_file = handout_dir / "index.html"
        md_file = handout_dir / "index.md"

        if not html_file.exists():
            print(f"✗ {handout_name}: HTML file not found")
            continue

        if md_file.exists():
            print(f"⊘ {handout_name}: markdown already exists")
            continue

        print(f"  Extracting {handout_name}...")
        body_html = extract_body_from_html(html_file)

        if not body_html:
            print(f"✗ {handout_name}: failed to extract body content")
            continue

        markdown = create_markdown(handout_name, info['title'], info['category'], body_html)

        try:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"✓ {handout_name}: recovered")
        except Exception as e:
            print(f"✗ {handout_name}: failed to write markdown - {e}")

    print("-" * 60)
    print("Recovery complete")


if __name__ == "__main__":
    recover_handouts()
