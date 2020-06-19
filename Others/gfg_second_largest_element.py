# gfg_second_largest_element.py
# in BST 
class Node:
    def __init__(self, data):  
        self.key = data
        self.left = None 
        self.right = None 

def secondLargestElement(root, c): 
    if root == None or c[0] >= 2:
        return 

    secondLargestElement(root.right, c)  
    c[0] += 1 

    if c[0] == 2:
        print("2nd largest element is: ", root.key) 
        return 

    secondLargestElement(root.left, c)   

def secondLargest(root):
    c = [0] 
    secondLargestElement(root, c)  

def insert(node, key):
    if node == None: 
        return Node(key) 
    
    if key < node.key: 
        node.left = insert(node.left, key) 
    elif key > node.key:
        node.right = insert(node.right, key) 
    return node 

# test 
# Let us create following BST  
#         50  
 #      /    \  
#     30     70  
#     / \    / \  
#    20 40  60 80  
root = None 
root = insert(root, 50) 
insert(root, 30) 
insert(root, 20) 
insert(root, 40) 
insert(root, 70) 
insert(root, 60) 
insert(root, 80) 

secondLargest(root) 
# https://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/