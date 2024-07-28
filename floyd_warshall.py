def floyd_warshall(graph):
    num_vertices = len(graph)
    # Initialize the solution matrix same as input graph matrix
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
 
    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]

    
    for i in range(num_vertices):
        dist[i][i] = 0

    # Update the solution matrix
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

distance_matrix = floyd_warshall(graph)

print("Shortest distances between every pair of vertices:")
for row in distance_matrix:
    print(row)


'''
Initialization:

num_vertices stores the number of vertices in the graph.
dist is initialized as a 2D list where dist[i][j] represents the shortest distance from vertex i to vertex j. Initially, it copies the input graph.
Distance from a vertex to itself:

Set dist[i][i] to 0 for all i, since the shortest distance from any vertex to itself is 0.
Main Algorithm:

The algorithm iterates through each possible intermediate vertex k and updates the shortest path from vertex i to vertex j considering k as an intermediate point.
If the path from i to j through k is shorter than the direct path from i to j, it updates dist[i][j].
Example Usage:

A graph is defined as a 2D list where graph[i][j] is the weight of the edge from vertex i to vertex j. If there is no edge, the weight is set to float('inf').
The floyd_warshall function is called with the graph, and the shortest distances between every pair of vertices are printed.
Example Output
Given the example graph:

0 -> 1: weight 3
0 -> 3: weight 5
1 -> 0: weight 2
1 -> 3: weight 4
2 -> 1: weight 1
3 -> 2: weight 2
The output shortest distance matrix will be:

Shortest distances between every pair of vertices:
[0, 3, 7, 5]
[2, 0, 6, 4]
[3, 1, 0, 5]
[5, 3, 2, 0]
This indicates that the shortest distance from vertex 0 to vertex 2 is 7, and so on for other pairs of vertices. The algorithm successfully computes the shortest paths between all pairs of vertices, handling positive and negative weights without any negative cycles.
'''
