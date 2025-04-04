def LCS(m, n):
    C = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]: C[i][j] = C[i-1][j-1]+1
            else: C[i][j] = max(C[i-1][j], C[i][j-1])
    return C[m][n]

a = input()
b = input()
print(LCS(len(a), len(b)))
