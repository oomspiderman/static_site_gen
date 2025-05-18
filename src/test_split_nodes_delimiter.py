import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_split(self):
        node = TextNode("This is `code`.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ])

    def test_delimiter_at_start(self):
        node = TextNode("`code` at the beginning", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("code", TextType.CODE),
            TextNode(" at the beginning", TextType.TEXT),
        ])

    def test_delimiter_at_end(self):
        node = TextNode("At the end is `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("At the end is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ])

    def test_delimiters_start_and_end(self):
        node = TextNode("`code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("code", TextType.CODE),
        ])

    def test_multiple_code_blocks(self):
        node = TextNode("One `first` and `second` block", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("One ", TextType.TEXT),
            TextNode("first", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.CODE),
            TextNode(" block", TextType.TEXT),
        ])

    def test_no_delimiters(self):
        node = TextNode("No special syntax here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])  # Should return unchanged

    def test_non_text_nodes_untouched(self):
        node1 = TextNode("Plain", TextType.TEXT)
        node2 = TextNode("Link", TextType.LINK, url="https://example.com")
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Plain", TextType.TEXT),
            node2
        ])

    def test_uneven_delimiters_raise(self):
        node = TextNode("This is `unmatched", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
