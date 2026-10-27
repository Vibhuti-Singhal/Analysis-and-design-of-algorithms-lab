"""
Program: Dijkstra's and Bellman-Ford Algorithms
Author: Vibhuti Singhal
Description: Finds shortest distances from a source vertex.
Input:Number of vertices, weighted edges, and source vertex.
Output:Shortest distance arrays or a negative cycle message.
"""

from typing import List

class ShortestPath:

    def __init__(self, vertices: int, edges: List[tuple]):
        self.vertices = vertices
        self.edges = edges

    # Dijkstra's Algorithm
    def dijkstra(self, src: int) -> List[int]:
        dist = [float('inf')] * self.vertices
        visited = [False] * self.vertices
        dist[src] = 0

        for _ in range(self.vertices):
            u = -1

            # Find the unvisited vertex with minimum distance
            for i in range(self.vertices):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i

            if u == -1 or dist[u] == float('inf'):
                break

            visited[u] = True

            # Update distances of adjacent vertices
            for a, b, weight in self.edges:
                if a == u and not visited[b]:
                    dist[b] = min(dist[b], dist[u] + weight)

                if b == u and not visited[a]:
                    dist[a] = min(dist[a], dist[u] + weight)

        return dist

    # Bellman-Ford Algorithm
    def bellman_ford(self, src: int) -> List[int]:
        dist = [float('inf')] * self.vertices
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for a negative-weight cycle
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return []

        return dist

# Create a weighted graph
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]

graph = ShortestPath(4, edges)
src = 0

print("Dijkstra distances:", graph.dijkstra(src))

result = graph.bellman_ford(src)
if result:
    print("Bellman-Ford distances:", result)
else:
    print("Negative-weight cycle detected")