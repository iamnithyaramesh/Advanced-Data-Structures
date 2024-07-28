import math
import random

def distance(node1, node2):
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

def tsp_nearest_neighbor(nodes):
    start_node = random.choice(nodes)
    path = [start_node]
    unvisited = set(nodes)
    unvisited.remove(start_node)

    current_node = start_node
    while unvisited:
        nearest_node = min(unvisited, key=lambda node: distance(current_node, node))
        path.append(nearest_node)
        unvisited.remove(nearest_node)
        current_node = nearest_node

    path.append(start_node)  # Return to the start node to complete the path
    return path

# Example usage
nodes = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 0)]
path = tsp_nearest_neighbor(nodes)
print(f"Path: {path}")
