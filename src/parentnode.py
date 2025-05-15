from typing import List, Dict, Optional
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], props: Optional[Dict[str, str]] = None):
        if tag is None:
            raise ValueError("ParentNode requires a non-None tag.")
        if not children:
            raise ValueError("ParentNode requires a non-empty list of children.")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Cannot render HTML: tag is missing.")

        if self.children is None or not isinstance(self.children, list):
            raise ValueError("Cannot render HTML: children are missing or invalid.")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return (
            f"ParentNode(tag={self.tag!r}, children={self.children!r}, "
            f"props={self.props!r})"
        )