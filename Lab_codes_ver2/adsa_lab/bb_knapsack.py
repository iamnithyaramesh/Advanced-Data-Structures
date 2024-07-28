import heapq

def bound(profit, weight, lst, m):
    n = len(profit)
    u = 0  # Profit
    total_weight = 0
    
    # Calculate the profit and weight of the current list
    for i in range(n):
        if lst[i] == 1:
            total_weight += weight[i]
            u += profit[i]
    
    # Check if the current weight exceeds the capacity
    if total_weight > m:
        return 0
    
    # Calculate the upper bound
    for i in range(n):
        if lst[i] == 0:
            if total_weight + weight[i] <= m:
                total_weight += weight[i]
                u += profit[i]
            else:
                u += (profit[i] / weight[i]) * (m - total_weight)
                break
    
    return u

def knapsack(profit, weight, m):
    n = len(profit)
    heap = []
    fp=[]
    # Initialize with an empty list and zero profit
    lst = [0] * n
    initial_profit = 0
    initial_upper_bound = bound(profit, weight, lst, m)
    heapq.heappush(heap, (-initial_upper_bound, initial_profit, lst))
    
    max_profit = 0
    while heap:
        upper_bound, current_profit, lst = heapq.heappop(heap)
        upper_bound = -upper_bound
        
        if current_profit > max_profit:
            max_profit = current_profit
            fp=lst
        
        # Explore further only if the bound is promising
        for i in range(n):
            if lst[i] == 0:
                new_lst = lst[:]
                new_lst[i] = 1
                new_profit = current_profit + profit[i]
                remaining_capacity = m - sum(weight[j] for j in range(n) if new_lst[j] == 1)
                
                if remaining_capacity >= 0:
                    upper_bound = bound(profit, weight, new_lst, m)
                    
                    if upper_bound > max_profit:
                        heapq.heappush(heap, (-upper_bound, new_profit, new_lst))
    
    return max_profit,fp

# Example usage
profit = [10, 10, 12, 18]
weight = [2, 4, 6, 9]
capacity = 15

max_profit = knapsack(profit, weight, capacity)
print(f"Maximum profit: {max_profit}")
