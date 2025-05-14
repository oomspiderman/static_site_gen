import unittest
from htmlnode import HTMLNode

#==============================================================================================

# # Basic element with tag and value only
# basic_node = HTMLNode(tag="p", value="Hello world!")

# # Node with attributes (props)
# link_node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})

# # Node with no tag (e.g., raw text only)
# text_node = HTMLNode(value="Just text with no tag.")

# # Node with children only
# parent_node = HTMLNode(
#     tag="ul",
#     children=[
#         HTMLNode(tag="li", value="Item 1"),
#         HTMLNode(tag="li", value="Item 2")
#     ]
# )

# # Node with both children and value (edge case)
# mixed_node = HTMLNode(
#     tag="div",
#     value="Parent value",
#     children=[
#         HTMLNode(tag="p", value="Child paragraph")
#     ],
#     props={"class": "container"}
# )

# # Node with deeply nested structure
# deep_node = HTMLNode(
#     tag="html",
#     children=[
#         HTMLNode(tag="body", children=[
#             HTMLNode(tag="div", children=[
#                 HTMLNode(tag="h1", value="Title"),
#                 HTMLNode(tag="p", value="Some content here.")
#             ])
#         ])
#     ]
# )

#==============================================================================================

class TestHTMLNode(unittest.TestCase):

    def test_basic_node(self):
        node = HTMLNode(tag="p", value="Hello world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props(self):
        node = HTMLNode(tag="a", value="Click", props={"href": "https://example.com"})
        self.assertEqual(node.props["href"], "https://example.com")

    def test_text_only_node(self):
        node = HTMLNode(value="Raw text")
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, "Raw text")

    def test_children(self):
        child1 = HTMLNode(tag="li", value="One")
        child2 = HTMLNode(tag="li", value="Two")
        parent = HTMLNode(tag="ul", children=[child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].value, "One")

    def test_repr(self):
        node = HTMLNode(tag="span", value="hello", props={"class": "note"})
        expected = "HTMLNode(tag='span', value='hello', children=[], props={'class': 'note'})"
        self.assertEqual(repr(node), expected)