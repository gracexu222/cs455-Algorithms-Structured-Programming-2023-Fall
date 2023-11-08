def linear_search(A, x):

    indices = []
    for i, value in enumerate(A):
        if value == x:
            indices.append(i)
    return indices

# Best-case inputs (for runtime and memory usage)
A_best = [1, 2, 3, 4, 5]
x_best = 6
print('Best-case for runtime and memory usage',linear_search(A_best, x_best)) 

# Worst-case inputs (for runtime)
A_worst_runtime = [1, 1, 1, 1, 1]
x_worst_runtime = 1
print('Worst-case inputs for runtime',linear_search(A_worst_runtime, x_worst_runtime))  # Output: [0, 1, 2, 3, 4]

# Worst-case inputs (for memory usage)
A_worst_memory = list(range(100000)) + [1]
x_worst_memory = 1
print('Worst-case inputs for memory usage',linear_search(A_worst_memory, x_worst_memory))  # Output: [100000]
