# sum_of_left_leaves.py
class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        def helper(root, direction = ""):
            if not root:
                return 0 

            if not root.left and not root.right:
                if direction == "l":
                    return root.val 

            left, right = 0, 0
            if root.left:
                left = helper(root.left, "l")

            if root.right:
                right = helper(root.right, "r")

            return left + right 
        return helper(root, "")
        



