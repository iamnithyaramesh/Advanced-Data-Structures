import copy
def graph(n):
    l=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            else:
                a=int(input(f'enter for {i} {j}'))
                if a!=0 and ([i,j] not in [i[0] for i in l] or [j,i] not in [i[0] for i in l]):
                    l.append([[i,j],a])

    return l

class Kruskal:
    def __init__(self,n):
        #l=graph(n)
        l=[[[0, 1], 1], [[0, 2], 2], [[0, 3], 3], [[1, 2], 3], [[1, 3], 2],[[1, 4], 3],  [[2, 3], 3], [[3, 4], 2]]
        self.graph=sorted(l,key = lambda x : x[1])
        self.n=n

    def kruskal_algo(self):
        l=[{i} for i in range(self.n)]
        graph=copy.deepcopy(self.graph)
        mst=[]
        # no. of edges (in mst)  = no. of vertices -1
        while len(mst) < self.n-1:
            lst=graph.pop(0)
            e1=lst[0][0]
            e2=lst[0][1]
            if not any({e1,e2}.issubset(i) for i in l) :
                mst.append(lst)
                for i in range(len(l)):
                    if {e1}.issubset(l[i]):
                        u=i
                    if {e2}.issubset(l[i]):
                        v=i
                # print(u,v)
                d1=l[u]
                d2=l[v]
                l.remove(d1)
                l.remove(d2)
                ele=d1 | d2
                l.append(ele)

        return mst



if __name__ == '__main__' : 
    k=Kruskal(5)
    print(k.kruskal_algo())