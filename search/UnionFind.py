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
