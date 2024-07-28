# Implementing Red-Black Tree in Python


import sys


# Node creation
class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Preorder
    def pre_order_helper(self, node):
        if node != NULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node):
        if node != NULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node):
        if node != TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)

    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete_node(40)
    bst.print_tree()


class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

    def __str__(self):
        return str(self.key)

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            self._merge_with_root_list(self.min_node, node)
            if key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1
        return node

    def get_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                children = [x for x in self._iterate(z.child)]
                for child in children:
                    self._merge_with_root_list(self.min_node, child)
                    child.parent = None

            self._remove_from_root_list(z)
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.total_nodes -= 1
        return z

    def union(self, other_heap):
        if other_heap.min_node is None:
            return self
        if self.min_node is None:
            self.min_node = other_heap.min_node
            self.total_nodes = other_heap.total_nodes
            return self
        self._merge_with_root_list(self.min_node, other_heap.min_node)
        if other_heap.min_node.key < self.min_node.key:
            self.min_node = other_heap.min_node
        self.total_nodes += other_heap.total_nodes
        return self

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError('New key is greater than current key')
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

    def _iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def _remove_from_root_list(self, node):
        if node.right == node:
            return
        node.right.left = node.left
        node.left.right = node.right

    def _merge_with_root_list(self, root, node):
        node.left = root
        node.right = root.right
        root.right.left = node
        root.right = node

    def _consolidate(self):
        a = [None] * self._upper_bound_degree()

        nodes = [x for x in self._iterate(self.min_node)]

        for w in nodes:
            x = w
            d = x.degree
            while a[d] is not None:
                y = a[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                a[d] = None
                d += 1
            a[d] = x

        self.min_node = None
        for i in range(len(a)):
            if a[i] is not None:
                if self.min_node is None:
                    self.min_node = a[i]
                else:
                    self._merge_with_root_list(self.min_node, a[i])
                    if a[i].key < self.min_node.key:
                        self.min_node = a[i]

    def _link(self, y, x):
        self._remove_from_root_list(y)
        y.left = y.right = y
        self._merge_with_child_list(x, y)
        y.parent = x
        x.degree += 1
        y.mark = False

    def _cut(self, x, y):
        self._remove_from_child_list(y, x)
        y.degree -= 1
        self._merge_with_root_list(self.min_node, x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _remove_from_child_list(self, parent, node):
        if parent.child == node:
            if node.right != node:
                parent.child = node.right
            else:
                parent.child = None
        node.left.right = node.right
        node.right.left = node.left

    def _merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            self._merge_with_root_list(parent.child, node)

    def _upper_bound_degree(self):
        import math
        return math.floor(math.log2(self.total_nodes)) + 1
    

class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.sibling = None
        self.parent = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def _merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.degree <= h2.degree:
            h1.sibling = self._merge(h1.sibling, h2)
            return h1
        else:
            h2.sibling = self._merge(h1, h2.sibling)
            return h2

    def _link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def _union(self, h):
        new_heap = BinomialHeap()
        new_heap.head = self._merge(self.head, h.head)
        if new_heap.head is None:
            return new_heap

        prev_x = None
        x = new_heap.head
        next_x = x.sibling

        while next_x is not None:
            if (x.degree != next_x.degree or
                (next_x.sibling is not None and next_x.sibling.degree == x.degree)):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    self._link(next_x, x)
                else:
                    if prev_x is None:
                        new_heap.head = next_x
                    else:
                        prev_x.sibling = next_x
                    self._link(x, next_x)
                    x = next_x
            next_x = x.sibling
        return new_heap

    def insert(self, key):
        node = BinomialHeapNode(key)
        temp_heap = BinomialHeap()
        temp_heap.head = node
        self.head = self._union(temp_heap).head

    def get_min(self):
        if self.head is None:
            return None
        y = None
        x = self.head
        min_key = float('inf')
        while x is not None:
            if x.key < min_key:
                min_key = x.key
                y = x
            x = x.sibling
        return y.key

    def extract_min(self):
        if self.head is None:
            return None

        min_node_parent = None
        min_node = self.head
        min_node_key = self.head.key

        # Find the node with the minimum key and its parent
        prev_temp = None
        temp = self.head
        while temp.sibling is not None:
            if temp.sibling.key < min_node_key:
                min_node_key = temp.sibling.key
                min_node_parent = prev_temp
                min_node = temp.sibling
            prev_temp = temp
            temp = temp.sibling

        # Remove min_node from the root list
        if min_node_parent is not None:
            min_node_parent.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        # Reverse the order of min_node's children and merge them with the root list
        child = min_node.child
        new_root = None
        while child is not None:
            next_child = child.sibling
            child.sibling = new_root
            new_root = child
            child = next_child

        temp_heap = BinomialHeap()
        temp_heap.head = new_root
        self.head = self._union(temp_heap).head

        return min_node.key

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("New key is greater than current key")
        x.key = k
        y = x
        z = y.parent
        while z is not None and y.key < z.key:
            y.key, z.key = z.key, y.key
            y = z
            z = y.parent

    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

    

class SkewHeapNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SkewHeap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.key > h2.key:
            h1, h2 = h2, h1
        h1.right = self.merge(h1.right, h2)
        h1.left, h1.right = h1.right, h1.left
        return h1

    def insert(self, key):
        new_node = SkewHeapNode(key)
        self.root = self.merge(self.root, new_node)

    def find_min(self):
        if self.root is None:
            raise ValueError("Heap is empty")
        return self.root.key

    def delete_min(self):
        if self.root is None:
            raise ValueError("Heap is empty")
        min_key = self.root.key
        self.root = self.merge(self.root.left, self.root.right)
        return min_key

    def is_empty(self):
        return self.root is None

# Example usage
heap = SkewHeap()
heap.insert(10)
heap.insert(5)
heap.insert(30)
heap.insert(2)

print(f"Minimum element: {heap.find_min()}")
print(f"Deleted minimum element: {heap.delete_min()}")
print(f"Minimum element after deletion: {heap.find_min()}")


