import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different(self):
        node = TextNode("This is a test text node", TextType.IMAGE)
        node2 = TextNode("THis is another test text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_url_diff(self):
        node = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        node2 = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690")
        self.assertNotEqual(node, node2)

    def test_eq_url_eq(self):
        node = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        node2 = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()