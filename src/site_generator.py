import os
from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 (# ) title found in markdown.")

def generate_page(from_path: str, template_path: str, dest_path: str, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to HTML using your node tree
    content_html = markdown_to_html_node(markdown).to_html()

    # Extract page title from markdown heading
    title = extract_title(markdown)

    # Inject into template
    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", content_html)

    # Inject basepath into static references
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the resulting HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(root, dir_path_content)
                src_md_path = os.path.join(root, file)
                dest_html_dir = os.path.join(dest_dir_path, rel_path)
                os.makedirs(dest_html_dir, exist_ok=True)

                dest_file = file.replace(".md", ".html")
                dest_path = os.path.join(dest_html_dir, dest_file)

                print(f" * {src_md_path} {template_path} -> {dest_path}")
                generate_page(src_md_path, template_path, dest_path, basepath)