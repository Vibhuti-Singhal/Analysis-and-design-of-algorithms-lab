"""
Program: Travelling Salesman Problem using Dynamic Programming
Author: Vibhuti Singhal
Description: Find the minimum cost of visiting every city exactly once
             and returning to the starting city.
Input: Adjacency distance matrix.
Output: Minimum tour cost.
"""
from typing import List

class TSPSolver:
    # Solve TSP using Dynamic Programming and Bitmasking
    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        """Return the minimum cost tour that visits every city and returns to the start."""
        n = len(dist_matrix)

        if n == 0:
            return 0

        dp = [[float('inf')] * n for _ in range(1 << n)]
        dp[1][0] = 0
        for mask in range(1 << n):
            for u in range(n):
                if dp[mask][u] == float('inf'):
                    continue

                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)

                        dp[new_mask][v] = min(dp[new_mask][v],
                            dp[mask][u] + dist_matrix[u][v])
        full_mask = (1 << n) - 1
        return min(
            dp[full_mask][u] + dist_matrix[u][0]
            for u in range(n))

n = int(input("Enter number of cities: "))

dist_matrix = []
print("Enter distance matrix:")
for i in range(n):
    dist_matrix.append(list(map(int, input().split())))
solver = TSPSolver()
print("Minimum Tour Cost:", solver.solve_tsp(dist_matrix))