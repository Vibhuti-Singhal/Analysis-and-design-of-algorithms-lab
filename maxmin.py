"""
Program: Kth Largest Element and Min-Max
Author: Vibhuti Singhal

Description:
Implements functions to find the kth largest element and the minimum-maximum pair in an unsorted list.

Input: An unsorted list of integers and k.
Output: The kth largest element and min-max pair.
"""
from typing import Tuple
def findKthLargest(nums: list[int], k: int) -> int:

    nums = sorted(nums, reverse=True)
    # Return the element at the required position.
    return nums[k - 1]

def findMinMax(nums: list[int]) -> Tuple[int, int]:

    return min(nums), max(nums)
    
nums = list(map(int, input("Enter unsorted array: ").split()))
k = int(input("Enter k: "))

print("Kth Largest Element:", findKthLargest(nums, k))
print("Min-Max:", findMinMax(nums))
