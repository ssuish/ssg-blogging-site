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

    # TODO: Do a line-by-line check for heading, quote, unordered list, and ordered list (w/ increments)
    #       Keep the code block check implementation.

    for l in lines:
        match block:
            case re.search(r"^#{1,6} .+", block):
                return BlockType.HEADING
            case block if block.startswith("```/n") and block.endswith("```"):
                return BlockType.CODE
            case block.startswith(">"):
                return BlockType.QUOTE
            case block.startswith("- "):
                return BlockType.UNORDERED_LIST
            case re.search(r"^(\d+)\. .+", block):
                return BlockType.ORDERED_LIST
            case _:
                return BlockType.PARAGRAPH
