"""
Program: KMP String Matching and Reservoir Sampling
Author: Vibhuti Singhal
Description: Find a pattern in a text using KMP algorithm and
             select a random element from a data stream.
Input: Text and pattern strings, and stream elements.
Output: Starting index of pattern and randomly sampled element.
"""

from typing import List
import random


# Find the starting index of a pattern in text using KMP
def strStr(haystack: str, needle: str) -> int:
    """Return the first occurrence index of needle in haystack using KMP."""
    if needle == "":
        return 0

    m = len(needle)
    n = len(haystack)

    lps = [0] * m
    j = 0

    # Build the LPS array
    i = 1
    while i < m:
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    # Search for the pattern in text
    i = 0
    j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == m:
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


class Randomizer:
    # Select a random element from a data stream
    def __init__(self, stream: List[int]):
        """Initialize the randomizer and sample one element from the stream."""
        self.sample = None
        count = 0

        for num in stream:
            count += 1
            if random.randint(1, count) == 1:
                self.sample = num

    def getRandom(self) -> int:
        """Return the randomly selected element from the stream."""
        return self.sample


# Taking input for KMP
haystack = input("Enter text: ")
needle = input("Enter pattern: ")

print("Pattern found at index:", strStr(haystack, needle))


# Taking input for Reservoir Sampling
stream = list(map(int, input("Enter stream elements: ").split()))

randomizer = Randomizer(stream)
print("Randomly selected element:", randomizer.getRandom())