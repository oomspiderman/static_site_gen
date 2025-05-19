import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "Visit [Boot.dev](https://www.boot.dev) and [YouTube](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("YouTube", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode("This text has no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_non_text_node_untouched(self):
        node = TextNode("Already a link", TextType.LINK, "https://example.com")
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_link_at_start_and_end(self):
        node = TextNode(
            "[Start](s.com) middle [End](e.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.LINK, "s.com"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("End", TextType.LINK, "e.com"),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
