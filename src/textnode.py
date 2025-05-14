from enum import Enum

class TextType(Enum):
    BOLD_TEXT         = "boldText"
    ITALIC_TEXT       = "italicText"
    CODE_TEXT         = "codeText"
    LINKS_ANCHOR_TEXT = "links"
    IMAGE_ALT_TEXT    = "images"

class TextNode:
    def __init__(self, text, text_type : TextType, url=None):
        if not isinstance(text_type, TextType):
            text_type = TextType(text_type)  # Convert string to enum if needed        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"