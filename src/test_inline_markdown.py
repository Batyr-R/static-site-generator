import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType

class TestDelimiterSplit(unittest.TestCase):
    def simple(self):
        result = split_nodes_delimiter([TextNode("a`b`c", TextType.TEXT)], "`", TextType.CODE)
        self.assertEqual(result, [TextNode("a", TextType.TEXT), TextNode("b", TextType.CODE), TextNode("c", TextType.TEXT)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
if __name__ == "__main__":
    unittest.main()
