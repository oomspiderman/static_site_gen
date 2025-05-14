from htmlnode import HTMLNode
from textnode import TextNode
from textnode import TextType

my_text_node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
print(my_text_node)

my_html_node_1 = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
print(my_html_node_1)

print(my_html_node_1.props_to_html())