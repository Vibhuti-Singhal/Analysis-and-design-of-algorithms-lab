
"""
Program: 0/1 Knapsack using Dynamic Programming
Author: Vibhuti Singhal
Description: Find the maximum value of items that can be
             placed in a knapsack without exceeding its capacity.
Input: Item weights, item values and knapsack capacity.
Output: Maximum possible value using 2D and 1D DP.
"""

from typing import List


# 0/1 Knapsack using 2D Dynamic Programming
def knapsack_01_2d(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# 0/1 Knapsack using 1D Dynamic Programming
def knapsack_01_1d(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


weights = list(map(int, input("Enter item weights: ").split()))
values = list(map(int, input("Enter item values: ").split()))
capacity = int(input("Enter knapsack capacity: "))

print("Maximum value using 2D DP:", knapsack_01_2d(weights, values, capacity))
print("Maximum value using 1D DP:", knapsack_01_1d(weights, values, capacity))
