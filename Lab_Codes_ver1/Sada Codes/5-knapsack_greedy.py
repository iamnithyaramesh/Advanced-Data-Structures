def knapsack_greedy(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    n = len(items)
    total_value = 0
    total_weight = 0
    selected_items = []

    for i in range(n):
        if total_weight + items[i][0] <= capacity:
            total_weight += items[i][0]
            total_value += items[i][1]
            selected_items.append(items[i])

    return total_value, selected_items
items = [
    (10, 60),  # Item 0: weight = 10, value = 60
    (20, 100),  # Item 1: weight = 20, value = 100
    (30, 120)  # Item 2: weight = 30, value = 120
]

capacity = 40
total_value, selected_items = knapsack_greedy(items, capacity)
print("Total Value:", total_value)
print("Selected Items:", selected_items)