# gfg_inorder_tree_traversal_no_recursion.py
class Node:
    # constructor 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

# loops for 'inorder' traversal 
def inorder(root):
    # set current 
    current = root 
    stack = [] 
    done = 0 

    while True: 
        if current is not None:
            stack.append(current) 
            current = current.left 

        # backtrack 
        elif stack:
            current = stack.pop() 
            print(current.data, end = " ") 
            # it's right subtree's turn 
            current = current.right 
        else:
            break 
    print() 

# test 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

inorder(root) 
