import heapq

def Dijkstra(G, r):
    d = [float("inf")] * n
    prev = [0] * n
    visited = [False] * n
    d[r-1] = 0
    queue = [(0, r)]
    r_t = "Impossible"
    while len(queue):
        dist, u = heapq.heappop(queue)
        if u==t: r_t= str(dist)
        if visited[u-1]: continue
        visited[u-1] = True
        for w, v in G[u-1]:
            if d[u-1]+w < d[v-1]:
                dist = d[v-1] = d[u-1]+w
                prev[v-1] = u
                heapq.heappush(queue, (dist, v))
    print(' '.join(str(k) for k in prev)+ ' ' + r_t)
    return d[t]

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    x, y, weight = map(int, input().split())
    G[x - 1].append((weight, y))
r, t = map(int, input().split())

Dijkstra(G, r)
