import re
from collections import defaultdict

# Read the Markdown file with UTF-8 encoding
with open(r"F:\Program\Arkonpy\elements_by_section.md", 'r', encoding='utf-8') as file:
    content = file.read()

# Updated regex pattern:
# - Matches headers starting with '**'
# - Captures one of the UI types (Listbox, Combobox, Treeview, or Scrollbar)
# - Captures the widget type inside parentheses
# - Captures all following content (details) until the next header or the end of the file.
# Note: The lookahead at the end is now noncapturing.
pattern = re.compile(
    r'\*\*\s*(Listbox|Combobox|Treeview|Scrollbar)\s*\((.*?)\)\s*\*\*(.*?)(?=\r?\n\*\*|\r?\n###|\Z)',
    re.DOTALL
)

# Dictionary to store UI types and their bullet items
ui_elements = defaultdict(list)

# Find all matches in the markdown file
matches = pattern.findall(content)

for match in matches:
    # Unpack the three capturing groups:
    #   ui_type: the type of UI element (e.g., Listbox, Combobox, etc.)
    #   widget_type: the text inside the parentheses (if needed for further processing)
    #   details: the block of text containing bullet items and other details
    ui_type, widget_type, details = match

    # Extract bullet items from the details.
    # This regex handles bullet items that start with '-' or '•' and captures the text until the end of the line.
    items = re.findall(r'[-•]\s+(.*?)(?=\r?\n|$)', details)

    # Clean the extracted items: remove extra whitespace and discard any empty items.
    items = [item.strip() for item in items if item.strip()]

    # Add the items to the corresponding UI type list in the dictionary.
    ui_elements[ui_type].extend(items)

# Remove duplicate items and sort the bullet items for each UI type
for ui_type in ui_elements:
    ui_elements[ui_type] = sorted(set(ui_elements[ui_type]))

# Write the consolidated UI elements to a new Markdown file.
output_file = r"F:\Program\Arkonpy\unified_ui_elements.md"
with open(output_file, 'w', encoding='utf-8') as f:
    # Write a header for the output file.
    f.write('# Unified UI Elements\n\n')
    # For each UI type, create a subsection and list the items.
    for ui_type, items in ui_elements.items():
        f.write(f'## {ui_type}\n')
        for item in items:
            f.write(f'- {item}\n')
        f.write('\n')

print(f'Unified UI elements saved to {output_file}')
