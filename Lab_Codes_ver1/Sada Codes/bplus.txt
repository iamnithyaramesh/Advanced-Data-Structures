class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node, otherwise false
        self.keys = []  # List of keys in node
        self.children = []  # List of children nodes

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.leaf:
            while i >= 0 and self.keys[i] > key:
                i -= 1
            self.keys.insert(i + 1, key)
        else:
            while i >= 0 and self.keys[i] > key:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if self.keys[i] < key:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BPlusTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def traverse(self):
        if self.leaf:
            return self.keys
        else:
            result = []
            for i in range(len(self.keys)):
                result.extend(self.children[i].traverse())
                result.append(self.keys[i])
            result.extend(self.children[len(self.keys)].traverse())
            return result

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == key:
            return self.keys[i]

        if self.leaf:
            return None
        else:
            return self.children[i].search(key)

    def display(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.keys))
        if not self.leaf:
            for i, child in enumerate(self.children):
                if i < len(self.keys):
                    child.display(level + 1, "Child of " + str(self.keys[i]) + ": ")
                else:
                    child.display(level + 1, "Child of " + str(self.keys[-1]) + ": ")

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(t, True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BPlusTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            temp.split_child(0)
            temp.insert_non_full(key)
        else:
            root.insert_non_full(key)

    def search(self, key):
        return self.root.search(key)

    def traverse(self):
        return self.root.traverse()

    def display(self):
        self.root.display()

    # Deletion method
    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, node, key):
        t = self.t

        def merge_nodes(x, y, i):
            x.keys.insert(i, y.keys.pop(0))
            if not y.leaf:
                x.children.append(y.children.pop(0))

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            if node.leaf:
                node.keys.pop(i)
            else:
                if len(node.children[i].keys) >= t:
                    predecessor = node.children[i]
                    while not predecessor.leaf:
                        predecessor = predecessor.children[-1]
                    node.keys[i] = predecessor.keys.pop()
                    self._delete(node.children[i], node.keys[i])
                elif len(node.children[i + 1].keys) >= t:
                    successor = node.children[i + 1]
                    while not successor.leaf:
                        successor = successor.children[0]
                    node.keys[i] = successor.keys.pop(0)
                    self._delete(node.children[i + 1], node.keys[i])
                else:
                    merge_nodes(node.children[i], node.children.pop(i + 1), i)
                    self._delete(node.children[i], key)
        else:
            if node.leaf:
                return
            flag = i == len(node.keys)
            if len(node.children[i].keys) < t:
                if i != 0 and len(node.children[i - 1].keys) >= t:
                    child = node.children[i]
                    sibling = node.children[i - 1]
                    child.keys.insert(0, node.keys[i - 1])
                    if not child.leaf:
                        child.children.insert(0, sibling.children.pop())
                    node.keys[i - 1] = sibling.keys.pop()
                elif i != len(node.keys) and len(node.children[i + 1].keys) >= t:
                    child = node.children[i]
                    sibling = node.children[i + 1]
                    child.keys.append(node.keys[i])
                    if not child.leaf:
                        child.children.append(sibling.children.pop(0))
                    node.keys[i] = sibling.keys.pop(0)
                else:
                    if i != len(node.keys):
                        merge_nodes(node.children[i], node.children.pop(i + 1), i)
                    else:
                        merge_nodes(node.children[i - 1], node.children.pop(i), i - 1)
            self._delete(node.children[i if not flag else i - 1], key)

# Driver code
if __name__ == "__main__":
    bplustree = BPlusTree(3)

    while True:
        print("\nB+ Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Traverse")
        print("5. Display")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            bplustree.insert(key)
            print(f"Inserted {key} into the B+ tree.")

        elif choice == 2:
            key = int(input("Enter key to delete: "))
            bplustree.delete(key)
            print(f"Deleted {key} from the B+ tree.")

        elif choice == 3:
            key = int(input("Enter key to search: "))
            result = bplustree.search(key)
            if result is not None:
                print(f"Key {key} found in the B+ tree.")
            else:
                print(f"Key {key} not found in the B+ tree.")

        elif choice == 4:
            print("Traversal of the B+ tree:")
            print(bplustree.traverse())

        elif choice == 5:
            print("Display of the B+ tree structure:")
            bplustree.display()

        elif choice == 6:
            break

        else:
            print("Invalid choice! Please try again.")
