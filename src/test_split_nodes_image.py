import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode("No images here!", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_non_text_node_untouched(self):
        node = TextNode("Not text", TextType.IMAGE, "img.jpg")
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_image_at_start_and_end(self):
        node = TextNode(
            "![first](a.png) middle ![second](b.png)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "a.png"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "b.png"),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()

