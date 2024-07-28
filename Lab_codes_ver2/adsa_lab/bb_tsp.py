inf = float('inf')
mat = [[inf, 20, 30, 10, 11],
       [15, inf, 16, 4, 2],
       [3, 5, inf, 2, 4],
       [19, 6, 18, inf,3],
       [16, 4, 7, 16, inf]]
n = 5
lr = [min(row) for row in mat]

for i in range(n):
    mat[i] = [j - lr[i] for j in mat[i]]


t_mat = [[mat[j][i] for j in range(n)] for i in range(n)]

lc = [min(col) for col in t_mat]

for i in range(n):
    t_mat[i] = [j - lc[i] for j in t_mat[i]]

mat = [[t_mat[j][i] for j in range(n)] for i in range(n)]

upper = sum(lr) + sum(lc)

def Cost(parent, child, mat,c):
    r_mat = [[None] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            if i == parent or j == child:
                r_mat[i][j] = inf
            else:
                r_mat[i][j] = mat[i][j]
    r_mat[child][parent] = inf

    l = []
    t_mat = [[r_mat[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        mr = min(r_mat[i])
        mc = min(t_mat[i])
        if mr != inf:
            l.append(mr)
        if mc != inf:
            l.append(mc)
    

    cost = mat[parent][child] + c + sum(l)
    #print(r_mat,cost)
    return r_mat, cost


def tsp(mat, ele, c,path):
 
    if len(path)==n:
        return c,path  
    min_cost = inf
    cur_mat = None
    min_ele= None
    for i in range(n):
        if i not in path:
            r_mat, cost = Cost(ele, i, mat,c)
            if cost < min_cost:
                min_cost = cost
                cur_mat = r_mat
                min_ele=i
    
    path.append(min_ele)
    return tsp(cur_mat,min_ele,min_cost,path)


print(tsp(mat,0, upper,[0]))
