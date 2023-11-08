def modified_edit_distance(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    ops = [[""] * (n + 1) for _ in range(m + 1)]

    # Initialization
    for i in range(m+1):
        dp[i][0] = i
        ops[i][0] = "D" * i
    for j in range(n+1):
        dp[0][j] = j
        ops[0][j] = "I" * j

    # Recurrence
    for i in range(1, m+1):
        for j in range(1, n+1):
            insert = dp[i][j-1] + 1
            delete = dp[i-1][j] + 1
            substitute = dp[i-1][j-1] + (0 if S[i-1] == T[j-1] else 1)

            # Check for the transpose operation
            if i > 1 and j > 1 and S[i-1] == T[j-2] and S[i-2] == T[j-1]:
                transpose = dp[i-2][j-2] + 1
            else:
                transpose = float('inf')

            # Update dp and operations table
            min_op = min(insert, delete, substitute, transpose)
            dp[i][j] = min_op
            
            if min_op == insert:
                ops[i][j] = ops[i][j-1] + "I"
            elif min_op == delete:
                ops[i][j] = ops[i-1][j] + "D"
            elif min_op == substitute:
                if S[i-1] != T[j-1]:
                    ops[i][j] = ops[i-1][j-1] + "S"
                else:
                    ops[i][j] = ops[i-1][j-1]
            else:
                ops[i][j] = ops[i-2][j-2] + "T"
                
    return dp[m][n], ops[m][n]

# Testing the function
S = "CTAC"
T = "GCTCA"
distance, operations = modified_edit_distance(S, T)
print("Edit Distance:", distance)
print("Operations:", operations)
