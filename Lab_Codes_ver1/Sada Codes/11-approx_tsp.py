import sys

def tsp_nearest_neighbor(graph):
    n = len(graph)
    visited = [False] * n
    path = [0]  
    total_cost = 0
    current_city = 0
    visited[current_city] = True
    for _ in range(n - 1):
        nearest_city = None
        min_distance = sys.maxsize
        for i in range(n):
            if not visited[i] and graph[current_city][i] < min_distance:
                min_distance = graph[current_city][i]
                nearest_city = i
        path.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
        visited[current_city] = True
    total_cost += graph[current_city][0]
    path.append(0)
    return path, total_cost

graph = [
    [0, 10, 15, 20],  # Distances from city 0 to other cities
    [10, 0, 35, 25],  # Distances from city 1 to other cities
    [15, 35, 0, 30],  # Distances from city 2 to other cities
    [20, 25, 30, 0]   # Distances from city 3 to other cities
]

best_path, best_cost = tsp_nearest_neighbor(graph)

print("Best Path:", best_path)
print("Best Cost:", best_cost)