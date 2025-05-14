import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a NOT text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a NEW text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.mdev")
        node2 = TextNode("This is a NEW text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)                

if __name__ == "__main__":
    unittest.main()