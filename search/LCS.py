def LCS(m, n):
    C = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i] == y[i]: C[i][j] = C[i-1][j-1]+1
            else: C[i][j] = max(C[i-1][j], C[i][j-1])
    return C[m][n]
            
x = [1, 5, 3, 2, 1, 6]
y = [6, 2, 5, 1, 6]
