def linear_search(arr, x):
    indices = [i for i, val in enumerate(arr) if val == x]
    return indices

# Running the function on worst-case and best-case inputs for each of running time and memory usage
arr_worst_case_time = [1] * 1000000
arr_best_case_time = [1] + [0] * 999999

arr_worst_case_memory = [1] * 1000000
arr_best_case_memory = [0] * 1000000

print(linear_search(arr_worst_case_time, 1))  # Worst case for time
print(linear_search(arr_best_case_time, 1))   # Best case for time
print(linear_search(arr_worst_case_memory, 1)) # Worst case for memory
print(linear_search(arr_best_case_memory, 1))  # Best case for memory
