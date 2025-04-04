def Prim(G, r):
    d = [float("inf")] * n
    tree = [None] * n
    w_sum = d[r-1] = 0
    visited = [False] * n
    queue = [(0, r)]
    while len(queue):
        queue.sort()
        w, u = queue.pop(0)
        w_sum += w
        print(u, end=' ')
        if visited[u-1]:  continue
        visited[u-1] = True
        for w, v in G[u-1]:
            if not visited[v-1] and w < d[v-1]:
                if tree[v-1]: queue.remove((d[v-1],v))
                d[v-1] = w
                tree[v-1] = u
                queue.append((w, v))
    print(w_sum)
    
n, m = map(int, input().split())
G=[[] for _ in range(n)]
for _ in range(m):
    x, y, weight = map(int, input().split())
    G[x-1].append((weight, y))
    G[y-1].append((weight, x))
Prim(G, 1)
