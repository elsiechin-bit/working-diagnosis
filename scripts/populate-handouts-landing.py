#!/usr/bin/env python3
"""
Populate the handouts landing page with actual handout data.
Reads metadata from markdown files and injects into the landing page.
"""

import json
import re
from pathlib import Path

HANDOUTS_BASE_DIR = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/patient-tools/handouts")
MAPPING_FILE = Path("/sessions/festive-keen-galileo/mnt/working-diagnosis/HANDOUT_CONVERSION_MAPPING.json")
LANDING_PAGE = HANDOUTS_BASE_DIR / "index.html"

# Load mapping
with open(MAPPING_FILE, 'r') as f:
    mapping = json.load(f)

handout_to_category = mapping.get('handout_to_category_map', {})
category_info = mapping.get('category_directory', {})

def extract_metadata(md_file):
    """Extract title and description from markdown front matter."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse front matter
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None, None

        front_matter = parts[1]
        title = None
        description = None

        for line in front_matter.split('\n'):
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip().strip("'\"")
            elif line.startswith('description:'):
                description = line.split(':', 1)[1].strip().strip("'\"")

        return title, description
    except Exception as e:
        print(f"  Error reading {md_file}: {e}")
        return None, None

def escape_js_string(s):
    """Escape string for JavaScript."""
    if not s:
        return ""
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    return s

print("Building handouts landing page data...")
print("-" * 60)

# Build data by category
handouts_by_category = {}
total_handouts = 0
errors = []

for category in category_info.keys():
    handouts_by_category[category] = []

# Process each handout
for handout_name in sorted(handout_to_category.keys()):
    category = handout_to_category[handout_name]
    handout_dir = HANDOUTS_BASE_DIR / handout_name
    md_file = handout_dir / "index.md"

    if not md_file.exists():
        errors.append(f"Missing: {handout_name}")
        continue

    title, description = extract_metadata(md_file)

    if not title:
        title = ' '.join(word.capitalize() for word in handout_name.split('-'))

    if not description:
        description = f"Learn more about {title}."

    # Truncate description to ~150 chars
    if len(description) > 150:
        description = description[:150].rstrip() + "..."

    handouts_by_category[category].append({
        'slug': handout_name,
        'title': title,
        'description': description
    })
    total_handouts += 1

# Generate JavaScript data
lines = []
lines.append("        // Load handouts from HANDOUT_CONVERSION_MAPPING")
lines.append("        const handoutsData = {")

for category, handouts in handouts_by_category.items():
    if category in category_info:
        cat_data = category_info[category]
        label = cat_data.get('display_name', category)
        color_token = cat_data.get('color_token', 'var(--general-accent)')

        lines.append(f"            '{category}': {{")
        lines.append(f"                label: '{escape_js_string(label)}',")
        lines.append(f"                accent: '{color_token}',")
        lines.append(f"                handouts: [")

        for handout in handouts:
            lines.append(f"                    {{ slug: '{handout['slug']}', title: '{escape_js_string(handout['title'])}', description: '{escape_js_string(handout['description'])}' }},")

        lines.append(f"                ],")
        lines.append(f"            }},")

lines.append("        };")
lines.append("")
lines.append("        // Populate categories")
lines.append("        Object.entries(handoutsData).forEach(([key, data]) => {")
lines.append("            if (categories[key]) {")
lines.append("                categories[key].label = data.label;")
lines.append("                categories[key].accent = data.accent;")
lines.append("                categories[key].handouts = data.handouts;")
lines.append("                categories[key].count = data.handouts.length;")
lines.append("            }")
lines.append("        });")

js_injection = '\n'.join(lines)

# Read current landing page
with open(LANDING_PAGE, 'r', encoding='utf-8') as f:
    landing_content = f.read()

# Find insertion point (the categories object definition)
insertion_point = landing_content.find("        const categories = {")
end_point = landing_content.find("        let currentCategory", insertion_point)

if insertion_point == -1 or end_point == -1:
    print("ERROR: Could not find insertion point in landing page")
else:
    # Replace the old categories block with new data injection
    new_content = (
        landing_content[:insertion_point] +
        js_injection +
        "\n\n" +
        landing_content[end_point:]
    )

    with open(LANDING_PAGE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Populated landing page with {total_handouts} handouts across {len([c for c in handouts_by_category.values() if c])} categories")

print("-" * 60)
if errors:
    print(f"Warnings ({len(errors)}):")
    for error in errors[:5]:
        print(f"  - {error}")
    if len(errors) > 5:
        print(f"  ... and {len(errors) - 5} more")
else:
    print("No errors detected")
