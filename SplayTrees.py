"""
This module provides the implementation of a Binary 
Search Tree with various operations such as insertion,
searching,deletion and traversal methods.

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Tue Feb 20 2024

Revised on Sun Feb 25 2024

Original Author:R.Nithyasri(IT-B)[Reg No:3122 22 5002 086]

"""

# Class Name : BST

# Creates a Tree Node with data, left, and right as its data members.
# The default value for the key argument data is set to None and
# the data members left and right are initially set to None as well.

# Concept:
# Binary Search Trees are essentially Tree Data structures where every
# node has utmost two children and the nodes of the tree follow a hierarchy
# such that every node to the left of the root node has a numerical value
# less than the root node and every node to the right of the root node has
# a numerical value greater than it

class BST:

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    # insert():
    # Implements the insertion to a Binary Search Tree

    def insert(root, val):
        if root is None:
            return BST(val)
        else:
            if root.data == val:
                return root
            elif val > root.data:
                root.right = BST.insert(root.right, val)
            else:
                root.left = BST.insert(root.left, val)
        return root

    # search():
    # Implements the search of a given key to a Binary Search Tree

    def search(root, key):
        if root is None or root.data == key:
            if root is None:
                return 'Not Found'
            else:
                return 'Found'
        elif key > root.data:
            return BST.search(root.right, key)
        else:
            return BST.search(root.left, key)

    # delete():
    # Implements the deletion of a given node from a Binary Search Tree

    def delete(root, key):
        if root is None:
            return root

        # No children attached to the key
        if key < root.data:
            root.left = BST.delete(root.left, key)
            return root
        elif key > root.data:
            root.right = BST.delete(root.right, key)
            return root

        # For nodes having a single child
        if root.left is None:
            x = root.right
            del root
            return x
        elif root.right is None:
            x = root.left
            del root
            return x

        # For nodes having two children
        parent = root
        temp = root.right
        while temp.left is not None:
            parent = temp
            temp = temp.left

        if parent != root:
            parent.left = temp.right
        else:
            parent.right = temp.left

        root.key = temp.key

        del temp
        return root

    # inorder_traversal():
    # Provides an inorder traversal of the tree [LST, root, RST]

    def inorder_traversal(root):
        if root:
            BST.inorder_traversal(root.left)
            print(root.data, end='-->')
            BST.inorder_traversal(root.right)

    # preorder_traversal():
    # Provides a preorder traversal of the tree [root, LST, RST]

    def preorder_traversal(root):
        if root:
            print(root.data, end='-->')
            BST.preorder_traversal(root.left)
            BST.preorder_traversal(root.right)

    # postorder_traversal():
    # Provides a postorder traversal of the tree [root, RST, LST]

    def postorder_traversal(root):
        if root:
            print(root.data, end='-->')
            BST.postorder_traversal(root.right)
            BST.postorder_traversal(root.left)


# Driver code
            
if __name__ == "__main__":
    bst = None
    bst = BST.insert(bst, 50)
    BST.insert(bst, 30)
    BST.insert(bst, 20)
    BST.insert(bst, 40)
    BST.insert(bst, 70)
    BST.insert(bst, 60)
    BST.insert(bst, 80)

    print("Inorder traversal:")
    BST.inorder_traversal(bst)
    print("\nPreorder traversal:")
    BST.preorder_traversal(bst)
    print("\nPostorder traversal:")
    BST.postorder_traversal(bst)

    key = 20
    print(f"\nSearching for key {key}: {BST.search(bst, key)}")
    key = 90
    print(f"Searching for key {key}: {BST.search(bst, key)}")

    print("Deleting 20")
    bst = BST.delete(bst, 20)
    print("Inorder traversal after deletion:")
    BST.inorder_traversal(bst)


