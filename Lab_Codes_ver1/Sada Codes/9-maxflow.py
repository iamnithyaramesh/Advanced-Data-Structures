class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.row
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.row
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Example usage:
graphmatrix = [
    [0, 3, 0, 0, 13, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 17, 2],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 5, 14, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

g = Graph(graphmatrix)
source = 0
sink = 5

print("Maximum Flow:", g.ford_fulkerson(source, sink))
