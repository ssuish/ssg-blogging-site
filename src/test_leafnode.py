import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_with_single_prop(self):
        node = LeafNode("h1", "Hello World", props={"class": "title"})
        self.assertEqual(node.to_html(), '<h1 class="title">Hello World</h1>')

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode(
            "p",
            "Lorem ipsum dolor sit amet.",
            props={
                "id": "intro",
                "class": "text-muted",
                "data-test": "paragraph-1",
            },
        )
        self.assertEqual(
            node.to_html(),
            '<p id="intro" class="text-muted" data-test="paragraph-1">Lorem ipsum dolor sit amet.</p>',
        )

    def test_leaf_to_html_raises_when_value_none(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
