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

    def actions(self, state):
        return [city for city, visited in state.items() if not visited]

    def path_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i+1]]
        cost += self.graph[path[-1]][path[0]]  # Return to initial city
        return cost

    def dfs(self, current_city, state, path, depth):
        if depth == self.num_cities:
            path_cost = self.path_cost(path)
            if path_cost < self.min_cost:
                self.min_cost = path_cost
                self.optimal_path = path[:]
            return
        for city in self.actions(state):
            state[city] = True
            path.append(city)
            self.dfs(city, state, path, depth + 1)
            path.pop()
            state[city] = False

    def bfs(self):
        queue = [(self.initial_city, [self.initial_city], self.visited.copy())]
        while queue:
            current_city, path, state = queue.pop(0)
            if self.is_goal_state(state):
                path_cost = self.path_cost(path)
                if path_cost < self.min_cost:
                    self.min_cost = path_cost
                    self.optimal_path = path
            else:
                for city in self.actions(state):
                    new_path = path + [city]
                    new_state = state.copy()
                    new_state[city] = True
                    queue.append((city, new_path, new_state))

    def iterative_deepening(self):
        for depth_limit in range(1, self.num_cities + 1):
            self.dfs(self.initial_city, self.visited.copy(), [self.initial_city], 1)

graph = {
    'A': {'B': 30, 'C': 15},
    'B': {'A': 45, 'C': 12},
    'C': {'A': 15, 'B': 25}
}

initial_city = 'A'
tsp = TSP(graph, initial_city)

tsp.dfs(initial_city, tsp.visited.copy(), [initial_city], 1)
print("DFS - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

tsp.bfs()
print("BFS - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

tsp.iterative_deepening()
print("Iterative Deepening - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)
'''


class TSP:

    def __init__(self, graph, initial_city):
        self.graph = graph
        self.initial_city = initial_city
        self.num_cities = len(graph)
        self.min_cost = float('inf')
        self.optimal_path = None

    def path_cost(self, path):
        cost = sum(self.graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        cost += self.graph[path[-1]][path[0]]  # Return to initial city
        return cost

    def dfs(self, current_city, state, path):
        if len(path) == self.num_cities:
            path_cost = self.path_cost(path)
            if path_cost < self.min_cost:
                self.min_cost = path_cost
                self.optimal_path = path[:]
            return
        for city in self.graph[current_city]:
            if city not in state:
                state.add(city)
                self.dfs(city, state, path + [city])
                state.remove(city)

    def bfs(self):
        queue = [(self.initial_city), [self.initial_city]]
        while queue:
            current_city, path = queue.pop(0)
            if len(path) == self.num_cities:
                path_cost = self.path_cost(path)
                if path_cost < self.min_cost:
                    self.min_cost = path_cost
                    self.optimal_path = path
            else:
                for city in self.graph[current_city]:
                    if city not in path:
                        queue.append((city, path + [city]))

    def iterative_deepening(self):
        for depth_limit in range(1, self.num_cities + 1):
            self.dfs(self.initial_city, {self.initial_city}, [self.initial_city])



graph = {
    'A': {'B': 30, 'C': 15},
    'B': {'A': 45, 'C': 12},
    'C': {'A': 15, 'B': 25}
}

initial_city = 'A'
tsp = TSP(graph, initial_city)

tsp.dfs(initial_city, {initial_city}, [initial_city])
print("DFS - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

tsp.bfs()
print("BFS - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

tsp.iterative_deepening()
print("Iterative Deepening - Optimal Path:", tsp.optimal_path, "Cost:", tsp.min_cost)

'''
        