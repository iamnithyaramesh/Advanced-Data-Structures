# Graph represented as an adjacency list with color placeholders
arr = [[[1, 2], None], [[0, 2], None], [[1, 3], None], [[2, 0], None]]

# List of possible colors
colors = ['R', 'G', 'B']

# List to store all valid ways to color the graph
ways = []

# Depth-First Search function to explore all colorings
def dfs(node, arr):
    # Try to color the current node with each color in 'colors'
    for c in colors:
        flag = True  # Flag to check if the color can be used

        # Check if any adjacent node has the same color
        for v in arr[node][0]:
            if c == arr[v][1]:  # If adjacent node has the same color
                flag = False  # Set flag to False
                break  # No need to check further, break out of the loop

        # If the color is valid (not used by any adjacent node)
        if flag:
            arr[node][1] = c  # Assign the color to the current node

            # Recursively try to color all adjacent nodes
            for v in arr[node][0]:
                if arr[v][1] == None:  # If the adjacent node is not colored yet
                    dfs(v, arr)  # Recursively call dfs for the adjacent node

            # Check if the entire graph is colored
            full = True
            for v in arr:
                if v[1] == None:  # If any node is not colored
                    full = False  # Set full to False
                    break  # No need to check further, break out of the loop

            # If all nodes are colored, add the current coloring to 'ways'
            if full:
                ways.append([v[1] for v in arr])  # Store the coloring

            # Backtrack: Remove the color from the current node to try other colorings
            arr[node][1] = None

# Start the DFS from the first node (node 0)
dfs(0, arr)

# Print the number of valid colorings found
print(len(ways))

# Print each valid coloring
for way in ways:
    print(way)
