#!/usr/bin/env python3
"""
Handout Markdown to React Component Converter

Converts all 222 markdown handouts to React components matching the design system.
Each component uses category-specific color tokens from HANDOUT_CONVERSION_MAPPING.json.
"""

import os
import json
import re
import sys
from pathlib import Path
from datetime import datetime

# Configuration
HANDOUTS_BASE_DIR = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/patient-tools/handouts")
MAPPING_FILE = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/HANDOUT_CONVERSION_MAPPING.json")

# Load mapping data
with open(MAPPING_FILE, 'r') as f:
    mapping = json.load(f)

handout_to_category = mapping.get('handout_to_category_map', {})


def parse_markdown_file(file_path):
    """Extract YAML front matter and HTML body from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split on --- to separate front matter
        parts = content.split('---', 2)

        if len(parts) < 3:
            return None, None

        front_matter_text = parts[1]
        body_html = parts[2].strip()

        # Parse YAML-like front matter
        metadata = {}
        for line in front_matter_text.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip("'\"")

        return metadata, body_html

    except Exception as e:
        print("  ERROR parsing {}: {}".format(file_path, str(e)))
        return None, None


def get_category_color(handout_name):
    """Look up category and color token for a handout."""
    category = handout_to_category.get(handout_name)
    if not category:
        return None, None

    for cat_name, cat_data in mapping.get('category_directory', {}).items():
        if cat_name == category:
            return category, cat_data.get('color_token', '')

    return None, None


def clean_html_body(html_content):
    """Clean and normalize HTML body content."""
    html_content = html_content.strip()
    html_content = re.sub(r'</p>\s+<h[2-3]', '</p>\n\n<h', html_content)
    html_content = re.sub(r'</li>\s+</ul>\s+<h[2-3]', '</li>\n</ul>\n\n<h', html_content)
    html_content = re.sub(r'</ul>\s+</p>', '</ul>\n</p>', html_content)
    html_content = re.sub(r'</ol>\s+</p>', '</ol>\n</p>', html_content)
    return html_content


def clean_handout_name(name):
    """Convert directory name to title case for display."""
    words = name.split('-')
    title = ' '.join(word.capitalize() for word in words)
    return title


def generate_react_component(handout_name, metadata, body_html, category, color_token):
    """Generate React component matching handout design system."""

    title = metadata.get('title', clean_handout_name(handout_name))
    description = metadata.get('description', '')
    body_html = clean_html_body(body_html)

    # HTML template
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Working Diagnosis</title>
    <style>
        :root {{
            --paper: #FAF8F2;
            --paper2: #F3EFE3;
            --ink: #1A1A19;
            --muted: #62615C;
            --faint: #9C9B94;
            --line: #E4E0D2;
            --accent: {color_token};
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background-color: var(--paper);
            color: var(--ink);
            font-family: 'Source Serif 4', Georgia, serif;
            font-size: 16px;
            line-height: 1.8;
        }}

        .page {{
            max-width: 760px;
            margin: 0 auto;
            padding: 48px 40px 60px;
        }}

        .breadcrumb {{
            display: flex;
            gap: 8px;
            font-size: 14px;
            color: var(--muted);
            margin-bottom: 32px;
        }}

        .breadcrumb a {{
            color: var(--muted);
            text-decoration: none;
        }}

        .breadcrumb a:hover {{
            color: var(--ink);
        }}

        h1 {{
            font-size: 32px;
            line-height: 1.3;
            margin-bottom: 12px;
            color: var(--ink);
        }}

        h1 .accent {{
            color: var(--accent);
        }}

        .subtitle {{
            font-size: 18px;
            font-style: italic;
            color: var(--muted);
            margin-bottom: 32px;
        }}

        .body-content {{
            margin-bottom: 40px;
        }}

        p {{
            margin-bottom: 16px;
        }}

        h2 {{
            font-size: 20px;
            margin-top: 32px;
            margin-bottom: 16px;
            color: var(--ink);
        }}

        h3 {{
            font-size: 16px;
            margin-top: 20px;
            margin-bottom: 12px;
            color: var(--accent);
            font-weight: 600;
        }}

        ul, ol {{
            margin-left: 24px;
            margin-bottom: 16px;
        }}

        li {{
            margin-bottom: 8px;
        }}

        strong {{
            color: var(--ink);
            font-weight: 600;
        }}

        a {{
            color: var(--accent);
            text-decoration: underline;
        }}

        a:hover {{
            color: var(--ink);
        }}

        .footer {{
            border-top: 1px solid var(--line);
            padding-top: 32px;
            margin-top: 48px;
            font-size: 14px;
            color: var(--muted);
        }}

        .footer-text {{
            margin-bottom: 16px;
        }}
    }}
    </style>
</head>
<body>
    <div class="page">
        <div class="breadcrumb">
            <a href="/handouts/">All handouts</a>
            <span>/</span>
            <span>{title}</span>
        </div>

        <h1>
            {title}
            <span class="accent">.</span>
        </h1>

        <div class="subtitle">{description}</div>

        <div class="body-content">
{body_html}
        </div>

        <div class="footer">
            <div class="footer-text">
                <strong>About this handout</strong><br>
                This handout is for patients. It is not a substitute for professional medical advice.
                Please discuss your health concerns with your GP.
            </div>
        </div>
    </div>
</body>
</html>"""

    return template.format(title=title, description=description, body_html=body_html, color_token=color_token)


def convert_handouts():
    """Main conversion function."""
    print("Starting handout conversion at {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("Mapping file: {}".format(MAPPING_FILE))
    print("Handouts directory: {}".format(HANDOUTS_BASE_DIR))
    print("-" * 60)

    stats = {
        'total_handouts': len(handout_to_category),
        'successful': 0,
        'failed': 0,
        'skipped': 0,
        'errors': []
    }

    # Iterate through all handouts in mapping
    for handout_name in sorted(handout_to_category.keys()):
        handout_dir = HANDOUTS_BASE_DIR / handout_name
        md_file = handout_dir / "index.md"

        if not handout_dir.exists():
            print("⊘ {}: directory not found".format(handout_name))
            stats['skipped'] += 1
            stats['errors'].append("Directory not found: {}".format(handout_name))
            continue

        if not md_file.exists():
            print("⊘ {}: index.md not found".format(handout_name))
            stats['skipped'] += 1
            stats['errors'].append("No index.md: {}".format(handout_name))
            continue

        # Parse markdown
        metadata, body_html = parse_markdown_file(md_file)

        if metadata is None or body_html is None:
            print("✗ {}: failed to parse".format(handout_name))
            stats['failed'] += 1
            stats['errors'].append("Parse error: {}".format(handout_name))
            continue

        # Get category and color
        category, color_token = get_category_color(handout_name)

        if not category:
            print("✗ {}: no category mapping found".format(handout_name))
            stats['failed'] += 1
            stats['errors'].append("No category: {}".format(handout_name))
            continue

        # Generate component
        try:
            component_html = generate_react_component(
                handout_name,
                metadata,
                body_html,
                category,
                color_token
            )

            # Write output file
            output_file = handout_dir / "index.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(component_html)

            print("✓ {}: converted ({})".format(handout_name, category))
            stats['successful'] += 1

        except Exception as e:
            print("✗ {}: {}".format(handout_name, str(e)))
            stats['failed'] += 1
            stats['errors'].append("Generation error: {} - {}".format(handout_name, str(e)))

    # Summary report
    print("-" * 60)
    print("Conversion complete at {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("Total handouts: {}".format(stats['total_handouts']))
    print("Successful: {}".format(stats['successful']))
    print("Failed: {}".format(stats['failed']))
    print("Skipped: {}".format(stats['skipped']))

    if stats['errors']:
        print("\nErrors:")
        for error in stats['errors'][:10]:
            print("  - {}".format(error))
        if len(stats['errors']) > 10:
            print("  ... and {} more".format(len(stats['errors']) - 10))

    return stats


if __name__ == "__main__":
    try:
        stats = convert_handouts()
        sys.exit(0 if stats['failed'] == 0 else 1)
    except KeyboardInterrupt:
        print("\n\nConversion cancelled by user")
        sys.exit(1)
    except Exception as e:
        print("\n\nFatal error: {}".format(str(e)))
        sys.exit(1)
