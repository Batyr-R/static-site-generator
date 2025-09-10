import re
from typing_extensions import NewType

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 != 1:
            raise Exception(f"{delimiter} unmatched in {node.text}")
        for i in range(len(parts)):
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^()]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue
        for image in images:
            splited = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splited) == 1:
                new_nodes.append(TextNode(text, TextType.TEXT))
                break
            left = splited[0]
            right = splited[1]
            if left != "":
                new_nodes.append(TextNode(left, TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = right
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue
        for link in links:
            splited = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splited) == 1:
                new_nodes.append(TextNode(text, TextType.TEXT))
                break
            left = splited[0]
            right = splited[1]
            if left != "":
                new_nodes.append(TextNode(left, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = right
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
