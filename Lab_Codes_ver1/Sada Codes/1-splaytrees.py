class Node:
  def __init__(self, data=None):
      self.data = data
      self.left = None
      self.right = None
      self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if data is None:
            raise ValueError("Data cannot be None.")

        n = Node(data)
        temp = self.root
        y = None

        while temp is not None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y
        if y is None:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def rightRotation(self, x):
        y = x.left

        if y is None:
            return

        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def leftRotation(self, x):
        y = x.right

        if y is None:
            return

        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def splay(self, n):
        while n.parent is not None:
            if n.parent == self.root:
                if n == n.parent.left:
                    self.rightRotation(n.parent)
                else:
                    self.leftRotation(n.parent)
            else:
                p = n.parent
                g = p.parent

                if n == p.left and p == g.left:
                    self.rightRotation(g)
                    self.rightRotation(p)
                elif n == p.right and p == g.right:
                    self.leftRotation(g)
                    self.leftRotation(p)
                elif n == p.left and p == g.right:
                    self.rightRotation(p)
                    self.leftRotation(g)
                else:
                    self.leftRotation(p)
                    self.rightRotation(g)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def getRoot(self):
        return self.root
    
    def search(self, key, pos = None):
        if pos is None:
            pos = self.root
        
        if key == pos.data:
            return pos
        elif key < pos.data:
            return self.search(key, pos.left)
        elif key > pos.data:
            return self.search(key, pos.right)
        else:
            return None
        
    def delete(self, key):

        node_to_delete = self.search(key)

        if node_to_delete is None:
            print("Element not in Tree")
            return

        self.splay(node_to_delete)

        if node_to_delete.left is None:
            self.root = node_to_delete.right
            if self.root is not None:
                self.root.parent = None
        else:
            max_left = node_to_delete.left
            while max_left.right:
                max_left = max_left.right

            self.splay(max_left)

            max_left.right = node_to_delete.right
            if max_left.right is not None:
                max_left.right.parent = max_left

            self.root = max_left
            self.root.parent = None

        print("deleted:", key)

        
        
    

s = SplayTree()
keys_to_insert = [10, 5, 15, 3, 7, 12, 17]
for key in keys_to_insert:
    s.insert(key)

s.inorder(s.root)

s.delete(12)
s.inorder(s.root) 