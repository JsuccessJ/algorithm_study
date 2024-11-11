class RedBlackTree:
    def __init__(self, parent=None, color=True):
        self.color = color
        self.parent = parent
        self.key = self.left = self.right = None

    def treeInsert(self, key: object, depth=-1):
        if self.key is None:
            self.key = key
            self.color = True
            self.left = RedBlackTree(self, False)
            self.right = RedBlackTree(self, False)
            self.balance()
            return depth
        depth += 1
        if key < self.key: depth = self.left.treeInsert(key, depth)
        elif key > self.key: depth = self.right.treeInsert(key, depth)
        return depth

    def balance(self, rotate=False):
        if not self.parent: self.color = False; return
        if not self.parent.key: self.color = False; return
        grandparent = self.parent.parent
        if self.color and self.parent.color or rotate:
            if grandparent.left == self.parent: uncle = grandparent.right
            else: uncle = grandparent.left
            if uncle.key and uncle.color:
                grandparent.recolor(True)
                grandparent.balance()
            else:
                if not grandparent.parent:
                    grandparent.left = self
                    rotate = False
                elif self.parent.key < grandparent.key:
                    if self==self.parent.left and not self.left.color: self.parent.balance(True); return
                    grandparent.left = self
                    rotate = self.parent.color and self.key > self.parent.key
                else:
                    if self==self.parent.right and not self.right.color: self.parent.balance(True); return
                    grandparent.right = self
                    rotate = self.parent.color and self.key < self.parent.key
                self.rotate(grandparent)
                if rotate: self.balance(rotate)
                else: self.recolor(False)

    def rotate(self, grandparent): #left rotate
        if self.key > self.parent.key:
            self.parent.right, self.left.parent = self.left, self.parent
            self.left = self.parent
        else:
            self.parent.left, self.right.parent = self.right, self.parent #right rotate
            self.right = self.parent
        self.parent.parent, self.parent = self, grandparent

    def recolor(self, color):
        self.color = color
        self.left.color = self.right.color = not color

    def minKey(self):
        if not self.left.key: return self.key
        else: return self.left.minKey()

    def treeDelete(self, key):
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
                self.left.parent.parent = self.right.parent.parent = self.parent
                if not child.color: self.deleteBalance()
                else: self.left.parent.color = self.right.parent.color = False
            else:
                self.key = self.left = self.right = None
                if not self.color: self.deleteBalance()
                else: self.color = False
            return

    def deleteBalance(self):
        if not self.parent.key: return
        left = self == self.parent.left
        if left: sibling = self.parent.right
        else: sibling = self.parent.left
        if sibling.color:
            self.parent.color, sibling.color = sibling.color, self.parent.color
            if left: self.parent.parent.left = sibling
            else: self.parent.parent.right = sibling
            sibling.rotate(self.parent.parent)
            self.deleteBalance()
        else:
            if not left and sibling.left.color or (left and sibling.right.color):
                sibling.color = self.parent.color
                if left:
                    self.parent.color = sibling.right.color = False
                    if not self.parent.parent.parent: self.parent.parent.left = sibling
                    elif self.parent.parent.right == self.parent: self.parent.parent.right = sibling
                    else: self.parent.parent.left = sibling
                else:
                    self.parent.color = sibling.left.color = False
                    if self.parent.parent.left == self.parent: self.parent.parent.left = sibling
                    else: self.parent.parent.right = sibling
                    sibling.rotate(self.parent.parent)

            elif left and sibling.left.color and not sibling.right.color:
                if self.parent.parent.right == self.parent: self.parent.parent.right = sibling
                else: self.parent.parent.left = sibling
                self.parent.right = sibling.left
                sibling.color, sibling.left.color = sibling.left.color, sibling.color
                sibling.left.rotate(self.parent)
                self.deleteBalance()

            elif not left and sibling.right.color and not sibling.left.color:
                if self.parent.parent.left == self.parent: self.parent.parent.left = sibling
                else: self.parent.parent.right = sibling
                self.parent.left = sibling.right
                sibling.color, sibling.right.color = sibling.right.color, sibling.color
                sibling.right.rotate(self.parent)
                self.deleteBalance()

            else:
                sibling.color = True
                if self.parent.color: self.parent.color = False
                else: self.parent.deleteBalance()

    def treePrint(self):
        if self.key is None: return
        dfs = []
        stack = [self]
        while len(stack):
            v = stack.pop()
            if v.right.key: stack.append(v.right)
            if v.left.key: stack.append(v.left)
            if v.color: color = 'RED'
            else: color = 'BLACK'
            dfs.append('    ' * self.treeInsert(v.key) + color + ' ' + str(v.key))
        for i in dfs: print(i)

t = RedBlackTree()
t.treeInsert(None)
n = int(input())
for _ in range(n):
    s, v = list(map(str, input().split()))
    if s=="I": t.left.treeInsert(int(v))
    if s=="D": t.left.treeDelete(int(v))
t.left.treePrint()
