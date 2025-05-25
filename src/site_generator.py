import os
import shutil
from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 (# ) title found in markdown.")

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to HTML
    content_html = markdown_to_html_node(markdown).to_html()

    # Extract title
    title = extract_title(markdown)

    # Replace template variables
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    # Ensure dest directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)