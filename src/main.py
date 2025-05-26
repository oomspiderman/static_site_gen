# from htmlnode import HTMLNode
# from textnode import TextNode
# from textnode import TextType
# from copy_directory_recursively import copy_directory_recursive

# from split_nodes_delimiter import split_nodes_delimiter

# from extract_markdown import *

# copy_directory_recursive("static", "public")

# my_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
# print(my_text_node)

# my_html_node_1 = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
# print(my_html_node_1)

# print(my_html_node_1.props_to_html())

# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

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

