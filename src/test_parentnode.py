import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        c1 = LeafNode("p", "First")
        c2 = LeafNode("p", "Second")
        parent = ParentNode("section", [c1, c2])
        self.assertEqual(parent.to_html(), "<section><p>First</p><p>Second</p></section>")

    def test_with_props(self):
        c1 = LeafNode("p", "Hello")
        parent = ParentNode("div", [c1], props={"class": "wrapper", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="wrapper" id="main"><p>Hello</p></div>'
        )

    def test_mixed_leaf_and_parent_children(self):
        subchild = LeafNode("i", "italic")
        child1 = ParentNode("span", [subchild])
        child2 = LeafNode("strong", "bold")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><span><i>italic</i></span><strong>bold</strong></div>"
        )

    def test_missing_tag_raises(self):
        c = LeafNode("p", "Content")
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [c])
        self.assertEqual(str(context.exception), "ParentNode requires a non-None tag.")

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(str(context.exception), "ParentNode requires a non-empty list of children.")

    def test_repr_output(self):
        c = LeafNode("p", "Text", props={"class": "text"})
        p = ParentNode("div", [c], props={"id": "container"})
        expected_start = "ParentNode(tag='div', children=[LeafNode(tag='p', value='Text', props={'class': 'text'})], props={'id': 'container'})"
        self.assertEqual(repr(p), expected_start)

if __name__ == "__main__":
    unittest.main()
