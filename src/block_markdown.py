from enum import Enum

from htmlnode import ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

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

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for b in blocks:
        block_type = block_to_block_type(b)
        if block_type == BlockType.HEADING:
            level = 0
            for char in b:
                if char == "#":
                    level += 1
                else:
                    break
            text = b[level + 1:]
            block_node = ParentNode(f"h{level}", text_to_children(text))

        elif block_type == BlockType.QUOTE:
            lines = b.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            block_node = ParentNode("blockquote", text_to_children(content))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = b.split("\n")
            html_items = []
            for line in lines:
                text = line[2:]
                children = text_to_children(text)
                html_items.append(ParentNode("li", children))
            block_node = ParentNode("ul", html_items)

        elif block_type == BlockType.ORDERED_LIST:
            lines = b.split("\n")
            html_items = []
            for line in lines:
                text = line[3:]
                children = text_to_children(text)
                html_items.append(ParentNode("li", children))
            block_node = ParentNode("ol", html_items)

        elif block_type == BlockType.CODE:
            code_text = b[4:-3]
            text_node = TextNode(code_text, TextType.TEXT)
            code_html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [code_html_node])
            block_node = ParentNode("pre", [code_node])

        else:
            block_node = ParentNode("p", text_to_children(b))
        block_nodes.append(block_node)
    return ParentNode("div", block_nodes)
