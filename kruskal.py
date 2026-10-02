"""
Program: Kruskal's and Prim's Minimum Spanning Tree
Author: Vibhuti Singhal
Description: Finds the Minimum Spanning Tree of a weighted graph.

Input:
Number of vertices and weighted edges.

Output:
MST edges using Kruskal's and Prim's algorithms.
"""

from typing import List, NamedTuple


class Edge(NamedTuple):
    u: int
    v: int
    weight: int


class Graph:

    def __init__(self, vertices: int, edges: List[Edge]):
        self.vertices = vertices
        self.edges = edges

    def kruskal_mst(self) -> List[Edge]:
        edges = sorted(self.edges, key=lambda e: e.weight)

        parent = list(range(self.vertices))
        mst = []

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for edge in edges:
            u = find(edge.u)
            v = find(edge.v)

            if u != v:
                mst.append(edge)
                parent[u] = v

            if len(mst) == self.vertices - 1:
                break

        return mst

    def prim_mst(self) -> List[Edge]:
        visited = [False] * self.vertices
        mst = []

        visited[0] = True

        while len(mst) < self.vertices - 1:
            smallest = None

            for edge in self.edges:
                if visited[edge.u] != visited[edge.v]:
                    if smallest is None or edge.weight < smallest.weight:
                        smallest = edge

            if smallest is None:
                break

            mst.append(smallest)
            visited[smallest.u] = True
            visited[smallest.v] = True

        return mst


# Example graph
edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]

graph = Graph(4, edges)

print("Kruskal MST:", graph.kruskal_mst())
print("Prim MST:", graph.prim_mst())