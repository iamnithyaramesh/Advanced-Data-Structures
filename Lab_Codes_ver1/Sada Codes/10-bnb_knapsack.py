class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Node structure to store information of decision tree
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Level of node in decision tree
        self.profit = profit    # Profit of nodes on path from root to this node
        self.weight = weight    # Weight of nodes on path from root to this node
        self.bound = bound      # Upper bound of maximum profit in subtree rooted with this node

def bound(node, n, capacity, items):
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (capacity - total_weight) * items[j].value / items[j].weight

    return profit_bound

def knapsack_branch_and_bound(capacity, items):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    n = len(items)
    
    Q = []
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    
    max_profit = 0
    u.bound = bound(u, n, capacity, items)
    Q.append(u)

    while Q:
        u = Q.pop(0)

        if u.level == -1:
            v.level = 0

        if u.level == n-1:
            continue

        v.level = u.level + 1

        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit

        v.bound = bound(v, n, capacity, items)

        if v.bound > max_profit:
            Q.append(v)
        v = Node(v.level, u.profit, u.weight, 0)
        v.bound = bound(v, n, capacity, items)
        
        if v.bound > max_profit:
            Q.append(v)

    return max_profit

# Example usage
items = [
    Item(value=40, weight=10),
    Item(value=42, weight=6),
    Item(value=25, weight=5),
    Item(value=12, weight=4)
]
capacity = 2

max_profit = knapsack_branch_and_bound(capacity, items)
print(f"Maximum profit: {max_profit}")
