from typing import Optional, List, Dict

class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}        
    
    def to_html(self) -> str:
        raise NotImplementedError("to_html() must be implemented in a subclass or future version.")

    def props_to_html(self):
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )
