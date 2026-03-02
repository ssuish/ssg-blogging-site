import unittest
from block import block_to_block_type, markdown_to_blocks


class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
                """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_BlockType(self):
        # TODO: Do a test for every block type

        md = """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
                """
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            [
                "paragraph",
                "paragraph",
                "unordered list",
            ],
        )


if __name__ == "__main__":
    unittest.main()
