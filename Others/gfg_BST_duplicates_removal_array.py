# gfg_duplicates_removal_array_BST.py
class newNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def insert(root, data):
    if root == None:
        return newNode(data) 
    else:
        if data < root.data:
            root.left = insert(root.left, data)   
        if data > root.data:
            root.right = insert(root.right, data)   
        return root 

# inorder to display a array 
def inOrder(root):
    if root == None:
        return 
    else:
        inOrder(root.left) 
        print(root.data, end = " ")
        inOrder(root.right)         
# test 
arr = [ 1, 2, 3, 2, 5, 4, 4 ]
n = len(arr) 
root = None 
for i in range(n):
    root = insert(root, arr[i]) 

# print out array after duplicates removal      
inOrder(root)

# https://www.geeksforgeeks.org/duplicates-removal-in-array-using-bst/?ref=leftbar-rightbar
