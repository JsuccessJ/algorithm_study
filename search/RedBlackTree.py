class RedBlackTree:
    def __init__(self, parent=None):
        self.color = True
        self.parent = parent
        self.key = self.left = self.right = None

    def treeInsert(self, key, parent=None):
        if not self.key:
            self.key = key
            self.left = RedBlackTree(self)
            self.right = RedBlackTree(self)
        self.balance()
        if key < self.key: self.left.treeInsert(key, self)
        elif key > self.key: self.right.treeInsert(key, self)
        else: return

    def balance(self):
        if not self.parent: self.color=False
        if self.color and self.parent.color:
            grandparent = self.parent.parent
            if grandparent.left == self.parent: uncle = grandparent.right
            else: uncle = grandparent.left
            if uncle and uncle.color: #uncle = red
                #recolor
                uncle.color = self.parent.color = False
                if grandparent.parent: grandparent.color = True
                grandparent.balance()
            else:
                    #rotate
                    return
        return

t = RedBlackTree()
t.treeInsert(15)
t.treeInsert(13)
t.treeInsert(11)

print(t.key)
