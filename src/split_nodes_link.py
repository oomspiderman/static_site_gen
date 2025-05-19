from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        link_pairs = extract_markdown_links(node.text)
        number_of_links = len(link_pairs)
        if number_of_links <= 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for link_text, link_url in link_pairs:          
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT, node.url))
            
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            remaining_text = sections[1]
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, node.url))

    return new_nodes


