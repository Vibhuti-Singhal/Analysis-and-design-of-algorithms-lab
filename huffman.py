"""
Program: Huffman Coding
Author: Vibhuti Singhal
Description: Builds a Huffman tree using character frequencies
and generates binary encoding mappings.

Input: A dictionary containing characters and their frequencies.
Output: Huffman codes for each character.
"""
import heapq
from typing import Dict
class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoder:

    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequencies cannot be empty.")
        
        if any(freq <= 0 for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive.")
        
        heap = [
            Node(char, freq)
            for char, freq in frequencies.items()
        ]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        self.root = heap[0]
        return self.root
    
    def generate_codes(self) -> Dict[str, str]:
        
        if self.root is None:
            raise ValueError("Build the Huffman tree first.")
        self.codes = {}

        def traverse(node, code):
            if node is None:
                return
            # Leaf node represents a character
            if node.char is not None:
                self.codes[node.char] = code or "0"
                return
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
        traverse(self.root, "")
        return self.codes
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}
coder = HuffmanCoder()
coder.build_tree(frequencies)
codes = coder.generate_codes()
print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(char, ":", code)