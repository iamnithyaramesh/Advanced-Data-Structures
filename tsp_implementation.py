class TSP:

    def __init__(self,graph,initial_city):

        self.graph=graph
        self.initial_city=initial_city
        self.num_cities=len(graph)
        self.min_cost=float('inf')
        self.path=None

    def path_cost(self,path):
        cost = sum(self.graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        cost+=self.graph[path[-1]][path[0]]
        return cost
    
    def dfs(self,current_city,state,path):
        if len(path)==self.num_cities:
            path_cost=self.path_cost(path)
            if path_cost<self.min_cost:
                self.min_cost=path_cost
                self.path=path[:]
            return
        for city in self.graph[current_city]:
            if city not in state:
                state.add(city)
                self.dfs(city,state,path+[city])
                state.remove(city)


        '''Pseudocode:
     Input: a graph(V,E)
     Output : a graph(V,E) with its vertices marked consecutively with integers 
     in the order of them being encountered
     
     Assign count=0
     for each vertex v in V:
        if mark(v)==0:
            do dfs(v)

        dfs(v)
        Does a search recursively on all the adjacent vertices of v and assigns integers
        in the order of encounter from v
        count=count+1
        mark v with count
        for each w vertex adjacent to v:
            if mark(w)==0:
            DFS(W)
            '''

    def bfs(self):
        queue=[(self.initial_city),[self.initial_city]]
        while queue:
            current_city=queue.pop(0)
            if len(path)==self.num_cities:
                path_cost=self.path_cost(path_cost)
                if path_cost<self.min_cost:
                    self.min_cost=path_cost
                    self.path=path
            else:
                for city in self.graph[current_city]:
                    if city not in path:
                        queue.append((city,path+[city]))

        
        '''
        Pseudocode:
        
        I/P : A graph (V,E)
        O/P A graph (V,E) with its vertices marked consecutively in the order
        of them being encountered by the search algorithm
        
        count=0
        for each vertex v in V:
            if mark(v)==0:
                bfs(v)
                
        bfs(v)
        count=count+1
        Initialize a queue with v
        
        while queue is not empty do
        for each vertex w adjacent to v :
             if mark(w)==0:
                count=count+1
                add w to queue
                remove the front vertex of the queue'''

        def iterative_deeepening(self):
            for depth_limit in range(1,self.num_cities+1):
                self.dfs(self.initial_city,{self.initial_city},[self.initial_city])



graph = {
    'A': {'B': 30, 'C': 15},
    'B': {'A': 45, 'C': 12},
    'C': {'A': 15, 'B': 25}
}

initial_city = 'A'
tsp = TSP(graph, initial_city)

tsp.dfs(initial_city, {initial_city}, [initial_city])
print("DFS - Optimal Path:", tsp.path, "Cost:", tsp.min_cost)

tsp.bfs()
print("BFS - Optimal Path:", tsp.path, "Cost:", tsp.min_cost)

tsp.iterative_deepening()
print("Iterative Deepening - Optimal Path:", tsp.path, "Cost:", tsp.min_cost)


        