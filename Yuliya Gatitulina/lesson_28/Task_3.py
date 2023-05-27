import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, limit):
    if len(arr) <= limit:
        insertion_sort(arr)
    else:
        if len(arr) > 1:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            quicksort(left, limit)
            quicksort(right, limit)
            arr[:] = left + middle + right


# Test with a random list of integers
random_list = random.sample(range(1, 1000), 900)
limits = [5, 10, 15]  # Different partition limits to analyze
for limit in limits:
    sorted_list = random_list.copy()
    start_time = time.time()
    quicksort(sorted_list, limit)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Sorted list (Partition Limit =", limit, "):", sorted_list)
    print("Execution time (Partition Limit =", limit, "):", execution_time, "seconds")
    print()