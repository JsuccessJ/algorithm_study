# 다음은 MST를 구하기 위한 여러 알고리즘 중 하나인 Kruskal's Algorithm의 의사코드이다.

# MST-KRUSKAL(G, w)
# A = empty set
# for each vertex v ∈ G.V
#    MAKE-SET(v)
# sort the edges of G.E into nondecreasing order by weight w
# for each edge (u, v) ∈ G.E, taken in nondecreasing order by weight
#    if FIND-SET(u) != FIND-SET(v)
#       total = total + w(u, v) --- (1)
#       A = A ∪ {(u, v)}
#       UNION(u, v)
# return A

# 위 의사 코드를 구현하고, 조건에 맞게 출력하시오. 
# Input Format
# 입력의 첫줄에는 노드의 수(n)과 간선의 정보 수(m)이 들어온다. 노드는 1부터 n까지 있다.
# 다음 m줄에는 간선을 이루는 노드(x, y)와 그 간선의 가중치 w가 들어온다.

# Output Format 
# (1) 에서 w(u,v)들을 출력하고, 마지막에 MST의 총 가중치의 합을 출력한다. 각 숫자는 빈 칸으로 분리 되어야 한다.

# Sample Input 
# 4 5
# 1 2 3
# 1 4 1
# 2 3 4
# 2 4 2
# 3 4 5

# Sample Output 
# 1 2 4 7

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
