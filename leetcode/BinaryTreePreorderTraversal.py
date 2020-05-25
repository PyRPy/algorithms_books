# 144. Binary Tree Preorder Traversal
# Definition for a binary tree node
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/binary-tree-preorder-traversal.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result, stack = [], [(root, False)] 
        while stack:
            root, is_visited = stack.pop() 
            if root is None:
                continue 
            if is_visited:
                result.append(root.val) 
            else:
                stack.append((root.right, False)) 
                stack.append((root.left, False)) 
                stack.append((root, True)) 
        return result 

# test 
root = TreeNode(1) 
root.left = None 
root.right = TreeNode(2)
root.right.left = TreeNode(3) 
root.right.right = None 

sol = Solution() 
print(sol.preorderTraversal(root)) 
