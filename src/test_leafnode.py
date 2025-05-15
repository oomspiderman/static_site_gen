import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_heading_tag(self):
        node = LeafNode("h1", "Main Heading")
        self.assertEqual(node.to_html(), "<h1>Main Heading</h1>")

    def test_emphasis_tag(self):
        node = LeafNode("em", "emphasized")
        self.assertEqual(node.to_html(), "<em>emphasized</em>")

    def test_strong_tag_with_class(self):
        node = LeafNode("strong", "important", props={"class": "bold"})
        self.assertEqual(node.to_html(), '<strong class="bold">important</strong>')

    def test_span_with_multiple_props(self):
        node = LeafNode("span", "inline text", props={"class": "note", "id": "highlight"})
        self.assertEqual(node.to_html(), '<span class="note" id="highlight">inline text</span>')

    def test_link_tag_valid(self):
        node = LeafNode("a", "Visit site", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Visit site</a>')

    def test_link_tag_missing_href(self):
        node = LeafNode("a", "Broken link", props={})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_image_tag_valid(self):
        node = LeafNode("img", None, props={"src": "logo.png", "alt": "Logo"})
        self.assertEqual(node.to_html(), '<img src="logo.png" alt="Logo">')

    def test_image_tag_missing_src(self):
        node = LeafNode("img", None, props={"alt": "no source"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_image_tag_with_value_ignored(self):
        node = LeafNode("img", "ignored", props={"src": "image.png"})
        self.assertEqual(node.to_html(), '<img src="image.png">')

    def test_tag_none_returns_value(self):
        node = LeafNode(None, "just text")
        self.assertEqual(node.to_html(), "just text")

    def test_unknown_tag(self):
        node = LeafNode("custom", "My content", props={"data-role": "widget"})
        self.assertEqual(node.to_html(), '<custom data-role="widget">My content</custom>')

    def test_repr_output(self):
        node = LeafNode("code", "print('hi')", props={"class": "code-snippet"})
        expected = "LeafNode(tag='code', value=\"print('hi')\", props={'class': 'code-snippet'})"
        self.assertEqual(repr(node), expected)

    def test_missing_value_on_non_img(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()
