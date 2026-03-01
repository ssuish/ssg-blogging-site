def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()

        if not block:
            continue

        lines = [x.strip() for x in block.split("\n")]
        result.append("\n".join(lines))

    return result
