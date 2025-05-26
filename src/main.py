import os
from site_generator import generate_page
from copy_directory_recursive import copy_directory_recursive

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, dir_path_content)
                rel_path_html = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, rel_path_html)

                # Make sure destination subdirectories exist
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                print(f"✅ Generating {dest_path} from {src_path}")
                generate_page(src_path, template_path, dest_path)

if __name__ == "__main__":
    from copy_directory_recursive import copy_directory_recursive

    copy_directory_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")

