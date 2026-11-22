"""
Program: Graph Coloring and Hamiltonian Cycle using Backtracking
Author: Vibhuti Singhal
Description: Implement graph coloring and Hamiltonian cycle using backtracking.
             Graph coloring assigns colors to vertices so that adjacent vertices
             have different colors. Hamiltonian cycle visits every vertex exactly
             once and returns to the starting vertex.
Input: Number of vertices, adjacency matrix, and number of colors.
Output: Valid vertex color mapping and Hamiltonian cycle.
"""
from typing import List

class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.V = len(graph)

    # Graph Coloring using Backtracking
    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.V

        def is_safe(vertex: int, color: int) -> bool:
            for i in range(self.V):
                if self.graph[vertex][i] == 1 and colors[i] == color:
                    return False
            return True

        def solve(vertex: int) -> bool:
            if vertex == self.V:
                return True

            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color
                    if solve(vertex + 1):
                        return True
                    colors[vertex] = 0
            return False

        if solve(0):
            return colors
        return []

    # Hamiltonian Cycle using Backtracking
    def hamiltonian_cycle(self) -> List[int]:
        path = [-1] * self.V
        path[0] = 0

        def is_safe(vertex: int, pos: int) -> bool:
            if self.graph[path[pos - 1]][vertex] == 0:
                return False
            if vertex in path[:pos]:
                return False
            return True

        def solve(pos: int) -> bool:
            if pos == self.V:
                return self.graph[path[pos - 1]][path[0]] == 1

            for vertex in range(1, self.V):
                if is_safe(vertex, pos):
                    path[pos] = vertex
                    if solve(pos + 1):
                        return True
                    path[pos] = -1
            return False
        if solve(1):
            return path + [path[0]]
        return []

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))
obj = GraphBacktracker(graph)
coloring = obj.graph_coloring(m)
cycle = obj.hamiltonian_cycle()

if coloring:
    print("Vertex color mapping:", coloring)
else:
    print("No valid graph coloring possible.")

if cycle:
    print("Hamiltonian cycle:", cycle)
else:
    print("No Hamiltonian cycle exists.")