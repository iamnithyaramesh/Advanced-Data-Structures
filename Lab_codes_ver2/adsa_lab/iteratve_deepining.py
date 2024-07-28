def iddfs(graph):
    num_nodes = len(graph)
    
    # Depth-limited search function
    def dfs_limited(node, depth, path, visited):

        if depth == 0:
            return False  # Reached depth limit
        
        # Mark the current node as visited
        visited[node] = True
        path.append(node)
        
        # Explore neighbors of the current node
        for neighbor in range(num_nodes):
            if graph[node][neighbor] !=0 :  # There is a connection
                if neighbor in path:
                    # Found a cycle
                    print("Cycle found:", path + [neighbor])
                    return True
                elif not visited[neighbor]:
                    return dfs_limited(neighbor, depth - 1, path, visited)
                        
        
        # Unmark the current node and backtrack
        # p=path.pop()
        # visited[p] = False
        visited[node]=False
        path.pop()


        return False
    
    # Iterative deepening loop
   
    for depth_limit in range(1,num_nodes):
        
        for start in range(num_nodes):
            path = []
            visited = [False] * num_nodes
            if dfs_limited(start, depth_limit, path, visited):
                print(visited)
                return True  # Cycle found

    return False  # No cycle found within the maximum depth limit

# Example adjacency matrix representing a graph
adjacency_matrix = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

#adjacency_matrix=[
#  [0, 1, 0, 0, 0],
#  [0, 0, 1, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0]
# ]

# Call the iterative deepening search function
found_cycle = iddfs(adjacency_matrix)

if not found_cycle:
    print("No cycle found within the depth limit.")
