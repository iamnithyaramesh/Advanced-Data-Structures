class BPlusTree:
    def __init__(self, order):
        self.root = BPlusNode(order)
    
    def insert(self, key, value):
        self.root.insert(key, value)
    
    def search(self, key):
        return self.root.search(key)
    

class BPlusNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []
        self.is_leaf = True
    
    def insert(self, key, value):
        if not self.is_leaf:
            i = len(self.keys) - 1
            while i >= 0 and key < self.keys[i]:
                i -= 1
            child = self.children[i + 1]
            child.insert(key, value)
            if child.is_overflow():
                self.split_child(i + 1, child)
        else:
            self.keys.append(key)
            self.keys.sort()
            i = self.keys.index(key)
            self.children.insert(i + 1, value)
            if len(self.keys) > self.order:
                self.is_leaf = False
    
    def search(self, key):
        if key in self.keys:
            return self.children[self.keys.index(key)]
        elif self.is_leaf:
            return None
        else:
            i = 0
            while i < len(self.keys) and key > self.keys[i]:
                i += 1
            return self.children[i].search(key)
    
    def split_child(self, i, child):
        new_child = BPlusNode(self.order)
        mid = len(child.keys) // 2
        new_child.keys = child.keys[mid:]
        new_child.children = child.children[mid:]
        child.keys = child.keys[:mid]
        child.children = child.children[:mid]
        if child.is_leaf:
            new_child.is_leaf = True
            child.next_leaf = new_child
        self.keys.insert(i, new_child.keys[0])
        self.children.insert(i + 1, new_child)
    
    def is_overflow(self):
        return len(self.keys) > self.order


# Example usage:
if __name__ == "__main__":
    bptree = BPlusTree(order=3)
    data = [(10, 'A'), (20, 'B'), (5, 'C'), (6, 'D'), (12, 'E'), (30, 'F')]
    for key, value in data:
        bptree.insert(key, value)
    
    print("Searching for key 5:", bptree.search(5))
    print("Searching for key 30:", bptree.search(30))
