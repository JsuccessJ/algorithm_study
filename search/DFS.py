def DFS(v):
    visited[v-1] = True
    print(v, end=' ')
    G[v-1].sort()
    for x in G[v-1]:
        if not visited[x-1]: DFS(x)
    return 0

n=int(input())
m=int(input())
G = [[] for _ in range(n)]
visited = [False] * n
for _ in range(m):
    v, e = map(int, input().split())
    G[v-1].append(e)
    G[e-1].append(v)
s=int(input())
DFS(s)
