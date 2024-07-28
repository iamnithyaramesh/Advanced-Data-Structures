# Function to implement the Floyd-Warshall algorithm
def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize the distance matrix with the graph's adjacency matrix
    dist =graph
    
    # Adding vertices individually
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

# Example usage
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

shortest_paths = floyd_warshall(graph)

print("Shortest distances between every pair of vertices:")
for row in shortest_paths:
    print(row)
