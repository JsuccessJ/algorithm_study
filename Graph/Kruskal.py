def makeSet(x):
    parent[x] = x
    rank[x] = 0

def findSet(x):
    if x != parent[x]: parent[x] = findSet(parent[x])
    return parent[x]

def union(x, y):
    x1 = findSet(x)
    y1 = findSet(y)
    if rank[x1] > rank[y1]: parent[y1] = x1
    else:
        parent[x1] = y1
        if rank[x1] == rank[y1]: rank[y1] += 1


def kruskal(G):
    A = []
    total = 0
    for i in range(1, n+1):
        makeSet(i)
    G.sort()
    for edge in G:
        w, x, y = edge
        if findSet(x) != findSet(y):
            total += w
            print(w, end=' ')
            union(x, y)
            A.append(edge)
    print(total)
    return A

n, m = map(int, input().split())
G=[]
parent = dict()
rank = dict()
for _ in range(m):
    x, y, weight = map(int, input().split())
    G.append((weight, x, y))
    G.append((weight, y, x))
kruskal(G)
