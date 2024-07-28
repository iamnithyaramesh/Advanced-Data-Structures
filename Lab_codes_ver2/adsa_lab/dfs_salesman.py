import copy
def matrix(n):
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                a=int(input(f"Enter the weight of {i}{j} : "))
                m[i][j]=a
            else:
                print(f"Value of {i}{j} : 0 ")
    return m

class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
        self.n=len(matrix)
        print(matrix)

    def dfs(self,start,visited,path,path_length,min_length,min_path):

        visited[start]=True
        path.append(start)


        if len(path)==self.n and self.matrix[path[0]][path[-1]] !=0:
            print(path,path_length)
            if path_length < min_length[0]:
                min_length[0]=path_length
                min_path[0]=copy.deepcopy(path)
                # print(min_path)

        else:
            for i in range(self.n):
                if visited[i]==False and self.matrix[start][i]!=0:
                    self.dfs(i,visited,path,path_length+self.matrix[start][i],min_length,min_path)

        p=path.pop()
        visited[p]=False

    def path_dfs(self,start):
        visited=[False]*self.n
        path=[]
        min_path=['Empty path']
        path_length=0
        min_length=[float('inf')]

        self.dfs(start,visited,path,path_length,min_length,min_path)
        # print(min_length,min_path)
        print("Min_path = ",min_path[0] +[min_path[0][0]] )
        print('Min_length = ',min_length[0]+self.matrix[min_path[0][0]][min_path[0][-1]])



if __name__=="__main__":
    n=int(input('Enter the number of nodes'))
    g=Graph(matrix(n))
    g.path_dfs(0)