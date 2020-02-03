# binary tree level order traversal
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

class Solution:
    def levelOrderBottom(self, root):
        """
        type root: TreeNode
        rtype: list[list[int]]
        """

        if root is None:
            return []
        result, current = [], [root]

        while current:
            next_level, vals = [], [] 
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level 
            result.append(vals)
        return result[::-1]
        