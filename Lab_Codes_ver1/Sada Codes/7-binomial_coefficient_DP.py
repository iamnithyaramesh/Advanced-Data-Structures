# Finding the Binomial Coefficient using Dynamic Programming

def bce(n, k):
    
    table = []                                                     # Creating table to store the values
    
    for i in range(n + 1):
        table.append([])
        
    for i in table:
        for j in range(k + 1):
            i.append(0)                                            # Table of req size created
            
    for i in table:                                                # C(n, 0) = 1 (Base Case)
        i[0] = 1
        
    for i in range(k + 1):                                         # C(n, n) = 1 (Base Case)
        table[i][i] = 1
        
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]    # C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
            
    for i in table:
        print(i)                                                   # Displaying the table created

    return table[n][k]


n = int(input("n - "))
r = int(input("r - "))

if n >= r:
    a = bce(n, r)
    print("nCr =", a)
else:
    print("Invalid Input")


def bce(n,k):
    table=[]

    for i in range(n+1):
        table.append([])

    for i in table:
        for j in range(k+1):
            i.append(0)
    
    for i in table:
        i[0]=1

    for x in range(k+1):
        table[x][x]=1

    for a in range(n+1):
        for b in range(k-1):
            table[a][b]=table[a-1][b-1]+table[a-1][b]
    return table[n][k]

n = int(input("n - "))
r = int(input("r - "))

if n >= r:
    a = bce(n, r)
    print("nCr =", a)
else:
    print("Invalid Input")
            