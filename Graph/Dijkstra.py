# 음의 가중치가 없는 양방향 그래프와 시작점과 도착점이 주어졌을 때, 
# 시작점에서 도착점까지의 가장 최단 거리를 구하는 여러 알고리즘 중에 Dijkstra's Algorithm이 있다. 
# 알고리즘의 의사 코드는 다음과 같다.

# Dijkstra(G, r){
#    S = empty; //S는 정점 집합
#    for each u ∈V
#       d[u] = INF
#    d[r] = 0
#    while(S!=V){
#       u = extractMin(V-S, d); ---(1)
#       for each v ∈ Adj(u)
#          if(v ∈ V-S and d[u] + w(u, v) < d[v]){
#             d[v] = d[u] + w(u, v);
#             prev[v] = u;
#          }
#    }
#    return d[t];
# }

# 위 Dijkstra 알고리즘을 구현하고, 조건에 맞게 출력하시오. 
# ※ 이완 조건(Relaxation condition)은 d[u] + w(u, v) < d[v]로 한다.

# Input Format
# 입력의 첫줄은 n과 m이 들어온다. n은 노드의 수이고 노드는 1부터 n까지 있다. m은 간선의 수를 나타낸다.
# 다음 m 줄에는 간선(x, y, w)이 들어온다. x는 시작점 y는 도착점 w는 그 간선의 가중치를 나타낸다.
# 마지막 줄에는 출발 노드 r와 도착 노드 t가 들어 온다.

# Output Format 
# 1부터 n까지 prev값을 순서대로 출력하고 마지막에, r에서 t까지의 최단 거리(Shortest path's distance)를 출력한다. 
# 각 숫자는 빈칸으로 분리되어야 한다.
# 만일 r에서 t까지 이르는 경로가 없다면 Impossible을 최단 거리 대신 출력한다.

# Sample Input 0
# 8 14
# 1 2 8
# 1 4 9
# 1 3 11
# 2 5 10
# 3 6 8
# 3 7 8
# 4 2 6
# 4 3 3
# 4 5 1
# 5 8 2
# 6 7 7
# 7 4 12
# 7 8 5
# 8 6 4
# 1 7

# Sample Output 0
# 0 1 1 1 4 8 3 5 19

# Sample Input 1
# 8 14
# 1 2 8
# 1 4 9
# 1 3 11
# 2 5 10
# 3 6 8
# 3 7 8
# 4 2 6
# 4 3 3
# 4 5 1
# 5 8 2
# 6 7 7
# 7 4 12
# 7 8 5
# 8 6 4
# 8 1

# Sample Output 1
# 0 4 4 7 4 8 6 0 Impossible

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
