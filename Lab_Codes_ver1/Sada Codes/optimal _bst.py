def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize cost for a single key
    for i in range(n):
        cost[i][i] = freq[i]

    # Calculate cost for chains of length 2 to n
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])

                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]

# Example usage
keys = [10, 12, 20]
freq = [34, 8, 50]

print(f"Cost of Optimal BST is {optimal_bst(keys, freq)}")


'''
Initialization:

keys: An array of keys.
freq: An array of frequencies, where freq[i] is the frequency of keys[i].
cost: A 2D list where cost[i][j] will store the cost of the optimal BST that can be formed with keys[i] to keys[j].
Base Case:

The cost of a single key BST is equal to its frequency. Therefore, for all i, cost[i][i] is initialized to freq[i].
Dynamic Programming Calculation:

The algorithm considers chains of increasing lengths from 2 to n.
For each subarray keys[i:j], it considers each key r as the root.
It computes the cost of making r the root which includes the cost of the left and right subtrees and the sum of frequencies of the keys from i to j.
It updates cost[i][j] with the minimum cost found for that subarray.
Result:

The final result, cost[0][n-1], gives the cost of the optimal BST for the entire set of keys.
Example
In the example provided:

keys = [10, 12, 20]
freq = [34, 8, 50]
The output Cost of Optimal BST is 142 means that the minimum search cost for this set of keys and frequencies is 142.
This implementation uses dynamic programming to ensure that the optimal cost is computed efficiently.
'''