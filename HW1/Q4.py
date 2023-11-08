def max_A(Y):
    n = len(Y)
    max_value = 0
    max_pair = (0, 1)

    for i in range(n):
        for j in range(i + 1, n):
            current_value = (j - i) * min(Y[i], Y[j])
            if current_value > max_value:
                max_value = current_value
                max_pair = (i, j)

    return max_pair, max_value

# Test inputs
Y1 = [10, 3, 8, 4, 19, 7, 12]
Y2 = [5, 9, 3, 10, 4, 7, 11]

print(max_A(Y1))
print(max_A(Y2)) 


