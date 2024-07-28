class Graph:

    def __init__(self):
        self.edges=[]
        self.vertices=set()

    def add_edge(self,v1,v2,w):
        self.edges.append((v1,v2,w))
        self.vertices.add(v1)
        self.vertices.add(v2)

    def find_set(self,v,sets):
        for s in sets:
            if v in s:
                return s
        return None

    def union(self,s1,s2):
        return s1.union(s2)
    
    def kruskals(self):
        sets=[{v} for v in self.vertices]
        sorted_edges=sorted(self.edges,key=lambda x:x[2])
        mst=[]
        for edge in sorted_edges:
            v1,v2,w=edge
            set_v1=self.find_set(v1,sets)
            set_v2=self.find_set(v2,sets)
            if set_v1!=set_v2:
                mst.append((v1,v2,w))
                new_set=self.union(set_v1,set_v2)
                sets.remove(set_v1)
                sets.remove(set_v2)
                sets.append(new_set)
        return mst
    
    def print_graph(self):
        for edge in self.edges:
            print("Edge",edge[0]-edge[1],"Weight",edge[2])

