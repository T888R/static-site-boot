import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestTextToTextNode(unittest.TestCase):
    def test_bold(self):
        text = "Hello this should be **bold text**"
        node_list = [
            TextNode("Hello this should be ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD)
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

    def test_double_bold(self):
        text = "Hello this should be **bold text** and heres **number two** bold"
        node_list = [
            TextNode("Hello this should be ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and heres ", TextType.TEXT),
            TextNode("number two", TextType.BOLD),
            TextNode(" bold", TextType.TEXT)
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

    def test_mixed_italic_and_bold(self):
        text = "Hello this should be *italic text* and heres **number two** bold"
        node_list = [
            TextNode("Hello this should be ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" and heres ", TextType.TEXT),
            TextNode("number two", TextType.BOLD),
            TextNode(" bold", TextType.TEXT)
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

    def test_links(self):
        text = "Here is a [link](https://boot.dev)"
        node_list = [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

    def test_images(self):
        text = "Here is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        node_list = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

    def test_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_list = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnode(text), node_list)

if __name__ == "__main__":
    unittest.main()

