class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"(Value: {self.value}, Weight: {self.weight})"

def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratio for each item
    for item in items:
        item.ratio = item.value / item.weight

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of items taken
    for item in items:
        if capacity - item.weight >= 0:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining item
            total_value += item.value * (capacity / item.weight)
            break

    return total_value

# Example usage
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50

max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the knapsack: {max_value}")

'''
Item Class: A class to represent an item with a value and weight.
Fractional Knapsack Function:
Computes the value-to-weight ratio for each item.
Sorts items based on this ratio in descending order.
Iterates through the sorted items, adding as much of each item as possible to the knapsack without exceeding the capacity.
If the entire item can be taken, it's added to the knapsack. Otherwise, a fraction of the item that fits into the remaining capacity is taken.
Example Usage: Defines a list of items and the knapsack capacity. The fractional_knapsack function calculates the maximum value that can fit into the knapsack.
'''


