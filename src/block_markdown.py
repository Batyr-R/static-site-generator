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
    i = 0
    while i < len(blocks):
        block = blocks[i].strip()
        i += 1
        if block == "":
            continue
        result.append(block)
    return result

def block_to_block_type(block):
    if " " in block:
        before_space = block[:block.index(" ")]
    else:
        before_space = ""

    if before_space == "#" * len(before_space) and len(before_space) >= 1 and len(before_space) <= 6:
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    block_lines = block.split("\n")
    while block_lines and block_lines[0] == "":
        block_lines.pop(0)
    while block_lines and block_lines[-1] == "":
        block_lines.pop()

    quote_check = True
    for l in block_lines:
        if not l.startswith(">"):
            quote_check = False
            break
    if quote_check == True:
        return BlockType.QUOTE

    unor_check = True
    for l in block_lines:
        if not l.startswith("- "):
            unor_check = False
            break
    if unor_check == True:
        return BlockType.UNORDERED_LIST

    or_check = True
    for i in range(len(block_lines)):
        if not block_lines[i].startswith(f"{i+1}. "):
            or_check = False
            break
    if or_check == True:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
