class Node:
    def __init__(self,key,left=None,right=None,):
        self.key=key
        self.left=left
        self.right=right

class BST:
    def __init__(self,rootkey=None):
        if rootkey is None:
            self.root=rootkey
        else:
            self.root=Node(rootkey)


    def insert(self,key,root):
        if root is None:
            root=Node(key)
            
        elif key<root.key:
            root.left=self.insert(key,root.left)
        elif key>root.key:
            root.right=self.insert(key,root.right)
        return root


    def insertlist(self,l):
        for i in l:
            self.root=self.insert(i,self.root)
    
            
    def inorder(self,root,):
        if root is None:
            return 
        else:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def inorderlist(self,root,l):
        if root is None:
            return l
        else:
            self.inorderlist(root.left,l)
            l.append(root.key)
            self.inorderlist(root.right,l)
        return l
    def preorder(self,root):
        if root is None:
            return 
        else:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return 
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)
    
    def search(self,key,root):
        if root is None or root.key==key:
            return root
        elif key<root.key:
            return self.search(key,root.left)
        elif key>root.key:
            return self.search(key,root.right)
    def searchlist(self,l):
        print(l)
        for i in l:
            if self.search(i,self.root) is not None:
                print("Found")
            else:
                print('Not Found')

    def delete(self,key,root):
        if key<root.key:
            root.left=self.delete(key,root.left)
        elif key>root.key:
            root.right=self.delete(key,root.right)
        else:#key==self.key
            if root.left is None and root.right is None:
                root.key=None
                return None    
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            
            elif root.left is not None and root.right is not None:
                ele=min(self.inorderlist(root.right,[]))
                root=self.delete(ele,root)
                root.key=ele 
                return root

        return root


        


            

if "__main__"==__name__:
    b=BST(50)
    b.insertlist([25,12,19,72])
    print("Inorder:")
    b.inorder(b.root)
    print("Preorder:")
    b.preorder(b.root)
    print("Postorder:")
    b.postorder(b.root)
    b.searchlist([50,12,19,13,100])
    b.root=b.delete(72,b.root)
    print("Inorder:")
    b.inorder(b.root)
    b.root=b.delete(12,b.root)
    print("Inorder:")
    b.inorder(b.root)
    

    bs=BST()
    bs.insertlist([5,2,1,7,6,8])
    print("Preorder:")
    b.preorder(b.root)
    print("Preorder:")
    bs.preorder(bs.root)
    bs.root=bs.delete(5,bs.root)
    print("Preorder:")
    bs.preorder(bs.root)


            
        