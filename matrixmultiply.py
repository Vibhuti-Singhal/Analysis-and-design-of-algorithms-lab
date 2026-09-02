"""
Program: Strassen Matrix Multiplication
Author: Vibhuti Singhal

Description:
Implements Strassen's algorithm to multiply two square matrices.

Input: Two square matrices entered by the user.
Output: Product matrix.
"""

from typing import List
def add_matrix(A: List[List[int]],
               B: List[List[int]]) -> List[List[int]]:
    
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)]
            for i in range(n)]


def subtract_matrix(A: List[List[int]],
                     B: List[List[int]]) -> List[List[int]]:
    
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)]
            for i in range(n)]


def strassen_multiply(A: List[List[int]],
                      B: List[List[int]]) -> List[List[int]]:
    
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    # Divide matrix A into four parts.
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide matrix B into four parts.
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate the seven Strassen products.
    M1 = strassen_multiply(add_matrix(A11, A22),
                           add_matrix(B11, B22))

    M2 = strassen_multiply(add_matrix(A21, A22), B11)

    M3 = strassen_multiply(A11,
                           subtract_matrix(B12, B22))

    M4 = strassen_multiply(A22,
                           subtract_matrix(B21, B11))

    M5 = strassen_multiply(add_matrix(A11, A12), B22)

    M6 = strassen_multiply(subtract_matrix(A21, A11),
                           add_matrix(B11, B12))

    M7 = strassen_multiply(subtract_matrix(A12, A22),
                           add_matrix(B21, B22))

    # Calculate the four result blocks.
    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(subtract_matrix(add_matrix(M1, M3), M2), M6)

    # Combine the four blocks.
    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])

    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result

n = int(input("Enter the size of matrix (power of 2): "))

print("Enter Matrix A:")
A = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    A.append(row)

print("\nEnter Matrix B:")
B = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    B.append(row)

C = strassen_multiply(A, B)
print("\nProduct Matrix:")
for row in C:
    print(*row)