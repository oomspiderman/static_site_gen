from htmlnode import HTMLNode
from textnode import TextNode
from textnode import TextType

from split_nodes_delimiter import split_nodes_delimiter

my_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(my_text_node)

my_html_node_1 = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
print(my_html_node_1)

print(my_html_node_1.props_to_html())

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)