from multiprocessing import Value
from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode):

    if text_node.text_type not in TextType:
        raise ValueError("Invalid text type")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise ValueError("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        delimiter_count = node.text.count(delimiter)

        if delimiter_count == 0:
            new_nodes.append(node)
            continue

        if delimiter_count % 2 == 1:
            raise ValueError("Invalid Markdown syntax")

        substrings = node.text.split(delimiter)

        for i in range(0, len(substrings)):
            part = substrings[i]

            if part == None or part == "":
                continue

            if i % 2 == 0:
                new_node = TextNode(part, TextType.TEXT)
            else:
                new_node = TextNode(part, text_type)
            
            new_nodes.append(new_node)
    print(new_nodes)
    return new_nodes

