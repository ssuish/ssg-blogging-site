import unittest
from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello ")

        self.assertEqual(title, "Hello")

        with self.assertRaises(ValueError):
            extract_title("## Hello")


if __name__ == "__main__":
    unittest.main()
