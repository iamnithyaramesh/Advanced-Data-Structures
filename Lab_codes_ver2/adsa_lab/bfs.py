def bfs(graph):
    num=len(graph)
    visited=[False]*num
    start=0
    def isvisited(node,path):
        return node in path


    queue=[(start,[start])]
      
    while queue:
        node,path=queue.pop(0)
        visited[node]=True

        if len(path)==num:
            print("Path : ",path)

        for neighbour,weight in enumerate(graph[node]):
            if weight !=0 and not isvisited(neighbour,path):
                queue.append((neighbour,path+[neighbour]))


if __name__ == '__main__' :
    adj_matrix = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
    bfs(adj_matrix)





