from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH      = "paragraph"
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   = "ordered_list"

def block_to_block_type(text):
    if re.match(r"^(#{1,6}) (.*)", text):
        return BlockType.HEADING

    if re.match(r"^```[\s\S]*```$", text, re.DOTALL):
        return BlockType.CODE

    lines = text.splitlines()

    if all(line.strip().startswith(">") for line in text.splitlines()):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(r"^\d+\. ", line) for line in lines):
        expected = 1
        for line in lines:
            actual = int(line.split(".")[0])
            if actual != expected:
                break
            expected += 1
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
