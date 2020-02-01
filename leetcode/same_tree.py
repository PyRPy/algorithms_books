# same tree or not
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None 
        self.left = None 

class Solution:
    def isSameTree(self, p, q):
        """
        type p: TreeNode
        type q: TreeNode 
        rtype: bool
        """

        if p is None and q is None:
            return True 

        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False 
