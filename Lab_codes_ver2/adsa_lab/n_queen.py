# 4 queen

#n=4
#mat = [[None]*n for _ in range(n)]
#path=[None]*n

#def check(mat,i,j): 
#    row=mat[i]
#    col=mat[j]
#    if not all(k==None for k in row):
#        return False
#    if not all(k==None for k in col):
#        return False
    
#    # diagonal down
#    l=[]
#    k=1
    
#    while True:
#        a=i+k
#        b=j+k
#        if a<n and b < n:
#            l.append((a,b))
#        else:
#            break
#        k+=1
    

#    # diagonal up

#    k=1
#    while True :
#        a=i-k
#        b=j-k
#        if a>=0 and b>=0:
#            l.append((a,b))
#        else:
#            break
#        k+=1

#    if not all(mat[a][b]==None for a,b in l ):
#        return False
    
#    return True

n=4
mat = [[None]*n for _ in range(n)]
path=[None]*n


def check(mat, i, j):
    # Check row on left side
    for x in range(j):
        if mat[i][x] is not None:
            return False

    # Check column on upper side
    for x in range(i):
        if mat[x][j] is not None:
            return False

    # Check upper diagonal on left side
    for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
        if mat[x][y] is not None:
            return False

    # Check lower diagonal on left side
    for x, y in zip(range(i, -1, -1), range(j, n)):
        if mat[x][y] is not None:
            return False

    return True

def btqueen(n, ele, mat, path):
    if ele == n:
        print(mat)
        #print(path)
        return

    for i in range(n):
        if check(mat, ele, i):
            mat[ele][i] = ele
            path[ele] = i
            btqueen(n, ele + 1, mat, path)
            mat[ele][i] = None
            path[ele] = None

# Start the backtracking algorithm
btqueen(n, 0, mat, path)
