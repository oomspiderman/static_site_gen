import os
import sys
from site_generator import generate_page
from copy_directory_recursive import copy_directory_recursive

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(root, dir_path_content)
                src_md_path = os.path.join(root, file)
                dest_html_dir = os.path.join(dest_dir_path, rel_path)
                os.makedirs(dest_html_dir, exist_ok=True)

                # Read content
                with open(src_md_path, "r", encoding="utf-8") as f:
                    markdown_content = f.read()

                with open(template_path, "r", encoding="utf-8") as f:
                    template = f.read()

                body_html = f"<p>{markdown_content.strip()}</p>"

                # Inject content and fix paths
                html = template.replace("{{ content }}", body_html)
                html = html.replace('href="/', f'href="{basepath}')
                html = html.replace('src="/', f'src="{basepath}')

                html_file = file.replace(".md", ".html")
                dest_path = os.path.join(dest_html_dir, html_file)

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(html)

if __name__ == "__main__":
    from copy_directory_recursive import copy_directory_recursive
    copy_directory_recursive("static", "docs")

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive("content", "template.html", "docs", basepath)

