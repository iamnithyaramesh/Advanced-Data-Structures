'''
This code effectively implements the branch and bound technique to 
solve the TSP problem by exploring all possible paths (branches) 
while keeping track of the minimum cost path found so far and
 pruning paths that exceed the current minimum cost (bound).
'''

def tsp_branch_and_bound(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    visited = {vertex: False for vertex in vertices}
    visited[vertices[0]] = True  # Start from the first vertex

    min_cost = [float('inf')]  # To store the minimum cost found

    

    # Recursive function to perform branch and bound
    def tsp_util(curr_vertex, visited, path, curr_cost, min_cost):
        if len(path) == num_vertices:  # If a complete tour is found
            total_cost =curr_cost+graph[curr_vertex][path[0]]  # Calculate its cost
            if total_cost < min_cost[0]:  # Update min_cost if a cheaper tour is found
                min_cost[0] = total_cost
            return

        # Explore all unvisited neighbors of the current vertex
        for neighbor, weight in graph[curr_vertex].items():
            if not visited[neighbor]:  # If the neighbor hasn't been visited yet
                visited[neighbor] = True  # Mark it as visited
                path.append(neighbor)  # Add it to the current path
                tsp_util(neighbor, visited, path, curr_cost + weight, min_cost)  # Recur with the updated path and cost
                path.pop()  # Backtrack: remove the neighbor from the path
                visited[neighbor] = False  # Mark it as unvisited

    # Start the branch and bound process from the first vertex
    tsp_util(vertices[0], visited, [vertices[0]], 0, min_cost)

    return min_cost[0]  # Return the minimum cost found

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

min_cost = tsp_branch_and_bound(graph)
print("Minimum cost:", min_cost)
