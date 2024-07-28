class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        distance = [float('inf')] * self.vertices
        distance[source] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for edge in self.edges:
                if distance[edge.source] + edge.weight < distance[edge.destination]:
                    distance[edge.destination] = distance[edge.source] + edge.weight

        # Step 3: Check for negative-weight cycles
        for edge in self.edges:
            if distance[edge.source] + edge.weight < distance[edge.destination]:
                print("Graph contains negative weight cycle")
                return None

        return distance

# Example usage
vertices = 5
graph = Graph(vertices)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)

source = 0
distances = graph.bellman_ford(source)

if distances is not None:
    print(f"Vertex Distance from Source {source}")
    for i in range(vertices):
        print(f"{i}\t\t{distances[i]}")

'''

Explanation
Edge Class: Represents an edge in the graph with a source, destination, and weight.
Graph Class: Represents the graph with a specified number of vertices and a list to store all edges.
add_edge method: Adds an edge to the graph.
bellman_ford method: Implements the Bellman-Ford algorithm.
Bellman-Ford Algorithm:
Initialization: Distance to the source is set to 0, and all other distances are set to infinity.
Relaxation: For each vertex, the algorithm iterates through all edges and updates the distances.
Negative Cycle Check: After |V| - 1 iterations, the algorithm checks for negative-weight cycles. If any distance can still be updated, it indicates a negative cycle.
Example Usage: Creates a graph, adds edges, and computes the shortest path distances from a specified source vertex.
Example Output
For the provided graph:

Source vertex is 0.
The output shows the shortest distances from vertex 0 to all other vertices.
plaintext
Copy code
Vertex Distance from Source 0
0               0
1              -1
2               2
3              -2
4               1
This indicates that the shortest path from vertex 0 to vertex 3 has a distance of -2, demonstrating that the algorithm can handle negative weights. The presence of a negative weight cycle would be indicated by the message "Graph contains negative weight cycle".
'''