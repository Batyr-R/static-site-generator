import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
 This is **bolded** paragraph


  This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks3(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        block = "I am cool"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)


    def test_block_to_block_type2(self):
        block = "#### I am cool"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_block_to_block_type3(self):
        block = """
>I
>am
>cool
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_to_block_type4(self):
        block = """
- I
- am
- cool
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_block_to_block_type5(self):
        block = """
1. I
2. am
3. cool
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_block_to_block_type6(self):
        block = "```I am cool```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

if __name__ == "__main__":
    unittest.main()
