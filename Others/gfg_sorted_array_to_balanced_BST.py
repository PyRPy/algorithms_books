# sorted_array_to_balanced_BST.py
# binary tree node 
class Node:
    def __init__(self, d):
        self.data = d   
        self.left = None 
        self.right = None 

def sortedArrayToBST(arr):
    if not arr:
        return None 
    mid = (len(arr)) // 2 

    root = Node(arr[mid]) # middle in array 
    root.left = sortedArrayToBST(arr[:mid]) # left 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 

# helper function to preorder traversal the BST 
def preOrder(node):
    if not node:
        return 
    print(node.data) 
    preOrder(node.left) 
    preOrder(node.right) 

# def inOrder(node):
#     if not node:
#         return 
#     print(node.left.data) 
#     inOrder(node) 
#     inOrder(node.right) 

# test 
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
print('preorder traversal of constructed BST: ') 
preOrder(root)  # root -> left -> right 

# print('inorder traversal of constructed BST: ') 
# inOrder(root)

# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/