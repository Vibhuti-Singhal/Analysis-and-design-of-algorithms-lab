# Binary Search
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