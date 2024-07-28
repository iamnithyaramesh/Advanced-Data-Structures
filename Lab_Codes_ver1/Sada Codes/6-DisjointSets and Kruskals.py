class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0
        #print(self.rank)
        
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((u, v, weight))
    
    # Sort edges in non-decreasing order based on weight
    edges.sort(key=lambda x: x[2])
    
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
        
    # print(vertices, "-------")
 
    mst = []
    ds = DisjointSet(vertices)
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v) 
    
    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 3)],
    'C': [('B', 3), ('D', 1)],
    'D': [('A', 5), ('B', 3), ('C', 1)]
}

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(edge)