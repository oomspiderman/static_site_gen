import unittest
from block_to_block_type import BlockType
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading_level_1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_level_6(self):
        block = "###### Smallest heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_invalid_heading_too_many_hashes(self):
        block = "####### Not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\ncode goes here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_invalid_quote_block(self):
        block = "> valid\nnope"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_block(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = "- valid\nnot valid"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_block(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_with_wrong_start(self):
        block = "2. wrong\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_with_wrong_increment(self):
        block = "1. start\n3. skip"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        block = "This is a regular paragraph of markdown text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_multi_paragraph_quote_block(self):
        md = """> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien"""
    
        from markdown_to_blocks import markdown_to_blocks
        from block_to_block_type import block_to_block_type
    
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.QUOTE)

if __name__ == "__main__":
    unittest.main()
