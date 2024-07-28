
class Node:
    def __init__(self, leaf=False):
        self.keys = []#[e,e]
        self.children = []#[n,n,n]
        self.leaf = leaf

    def display(self, depth=0):
        prefix = '    ' * depth
        print(f"{prefix}Leaf: {self.leaf}, Keys: {self.keys}")
        if not self.leaf:
            for i, child in enumerate(self.children):
                print(f"{prefix}Child {i+1}:")
                child.display(depth + 1)
class Bplus():

    def __init__(self,degree):
        self.root = Node(True)
        self.degree = degree

    def insert_deep( self, element, node):

        if node.leaf == True:
            # if element == 105:
            #     print("False leaf ",element,node.keys)

            node.keys.append(element)
            if len(node.keys) == self.degree :
                self.split(node)

        else:

            c = False

            for i in range(len(node.keys)): # len(self.children)-1

                if element < node.keys[i]:
                    self.insert_deep(element,node.children[i])

                #to append on right side of the keys (last element)
                if i == len(node.keys)-1:
                    c = True


            if c == True:

                if element > node.keys[-1]:
                    self.insert_deep(element,node.children[-1])



    def insert(self,element):

        self.insert_deep(element,self.root) #78,root 

    # splitting a node
    def split(self,arr):

        length = len(arr.keys)//2

        new_node1 = Node(arr.leaf)
        new_node2 = Node(arr.leaf)

        new_node1.keys.extend(arr.keys[:length])
        new_node2.keys.extend(arr.keys[length:])

        new_node1.children.extend(arr.children[:length+1])
        new_node2.children.extend(arr.children[length+1:])

        parent = self.find_parent(arr)

        if arr == self.root:  # or parent = none
            #creating a new node for root
            new_root = Node (False)
            new_root.keys = [new_node2.keys[0]]
            #splitting the children
            # new_node1.children.extend(arr.children[:length+1])
            # new_node2.children.extend(arr.children[length+1:])
            new_root.children.extend([new_node1,new_node2])


            if new_node2.leaf == False:
                new_node2.keys.remove(new_node2.keys[0])  # or new_node2.keys.pop(0)
            #assigning the new root to the existing root
            self.root = new_root
        # parent is a internal node
        elif parent != None:


            parent.keys.append(new_node2.keys[0])
            parent.keys.sort()



            # to also split and arrange the child appropriately  during splitting
            req_position = parent.children.index(arr)
            parent.children[req_position] = new_node1
            parent.children.insert(req_position+1,new_node2)



            # if arr.keys == [90,92,105]:
            #     print("Here")
            #     for i in parent.children:
            #         print("Keyd",i.keys)

            # print(parent.keys)
            if len(parent.keys) == self.degree:
                self.split(parent)

            if new_node2.leaf == False:
                new_node2.keys.remove(new_node2.keys[0])



    #find the parent
    def find_parent(self, node):
        def traverse(curr_node, parent):
            if curr_node == node:
                return parent
            #else
            if not curr_node.leaf:
                for child in curr_node.children:
                    result = traverse(child, curr_node)
                    if result:
                        return result
            return None

        return traverse(self.root, None)
    


    
    def display(self):
        
        self.root.display()


if __name__ == '__main__':
    b_plus_tree = Bplus(degree=3)
    keys = [18, 76, 90, 45, 78, 60, 13 , 16, 55, 92, 38, 105, 200, 164]

    for key in keys:     
        b_plus_tree.insert(key)

    print("B+ Tree Key")

    b_plus_tree.display()

