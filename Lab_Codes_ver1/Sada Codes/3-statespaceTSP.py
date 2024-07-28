class TSP:
    def __init__(self, graph, initial_city):
        self.graph = graph
        self.initial_city = initial_city
        self.num_cities = len(graph)
        self.visited = {city: False for city in graph.keys()}
        self.visited[initial_city] = True
        self.min_cost = float('inf')
        self.optimal_path = None
    
    def is_goal_state(self, state):
        return all(state.values())
    
    def get_unvisited_cities(self, state):
        return [city for city, visited in state.items() if not visited]
    
    def calculate_path_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i+1]]
        cost += self.graph[path[-1]][path[0]]  # Return to initial city
        return cost
    
    def depth_first_search(self, current_city, state, path, depth):
        if depth == self.num_cities:
            path_cost = self.calculate_path_cost(path)
            if path_cost < self.min_cost:
                self.min_cost = path_cost
                self.optimal_path = path[:]
            return
        for city in self.get_unvisited_cities(state):
            state[city] = True
            path.append(city)
            self.depth_first_search(city, state, path, depth + 1)
            path.pop()
            state[city] = False
    
    def breadth_first_search(self):
        queue = [(self.initial_city, [self.initial_city], self.visited.copy())]
        while queue:
            current_city, path, state = queue.pop(0)
            if self.is_goal_state(state):
                path_cost = self.calculate_path_cost(path)
                if path_cost < self.min_cost:
                    self.min_cost = path_cost
                    self.optimal_path = path
            else:
                for city in self.get_unvisited_cities(state):
                    new_path = path + [city]
                    new_state = state.copy()
                    new_state[city] = True
                    queue.append((city, new_path, new_state))
    
    def iterative_deepening_search(self):
        for depth_limit in range(self.num_cities):
            self.depth_first_search(self.initial_city, self.visited.copy(), [self.initial_city], 1)

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
initial_city = 'A'
tsp = TSP(graph, initial_city)

# Depth First Search
tsp.depth_first_search(initial_city, tsp.visited.copy(), [initial_city], 1)
print("Depth First Search - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

# Breadth First Search
tsp.breadth_first_search()
print("Breadth First Search - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

# Iterative Deepening Search
tsp.iterative_deepening_search()
print("Iterative Deepening Search - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)
