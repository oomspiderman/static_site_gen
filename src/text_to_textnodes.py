from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]

    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)

    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

    new_nodes = split_nodes_link(new_nodes)

    new_nodes = split_nodes_image(new_nodes)

    return new_nodes
