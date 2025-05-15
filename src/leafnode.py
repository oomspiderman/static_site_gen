from typing import Optional, Dict
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str],
        value: Optional[str],
        props: Optional[Dict[str, str]] = None,
    ):
        if tag != "img" and value is None:
            raise ValueError("LeafNode requires a non-None value for non-image tags.")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def to_html(self) -> str:
        if self.tag is None:
            if self.value is None:
                raise ValueError("LeafNode must have value if tag is None")
            return self.value

        if self.tag == "a":
            href = self.props.get("href") if self.props else None
            if not href:
                raise ValueError("Missing 'href' in props for <a> tag")

        if self.tag == "img":
            src = self.props.get("src") if self.props else None
            if not src:
                raise ValueError("Missing 'src' in props for <img> tag")
            return f"<img{self.props_to_html()}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (
            f"LeafNode(tag={self.tag!r}, value={self.value!r}, "
            f"props={self.props!r})"
        )