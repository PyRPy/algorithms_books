# mininum_absoluate_difference_bst.py
# definition for a binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution:
    def getMininumDifference(self, root):
        output = []

        self.InOrferTraversal(root, output)
        min_abs = float('inf')
        for i in range(1, len(output)):
            mins_abs = min(min_abs, output[i] - output[i-1])
        return min_abs

    def InOrferTraversal(self, root, output):
        if root == None:
            return 
        else:
            self.InOrferTraversal(root.left, output)
            output.append(root.val)
            self.InOrferTraversal(root.right, output)
            