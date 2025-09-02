import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode("p", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode("a", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = HTMLNode("p", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode("p", "I am cool", None,{
            "href": "https://www.boot.dev",
            "target": "_blank",
        })
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "I am cool", None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
