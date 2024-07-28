#Single Source Shortest Path
#[u, v, wt]
edges = [[2,5,-1],[1,2,6],[5,7,3],[3,5,1],[3,2,-2],[6,7,3],[4,6,-1],[1,4,5],[1,3,5],[4,3,-2]]

dis = [5000 for i in range(10)]

dis[1] = 0
n=7

for k in range(n-1):
    for i in edges:
        u = i[0]
        v = i[1]
        wt = i[2]
        if dis[v]>wt+dis[u]:
            dis[v] = wt+dis[u]
print(dis)
for i in edges:
    u = i[0]
    v = i[1]
    wt = i[2]
    if dis[v]>wt+dis[u]:
        print("negative cyle")

# print(dis)
for i in range(1,n+1):
    print("distance of node ",i, "from source = ",dis[i])


