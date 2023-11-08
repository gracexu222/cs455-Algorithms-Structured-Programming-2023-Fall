def longest_increasing_subsequence(arr):
    n = len(arr)
    lengths = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1

    # Reconstructing the LIS
    max_length = max(lengths)
    lis = []
    for i in range(n-1, -1, -1):
        if lengths[i] == max_length:
            lis.append(arr[i])
            max_length -= 1

    return lis[::-1]

# Testing the function
sequence = [3, 2, 5, 1, 6, 3, 9, 2]
result = longest_increasing_subsequence(sequence)
print(result)
