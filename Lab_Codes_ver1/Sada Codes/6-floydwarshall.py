# Define the Floyd-Warshall algorithm function
def floyd_warshall(graph):
    # Get the number of vertices in the graph
    num_vertices = len(graph)
    
    # Initialize the distance matrix with the given graph
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    # Fill in the initial distances based on the graph's adjacency matrix
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Perform the Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance if a shorter path is found
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example usage
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

# Run the Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Print the result
print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
