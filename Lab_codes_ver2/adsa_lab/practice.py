'''class Item:

    def __init__(self,value,wt):
        self.value=value
        self.wt=wt

class Node:
    def __init__(self,level,weight,profit,bound):
        self.level=level
        self.weight=weight
        self.profit=profit
        self.bound=bound

def bound(node,n,capacity,items):
    if node.weight>=capacity:
        return
    profit_bound=node.profit
    j=node.level+1
    total_weight=node.weight

    while j<n and total_weight+items[j].weight<=capacity:
        total_weight+=items[j].weight
        profit_bound+=items[j].value
        j+=1

    if j<n:
        profit_bound+=(capacity-total_weight)'''

class Node:
    def __init__(self,data=None):
        self.key=data
        self.left=None
        self.right=None
        self.parent=None

class SplayTree:

    def __init__(self,root=None):
        self.root=None
    def right_rotate(self,node):
        y=node.left
        node.left=y.right 
        if y.right is not None:
            y.right.parent=node
        y.parent=node.parent
        if node.parent is None:
            self.root=y
        elif node.parent.left==node:
            node.parent.left=y
        elif node.parent.right==node:
            node.parent.right=y

        y.right=node
        node.parent=y
    
    def left_rotate(self,node):
        y=node.right
        node.right=y.left
        if y.left is not None:
            y.left.parent=node
        y.parent=node.parent
        if node.parent is None:
            self.root=y
        elif node.parent.left==node:
            node.parent.left=y
        elif node.parent.right==node:
            node.parent.right=y
        y.left=node
        node.parent=y

    def splay(self,n):
        while n.parent is not None:
            if n.parent==self.root:
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
                    self.right_rotate(p)
                elif p.left==n and g.right==p:
                    self.right_rotate(p)
                    self.left_rotate(g)
                elif p.right==n and g.left==p:
                    self.left_rotate(p)
                    self.right_rotate(g)

    def insert(self,n):
        temp=self.root
        y=None
        while temp is not None:
            y=temp
            if n.key<temp.key:
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

    def search(self,key,n):
            if key==n.key:
                self.splay(n)
                return 'Found'
            elif key<n.key:
                return self.search(key,n.left)
            elif key>n.key:
                return self.search(key,n.right)
            else:
                return None
            
    def preorder(self,root):
        if root is not None:
            print(root.key,end='->')
            self.preorder(root.left)
            self.preorder(root.right)

if __name__=="__main__":    
    st=SplayTree()
    l=[4,7,17,92,15,32,67,43,65,1]
    for i in l:
        st.insert(Node(i))
        st.preorder(st.root)
        print('\n')
    st.search(92,st.root)



    