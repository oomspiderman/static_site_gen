from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        image_pairs = extract_markdown_images(node.text)
        number_of_images = len(image_pairs)
        if number_of_images <= 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for image_alt, image_link in image_pairs:          
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT, node.url))
            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            remaining_text = sections[1]
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, node.url))

    return new_nodes

