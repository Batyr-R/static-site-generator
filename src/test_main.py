import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_extract_title2(self):
        md = """
This is **bolded** paragraph

# I AM AMAZING

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        result = extract_title(md)
        self.assertEqual(result, "I AM AMAZING")
