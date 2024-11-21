def BFS(G, s):
    visited = [False]*(s-1) + [True] + [False]*(len(G)-s)
    queue=[s]
    bfs=[]
    while len(queue) :
        u = queue.pop(0)
        bfs.append(u)
        G[u-1].sort()
        for v in G[u-1]:
            if not visited[v-1]:
                visited[v-1] = True
                queue.append(v)
    for i in bfs: print(i, end=' ')

n=int(input())
m=int(input())
G = [[] for _ in range(n)]
for _ in range(m):
    v, e = map(int, input().split())
    G[v-1].append(e)
    G[e-1].append(v)
s=int(input())
BFS(G, s)
