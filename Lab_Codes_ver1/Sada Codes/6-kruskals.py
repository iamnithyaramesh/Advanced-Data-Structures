# Initialize the parent array
n = int(input("Enter the number of nodes: "))
parent = [i for i in range(n + 1)]  # Initialize each node as its own parent
#parent = {chr(ord('A') + i): chr(ord('A') + i) for i in range(n)}


# Define functions for union-find operations
def find_parent(node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find_parent(parent[node])  # Path compression
        return parent[node]

def union(n1, n2):
    p1 = find_parent(n1)
    p2 = find_parent(n2)
    
    if p1 != p2:
        parent[p1] = p2
    # No else condition needed for Kruskal's algorithm

# Input the edges and weights
graph = []
e = int(input("Enter the number of edges: "))
for i in range(e):
    n1 = int(input("Enter node 1: "))
    n2 = int(input("Enter node 2: "))
    wt = int(input("Enter weight: "))
    graph.append((wt, (n1, n2)))

# Sort the edges based on weight
graph = sorted(graph)

# Perform Kruskal's algorithm to find the MST
mst = []
for edge in graph:
    weight, (n1, n2) = edge
    
    if find_parent(n1) != find_parent(n2):  # Check if adding edge creates a cycle
        union(n1, n2)
        mst.append((n1, n2, weight))

print("Minimum Spanning Tree (MST):", mst)
