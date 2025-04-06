# 이번 문제에서 그래프는 다음과 같이 구성된다.

# 1부터 n까지의 노드로 구성된다.
# 각 노드는 이어져있을 수도 있고 그렇지 않을 수도 있다.
# 간선의 방향은 없다.
# BFS로 방문 할 때 숫자 순으로 방문한다. 예를 들어서 1번 노드에 2번 노드와 3번 노드가 동시에 이어져 있을 경우, 1번 노드에서는 2번 노드를 먼저 방문한다.
# 그래프 G와 출발점 s가 주어졌을 때, s에서 출발하는 BFS를 하면서 방문하는 노드를 출력하라.

# Input Format
# 입력의 첫줄은 n이 들어온다. 그 다음 줄에는 간선의 수 m이 들어온다.
# 다음 m 줄에는 간선(x, y)이 들어온다.
# 마지막 줄에는 출발 노드 s가 들어 온다.

# Output Format
# s에서 출발하여 BFS를 하면서 방문하는 노드를 출력한다. 각 노드는 빈칸으로 구별한다.

# Sample Input 
# 5
# 6
# 1 3
# 1 2
# 1 5
# 2 3
# 3 4
# 4 5
# 1

# Sample Output
# 1 2 3 5 4

def BFS(G, s):
    visited = [False]*(s-1) + [True] + [False]*(len(G)-s)
    queue=[s]
    while len(queue) :
        u = queue.pop(0)
        print(u, end=' ')
        G[u-1].sort()
        for v in G[u-1]:
            if not visited[v-1]:
                visited[v-1] = True
                queue.append(v)

n=int(input())
m=int(input())
G = [[] for _ in range(n)]
for _ in range(m):
    v, e = map(int, input().split())
    G[v-1].append(e)
    G[e-1].append(v)
s=int(input())
BFS(G, s)
