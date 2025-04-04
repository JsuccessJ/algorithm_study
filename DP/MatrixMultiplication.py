def matrixChain(n):
    m = [[0] * (n+1) for _ in range(n+1)]
    for r in range(1, n):
        for i in range(1, n-r+1):
            j = i+r
            m[i][j] = min(m[i][k] + m[k+1][j] + p[i-1][0]*p[k-1][1]*p[j-1][1] for k in range(i, j))
    return m[1][n]

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
print(matrixChain(n))
