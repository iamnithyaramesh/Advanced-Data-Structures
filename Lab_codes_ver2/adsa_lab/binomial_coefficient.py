def matrix(n):
    l=[[None]*(n+1)for i in range(n+1)]

    for i in  range(n+1):
        for j in range(n+1):
            if j==0 or i==j:
                l[i][j]=1
    return l

def bc(m,a,b,n):
    for i in range(2,n+1):
        for j in range(1,i):
            print(i,j)
            m[i][j]=m[i-1][j-1]+m[i-1][j]
    print(m)

    result=0
    ac=a*n
    bc=1
    for i in range(n+1):
        result+=m[n][i]*ac*bc
        ac//=a
        bc*=b

    return result

n=int(input('Enter the no.'))
a=int(input('Enter a'))
b=int(input('Enter b'))
print(bc(matrix(n),a,b,n))