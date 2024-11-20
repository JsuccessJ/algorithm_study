def pebble(m):
    peb = [[0] * 4 for _ in range(m)]
    for i in range(m):
        for p in range(3):
            peb[i][p] = matrix[p][i]
        peb[i][3] = matrix[0][i] + matrix[2][i]
    for i in range(1, m):
        for p in range(4):
            if p == 3: k = peb[i-1][1]
            else: k = max(peb[i-1][j] for j in range(3+p%2) if p != j)
            peb[i][p] += k
    return max(peb[m-1][k] for k in range(4))

m = int(input())
matrix = [list(map(int, input().split())) for _ in range(3)]
print(pebble(m))
