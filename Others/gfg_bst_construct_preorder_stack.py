# gfg_bst_construct_preorder.py
# binary tree node built with a stack 
class Node:
    def __init__(self, data = 0):
        self.data = data 
        self.left = None 
        self.right = None 

class BinaryTree:
    def constructTree(self, pre, size):
        root = Node(pre[0]) 
        s = [] 
        s.append(root) 
        i = 1 
        while i < size:
            temp = None 
            while len(s) > 0 and pre[i] > s[-1].data:
                temp = s.pop() 
            if temp != None:
                temp.right = Node(pre[i]) 
                s.append(temp.right) 
            else:
                temp = s[-1] 
                temp.left = Node(pre[i]) 
                s.append(temp.left) 
            i = i + 1 
        return root 

    def printInorder(self, node):
        if node == None:
            return 
        self.printInorder(node.left) 
        print(node.data, end = " ")
        self.printInorder(node.right) 

# test 
tree = BinaryTree()
pre = [10, 5, 1, 7, 40, 50] 
size = len(pre) 

root = tree.constructTree(pre, size)
print("inorder traveral of the constructed tree: ")    
tree.printInorder(root) 

# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/?ref=rp
# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
