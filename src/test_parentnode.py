import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
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

    def test_missing_tag_raises(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_missing_children_raises(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_parent_with_multiple_children(self):
        child_one = LeafNode("span", "one")
        child_two = LeafNode("span", "two")
        parent_node = ParentNode("div", [child_one, child_two])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>one</span><span>two</span></div>",
        )

    def test_nested_parents_with_props(self):
        inner_child = LeafNode("span", "inner")
        inner_parent = ParentNode("div", [inner_child], props={"id": "inner"})
        outer_parent = ParentNode("section", [inner_parent], props={"class": "outer"})
        self.assertEqual(
            outer_parent.to_html(),
            '<section class="outer"><div id="inner"><span>inner</span></div></section>',
        )

if __name__ == "__main__":
    unittest.main()
