import unittest
from inline import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_links,
    text_node_to_html_node,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


class TestInline(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_italic_text(self):
        node = TextNode("italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")

    def test_code_text(self):
        node = TextNode("code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code text")

    def test_link_text(self):
        node = TextNode("anchor", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "anchor")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image_text(self):
        node = TextNode(
            "alt text", TextType.IMAGE, url="https://i.imgur.com/zjjcJKZ.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://i.imgur.com/zjjcJKZ.png", "alt": "alt text"},
        )

    def test_invalid_text_type_raises(self):
        class FakeTextType:
            pass

        node = TextNode("invalid", FakeTextType())
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_split_nodes_delimiter_code_block(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def text_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [example link](https://example.com)"
        )
        self.assertListEqual([("example link", "https://example.com")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [example link 1](https://example.com) and another [example link 2](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("example link 1", TextType.IMAGE, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("example link 2", TextType.IMAGE, "https://example.org"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
