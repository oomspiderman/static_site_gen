from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import BlockType
from block_to_block_type import block_to_block_type

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        collapsed = block.replace("\n", " ")
        return ParentNode("p", text_to_children(collapsed))

    if block_type == BlockType.HEADING:
        level = len(block.split(" ")[0])
        content = block[level + 1:]  # skip #s and the space
        return ParentNode(f"h{level}", text_to_children(content))

    if block_type == BlockType.CODE:
        lines = block.split("\n")[1:-1]  # Skip opening/closing ```
        stripped_lines = [line[1:] if line.startswith(" ") else line for line in lines]
        inner = "\n".join(stripped_lines)
        code_node = LeafNode("code", inner + "\n")
        return ParentNode("pre", [code_node])

    if block_type == BlockType.QUOTE:
        # Remove leading '> ' or just '>' from each line
        lines = [line.lstrip("> ").strip() for line in block.splitlines()]
        joined = "\n".join(lines)
        # Let text_to_children parse paragraphs/formatting normally
        return ParentNode("blockquote", text_to_children(joined))


    if block_type == BlockType.UNORDERED_LIST:
        lines = [line[2:] for line in block.split("\n")]
        children = [ParentNode("li", text_to_children(line)) for line in lines]
        return ParentNode("ul", children)

    if block_type == BlockType.ORDERED_LIST:
        lines = [line.split(". ", 1)[1] for line in block.split("\n")]
        children = [ParentNode("li", text_to_children(line)) for line in lines]
        return ParentNode("ol", children)

    raise Exception("Unknown block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)