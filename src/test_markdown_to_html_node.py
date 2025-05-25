import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_codeblock(self):
        md = """
 ```
 This is text that _should_ remain
 the **same** even with inline stuff
 ```
 """
    
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_levels(self):
        for i in range(1, 7):
            hashes = "#" * i
            md = f"{hashes} Heading {i}"
            html = markdown_to_html_node(md).to_html()
            self.assertEqual(html, f"<div><h{i}>Heading {i}</h{i}></div>")

    def test_quote_block(self):
        md = """> This is a quote
> with multiple lines"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote\nwith multiple lines</blockquote></div>")

    def test_unordered_list(self):
        md = "- item 1\n- item 2\n- item 3"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item 1</li><li>item 2</li><li>item 3</li></ul></div>"
        )

    def test_ordered_list(self):
        md = "1. first\n2. second\n3. third"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>"
        )

    def test_inline_formatting_in_paragraph(self):
        md = "This has _italic_, **bold**, and `code`."
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p>This has <i>italic</i>, <b>bold</b>, and <code>code</code>.</p></div>"
        )

if __name__ == "__main__":
    unittest.main()

