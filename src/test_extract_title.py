import unittest
from site_generator import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_valid_title_single_line(self):
        md = "# Welcome"
        self.assertEqual(extract_title(md), "Welcome")

    def test_valid_title_with_whitespace(self):
        md = "   #   Hello World   "
        self.assertEqual(extract_title(md.strip()), "Hello World")

    def test_title_with_punctuation(self):
        md = "# Welcome to my site!"
        self.assertEqual(extract_title(md), "Welcome to my site!")

    def test_multiple_headings_uses_first_h1(self):
        md = """
# First Title
## Second Title
# Third Title
"""
        self.assertEqual(extract_title(md), "First Title")

    def test_raises_exception_if_no_h1(self):
        md = """
## This is h2
Paragraph text here.
"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("No h1", str(context.exception))

if __name__ == "__main__":
    unittest.main()
