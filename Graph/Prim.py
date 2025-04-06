# 다음은 MST를 구하기 위한 여러 알고리즘 중 하나인 Prim's Algorithm의 의사코드이다.

# MST-PRIM(G, r)
#    Q = V
#    for each u ∈ V[G]
#       do d[u] = INF
#          tree[u] = NIL
#    d[r] = 0
#    while Q != 0
#       do u = EXTRACT-MIN(Q) ---- (1)
#          for each v ∈ Adj[u]
#             do if v ∈ Q and w(u, v) < d[v]
#                   then d[v] = w(u, v)
#                        tree[v] = u
# EXTRACT-MIN(Q){
#    집합 Q에서 d값이 가장 작은 정점 u를 리턴하고, u를 집합 Q에서 제거한다.
# }

# 위 의사 코드를 구현하고, 시작 노드 1에서 출발하는 MST를 구하면서 Output 조건에 맞게 출력하시오. 

# Input Format
# 입력의 첫줄에는 노드의 수(n)과 간선의 정보 수(m)이 들어온다. 노드는 1부터 n까지 있다.
# 다음 m줄에는 간선을 이루는 노드(x, y)와 그 간선의 가중치 w가 들어온다.

# Output Format
# (1)에서 추출되는 u를 순서대로 출력하고 마지막에 MST의 총 가중치의 합을 출력한다.
# 각 숫자는 빈칸으로 구분한다.

# Sample Input
# 4 5
# 1 2 3
# 1 4 1
# 2 3 4
# 2 4 2
# 3 4 5

# Sample Output
# 1 4 2 3 7

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
