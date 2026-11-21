"""
Program: Longest Increasing Subsequence using Dynamic Programming
Author: Vibhuti Singhal
Description: Find the length of the longest strictly increasing
             subsequence in a given integer array.
Input: A list of integers.
Output: Length of the longest increasing subsequence.
"""
from typing import List

# Find the length of the Longest Increasing Subsequence
def lengthOfLIS(nums: List[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    n = len(nums)

    if n == 0:
        return 0

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

nums = list(map(int, input("Enter array elements: ").split()))

print("Length of Longest Increasing Subsequence:", lengthOfLIS(nums))