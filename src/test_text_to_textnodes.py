import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_all_text(self):
        text = "Just some normal text"
        result = text_to_textnodes(text)
        self.assertEqual(result, [TextNode("Just some normal text", TextType.TEXT)])

    def test_bold_text(self):
        text = "This is **bold**"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ])

    def test_italic_text(self):
        text = "Text with _italic_ word"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])

    def test_code_text(self):
        text = "Some `code` here"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT)
        ])

    def test_link_text(self):
        text = "Go to [Google](https://google.com)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Go to ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com")
        ])

    def test_image_text(self):
        text = "Here is ![alt](https://img.com/img.png)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Here is ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://img.com/img.png")
        ])

    def test_mixed_formatting(self):
        text = "This is **bold**, _italic_, and `code`"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE)
        ])

    def test_full_markdown_line(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_unbalanced_bold_raises(self):
        text = "This is **bold and never closed"
        with self.assertRaises(Exception):
            text_to_textnodes(text)

    def test_unbalanced_code_raises(self):
        text = "Here is `open code but no close"
        with self.assertRaises(Exception):
            text_to_textnodes(text)

if __name__ == "__main__":
    unittest.main()
