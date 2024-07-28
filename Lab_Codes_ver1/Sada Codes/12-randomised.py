import concurrent.futures
import itertools

def calculate_distance(city_a, city_b):

    return ((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2) ** 0.5

def calculate_path_distance(path, cities):

    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities):
        city_a = cities[path[i]]
        city_b = cities[path[(i + 1) % num_cities]]
        total_distance += calculate_distance(city_a, city_b)
    return total_distance

def find_best_path(cities):
    num_cities = len(cities)
    best_distance = float('inf')
    best_path = None

    with concurrent.futures.ThreadPoolExecutor() as executor:

        permutations = itertools.permutations(range(num_cities))

        results = executor.map(lambda path: (path, calculate_path_distance(path, cities)), permutations)

        for path, distance in results:
            if distance < best_distance:
                best_distance = distance
                best_path = path

    return best_path, best_distance

cities = [(0, 0), (1, 2), (3, 1), (2, 3)]
best_path, best_distance = find_best_path(cities)
print("Best Path:", best_path)
print("Best Distance:", best_distance)


# with concurrent.futures.ThreadPoolExecutor as executor:

'''
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Example usage:
arr = [3, 7, 1, 9, 4, 6, 8, 2, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


'''