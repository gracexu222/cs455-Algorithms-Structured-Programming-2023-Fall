def count_pairs(A, T):
    if len(A) <= 1:
        return 0
    
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    
    # Conquer
    count = count_pairs(left, T) + count_pairs(right, T)
    
    # Combine
    j = 0
    for i in range(len(left)):
        while j < len(right) and right[j] - left[i] < T:
            j += 1
        count += j
    
    return count


A = [2, 7, 14, 22, 30, 37, 43, 50, 57, 63, 71, 78, 85, 91, 98, 105, 112, 118, 125, 133]
T = 8
result = count_pairs(A, T)
print(result)  
