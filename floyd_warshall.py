"""
Program: Floyd-Warshall and Optimal Binary Search Tree
Author: Vibhuti Singhal
Description: Find all-pairs shortest paths using Floyd-Warshall
             and minimum search cost using Optimal BST.
Input: Distance matrix, keys and their frequencies.
Output: Shortest path matrix and minimum OBST cost.
"""
from typing import List

# Find shortest paths between all pairs of vertices
def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    """Return the shortest distance matrix using Floyd-Warshall algorithm."""
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Find the minimum search cost of an Optimal Binary Search Tree
def optimal_bst(keys: List[int], freq: List[int]) -> int:
    """Return the minimum search cost of an Optimal Binary Search Tree."""
    n = len(keys)
    if n == 0:
        return 0
        
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]

# Taking input for Floyd-Warshall
n = int(input("Enter number of vertices: "))
graph = []

print("Enter distance matrix (use 99999 for infinity):")
for i in range(n):
    graph.append(list(map(int, input().split())))

result = floyd_warshall(graph)

print("Shortest Path Matrix:")
for row in result:
    print(row)

# Taking input for Optimal BST
keys = list(map(int, input("Enter sorted keys: ").split()))
freq = list(map(int, input("Enter frequencies: ").split()))
print("Minimum Optimal BST Cost:", optimal_bst(keys, freq))