import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_single_image(self):
        text = "Here's an image ![alt](https://example.com/image.png)"
        expected = [("alt", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "Look ![one](url1) and ![two](url2)"
        expected = [("one", "url1"), ("two", "url2")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_image_with_empty_alt(self):
        text = "An image with no alt ![](image.jpg)"
        expected = [("", "image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_single_link(self):
        text = "Go to [Google](https://google.com)"
        expected = [("Google", "https://google.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_multiple_links(self):
        text = "Visit [Site1](url1) and [Site2](url2)"
        expected = [("Site1", "url1"), ("Site2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_link_with_exclamation(self):
        text = "This is an image ![desc](img.png) not a link"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_and_images(self):
        text = "Image ![pic](pic.jpg) and [link](url.com)"
        self.assertEqual(extract_markdown_images(text), [("pic", "pic.jpg")])
        self.assertEqual(extract_markdown_links(text), [("link", "url.com")])

    def test_extract_image_with_escaped_alt_text(self):
        text = "Image: ![alt text](image.jpg)"
        expected = [("alt text", "image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)


    def test_malformed_markdown(self):
        text = "Oops [broken(link.com"
        self.assertEqual(extract_markdown_links(text), [])

        text = "Oops ![broken(image.com"
        self.assertEqual(extract_markdown_images(text), [])

if __name__ == "__main__":
    unittest.main()
