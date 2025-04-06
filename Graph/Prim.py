# Input Format
# 입력의 첫줄에는 노드의 수(n)과 간선의 정보 수(m)이 들어온다. 노드는 1부터 n까지 있다.
# 다음 m줄에는 간선을 이루는 노드(x, y)와 그 간선의 가중치 w가 들어온다.

# Output Format
# u = EXTRACT-MIN(Q)에서 추출되는 u를 순서대로 출력하고 마지막에 MST의 총 가중치의 합을 출력한다.
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
