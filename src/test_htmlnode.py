import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_one_attr(self):
        node1 = HTMLNode(tag="h1", value="Hello World", props={"class": "title"})
        self.assertEqual(node1.props_to_html(), ' class="title"')

    def test_props_to_html_multiple_attr(self):
        node2 = HTMLNode(
            tag="p",
            value="Lorem ipsum dolor sit amet.",
            props={
                "id": "intro",
                "class": "text-muted",
                "data-test": "paragraph-1",
            },
        )
        self.assertEqual(
            node2.props_to_html(),
            ' id="intro" class="text-muted" data-test="paragraph-1"',
        )

    def test_props_to_html_link(self):
        node3 = HTMLNode(
            tag="a",
            value="Click here",
            props={
                "href": "https://example.com",
                "target": "_blank",
                "rel": "noopener",
            },
        )
        self.assertEqual(
            node3.props_to_html(),
            ' href="https://example.com" target="_blank" rel="noopener"',
        )


if __name__ == "__main__":
    unittest.main()
