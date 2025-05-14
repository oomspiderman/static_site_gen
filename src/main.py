from textnode import TextNode
from textnode import TextType

mynode = TextNode("This is some anchor text", TextType.LINKS_ANCHOR_TEXT, "https://www.boot.dev")
print(mynode)