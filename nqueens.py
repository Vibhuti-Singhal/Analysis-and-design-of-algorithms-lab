"""
Program: N-Queens Problem using Backtracking
Author: Vibhuti Singhal
Description: Place N queens on an N x N chessboard such that no two queens
             attack each other. Find all valid board configurations.
Input: Board dimension N.
Output: All valid N-Queens board configurations.
"""
from typing import List

# N-Queens using Backtracking
def solveNQueens(n: int) -> List[List[str]]:
    result = []
    board = [["."] * n for _ in range(n)]

    def is_safe(row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row: int):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."
    backtrack(0)
    return result

n = int(input("Enter board dimension: "))
solutions = solveNQueens(n)
print("Total number of solutions:", len(solutions))

for index, solution in enumerate(solutions, start=1):
    print(f"\nSolution {index}:")
    for row in solution:
        print(row)