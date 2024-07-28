''' Brute Force Approach - coming up with all possible solutions from where 
the optimal solution is to be found'''


'''class TSP:

    def __init__(self,graph,initial_city):
    
        self.graph=graph
        self.initial_city=initial_city
        self.num_cities=len(self.graph)
        self.visited={city:False for city in self.graph}
        self.visited[initial_city]=True
        self.path=None
        self.min_cost=float('inf')

    def is_goal_state(self,state):

        # state is a dictionary

        return all(state.values())
    
    def actions(self,state):
        return [city for city,visited in state.items() if  not visited]
    
    def path_cost(self,path):
        cost=0
        for i in range(len(path)-1):
            cost+=self.graph[path[i]][path[i+1]]
        cost+=self.graph[path[-1]][path[0]]
        return cost'''
    

'''class Item:
    def __init__(self,value,wt):
        self.value=value
        self.wt=wt
    
    def __repr__(self):
        return f'Value : {self.value}, Weight: {self.wt}'
    
def fractional_knapsack(items,cap):
        for item in items:
            item.ratio=item.value/item.wt

        items.sort(key=lambda x:x.ratio,reverse=True) # Descending order of P/W Ratios

        total_val=0.0
        for items in items:
            if cap-item.wt>=0:
                cap-=item.wt
                total_val+=item.value

            else:
                total_val+=item.value*(cap/item.wt)
                break
        return total_val
    
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50

max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the knapsack: {max_value}")'''
'''import heapq
class HuffMann_Node:
    def __init__(self,symbol,freq,left=None,right=None):
        self.symbol=symbol
        self.freq=freq
        self.left=left
        self.right=right
        self.huff=''

    def __lt__(self,nxt):
        return self.freq<nxt.freq
    
    def __repr__(self):
        return str(self.symbol)
    
def printNodes(node,val=''):
        newVal=val+str(node.huff)
        if node.left:
            printNodes(node.left,val)
        if node.right:
             printNodes(node.right,val)
        if (not node.left and not node.right):
             print(f'{node.symbol}')

chars=['a','b','c','d','e','f']
freq=[5,9,12,13,16,45]
freq_prob=[freq[i]/sum(freq) for i in range(len(freq))]
print(freq_prob)

nodes=[]
for x in range(len(chars)):
     heapq.heappush(nodes,HuffMann_Node(freq[x],chars[x]))

while len(nodes)>1:
     left=heapq.heappop(nodes)
     right=heapq.heappop(nodes)
     print(nodes)

     left.huff=0
     right.huff=1

     newNode=HuffMann_Node(left.freq+right.freq,left.symbol+right.symbol,left,right)
     heapq.heappush(nodes,newNode)

printNodes(nodes[0])'''

'''def optimal_bst(keys,freq):
    n=len(keys)
    cost=[[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        cost[i][i]=freq[i]

    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            cost[i][j]=float('inf')
            for r in range((i,j+1)):
                c=(cost[i][r-1] if r>i else 0)+\
                (cost[r+1][j] if r<j else 0)+\
                sum(freq[i:j+1])
            if c<cost[i][j]:
                cost[i][j]=c
        return cost[0][n-1]'''








 

