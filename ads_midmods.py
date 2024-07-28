'''class TreeNode:

    def __init__(self,key,left=None,right=None,parent=None):
        self.key=key
        self.left=left
        self.right=right
        self.left=left

    def left_rotate(self,node):
        y=node.left
        node.left=y.right
        if y.right is not None:
            y.right.parent=node
        y.parent=node.parent
        if node.parent is None:
            self.root=y
        elif node.parent.left==node:
            node.parent.left=y
        elif node.parent.right==node:
            node.parent.right=y

        y.right=node
        node.parent=y

    def right_rotate(self,node):
        y=node.right
        node.right=y.left
        if y.left is not None:
            y.left.parent=node
        y.parent=node.parent

        if node.parent is None:
            self.root=y
        elif node.parent.left==node:
            node.parent.left=y
        else:
            node.parent.right=y

    def splay(self,node):
        while node.parent is not None:
            if node.parent==self.root:
                if node.parent.left==node:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
            p=node.parent
            g=p.parent
            if p.left==node and g.left==p:
                self.right_rotate(g)
                self.right_rotate(p)
            elif p.right==node and g.right==p:
                self.left_rotate(g)
                self.right_rotate(p)
            elif p.right==node and g.left==p:
                self.right_rotate(p)
                self.left_rotate(g)
            elif p.left==node and g.right==p:
                self.left_rotate(p)
                self.right_rotate(g)'''


class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def dist(self,other):
        return ((self.x-other.x)**2-(self.y-other.y)**2)**0.5
    

    def __repr__(self):
        return f'({self.x},{self.y})'
    

def brute_force_closest(lst,n=0):
        distances=[]
        n=len(lst)
        for i in lst:
            for j in lst:
                if i.x!=j.x or i.y!=j.y:
                    distance=i.dist(j)
                    distances.append((i,j),distance)
        distances.sort(key=lambda pair:pair[1])
        try:
            return distances[0]
        except IndexError:
            return None
        
def closest_in_strip(strip,d):
        min_dist=d
        strip=sorted(strip,key=lambda point:point.y)
        for i in range(len(strip)):
            for j in range(i+1,min(i+7,len(strip))):
                if strip[j].y-strip[i].y>=min_dist:
                    break
                if strip[i].dist(strip[j])<min_dist:
                    min_dist=strip[i].dist(strip[j])
            if min_dist==d:
                return None
            return min_dist
    
def doc(lst):
    if len(lst)<3:
        res=brute_force_closest(lst,len(lst))
        if res is not None:
            return res
        else:
            return ((Point(),Point(),float('inf')))
        
    else:
        x_sorted=sorted(lst,key=lambda p:p.x)
        n=len(lst)
        mid=n//2
        mid_pt=x_sorted[mid]
        dlp=doc(x_sorted[:mid])
        drp=doc(x_sorted[mid:])
        d=min(dlp[1],drp[1])

class TSP:

    def __init__(self,graph,initial_city):
        self.graph=graph
        self.initial_city=initial_city
        self.num_cities=len(graph)
        self.min_cost=float('inf')
        self.optimal_path=None

    
    def path_cost(self,path):
        cost=sum(self.graph[path[i]][path[i+1]] for i in range(len(path)-1))
        cost+=self.graph(path[-1][path[0]])
        return cost
    
    def dfs(self,current_city,state,path):
        if len(path)==self.num_cities:
            path_cost=self.path_cost(path)
            if path_cost<self.min_cost:
                self.min_cost=path_cost
                self.optimal_path=path[:]
            return 
        for city in self.graph[current_city]:
            if city not in state:
                state.add(city)
                self.dfs(city,state,path+[city])
                state.remove(city)


    def bfs(self):
        queue=[(self.initial_city),[self.initial_city]]
        while queue:
            current_city,path=queue.pop(0)
            if len(path)==self.num_cities:
                path_cost=self.path_cost(path)
                if path_cost<self.min_cost:
                    self.min_cost=path.cost
                    self.path=path
            else:
                for city in self.graph[current_city]:
                    if city not in path:
                        queue.append((city,path+[city]))


        


    



