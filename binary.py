"""
Program: Binary Search and Fast Power
Author: Vibhuti Singhal

Description:
Implements recursive Binary Search and Fast Power algorithms.

Input: Sorted list, target value, base, and exponent.
Output: Target index/status and calculated power.
"""
# Binary Search
def search(nums: list[int], target: int) -> int:
    # Recursively searches within the specified range.
    def binary_search(left, right):
        if left > right:
            return -1

        # Determine the middle index of the current range.
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        
        else:
            return binary_search(left, mid - 1)

    # Initiate the search over the entire list.
    return binary_search(0, len(nums) - 1)

# Fast Power
def myPow(x: float, n: int) -> float:

    # Base case: any number raised to the power 0 is 1.
    if n == 0:
        return 1.0

    # Handle negative exponents using the reciprocal.
    if n < 0:
        return 1 / myPow(x, -n)

    # Recursively calculate the power for half the exponent.
    half = myPow(x, n // 2)

    # For even exponents, square the half result.
    if n % 2 == 0:
        return half * half

    # For odd exponents, multiply the result by the base.
    else:
        return x * half * half

print("Binary Search Program")

nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
index = search(nums, target)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found")

print("Fast Power Program")

x = float(input("Enter base: "))
n = int(input("Enter exponent: "))
print("Power =", myPow(x, n))# Binary Search
def search(nums: list[int], target: int) -> int:
    # Recursive Binary Search function
    def binary_search(left, right):
        if left > right:
            return -1

        mid = left +(right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    return binary_search(0, len(nums) - 1)

# Fast Power
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / myPow(x, -n)
    half = myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
    
print( "Binary Search Program")
nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
index = search(nums, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found")

print( "Fast Power Program")
x = float(input("Enter base: "))
n = int(input("Enter exponent: "))
print("Power =", myPow(x, n))
