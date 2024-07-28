class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent
    
class ST:
    def __init__(self,root=None):
        self.root=None
    
    # Right rotation operation
    def right_rotate(self,n):
        y=n.left
        n.left=y.right
        if y.right is not None:
            y.right.parent=n

        y.parent=n.parent
        if n.parent is None:
            self.root=y
        elif n.parent.left==n:
            n.parent.left=y
        elif n.parent.right==n:
            n.parent.right=y 

        y.right=n
        n.parent=y

    # Left rotation operation
    def left_rotate(self,n):
        y=n.right
        n.right=y.left
        if y.left is not None:
            y.left.parent=n

        y.parent=n.parent
        if n.parent is None:
            self.root=y
        elif n.parent.left==n:
            n.parent.left=y
        elif n.parent.right==n:
            n.parent.right=y
            
        y.left=n
        n.parent=y
        
    # Splay operation
    def splay(self,n):
        while n.parent is not None:
            if n.parent == self.root:
                if n.parent.left==n:
                    self.right_rotate(n.parent) 
                elif n.parent.right==n:
                    self.left_rotate(n.parent)
            else:
                p=n.parent
                g=p.parent
                if p.left==n and g.left==p:
                    self.right_rotate(g)
                    self.right_rotate(p)
                elif p.right==n and g.right==p:
                    self.left_rotate(g)
                    self.left_rotate(p)
                elif p.left==n and g.right==p:
                    self.right_rotate(p)
                    self.left_rotate(g)
                elif p.right==n and g.left==p:
                    self.left_rotate(p)
                    self.right_rotate(g)
    
    # Insertion of a list of elements
    def insertlist(self,l):
        for i in l:
            self.insert(Node(i))
    
    # Insertion of a single node
    def insert(self,n):
        temp=self.root
        y=None
        while temp is not None:
            y=temp
            if n.key < temp.key:
                temp=temp.left
            else:
                temp=temp.right

        n.parent=y
        
        if y is None:
            self.root=n
        elif n.key<y.key:
            y.left=n
        elif n.key>y.key:
            y.right=n
        
        self.splay(n)                                     


    # Search for a node with a given key
    def search(self,key,n):
        if key==n.key:
            self.splay(n)
            return n
        elif key<n.key:
            return self.search(key,n.left)
        elif key > n.key:
            return self.search(key,n.right)
        else:
            return None
    
    # In-order traversal to get a sorted list of keys
    def inorderlist(self,root,l):
        if root is None:
            return l
        else:
            self.inorderlist(root.left,l)
            l.append(root.key)
            self.inorderlist(root.right,l)
        return l

    # Deletion of a node with a given key
    def delete(self,key):
        n=self.search(key,self.root)
        lst=n.left
        rst=n.right

        if lst is not None:
            lst.parent=None
        if rst is not None:
            rst.parent=None
        n.left=None
        n.right=None

        if lst is not None:
            self.root=lst
            ele=max(self.inorderlist(lst,[]))
            lst = self.search(ele,self.root)# or lst
            lst.right=rst
            if rst is not None:
                rst.parent=lst

        else:
            self.root=rst

    # Pre-order traversal for printing
    def preorder(self,root):
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

if __name__=="__main__":    
    st=ST()
    l=[4,7,17,92,15,32,67,43,65,1]
    st.insertlist(l)
    st.preorder(st.root)
    print('--------------------------')
    st.delete(17)
    st.preorder(st.root)
    print('--------------------------')
    st.delete(1)
    st.preorder(st.root)
    print('--------------------------')
    st.delete(32)
    st.preorder(st.root)
    print('--------------------------')
    st.delete(65)
    st.preorder(st.root)
    print('--------------------------')
    st.delete(43)
    st.preorder(st.root)
    print('--------------------------')
