wt = [3,4,6,5]
profit = [2,3,1,4]
weight = 8      #weight of the container
n = len(wt)
k = [[0 for i in range(weight+1)]for i in range(n+1)]

selected_items = [[False for i in range(weight + 1)] for i in range(n + 1)]

for i in range(n+1):
    for w in range(weight+1):
        if i==0 or w==0:
            k[i][w] = 0
        elif w>wt[i-1]:     #if columns weight is greater
            if profit[i - 1] + k[i - 1][w - wt[i - 1]] > k[i - 1][w]:
                k[i][w] = profit[i - 1] + k[i - 1][w - wt[i - 1]]
                selected_items[i][w] = True
            else:
                k[i][w] = k[i - 1][w]
        else:
            k[i][w] = k[i-1][w]

# Backtrack to find selected items
selected = []
i = n
j = weight
while i > 0 and j > 0:
    if selected_items[i][j]:
        selected.append(i - 1)
        j -= wt[i - 1]
    i -= 1

selected_items_binary = [1 if i in selected else 0 for i in range(n)]
for i in k:
    print(i)            
print("Maximum profit:", k[n][weight])
print("Selected items:", selected_items_binary)