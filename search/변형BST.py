class BinarySearchTree:
    def __init__(self, key=None):
        self.key = key
        if self.key:    #node exist
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else: self.left = self.right = None

    def treeInsert(self, key, depth=-1):
        if not self.key: #node is empty
            self.key = key
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        depth+=1
        if key < self.key: depth = self.left.treeInsert(key,depth)
        elif key > self.key: depth = self.right.treeInsert(key,depth)
        else: return depth
        return depth

    def minKey(self):
        if not self.left.key: return self.key
        else: return self.left.minKey()

    def treeDelete(self, key):
        if not self.key: return
        if key < self.key: self.left.treeDelete(key)
        if key > self.key: self.right.treeDelete(key)
        if key == self.key:
            if self.left.key and self.right.key:
                self.key = self.right.minKey()
                self.right.treeDelete(self.key)
            elif self.left.key or self.right.key:
                if self.left.key: child = self.left
                else : child = self.right
                self.key = child.key
                self.left = child.left
                self.right = child.right
            else:
                self.key = self.left = self.right = None
            return

    def treePrint(self):
        #DFS
        dfs = []
        stack = [self]
        while len(stack):
            v = stack.pop()
            if v.right.key: stack.append(v.right)
            if v.left.key: stack.append(v.left)
            dfs.append("    " * self.treeInsert(v.key) + str(v.key))
        for i in dfs: print(i)

t = BinarySearchTree()
n = int(input())
for _ in range(n):
    s, v = list(map(str, input().split()))
    if s=="I": t.treeInsert(int(v))
    if s=="D": t.treeDelete(int(v))

t.treePrint()
