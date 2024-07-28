#Checking:
    #no duplicates
    #if a vertex is taken there should be an edge with prev vertex
    #check if circuits doesnt repeat in a different way
    #if we are at last vertex then there should be an edge with first node
        #First 3 checks in isValid() fn
        #4th check is the return condition for backtracking to append a copy to the final result list


def isvalid(graph,v,pos,path,circuits):
    #for checking edge is present or not with previous vertex
    if graph[path[pos-1]][v]==0:
        return False
    #for duplicate
    if v in path:
        return False
    #if circuit already present.
    if path[:pos+1] in circuits:
        return False
    return True


#this will generate a path from source and traverse all vertex and back to source.
def hamiltonian(graph,path,pos,circuits):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            circuits.append(path[:])                        #appending the copy of path list to circuits list
        else:
            return
    else: 
        for v in range(1,len(path)):
            if isvalid(graph,v,pos,path,circuits) is True:
                path[pos] = v                               #if valid vertex,then fixing that vertex in path list
                hamiltonian(graph,path,pos+1,circuits)      #for next position--->backtracking.
                path[pos] = -1                              #reset the value of the path array 
                
                
#this will print all cycles.
def hamiltonianCircuit(graph):
    path = [-1]*len(graph)
    path[0] = 0         #source as 0.
    circuits = []
    hamiltonian(graph,path,1,circuits)      #sending 1 as next pos
    if circuits:
        print('Cycles are:')
        for circuit in circuits:
            print('->'.join(str(vertex+1)for vertex in circuit))   
    
    else:
        print('Hamiltonian circuit is not present')
        
adj_matrix = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

hamiltonianCircuit(adj_matrix)