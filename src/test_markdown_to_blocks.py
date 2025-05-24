import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_paragraph(self):
        md = "Just a single paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single paragraph"])

    def test_paragraph_with_leading_and_trailing_newlines(self):
        md = "\n\n  This is a paragraph with space and newlines  \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph with space and newlines"])

    def test_multiple_lists(self):
        md = """
- Item 1
- Item 2

- Item A
- Item B
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- Item 1\n- Item 2",
                "- Item A\n- Item B"
            ]
        )

    def test_extra_spacing(self):
        md = """
First paragraph


Second paragraph



- List item one
- List item two
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
                "- List item one\n- List item two"
            ]
        )

if __name__ == "__main__":
    unittest.main()
