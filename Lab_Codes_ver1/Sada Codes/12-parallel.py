import concurrent.futures
import itertools

def calculate_distance(city_a, city_b):
    return ((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2) ** 0.5

def calculate_path_distance(path, cities):

    total_distance = 0
    num_cities = len(cities)
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

cities = [(0, 0), (1, 2), (3, 1), (2, 3)]     # cities are represented by coordinates
best_path, best_distance = find_best_path(cities)
print("Best Path:", best_path)
print("Best Distance:", best_distance)


'''
import multiprocessing

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with multiprocessing.Pool(2) as pool:
        left = pool.map(parallel_merge_sort, [left])[0]
        right = pool.map(parallel_merge_sort, [right])[0]

    return merge(left, right)

# Example usage:
arr = [3, 7, 1, 9, 4, 6, 8, 2, 5]
sorted_arr = parallel_merge_sort(arr)
print("Sorted array:", sorted_arr)


'''