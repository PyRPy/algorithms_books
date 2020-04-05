# construct_binary_tree_from_traversals.py
# definition for a binary tree node:
class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None 

        rootValue = preorder[0] 
        root = TreeNode(rootValue) 
        inorderIndex = inorder.index(rootValue) 

        root.left = self.buildTree(preorder[1: inorderIndex + 1], inorder[: inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex+1:], inorder[inorderIndex+1:])

        return root 

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(preorder, " ", inorder) 
sol = Solution() 
node1 = sol.buildTree(preorder, inorder) 
print(node1.val) # root is 3 