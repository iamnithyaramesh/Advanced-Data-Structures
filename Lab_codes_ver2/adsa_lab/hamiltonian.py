def matrix(n):
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                a = int(input(f"Enter the weight of {i}{j}: "))
                m[i][j] = a
            else:
                print(f"Value of {i}{j}: 0")    
    return m

def hamiltonian(start, lst, path, n, mat, path_lst):
    lst[start] = True
    path.append(start)

    if len(path) == n:
        if mat[path[-1]][path[0]] != 0:
            cycle = path + [path[0]]
            if cycle not in path_lst:  # Check to avoid duplicates
                path_lst.append(cycle)
                

    else:
        for i in range(n):
            if not lst[i] and mat[start][i] != 0:
                hamiltonian(i, lst, path, n, mat, path_lst)

    p = path.pop()
    lst[p] = False

def normalize(lst):
    """Rotate the list to its smallest lexicographical form."""
    return min(lst[i:] + lst[:i] for i in range(len(lst)))

def eliminate_cyclic_permutations(lists):
    """Eliminate cyclic permutations from a list of lists."""
    normalized_set = set()
    unique_lists = []
    
    for lst in lists:
        norm = tuple(normalize(lst))
        if norm not in normalized_set:
            normalized_set.add(norm)
            unique_lists.append(lst)
    
    
    return unique_lists

if __name__ == "__main__":
    #n = int(input('Enter the number of nodes: '))
    # m = matrix(n)
    n=5
    mat = [[0, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]]
    path_lst = []

    for start in range(n):
        lst = [False] * n
        hamiltonian(start, lst, [], n, mat, path_lst)
    
    path_lst=eliminate_cyclic_permutations(path_lst)
    print("Hamiltonian cycles found:")
    for cycle in path_lst:
        print(cycle)
