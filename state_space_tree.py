class StateNode:
    def __init__(self, state, parent=None):
        self.state = state  
        self.parent = parent  
        self.children = []  

    def add_child(self, child_state):
        child_node = StateNode(child_state, self)
        self.children.append(child_node)
        return child_node

def display_state_space_tree(node, depth=0):
    print("  " * depth + str(node.state))
    for child in node.children:
        display_state_space_tree(child, depth + 1)

# Example usage:
if __name__ == "__main__":
    # Define an example state space tree
    root = StateNode("A")
    b_node = root.add_child("B")
    c_node = root.add_child("C")
    b_node.add_child("D")
    b_node.add_child("E")
    c_node.add_child("F")
    f_node = c_node.add_child("G")
    f_node.add_child("H")

    # Display the state space tree
    display_state_space_tree(root)
