def matrixPath(n, m):
    c = [[float('inf')] * (m+1) for _ in range(n+1)]
    c[0][1] = c[1][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            c[i][j] = matrix[i-1][j-1] + min(c[i-1][j], c[i][j-1])
    return c[n][m]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrixPath(n, m))
