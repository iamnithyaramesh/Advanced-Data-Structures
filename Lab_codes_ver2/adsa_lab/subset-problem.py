n = 6
w = 30
arr = [5, 10, 12, 13, 15, 18]
ways = []

def fun(i, sum, set):
    if sum == 0: 
        ways.append(set)
        return 1
    if i < 0:
        return 0 
    return fun(i - 1, sum - arr[i], set + [arr[i]]) + fun(i - 1, sum, set)

fun(n - 1, w, [])
print(ways)    
