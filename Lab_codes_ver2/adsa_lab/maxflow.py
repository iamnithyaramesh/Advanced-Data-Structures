def ford_fulkerson(source, sink, graph):
    n = len(graph)
    all_augmented_paths = []
    
    def dfs(cur, path):
        path.append(cur)

        if cur == sink:
            all_augmented_paths.append(path[:])
            
        for i in range(n):
            if i not in path and graph[cur][i]: 
                dfs(i, path)
                
        print(cur, sink)
        print(path)        
        
        path.pop()        
    
    dfs(source, [])
    ans = 0
    while True:
        mx = 0
        best = []
        for path in all_augmented_paths:
            mn = float('inf')
            for i in range(len(path) - 1):
                mn = min(mn, graph[path[i]][path[i + 1]])
            if mx < mn:
                mx = mn
                best = path
        if mx == 0:
            break
        for i in range(len(best) - 1):
            graph[best[i]][best[i + 1]] -= mx
        ans += mx
    return ans

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source = 0
sink = 5
max_flow = ford_fulkerson(source, sink, graph)
print(f"Maximum flow: {max_flow}")