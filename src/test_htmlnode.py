import unittest

from htmlnode import LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
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

    def test_basic_eq(self):
        child_node = LeafNode("lol", "child")
        child_node2 = LeafNode("lol", "child")
        node = ParentNode("div", [child_node])
        node2 = ParentNode("div", [child_node2])
        self.assertEqual(node, node2)

    def test_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = LeafNode("span", [grandchild_node])
        node = ParentNode("div", [child_node])
        child_node2 = LeafNode("span", "child")
        node2 = ParentNode("div", [child_node2])
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
