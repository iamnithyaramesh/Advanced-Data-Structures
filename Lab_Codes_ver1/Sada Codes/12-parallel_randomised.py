import multiprocessing
import random

def calculate_sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()  # Get the number of available CPU cores

    # Get input from the user
    num_elements = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(num_elements):
        numbers.append(random.randint(1, 10))

    # Split the list into chunks for parallel processing
    chunk_size = num_elements // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, num_elements, chunk_size)]

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Perform parallel computations
    results = pool.map(calculate_sum_of_squares, chunks)

    # Combine the results
    total_sum = sum(results)
    print("Total sum of squares:", total_sum)
