# 마을에 N명의 시민이 있다.  입력으로 친구인 사람들의 쌍이 주어진다. 
# 옛말에 의하면 친구의 친구는 친구라고 한다.
# 즉, A와 B와 친구고 B와 C와 친구면 A와 C 또한 친구이다.
# 여러분이 할 일은 친구의 수가 가장 큰 그룹의 사람 수를 출력하는 것이다.
 
# Input Format
# 입력의 첫줄은 n과 m이 들어온다. n은 마을 사람 수(1 < N < 30000)"이고, M은 친구 쌍의 수(1 < M < 50000)이 들어온다.
# 다음 m 줄에는 x, y이 들어오는데 x와 y는 친구라는 뜻이다.

# Output Format
# 가장 큰 친구 그룹의 사람 수를 출력한다.

class UnionFind:
    def __init__(self):
        self.parent = self.rank = None

    def makeSet(self):
        self.parent = self
        self.rank = 1

    def union(self, y):
        if self.findSet() != y.findSet():
            self.findSet().rank += y.findSet().rank
            y.findSet().parent = self.findSet()
        return self.findSet().rank

    def findSet(self):
        if self == self.parent: return self
        else: return self.parent.findSet()

n, m = map(int, input().split())
maxRank = 0
arr = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = UnionFind()
    arr[i].makeSet()

for i in range(m):
    a, b = map(int, input().split())
    rank = arr[a].union(arr[b])
    if maxRank < rank: maxRank = rank

print(maxRank)
