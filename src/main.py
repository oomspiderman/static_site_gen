from htmlnode import HTMLNode
from textnode import TextNode
from textnode import TextType
from copy_directory import copy_directory_recursive

from split_nodes_delimiter import split_nodes_delimiter

from extract_markdown import *

copy_directory_recursive("static", "public")

my_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(my_text_node)

my_html_node_1 = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
print(my_html_node_1)

print(my_html_node_1.props_to_html())

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]