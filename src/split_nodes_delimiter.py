from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown Syntax")            

        node_text_parts = node.text.split(delimiter)

        for i, new_text in enumerate(node_text_parts):
            if new_text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(new_text, TextType.TEXT, node.url))
            else:
                new_nodes.append(TextNode(new_text, text_type, node.url))
               
    return new_nodes
