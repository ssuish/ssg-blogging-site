import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()

        if not block:
            continue

        lines = [x.strip() for x in block.split("\n")]
        result.append("\n".join(lines))

    return result


def block_to_block_type(block):
    lines = block.split("\n")

    if re.search(r"^#{1,6} .+", block):
        return BlockType.HEADING

    if len(lines) > 1 and block.startswith("```/n") and block.endswith("```"):
        return BlockType.CODE

    if lines[0].startswith(">"):
        for l in lines[1:]:
            if not l.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if lines[0].startswith("- "):
        for l in lines[1:]:
            if not l.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for l in lines:
            if not l.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

# TODO: Create helper functions to handle block type to html tag, then use it to build ParentNode. Note: Quote is <blockquote>
# TODO: Handle special cases for code block: <pre><code> value </code></pre>
# TODO: Handle special case for ol and ul: <ul><li> value </li> ... </ul>
# TODO: Handle special case for headings: <h1> ... <h6> Note: Should count based on the number of '#' chars


def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)

    for block in blocks:
        block_type = block_to_block_type(block)

# TODO: text_to_children should handle inline markdown within each block

def text_to_children(text):
    pass
